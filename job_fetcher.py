"""
Job fetcher module querying strictly 100% free, UN-PAYWALLED public tech job boards:
- Jobicy (Remote engineering jobs, zero candidate fees)
- Arbeitnow (Direct company postings, no paywalls)
- Himalayas (Open remote tech jobs with direct application links)
- Remotive (Curated software dev jobs, zero candidate fees)
- HackerNews Who is Hiring (Direct founder/CTO posts with direct email links)

Note: RemoteOK was deliberately removed due to candidate paywalls and subscription gating.
"""
import asyncio
import time
import re
from typing import List, Dict, Any, Optional
import httpx

_CACHE: Dict[str, Any] = {
    "jobs": [],
    "last_fetched": 0,
    "ttl": 600  # 10 minutes cache
}

FEED_TIMEOUT = 7.0  # Vercel serverless execution safe limit

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

async def fetch_jobicy(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch jobs from Jobicy public API (100% free, direct apply)."""
    jobs = []
    try:
        url = "https://jobicy.com/api/v2/remote-jobs?count=50&industry=engineering"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get("jobs", []):
                jobs.append({
                    "id": f"jobicy-{item.get('id', '')}",
                    "title": item.get("jobTitle", "").strip(),
                    "company": item.get("companyName", "").strip(),
                    "location": item.get("jobGeo", "Remote"),
                    "job_type": item.get("jobType", "Full-Time"),
                    "salary": item.get("annualSalaryMin", "") and f"${item.get('annualSalaryMin')} - ${item.get('annualSalaryMax', '')}" or "Not Disclosed",
                    "tags": item.get("jobIndustry", []) if isinstance(item.get("jobIndustry"), list) else [item.get("jobIndustry", "Tech")],
                    "url": item.get("url", ""),
                    "description": item.get("jobDescription", "")[:1500],
                    "posted_at": item.get("pubDate", "")[:10],
                    "source": "Jobicy"
                })
    except Exception as e:
        print(f"[Warning] Jobicy fetch error: {e}")
    return jobs

async def fetch_arbeitnow(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch tech jobs from Arbeitnow public API (100% free, direct company links)."""
    jobs = []
    try:
        url = "https://www.arbeitnow.com/api/job-board-api"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get("data", []):
                jobs.append({
                    "id": f"arbeitnow-{item.get('slug', '')}",
                    "title": item.get("title", "").strip(),
                    "company": item.get("company_name", "").strip(),
                    "location": "Remote" if item.get("remote") else item.get("location", "Global"),
                    "job_type": item.get("job_types", ["Full-Time"])[0] if item.get("job_types") else "Full-Time",
                    "salary": "Competitive",
                    "tags": item.get("tags", []),
                    "url": item.get("url", ""),
                    "description": item.get("description", "")[:1500],
                    "posted_at": time.strftime("%Y-%m-%d", time.localtime(item.get("created_at", time.time()))),
                    "source": "Arbeitnow"
                })
    except Exception as e:
        print(f"[Warning] Arbeitnow fetch error: {e}")
    return jobs

async def fetch_himalayas(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch jobs from Himalayas public API (100% free, direct candidate links)."""
    jobs = []
    try:
        url = "https://himalayas.app/jobs/api?limit=40"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get("jobs", []):
                title = item.get("title", "").strip()
                company = item.get("companyName", "").strip()
                link = item.get("applicationLink") or item.get("guid") or ""
                if not title or not link:
                    continue
                salary_str = "Not Disclosed"
                if item.get("minSalary") and item.get("maxSalary"):
                    salary_str = f"${item.get('minSalary'):,} - ${item.get('maxSalary'):,}"
                
                categories = item.get("categories", [])
                tags = categories if isinstance(categories, list) else ["Engineering"]

                pub_date = str(item.get("pubDate") or "")[:10]
                excerpt = str(item.get("excerpt") or item.get("description") or "")[:1500]

                jobs.append({
                    "id": f"himalayas-{abs(hash(link))}",
                    "title": title,
                    "company": company,
                    "location": "Remote / Worldwide",
                    "job_type": item.get("employmentType", "Full-Time"),
                    "salary": salary_str,
                    "tags": tags[:5],
                    "url": link,
                    "description": excerpt,
                    "posted_at": pub_date,
                    "source": "Himalayas"
                })
    except Exception as e:
        print(f"[Warning] Himalayas fetch error: {e}")
    return jobs

async def fetch_remotive(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch software developer jobs from Remotive API (100% free, direct links)."""
    jobs = []
    try:
        url = "https://remotive.com/api/remote-jobs?category=software-dev"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get("jobs", []):
                jobs.append({
                    "id": f"remotive-{item.get('id', '')}",
                    "title": item.get("title", "").strip(),
                    "company": item.get("company_name", "").strip(),
                    "location": item.get("candidate_required_location", "Remote"),
                    "job_type": item.get("job_type", "Full-Time"),
                    "salary": item.get("salary", "Competitive") or "Competitive",
                    "tags": item.get("tags", []),
                    "url": item.get("url", ""),
                    "description": re.sub(r'<[^>]+>', ' ', item.get("description", ""))[:1500],
                    "posted_at": item.get("publication_date", "")[:10],
                    "source": "Remotive"
                })
    except Exception as e:
        print(f"[Warning] Remotive fetch error: {e}")
    return jobs

async def fetch_hacker_news_hiring(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch direct hiring posts from Hacker News 'Who is Hiring' threads (zero paywalls, direct founder emails)."""
    jobs = []
    try:
        search_url = "https://hn.algolia.com/api/v1/search?tags=story,ask_hn&query=Who+is+hiring"
        resp = await client.get(search_url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code != 200:
            return jobs
        hits = resp.json().get("hits", [])
        if not hits:
            return jobs
            
        story_id = hits[0].get("objectID")
        comments_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=comment,story_{story_id}&hitsPerPage=40"
        c_resp = await client.get(comments_url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if c_resp.status_code == 200:
            for c in c_resp.json().get("hits", []):
                text = c.get("comment_text", "")
                if not text or len(text) < 50:
                    continue
                clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
                first_line = clean_text.split("\n")[0]
                parts = [p.strip() for p in first_line.split("|")]
                company = parts[0] if len(parts) > 0 else "HackerNews Startup"
                title = parts[1] if len(parts) > 1 else "Software Engineer"
                loc = parts[2] if len(parts) > 2 else "Remote"
                
                techs = ["Python", "Rust", "Node", "React", "TypeScript", "JavaScript", "PostgreSQL", "AWS", "FastAPI", "HFT"]
                found_tags = [t for t in techs if re.search(r'\b' + re.escape(t) + r'\b', clean_text, re.IGNORECASE)]
                
                jobs.append({
                    "id": f"hn-{c.get('objectID')}",
                    "title": title[:60],
                    "company": company[:50],
                    "location": loc[:50],
                    "job_type": "Full-Time",
                    "salary": "See post description",
                    "tags": found_tags,
                    "url": f"https://news.ycombinator.com/item?id={c.get('objectID')}",
                    "description": clean_text[:1500],
                    "posted_at": c.get("created_at", "")[:10],
                    "source": "HackerNews (Direct)"
                })
    except Exception as e:
        print(f"[Warning] HackerNews fetch error: {e}")
    return jobs

async def fetch_all_jobs(force_refresh: bool = False) -> List[Dict[str, Any]]:
    """Fetch jobs concurrently from 100% free un-paywalled sources with caching."""
    global _CACHE
    now = time.time()
    if not force_refresh and _CACHE["jobs"] and (now - _CACHE["last_fetched"] < _CACHE["ttl"]):
        return _CACHE["jobs"]

    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            fetch_jobicy(client),
            fetch_arbeitnow(client),
            fetch_himalayas(client),
            fetch_remotive(client),
            fetch_hacker_news_hiring(client),
            return_exceptions=True
        )

    all_jobs: List[Dict[str, Any]] = []
    seen = set()
    for res in results:
        if isinstance(res, list):
            for job in res:
                key = (job.get("title", "").lower(), job.get("company", "").lower())
                if key not in seen and job.get("title") and job.get("company"):
                    seen.add(key)
                    all_jobs.append(job)

    _CACHE["jobs"] = all_jobs
    _CACHE["last_fetched"] = now
    return all_jobs

def search_jobs(
    jobs: List[Dict[str, Any]],
    query: Optional[str] = None,
    location: Optional[str] = None,
    source: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Filter jobs based on query keywords, location, and source."""
    filtered = jobs
    
    if query:
        q_tokens = [t.strip().lower() for t in query.split() if t.strip()]
        def matches_q(j):
            searchable = (
                f"{j.get('title', '')} {j.get('company', '')} "
                f"{' '.join(j.get('tags', []))} {j.get('description', '')}"
            ).lower()
            return all(token in searchable for token in q_tokens)
        filtered = [j for j in filtered if matches_q(j)]
        
    if location and location.lower() != "all":
        loc_q = location.lower()
        filtered = [
            j for j in filtered
            if loc_q in j.get("location", "").lower() or (loc_q == "remote" and "remote" in j.get("location", "").lower())
        ]
        
    if source and source.lower() != "all":
        filtered = [j for j in filtered if j.get("source", "").lower() == source.lower()]
        
    return filtered
