"""
Job fetcher module querying strictly 100% free, UN-PAYWALLED public tech job boards:
- Jobicy (Remote engineering jobs, zero candidate fees, 100+ fresh openings)
- WeWorkRemotely (Premier remote tech boards: Full-Stack, Backend, DevOps)
- Arbeitnow (Direct company postings, no recruiters, verified tech roles)
- Himalayas (Open remote tech jobs with direct application links)
- Remotive (Software dev, DevOps, and Data engineering roles)
- Python.org (Official Python Software Foundation direct listings)
- LaraJobs (Curated full-stack and web engineering opportunities)
- HackerNews Who is Hiring (Direct founder/CTO posts with direct email links)

Note: RemoteOK was deliberately removed due to candidate paywalls and subscription gating.
"""
import asyncio
import time
import re
import html
import xml.etree.ElementTree as ET
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
    "Accept": "application/json, text/plain, application/xml, text/xml, */*"
}

TECH_KEYWORDS_REGEX = re.compile(
    r'\b(software|developer|engineer|full\s*stack|backend|frontend|devops|cloud|architect|data|python|java|react|node|typescript|golang|rust|aws|azure|systems|machine\s*learning|ai)\b',
    re.IGNORECASE
)

def clean_html(raw_html: str) -> str:
    """Strip HTML tags and unescape entities."""
    if not raw_html:
        return ""
    text = re.sub(r'<[^>]+>', ' ', raw_html)
    return html.unescape(text).strip()

async def fetch_jobicy(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch jobs from Jobicy public API (100% free, direct apply, up to 100 jobs)."""
    jobs = []
    try:
        url = "https://jobicy.com/api/v2/remote-jobs?count=100&industry=engineering"
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
                    "description": clean_html(item.get("jobDescription", ""))[:1500],
                    "posted_at": item.get("pubDate", "")[:10],
                    "source": "Jobicy"
                })
    except Exception as e:
        print(f"[Warning] Jobicy fetch error: {e}")
    return jobs

async def fetch_weworkremotely(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch premier developer jobs from WeWorkRemotely public RSS feeds."""
    jobs = []
    categories = [
        ("remote-full-stack-programming-jobs", "Full-Stack"),
        ("remote-devops-sysadmin-jobs", "DevOps / Cloud"),
        ("remote-back-end-programming-jobs", "Backend")
    ]
    for cat_slug, default_tag in categories:
        try:
            url = f"https://weworkremotely.com/categories/{cat_slug}.rss"
            resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
            if resp.status_code == 200 and resp.content:
                root = ET.fromstring(resp.content)
                for item in root.findall(".//item"):
                    raw_title = (item.find("title").text or "").strip() if item.find("title") is not None else ""
                    link = (item.find("link").text or "").strip() if item.find("link") is not None else ""
                    if not raw_title or not link:
                        continue
                        
                    # Title format is typically "Company: Title"
                    company = "Tech Company"
                    title = raw_title
                    if ":" in raw_title:
                        c_part, t_part = raw_title.split(":", 1)
                        company = c_part.strip()
                        title = t_part.strip()
                        
                    region_elem = item.find("region")
                    location = region_elem.text.strip() if region_elem is not None and region_elem.text else "Remote / Worldwide"
                    
                    cat_elem = item.find("category")
                    tag = cat_elem.text.strip() if cat_elem is not None and cat_elem.text else default_tag
                    
                    desc_elem = item.find("description")
                    description = clean_html(desc_elem.text or "")[:1500] if desc_elem is not None else ""
                    
                    pub_elem = item.find("pubDate")
                    posted_at = pub_elem.text[:16] if pub_elem is not None and pub_elem.text else ""
                    
                    jobs.append({
                        "id": f"wwr-{abs(hash(link))}",
                        "title": title,
                        "company": company,
                        "location": location,
                        "job_type": "Full-Time",
                        "salary": "Competitive",
                        "tags": [tag, "Remote"],
                        "url": link,
                        "description": description,
                        "posted_at": posted_at,
                        "source": "WeWorkRemotely"
                    })
        except Exception as e:
            print(f"[Warning] WeWorkRemotely ({cat_slug}) fetch error: {e}")
    return jobs

async def fetch_arbeitnow(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch tech jobs from Arbeitnow public API (filtered for technical engineering roles)."""
    jobs = []
    try:
        url = "https://www.arbeitnow.com/api/job-board-api"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get("data", []):
                title = item.get("title", "").strip()
                company = item.get("company_name", "").strip()
                desc = item.get("description", "")
                tags = item.get("tags", [])
                
                # Filter for technical/engineering positions
                text_to_check = f"{title} {' '.join(tags)} {desc[:300]}"
                if not TECH_KEYWORDS_REGEX.search(text_to_check):
                    continue

                jobs.append({
                    "id": f"arbeitnow-{item.get('slug', '')}",
                    "title": title,
                    "company": company,
                    "location": "Remote" if item.get("remote") else item.get("location", "Global"),
                    "job_type": item.get("job_types", ["Full-Time"])[0] if item.get("job_types") else "Full-Time",
                    "salary": "Competitive",
                    "tags": tags[:5],
                    "url": item.get("url", ""),
                    "description": clean_html(desc)[:1500],
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
                excerpt = clean_html(str(item.get("excerpt") or item.get("description") or ""))[:1500]

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
    """Fetch software developer and DevOps jobs from Remotive API."""
    jobs = []
    categories = ["software-dev", "devops", "data"]
    for cat in categories:
        try:
            url = f"https://remotive.com/api/remote-jobs?category={cat}"
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
                        "description": clean_html(item.get("description", ""))[:1500],
                        "posted_at": item.get("publication_date", "")[:10],
                        "source": "Remotive"
                    })
        except Exception as e:
            print(f"[Warning] Remotive ({cat}) fetch error: {e}")
    return jobs

async def fetch_python_org(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch official developer roles from Python Software Foundation (python.org)."""
    jobs = []
    try:
        url = "https://www.python.org/jobs/feed/rss/"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200 and resp.content:
            root = ET.fromstring(resp.content)
            for item in root.findall(".//item"):
                raw_title = (item.find("title").text or "").strip() if item.find("title") is not None else ""
                link = (item.find("link").text or "").strip() if item.find("link") is not None else ""
                if not raw_title or not link:
                    continue
                
                # Title format: "Job Title, Company"
                title = raw_title
                company = "Python Ecosystem"
                if "," in raw_title:
                    parts = raw_title.rsplit(",", 1)
                    title = parts[0].strip()
                    company = parts[1].strip()
                    
                desc_elem = item.find("description")
                desc = clean_html(desc_elem.text or "")[:1500] if desc_elem is not None else ""
                
                jobs.append({
                    "id": f"pythonorg-{abs(hash(link))}",
                    "title": title,
                    "company": company,
                    "location": "Remote / Worldwide",
                    "job_type": "Full-Time",
                    "salary": "Competitive",
                    "tags": ["Python", "Backend", "Data"],
                    "url": link,
                    "description": desc,
                    "posted_at": time.strftime("%Y-%m-%d"),
                    "source": "Python.org"
                })
    except Exception as e:
        print(f"[Warning] Python.org fetch error: {e}")
    return jobs

async def fetch_larajobs(client: httpx.AsyncClient) -> List[Dict[str, Any]]:
    """Fetch modern web engineering jobs from LaraJobs."""
    jobs = []
    try:
        url = "https://larajobs.com/feed"
        resp = await client.get(url, headers=HEADERS, timeout=FEED_TIMEOUT)
        if resp.status_code == 200 and resp.content:
            root = ET.fromstring(resp.content)
            for item in root.findall(".//item"):
                raw_title = (item.find("title").text or "").strip() if item.find("title") is not None else ""
                link = (item.find("link").text or "").strip() if item.find("link") is not None else ""
                if not raw_title or not link:
                    continue
                
                company = "Web Tech Firm"
                title = raw_title
                if " at " in raw_title:
                    parts = raw_title.split(" at ", 1)
                    title = parts[0].strip()
                    company = parts[1].strip()
                    
                desc_elem = item.find("description")
                desc = clean_html(desc_elem.text or "")[:1500] if desc_elem is not None else ""
                
                pub_elem = item.find("pubDate")
                posted_at = pub_elem.text[:16] if pub_elem is not None and pub_elem.text else ""
                
                jobs.append({
                    "id": f"larajobs-{abs(hash(link))}",
                    "title": title,
                    "company": company,
                    "location": "Remote / Hybrid",
                    "job_type": "Full-Time",
                    "salary": "Competitive",
                    "tags": ["Full-Stack", "Backend", "Web"],
                    "url": link,
                    "description": desc,
                    "posted_at": posted_at,
                    "source": "LaraJobs"
                })
    except Exception as e:
        print(f"[Warning] LaraJobs fetch error: {e}")
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
                clean_text = clean_html(text)
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
            fetch_weworkremotely(client),
            fetch_arbeitnow(client),
            fetch_himalayas(client),
            fetch_remotive(client),
            fetch_python_org(client),
            fetch_larajobs(client),
            fetch_hacker_news_hiring(client),
            return_exceptions=True
        )

    all_jobs: List[Dict[str, Any]] = []
    seen = set()
    for res in results:
        if isinstance(res, list):
            for job in res:
                key = (job.get("title", "").lower().strip(), job.get("company", "").lower().strip())
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
