"""
JobPulse AI — Fast, Local Job Search Assistant & ATS Tailoring System.
FastAPI Backend with Web UI.
"""
from pathlib import Path
from typing import Optional, Dict, Any, List
import os
import shutil
from fastapi import FastAPI, Query, HTTPException, Body, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from resume_parser import parse_resume, set_active_resume, set_active_resume_bytes, reset_to_default_resume
from job_fetcher import fetch_all_jobs, search_jobs
from matcher import calculate_ats_match, generate_tailored_bullets, generate_outreach_messages
from company_directory import get_companies
import db

app = FastAPI(title="JobPulse AI", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMPLATE_DIR = Path(__file__).parent / "templates"
if os.environ.get("VERCEL"):
    UPLOAD_DIR = Path("/tmp/uploads")
else:
    UPLOAD_DIR = Path(__file__).parent / "uploads"
try:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
except Exception:
    pass

class ManualJDRequest(BaseModel):
    company: str = "Company"
    title: str = "Software Engineer"
    jd: str
    target_persona: Optional[str] = "auto"
    gemini_api_key: Optional[str] = None
    custom_skills: Optional[List[str]] = None
    candidate_name: Optional[str] = None
    raw_resume_text: Optional[str] = None

class ApplicationCreate(BaseModel):
    job_id: Optional[str] = ""
    title: str
    company: str
    location: Optional[str] = "Remote"
    salary: Optional[str] = "Not Disclosed"
    url: Optional[str] = ""
    source: Optional[str] = "Manual"
    status: Optional[str] = "Saved"
    match_score: Optional[int] = 0
    notes: Optional[str] = ""
    applied_date: Optional[str] = ""

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None
    applied_date: Optional[str] = None
    salary: Optional[str] = None

@app.on_event("startup")
def startup_event():
    db.init_db()
    # Warm up resume parser
    parse_resume()

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = TEMPLATE_DIR / "index.html"
    if not index_file.exists():
        raise HTTPException(status_code=404, detail="Web UI template not found")
    return HTMLResponse(content=index_file.read_text(encoding="utf-8"))

@app.get("/api/debug")
async def debug_endpoint(request: Request):
    """Debug endpoint to inspect headers and paths received on Vercel."""
    return {
        "url": str(request.url),
        "path": request.url.path,
        "scope_path": request.scope.get("path"),
        "headers": dict(request.headers)
    }

@app.get("/preview", response_class=HTMLResponse)
async def serve_preview():
    preview_file = TEMPLATE_DIR / "preview_modern.html"
    if not preview_file.exists():
        raise HTTPException(status_code=404, detail="Preview template not found")
    return HTMLResponse(content=preview_file.read_text(encoding="utf-8"))

@app.get("/api/resume")
async def get_resume():
    """Returns the parsed resume metadata, skills, and experience."""
    return parse_resume()

@app.post("/api/resume/upload")
async def upload_resume(file: UploadFile = File(...)):
    """
    Statelessly uploads a new resume PDF, extracts candidate profile and skills,
    and returns them to the caller without mutating server-level shared state.
    This guarantees 100% private per-user isolation.
    """
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported.")
    
    try:
        content = await file.read()
        from resume_parser import parse_custom_resume
        # Pure stateless parse: does not alter server global state
        parsed = parse_custom_resume(content, filename=file.filename)
        return {
            "success": True,
            "filename": file.filename,
            "profile": parsed
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process resume: {str(e)}")

@app.post("/api/resume/reset")
async def reset_resume():
    """Resets active resume back to the default profile (Venu Gopal Potnuru.pdf)."""
    parsed = reset_to_default_resume()
    return {
        "success": True,
        "message": "Reset to default profile successfully.",
        "profile": parsed
    }

@app.get("/api/companies")
async def list_companies(
    category: str = Query("all", description="Category: hft, mnc, unicorn, enterprise_sap, ai, europe_apac, all"),
    search: str = Query("", description="Keyword search")
):
    """Returns curated directory of top firms, MNCs, and product companies with direct career links."""
    results = get_companies(category=category, search=search)
    return {
        "count": len(results),
        "companies": results
    }

@app.get("/api/companies/resolve")
async def resolve_company(name: str = Query(..., description="Company name to dynamically resolve")):
    """
    Dynamically generates direct un-paywalled ATS links, Google Jobs search, and metadata
    for ANY company worldwide, even if not pre-indexed in the static directory.
    """
    clean_name = name.strip()
    if not clean_name:
        raise HTTPException(status_code=400, detail="Company name is required")
        
    import urllib.parse
    encoded_name = urllib.parse.quote(clean_name)
    
    return {
        "name": clean_name,
        "is_dynamic": True,
        "google_jobs_url": f"https://www.google.com/search?q={encoded_name}+%28Software+Engineer+OR+Developer+OR+Full+Stack+OR+Backend+OR+Frontend+OR+Cloud+OR+AI%29&ibp=htl;jobs",
        "ats_shortcuts": {
            "greenhouse": f"https://www.google.com/search?q=site%3Aboards.greenhouse.io+{encoded_name}",
            "lever": f"https://www.google.com/search?q=site%3Ajobs.lever.co+{encoded_name}",
            "ashby": f"https://www.google.com/search?q=site%3Ajobs.ashbyhq.com+{encoded_name}",
            "workday": f"https://www.google.com/search?q=site%3Amyworkdayjobs.com+{encoded_name}",
            "direct": f"https://www.google.com/search?q={encoded_name}+official+careers+jobs"
        }
    }


@app.get("/api/jobs/search")
async def search_live_jobs(
    request: Request,
    q: Optional[str] = Query(None, description="Search term / skill"),
    location: Optional[str] = Query("all", description="Location filter"),
    source: Optional[str] = Query("all", description="Source board filter"),
    skills: Optional[str] = Query(None, description="Comma-separated skills for per-user candidate scoring"),
    force: bool = Query(False, description="Force refresh job caches")
):
    """
    Fetches active tech jobs, filters by query/location, and pre-scores each
    job with ATS match against the user's isolated candidate skills.
    """
    raw_jobs = await fetch_all_jobs(force_refresh=force)
    filtered = search_jobs(raw_jobs, query=q, location=location, source=source)

    # Check query param or header for per-user candidate skills
    hdr_skills = request.headers.get("x-candidate-skills")
    custom_skills_raw = skills or hdr_skills
    target_skills = [s.strip() for s in custom_skills_raw.split(",") if s.strip()] if custom_skills_raw else None

    # Score each job
    scored_jobs = []
    for job in filtered:
        match_info = calculate_ats_match(job["title"], job["description"], candidate_skills=target_skills)
        j_copy = dict(job)
        j_copy["match"] = match_info
        scored_jobs.append(j_copy)

    # Sort primarily by ATS match score descending
    scored_jobs.sort(key=lambda x: x["match"]["score"], reverse=True)

    return {
        "count": len(scored_jobs),
        "total_available": len(raw_jobs),
        "jobs": scored_jobs[:100]  # Return top 100 matching jobs for high coverage
    }

@app.post("/api/analyze-jd")
async def analyze_jd(payload: ManualJDRequest):
    """
    Analyzes any pasted job description: returns ATS match, missing skills,
    tailored Google X-Y-Z resume bullets, and personalized outreach pitches.
    Uses candidate's private session skills and name if provided.
    """
    if not payload.jd.strip():
        raise HTTPException(status_code=400, detail="Job description text is required")

    from matcher import calculate_ats_match, generate_tailored_bullets, generate_outreach_messages, generate_with_gemini

    match_info = calculate_ats_match(
        payload.title, 
        payload.jd,
        candidate_skills=payload.custom_skills,
        raw_resume_text=payload.raw_resume_text
    )
    persona = payload.target_persona if (payload.target_persona and payload.target_persona != "auto") else match_info["role_persona"]

    # Try Gemini Generative AI if key provided
    ai_generated = None
    if payload.gemini_api_key:
        ai_generated = await generate_with_gemini(
            payload.company, payload.title, payload.jd, api_key=payload.gemini_api_key
        )

    if ai_generated and "bullets" in ai_generated:
        bullets = ai_generated["bullets"]
        outreach = {
            "linkedin_connection": ai_generated.get("linkedin_connection", ""),
            "cold_email": ai_generated.get("cold_email", ""),
            "referral_pitch": ai_generated.get("referral_pitch", "")
        }
        engine_used = "Google Gemini 2.5 Flash"
    else:
        bullets = generate_tailored_bullets(payload.title, match_info["matched_skills"], role_persona=persona)
        candidate_profile = None
        if payload.candidate_name:
            candidate_profile = {
                "name": payload.candidate_name,
                "title": persona,
                "location": "Remote",
                "links": {}
            }
        outreach = generate_outreach_messages(
            payload.company, 
            payload.title, 
            match_info["matched_skills"], 
            role_persona=persona,
            candidate_profile=candidate_profile
        )
        engine_used = "High-Accuracy Persona Engine"

    return {
        "company": payload.company,
        "title": payload.title,
        "role_persona": persona,
        "persona_label": match_info.get("persona_label", "Full Stack Engineer"),
        "engine_used": engine_used,
        "match": match_info,
        "bullets": bullets,
        "outreach": outreach
    }

@app.get("/api/applications")
async def list_applications(status: Optional[str] = None):
    """Returns all tracked job applications."""
    return db.get_applications(status=status)

@app.post("/api/applications")
async def create_application(app_data: ApplicationCreate):
    """Saves a job to the tracker pipeline."""
    app_id = db.save_application(app_data.dict())
    return {"success": True, "id": app_id}

@app.patch("/api/applications/{app_id}")
async def patch_application(app_id: int, updates: ApplicationUpdate):
    """Updates status, applied date, or notes for an application."""
    data = {k: v for k, v in updates.dict().items() if v is not None}
    success = db.update_application(app_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Application not found or no changes made")
    return {"success": True}

@app.delete("/api/applications/{app_id}")
async def delete_application(app_id: int):
    """Removes an application from tracker."""
    success = db.delete_application(app_id)
    if not success:
        raise HTTPException(status_code=404, detail="Application not found")
    return {"success": True}

@app.get("/api/stats")
async def get_application_stats():
    """Returns counts of saved, applied, interviewing, and offers."""
    return db.get_stats()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
