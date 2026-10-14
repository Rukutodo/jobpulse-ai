# JobPulse AI — Personal Job Search & ATS Matcher

A personalized job search and application suite built for **Venu Gopal Potnuru** (`Venu Gopal Potnuru.pdf`), featuring a high-performance Python FastAPI backend, multi-board job aggregators, automated ATS matching, tailored resume bullet generation, 1-click cold outreach pitches, and a persistent SQLite application tracker.

---

## 🚀 Key Features

### 1. 🎯 Live Multi-Board Job Radar
- **5 Live Un-Paywalled Feeds**: Aggregates developer jobs from **Jobicy**, **Arbeitnow**, **Himalayas**, **Remotive**, and **Hacker News 'Who is Hiring'** threads (100% free with zero paywalls or subscriptions).
- **Auto-Ranked by ATS Fit**: Every job retrieved is automatically evaluated and scored against your resume.
- **Instant Filtering**: Filter by role title, tech keywords (`Node.js`, `Python`, `React`, `Rust`, `Full Stack`, `Backend`, `HFT`), location (`Remote`, `India`), or source.

### 2. 🔍 Instant JD Analyzer & Tailor
- Paste any job description from **LinkedIn**, **Naukri**, **Wellfound**, or company portals.
- **ATS Fit Breakdown**:
  - Match score (%) & tier (High, Strong, Moderate, Growth).
  - **Matched Skills**: Highlights the skills you possess.
  - **Missing / Desired Skills**: Identifies keywords to brush up on or emphasize.
- **Tailored Resume Bullets**: Generates 3 impactful bullet points using the **Google X-Y-Z formula** (`Accomplished [X] as measured by [Y], by doing [Z]`) based on your TCS and Voxa achievements.
- **1-Click Outreach Pitches**:
  - **LinkedIn Connection Note** (strictly kept under the 300-character limit).
  - **Direct Cold Email** to hiring managers with metrics.
  - **Referral Pitch** to send to engineering team members.

### 3. 📋 Application Pipeline Tracker
- Track applications across stages: `Saved` ➔ `Applied` ➔ `Interviewing` ➔ `Offer` ➔ `Rejected`.
- Stores interview notes, follow-up dates, salaries, and direct links.
- Persisted locally in SQLite (`jobsearch.db`).

### 4. 📄 Resume Sync
- Directly extracts and displays your structured skills, enterprise metrics (10K DAU, 200K peak load, ~1m to <15s latency reduction, rate-limiting backoff), and desktop AI achievements (Voxa) from `Venu Gopal Potnuru.pdf`.

---

## 🛠️ How to Run

### Quick Start (Recommended)
From PowerShell in `D:\upskilling\jobsearch`:

```powershell
.venv\Scripts\python.exe run.py
```
*This starts the server and automatically opens `http://127.0.0.1:8000` in your default browser.*

Alternatively:
```powershell
.venv\Scripts\uvicorn.exe app:app --reload --port 8000
```
Then visit: **http://127.0.0.1:8000**

---

## 📁 Project Architecture

- [`run.py`](file:///D:/upskilling/jobsearch/run.py): One-click launcher script with browser auto-open.
- [`app.py`](file:///D:/upskilling/jobsearch/app.py): FastAPI backend routes for searching, scoring, tailoring, and tracking.
- [`resume_parser.py`](file:///D:/upskilling/jobsearch/resume_parser.py): PDF reader extracting skills, metrics, and experience from `Venu Gopal Potnuru.pdf`.
- [`job_fetcher.py`](file:///D:/upskilling/jobsearch/job_fetcher.py): Async multi-board scraper (RemoteOK, Jobicy, Arbeitnow, HN).
- [`matcher.py`](file:///D:/upskilling/jobsearch/matcher.py): ATS scoring algorithm, gap analysis, and tailored bullet/outreach generator.
- [`db.py`](file:///D:/upskilling/jobsearch/db.py): SQLite persistence layer for pipeline tracking.
- [`templates/index.html`](file:///D:/upskilling/jobsearch/templates/index.html): Modern, responsive single-page web UI (Tailwind CSS + Lucide icons).
