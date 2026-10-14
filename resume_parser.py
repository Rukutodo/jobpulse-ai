"""
Resume parser module for extracting profile, skills, experience, and projects
from Venu Gopal Potnuru's resume.
"""
import io
from pathlib import Path
import re
from typing import Dict, List, Set, Any, Optional, Union
import pypdf

RESUME_PDF_PATH = Path(__file__).parent / "Venu Gopal Potnuru.pdf"

# Standard comprehensive tech taxonomy for exact & fuzzy keyword matching
TECH_SKILLS = {
    # Languages
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "python": "Python",
    "rust": "Rust",
    "sql": "SQL",
    "html": "HTML",
    "css": "CSS",
    "c++": "C++",
    "go": "Go",
    "golang": "Go",
    
    # Frontend
    "react": "React.js",
    "react.js": "React.js",
    "reactjs": "React.js",
    "next.js": "Next.js",
    "nextjs": "Next.js",
    "vite": "Vite",
    "tailwind": "Tailwind CSS",
    "tailwind css": "Tailwind CSS",
    "redux": "Redux",
    
    # Backend & API
    "node": "Node.js",
    "node.js": "Node.js",
    "nodejs": "Node.js",
    "express": "Express.js",
    "express.js": "Express.js",
    "fastapi": "FastAPI",
    "rest": "REST APIs",
    "rest api": "REST APIs",
    "restful": "REST APIs",
    "graphql": "GraphQL",
    "microservices": "Microservices",
    
    # Databases & Caching
    "postgresql": "PostgreSQL",
    "postgres": "PostgreSQL",
    "sqlite": "SQLite",
    "mysql": "MySQL",
    "mongodb": "MongoDB",
    "redis": "Redis",
    
    # Systems, Desktop & AI
    "tauri": "Tauri 2",
    "tauri 2": "Tauri 2",
    "nvidia parakeet": "NVIDIA Parakeet",
    "parakeet": "NVIDIA Parakeet",
    "whisper": "Whisper",
    "faster-whisper": "faster-whisper",
    "qwen tts": "Qwen TTS",
    "speech recognition": "Speech Recognition",
    "tts": "Text-to-Speech (TTS)",
    "asr": "Automatic Speech Recognition (ASR)",
    "cpal": "CPAL",
    "ai engineer": "AI Engineering",
    "applied ai": "Applied AI",
    "llm": "LLMs",
    "rag": "RAG (Retrieval-Augmented Gen)",
    "langchain": "LangChain",
    "transformers": "Transformers",
    "pytorch": "PyTorch",
    "vector database": "Vector Databases",
    "embeddings": "Embeddings",
    "prompt engineering": "Prompt Engineering",

    # Forward Deployed Engineer (FDE) & Solutions
    "fde": "Forward Deployed Engineer (FDE)",
    "forward deployed": "Forward Deployed Engineering",
    "forward deployed engineer": "Forward Deployed Engineer (FDE)",
    "client solutions": "Client Solutions Engineering",
    "enterprise integration": "Enterprise Integrations",
    "stakeholder management": "Stakeholder Collaboration",
    "technical consulting": "Technical Consulting",
    "workflow automation": "Workflow Automation",
    "solution architecture": "Solution Architecture",

    # SAP & Enterprise ERP
    "sap": "SAP",
    "abap": "SAP ABAP",
    "sap abap": "SAP ABAP",
    "bapi": "BAPI",
    "idoc": "IDoc",
    "odata": "OData",
    "rfc": "RFC",
    "s/4hana": "SAP S/4HANA",
    "ecc": "SAP ECC",
    "erp": "ERP Systems",
    "cds views": "CDS Views",

    # HFT & Low-Latency Systems
    "hft": "High-Frequency Trading (HFT)",
    "low latency": "Low-Latency Systems",
    "low-latency": "Low-Latency Systems",
    "multithreading": "Multithreading & Concurrency",
    "concurrency": "Concurrency",
    "systems programming": "Systems Programming (Rust)",
    "zero-copy": "Zero-Copy Architecture",
    "quant": "Quantitative Engineering",
    "market data": "Market Data / Real-time Streams",
    
    # Cloud, DevOps & Tools
    "docker": "Docker",
    "aws": "AWS",
    "vercel": "Vercel",
    "git": "Git",
    "github": "GitHub",
    "postman": "Postman",
    "linux": "Linux",
    "ci/cd": "CI/CD",
    
    # Architecture & Engineering Concepts
    "rate limiting": "Rate Limiting",
    "rate limit": "Rate Limiting",
    "backoff": "Backoff Strategies & Jitter",
    "caching": "Caching",
    "performance optimization": "Performance Optimization",
    "api integration": "API Integration",
    "data processing": "Data Processing",
    "csod": "Cornerstone OnDemand (CSOD)",
    "sit": "SIT / UAT",
    "uat": "SIT / UAT",
    "authentication": "Authentication (JWT / OAuth)",
    "local-first": "Local-First Architecture"
}

ACTIVE_RESUME_PATH: Path = RESUME_PDF_PATH
IS_CUSTOM_RESUME: bool = False
ACTIVE_RESUME_NAME: str = "Venu Gopal Potnuru.pdf"
_CACHED_PROFILE: Dict[str, Any] = {}

def extract_resume_text(pdf_source: Union[Path, bytes, io.BytesIO] = RESUME_PDF_PATH) -> str:
    """Extract raw text from resume PDF (accepts Path, bytes, or BytesIO)."""
    try:
        if isinstance(pdf_source, (bytes, bytearray)):
            reader = pypdf.PdfReader(io.BytesIO(pdf_source))
        elif isinstance(pdf_source, io.BytesIO):
            reader = pypdf.PdfReader(pdf_source)
        else:
            p = Path(pdf_source)
            if not p.exists():
                return ""
            reader = pypdf.PdfReader(str(p))
            
        text_parts = []
        for page in reader.pages:
            txt = page.extract_text()
            if txt:
                text_parts.append(txt)
        return "\n".join(text_parts)
    except Exception as e:
        print(f"[Warning] Error extracting PDF text: {e}")
        return ""

def extract_resume_hyperlinks(pdf_source: Union[Path, bytes, io.BytesIO] = RESUME_PDF_PATH) -> Dict[str, str]:
    """Extract embedded clickable URLs from PDF annotations (accepts Path, bytes, or BytesIO)."""
    links = {
        "linkedin": "https://www.linkedin.com/in/venu-gopal-potnuru-8b272b199",
        "github": "https://github.com/Rukutodo",
        "voxa_github": "https://github.com/Rukutodo/voxa",
        "voxa_live": "https://voiceflow-website-lovat.vercel.app/"
    }
    try:
        if isinstance(pdf_source, (bytes, bytearray)):
            reader = pypdf.PdfReader(io.BytesIO(pdf_source))
        elif isinstance(pdf_source, io.BytesIO):
            reader = pypdf.PdfReader(pdf_source)
        else:
            p = Path(pdf_source)
            if not p.exists():
                return links
            reader = pypdf.PdfReader(str(p))

        extracted = {}
        for page in reader.pages:
            if "/Annots" in page:
                for annot in page["/Annots"]:
                    obj = annot.get_object()
                    if "/A" in obj and "/URI" in obj["/A"]:
                        uri = obj["/A"]["/URI"]
                        if "linkedin.com" in uri:
                            extracted["linkedin"] = uri
                        elif "github.com/Rukutodo/voxa" in uri:
                            extracted["voxa_github"] = uri
                        elif "github.com" in uri:
                            extracted["github"] = uri
                        elif "vercel.app" in uri:
                            extracted["voxa_live"] = uri
        if extracted:
            links.update(extracted)
    except Exception as e:
        print(f"[Warning] Error extracting PDF links: {e}")
    return links

def parse_default_venu_profile(raw_text: str, links: Dict[str, str]) -> Dict[str, Any]:
    """Return the structured default profile for Venu Gopal Potnuru."""
    return {
        "name": "Venu Gopal Potnuru",
        "title": "Full Stack Developer | Assistant System Engineer",
        "location": "Hyderabad, India",
        "email": "vvarun321@gmail.com",
        "phone": "+91 95025 21952",
        "links": links,
        "experience_years": "2+",
        "summary": (
            "Full Stack Developer with 2+ years of experience building enterprise applications, "
            "REST APIs, platform integrations, and data-processing solutions using JavaScript, "
            "Node.js, Express.js, PostgreSQL, and Python. Experienced in performance optimization, "
            "API rate limiting, SIT/UAT, production deployment, and stakeholder collaboration. "
            "Built and deployed a local-first AI voice application using Rust, Tauri, Python, and speech recognition."
        ),
        "skills_by_category": {
            "Languages": ["JavaScript", "Python", "Rust", "SQL", "HTML", "CSS"],
            "Frontend": ["React.js", "JavaScript", "Tailwind CSS"],
            "Backend": ["Node.js", "Express.js", "REST APIs", "Python"],
            "Databases": ["PostgreSQL", "SQLite"],
            "AI / Speech": ["NVIDIA Parakeet", "Whisper", "faster-whisper", "Qwen TTS", "Speech Recognition"],
            "Desktop": ["Rust", "Tauri 2", "CPAL"],
            "Tools & Cloud": ["GitHub", "Docker", "Postman", "AWS", "Vercel", "VS Code"],
            "Engineering": [
                "API Integration", "Authentication", "Rate Limiting", "Caching",
                "Performance Optimization", "Data Processing", "SIT / UAT"
            ]
        },
        "all_skills": [
            "JavaScript", "Python", "Rust", "SQL", "HTML", "CSS", "React.js", "Tailwind CSS",
            "Node.js", "Express.js", "REST APIs", "PostgreSQL", "SQLite", "NVIDIA Parakeet",
            "Whisper", "faster-whisper", "Qwen TTS", "Tauri 2", "CPAL", "GitHub", "Docker",
            "Postman", "AWS", "Vercel", "API Integration", "Authentication", "Rate Limiting",
            "Caching", "Performance Optimization", "Data Processing", "CSOD"
        ],
        "experience": [
            {
                "company": "Tata Consultancy Services (TCS)",
                "role": "Assistant System Engineer / Full Stack Developer",
                "period": "May 2024 – Present",
                "location": "Hyderabad, India",
                "highlights": [
                    "Developed and maintained full-stack features for an enterprise learning platform integrated with Cornerstone OnDemand (CSOD), supporting ~10K daily active users and 200K peak load.",
                    "Built backend services using Node.js and Express.js, integrating CSOD APIs and developing custom internal APIs.",
                    "Developed custom application screens, validations, business logic, workflow integrations, and email notification triggers using JavaScript, Tailwind CSS, and HTML.",
                    "Reduced application/API load time from ~1 minute to consistently under 15 seconds by identifying bottlenecks and optimizing application and API processing.",
                    "Resolved API rate-limiting issues by implementing a custom rate-control mechanism using jitter, progressive delays, and backoff strategies.",
                    "Designed and implemented data-processing solutions using PostgreSQL and SQLite for high-volume enterprise records and workflows.",
                    "Built automation to retrieve external data, process records, and load the resulting data into databases, reducing repetitive manual work.",
                    "Worked directly with clients and business stakeholders to clarify business rules and deliver application changes.",
                    "Participated in SIT and UAT, defect resolution, and independently handled application deployment activities."
                ]
            }
        ],
        "projects": [
            {
                "name": "Voxa",
                "tagline": "Local-First AI Voice Typing Application",
                "stack": ["Rust", "Tauri 2", "Python", "SQLite", "NVIDIA Parakeet", "Qwen TTS"],
                "highlights": [
                    "Built a local-first Windows voice application that captures microphone audio, performs local speech recognition, and injects generated text into desktop applications.",
                    "Implemented the speech-processing pipeline using NVIDIA Parakeet and built the application with Rust, Tauri 2, and Python for local AI inference.",
                    "Developed the next version with voice activation, custom phrases, and custom meaning handling to improve recognition for Indian diction and usage patterns.",
                    "Independently developed, packaged, deployed, and published downloadable releases for public testing."
                ]
            },
            {
                "name": "Voxa Website",
                "tagline": "Product Showcase",
                "stack": ["React", "Vite", "Tailwind CSS", "JavaScript", "Vercel"],
                "highlights": [
                    "Built and deployed a responsive React/Vite product showcase using Tailwind CSS, reusable components, and interactive product sections.",
                    "Configured the production deployment using Vercel and maintained the public-facing website alongside application releases."
                ]
            }
        ],
        "raw_text": raw_text,
        "is_custom": False,
        "filename": "Venu Gopal Potnuru.pdf"
    }

def parse_custom_resume(pdf_source: Union[Path, bytes, io.BytesIO], original_filename: str) -> Dict[str, Any]:
    """Dynamically parse an arbitrary uploaded PDF resume from disk or in-memory bytes."""
    raw_text = extract_resume_text(pdf_source)
    links = extract_resume_hyperlinks(pdf_source)

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', raw_text)
    email = email_match.group(0) if email_match else "contact@candidate.com"

    # Extract phone
    phone_match = re.search(r'(\+?\d[\d\s-]{8,14}\d)', raw_text)
    phone = phone_match.group(0).strip() if phone_match else ""

    # Extract candidate name from top lines
    lines = [l.strip() for l in raw_text.splitlines() if l.strip()]
    candidate_name = Path(original_filename).stem.replace("_", " ").replace("-", " ")
    for line in lines[:5]:
        if len(line) < 35 and not any(w in line.lower() for w in ["resume", "curriculum", "http", "@", "phone", "profile", "page"]):
            candidate_name = line.title()
            break

    # Discover skills using taxonomy
    matched_skills = set()
    raw_text_lower = raw_text.lower()
    for kw, canonical in TECH_SKILLS.items():
        pattern = r'(?<![a-z0-9])' + re.escape(kw) + r'(?![a-z0-9])'
        if re.search(pattern, raw_text_lower):
            matched_skills.add(canonical)

    skills_list = sorted(list(matched_skills))
    if not skills_list:
        skills_list = ["JavaScript", "Python", "SQL", "REST APIs", "Git"]

    profile = {
        "name": candidate_name,
        "title": "Software Engineer / Tech Professional",
        "location": "Global / Remote",
        "email": email,
        "phone": phone,
        "links": links,
        "experience_years": "2+",
        "summary": f"Software engineering professional with hands-on skills in {', '.join(skills_list[:6])}.",
        "skills_by_category": {
            "Discovered Skills": skills_list[:12],
            "All Extracted Tech": skills_list
        },
        "all_skills": skills_list,
        "experience": [
            {
                "company": "Professional Experience",
                "role": "Software Developer / Engineer",
                "period": "Extracted from Resume",
                "location": "Remote / On-site",
                "highlights": [line for line in lines if len(line) > 50][:6]
            }
        ],
        "projects": [
            {
                "name": "Featured Project",
                "tagline": "Software Solution",
                "stack": skills_list[:4],
                "highlights": ["Extracted from uploaded resume document."]
            }
        ],
        "raw_text": raw_text,
        "is_custom": True,
        "filename": original_filename
    }
    return profile

def parse_resume(pdf_path: Optional[Path] = None) -> Dict[str, Any]:
    """Parse resume into structured data representation."""
    global _CACHED_PROFILE, ACTIVE_RESUME_PATH, IS_CUSTOM_RESUME, ACTIVE_RESUME_NAME

    if pdf_path is None:
        pdf_path = ACTIVE_RESUME_PATH

    if _CACHED_PROFILE:
        return _CACHED_PROFILE

    raw_text = extract_resume_text(pdf_path)
    links = extract_resume_hyperlinks(pdf_path)

    if IS_CUSTOM_RESUME:
        profile = parse_custom_resume(pdf_path, ACTIVE_RESUME_NAME)
    else:
        profile = parse_default_venu_profile(raw_text, links)

    _CACHED_PROFILE = profile
    return profile

def set_active_resume(pdf_path: Path, filename: str) -> Dict[str, Any]:
    """Sets a newly uploaded resume as the active resume and re-parses it."""
    global ACTIVE_RESUME_PATH, IS_CUSTOM_RESUME, ACTIVE_RESUME_NAME, _CACHED_PROFILE
    ACTIVE_RESUME_PATH = pdf_path
    IS_CUSTOM_RESUME = True
    ACTIVE_RESUME_NAME = filename
    _CACHED_PROFILE = {}
    return parse_resume(pdf_path)

def set_active_resume_bytes(file_bytes: bytes, filename: str) -> Dict[str, Any]:
    """Sets a newly uploaded resume from raw in-memory bytes and re-parses it (zero disk writes)."""
    global ACTIVE_RESUME_PATH, IS_CUSTOM_RESUME, ACTIVE_RESUME_NAME, _CACHED_PROFILE
    IS_CUSTOM_RESUME = True
    ACTIVE_RESUME_NAME = filename
    _CACHED_PROFILE = parse_custom_resume(file_bytes, filename)
    return _CACHED_PROFILE

def reset_to_default_resume() -> Dict[str, Any]:
    """Resets active resume back to Venu Gopal Potnuru.pdf."""
    global ACTIVE_RESUME_PATH, IS_CUSTOM_RESUME, ACTIVE_RESUME_NAME, _CACHED_PROFILE
    ACTIVE_RESUME_PATH = RESUME_PDF_PATH
    IS_CUSTOM_RESUME = False
    ACTIVE_RESUME_NAME = "Venu Gopal Potnuru.pdf"
    _CACHED_PROFILE = {}
    return parse_resume(RESUME_PDF_PATH)

def get_skill_set() -> Set[str]:
    """Return lowercase set of normalized skills present in resume."""
    profile = parse_resume()
    skills = set()
    for s in profile.get("all_skills", []):
        skills.add(s.lower())
    # Add mapped tech skills keywords
    for k, v in TECH_SKILLS.items():
        if v.lower() in skills or any(s in profile.get("raw_text", "").lower() for s in [k, v.lower()]):
            skills.add(k)
            skills.add(v.lower())
    return skills

