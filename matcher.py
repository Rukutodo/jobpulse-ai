"""
ATS Matcher and Tailoring Generator for Venu Gopal Potnuru's resume.
Calculates keyword match score, identifies gaps, and generates tailored
application bullets and outreach messages for:
- Full Stack Developer
- Backend Developer
- Frontend Developer
- AI / Speech Engineer
- Forward Deployed Engineer (FDE)
- SAP ABAP & Enterprise ERP
- High-Frequency Trading (HFT) & Low-Latency Systems

Uses 100% free, un-paywalled job sources. Includes optional Google Gemini 2.5 Flash API support.
"""
import os
import re
import json
from typing import Dict, List, Any, Set, Tuple, Optional
import httpx

from resume_parser import parse_resume, TECH_SKILLS, get_skill_set

def extract_tech_keywords_from_text(text: str) -> Set[str]:
    """Find tech keywords mentioned in text using TECH_SKILLS map and regex."""
    found = set()
    text_lower = text.lower()
    
    for kw, canonical in TECH_SKILLS.items():
        pattern = r'(?<![a-z0-9])' + re.escape(kw) + r'(?![a-z0-9])'
        if re.search(pattern, text_lower):
            found.add(canonical)
            
    extra_keywords = [
        "Docker", "Kubernetes", "AWS", "GCP", "Azure", "CI/CD", "Redis",
        "MongoDB", "GraphQL", "Microservices", "System Design", "Agile",
        "Kafka", "RabbitMQ", "OAuth", "JWT", "TypeScript", "Next.js",
        "FastAPI", "Django", "Flask", "Spring Boot", "Unit Testing", "Jest",
        "PyTorch", "LangChain", "LLMs", "RAG", "SAP ABAP", "BAPI", "IDoc", "OData",
        "HFT", "Low Latency", "Concurrency", "Zero-Copy"
    ]
    for term in extra_keywords:
        pattern = r'(?<![a-z0-9])' + re.escape(term.lower()) + r'(?![a-z0-9])'
        if re.search(pattern, text_lower):
            found.add(term)
            
    return found

def detect_target_role(job_title: str, jd_text: str) -> str:
    """Classify the target persona of the job."""
    combined = f"{job_title} {jd_text}".lower()
    
    # 1. HFT & Low-Latency Systems
    if any(k in combined for k in [
        "hft", "high frequency trading", "low latency", "low-latency", "market maker",
        "trading systems", "quantitative developer", "quant developer", "zero-copy", "order execution"
    ]):
        return "hft"

    # 2. Forward Deployed Engineer (FDE)
    if any(k in combined for k in [
        "forward deployed", "forward-deployed", "fde", "solutions engineer", 
        "solutions architect", "client solutions", "deployment engineer", "customer engineer"
    ]):
        return "fde"
        
    # 3. SAP / ABAP / Enterprise ERP
    if any(k in combined for k in [
        "sap", "abap", "bapi", "idoc", "s/4hana", "ecc", "cds views", "rfc"
    ]):
        return "sap_abap"

    # 4. AI / Applied AI / Speech
    if any(k in combined for k in [
        "ai engineer", "applied ai", "speech recognition", "whisper", "parakeet",
        "tts", "asr", "llm", "machine learning engineer", "ml engineer", "genai", "deep learning"
    ]):
        return "ai_engineer"

    # 5. Frontend Developer
    if any(k in combined for k in [
        "frontend", "front-end", "ui developer", "react developer", "web designer", "ui engineer"
    ]) and not any(k in combined for k in ["backend", "full stack", "fullstack"]):
        return "frontend"

    # 6. Backend Developer
    if any(k in combined for k in [
        "backend", "back-end", "api developer", "server engineer", "node developer", "python developer"
    ]) and not any(k in combined for k in ["frontend", "full stack", "fullstack"]):
        return "backend"
        
    # Default Full Stack
    return "fullstack"

def calculate_ats_match(job_title: str, job_description: str) -> Dict[str, Any]:
    """
    Calculate ATS match score between job and Venu's resume.
    Returns match percentage, role persona, matched skills, missing skills, and recommendations.
    """
    profile = parse_resume()
    resume_skills_lower = get_skill_set()
    role_persona = detect_target_role(job_title, job_description)
    
    combined_jd_text = f"{job_title} {job_description}"
    jd_skills = extract_tech_keywords_from_text(combined_jd_text)
    
    if not jd_skills:
        jd_skills = {"JavaScript", "Node.js", "REST APIs", "SQL"}

    matched_skills = []
    missing_skills = []
    
    for skill in sorted(jd_skills):
        skill_lower = skill.lower()
        if (skill_lower in resume_skills_lower or 
            any(w in profile["raw_text"].lower() for w in skill_lower.split())):
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    skill_score = (len(matched_skills) / max(len(jd_skills), 1)) * 60

    title_lower = job_title.lower()
    title_score = 0
    if role_persona == "hft":
        title_score = 25 if any(k in title_lower for k in ["hft", "low latency", "systems", "rust", "c++"]) else 15
    elif role_persona == "ai_engineer":
        title_score = 25 if any(k in title_lower for k in ["ai", "speech", "ml", "python"]) else 15
    elif role_persona == "fde":
        title_score = 25 if any(k in title_lower for k in ["forward", "solutions", "engineer", "client"]) else 15
    elif role_persona == "sap_abap":
        title_score = 20 if any(k in title_lower for k in ["sap", "abap", "integration"]) else 12
    elif role_persona == "backend":
        title_score = 25 if any(k in title_lower for k in ["backend", "node", "python", "api"]) else 15
    elif role_persona == "frontend":
        title_score = 25 if any(k in title_lower for k in ["frontend", "react", "ui", "web"]) else 15
    else:
        title_score = 20

    base_bonus = 15
    total_score = min(int(skill_score + title_score + base_bonus), 98)
    total_score = max(total_score, 30)

    if total_score >= 80:
        match_tier = "High Match"
        tier_color = "emerald"
    elif total_score >= 60:
        match_tier = "Strong Match"
        tier_color = "blue"
    elif total_score >= 40:
        match_tier = "Moderate Match"
        tier_color = "amber"
    else:
        match_tier = "Growth Role"
        tier_color = "purple"

    recommendations = []
    if role_persona == "hft":
        recommendations.append("Emphasize Rust systems programming in Voxa, microsecond CPAL audio streaming, zero-copy concepts, and backoff jitter rate-limiting.")
    elif role_persona == "ai_engineer":
        recommendations.append("Lead with your Voxa architecture: local-first Rust/Python audio capture, NVIDIA Parakeet inference, and custom dictionary tuning.")
    elif role_persona == "fde":
        recommendations.append("Emphasize your TCS client-facing delivery: direct stakeholder collaboration, CSOD enterprise integrations, and rapid SIT/UAT execution.")
    elif role_persona == "sap_abap":
        recommendations.append("Highlight enterprise platform integrations (OData/REST APIs, CSOD, high-volume PostgreSQL/SQLite data pipelines) and rate-limiting controls.")
    elif role_persona == "backend":
        recommendations.append("Lead with high-scale API optimizations: 1-min to <15s latency reduction, rate-limiting jitter/backoff, and 10K+ DAU scalability.")
    elif role_persona == "frontend":
        recommendations.append("Highlight modern UI workflows: React, Vite, Tailwind CSS, component modularity, dynamic form validation engines, and Vercel deployments.")
    else:
        recommendations.append("Emphasize end-to-end full stack breadth: React/Tailwind frontends interfacing with high-throughput Node.js/PostgreSQL backends.")

    if missing_skills:
        recommendations.append(f"Review or bridge missing JD keywords: {', '.join(missing_skills[:4])}.")

    persona_labels = {
        "hft": "HFT & Low-Latency Systems",
        "ai_engineer": "AI / Speech Engineer",
        "fde": "Forward Deployed Engineer (FDE)",
        "sap_abap": "SAP ABAP / Enterprise Integration",
        "backend": "Backend Developer",
        "frontend": "Frontend Developer",
        "fullstack": "Full Stack Developer"
    }

    return {
        "score": total_score,
        "tier": match_tier,
        "tier_color": tier_color,
        "role_persona": role_persona,
        "persona_label": persona_labels.get(role_persona, "Full Stack Developer"),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "jd_skills_count": len(jd_skills),
        "recommendations": recommendations
    }

def generate_tailored_bullets(job_title: str, matched_skills: List[str], role_persona: str = "fullstack") -> List[str]:
    """Generate 3 tailored bullet points using the Google X-Y-Z formula tailored to the target persona."""
    bullets = []
    
    if role_persona == "hft":
        bullets.append(
            "Engineered high-performance real-time audio and inference systems in Rust utilizing CPAL and zero-cost abstractions, "
            "achieving deterministic, low-latency streaming and on-device processing with zero garbage collection overhead."
        )
        bullets.append(
            "Designed resilient rate-control algorithms utilizing progressive backoff and jitter strategies to mitigate high-load spikes, "
            "eliminating system throttling and maintaining high-throughput stability across enterprise services."
        )
        bullets.append(
            "Profiled and optimized end-to-end data processing pipelines, cutting execution latency from ~1 minute to consistently under 15 seconds "
            "while maintaining transactional consistency across distributed relational stores."
        )

    elif role_persona == "ai_engineer":
        bullets.append(
            "Engineered Voxa, an end-to-end local-first desktop AI voice application in Rust, Tauri 2, and Python, "
            "streaming low-latency microphone audio into NVIDIA Parakeet for high-accuracy local speech recognition."
        )
        bullets.append(
            "Implemented custom acoustic phrases, voice activation, and custom vocabulary dictionary handling to optimize "
            "speech recognition accuracy for Indian diction and localized speech patterns."
        )
        bullets.append(
            "Architected decoupled local inference pipelines with SQLite caching and asynchronous worker queues, "
            "enabling instant on-device text injection into desktop applications without cloud latency or API costs."
        )

    elif role_persona == "fde":
        bullets.append(
            "Partnered directly with enterprise clients and business stakeholders to translate complex domain requirements "
            "into production-ready full-stack integrations, reducing application/API load times from ~1 minute to consistently under 15 seconds."
        )
        bullets.append(
            "Engineered robust integration services and custom internal APIs connecting enterprise learning platforms (Cornerstone OnDemand / CSOD), "
            "supporting 10K+ daily active users and 200K peak transaction loads."
        )
        bullets.append(
            "Spearheaded technical delivery from initial system scoping through SIT/UAT defect triage and independent production deployments, "
            "guaranteeing 99.9% data synchronization across high-volume enterprise records."
        )

    elif role_persona == "sap_abap":
        bullets.append(
            "Architected enterprise-grade integration services and OData/REST APIs connecting external systems with core enterprise platforms, "
            "ensuring transactional consistency across high-volume relational records (PostgreSQL / SQLite)."
        )
        bullets.append(
            "Engineered custom rate-limiting and progressive backoff mechanisms with jitter algorithms, preventing system throttling "
            "and stabilizing enterprise batch data-processing workflows."
        )
        bullets.append(
            "Collaborated directly with functional business teams to automate custom validation engines, business logic rules, "
            "and event-driven notification triggers, eliminating repetitive manual data reconciliation."
        )

    elif role_persona == "frontend":
        bullets.append(
            "Developed responsive, accessible, and high-performance user interfaces and validation workflows using React, JavaScript, Vite, and Tailwind CSS."
        )
        bullets.append(
            "Engineered custom application screens, dynamic form state management, and real-time client-side business logic engines integrated with enterprise backend APIs."
        )
        bullets.append(
            "Built and deployed product showcase web applications with modern modular architectures, component reusability, and automated CI/CD deployments on Vercel."
        )

    elif role_persona == "backend":
        bullets.append(
            "Architected and optimized high-throughput REST APIs and microservices in Node.js, Express, and Python, handling 10K+ DAU and 200K peak transaction volumes."
        )
        bullets.append(
            "Reduced API and data-processing latency by over 75% (from ~1 minute to consistently under 15 seconds) through surgical database indexing and query profiling in PostgreSQL and SQLite."
        )
        bullets.append(
            "Implemented custom rate-limiting algorithms with progressive delays and backoff jitter, preventing downstream system throttling under extreme enterprise loads."
        )

    else:
        # Standard Full Stack
        bullets.append(
            "Optimized enterprise backend services and REST APIs in Node.js/Express, resolving high-load rate-limiting "
            "with progressive delay & jitter algorithms while slashing endpoint latency from ~1 minute to under 15 seconds."
        )
        bullets.append(
            "Built responsive, accessible frontend workflows and automated business validation engines using JavaScript, "
            "React, and Tailwind CSS, interfacing directly with enterprise platforms (CSOD) and relational databases."
        )
        bullets.append(
            "Engineered Voxa, a local-first desktop AI voice typing application in Rust, Tauri 2, and Python, "
            "utilizing NVIDIA Parakeet and Qwen TTS for real-time, low-latency audio capture and local inference."
        )

    return bullets

def generate_outreach_messages(
    company: str,
    job_title: str,
    matched_skills: List[str],
    role_persona: str = "fullstack"
) -> Dict[str, str]:
    """Generate persona-specific LinkedIn connection notes, cold emails, and referral pitches with verified URLs."""
    profile = parse_resume()
    name = profile.get("name", "Venu Gopal Potnuru")
    first_name = name.split()[0] if name else "Candidate"
    loc = profile.get("location", "Hyderabad, India")
    phone = profile.get("phone", "+91 95025 21952")
    email_addr = profile.get("email", "vvarun321@gmail.com")
    links = profile.get("links", {})
    li_url = links.get("linkedin", "https://www.linkedin.com/in/venu-gopal-potnuru-8b272b199")
    gh_url = links.get("github", "https://github.com/Rukutodo")
    voxa_url = links.get("voxa_github", "https://github.com/Rukutodo/voxa")
    voxa_live = links.get("voxa_live", "https://voiceflow-website-lovat.vercel.app/")
    top_skills_str = ", ".join(matched_skills[:3]) if matched_skills else "Full Stack & Distributed Systems"

    sig_block = f"""Best regards,
{name}
{loc} | {phone} | {email_addr}
LinkedIn: {li_url}
GitHub: {gh_url}"""
    if voxa_url:
        sig_block += f"\nFeatured Project (Voxa): {voxa_url}"
        if voxa_live:
            sig_block += f" (Live: {voxa_live})"


    if role_persona == "hft":
        li_note = (
            f"Hi [Name], saw {company}'s opening for {job_title}. I build high-performance systems in "
            f"Rust (real-time audio & local inference) with 2+ yrs optimizing latency from 1m to <15s at TCS. "
            f"Would love to connect! - Venu"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s {job_title} role. I engineer high-performance systems in Rust "
                f"and low-latency backend architectures at TCS. Would love to connect! - Venu"
            )

        email = f"""Subject: Application: {job_title} - Venu Gopal Potnuru (Systems & Low-Latency Engineer)

Hi [Hiring Manager / Tech Lead],

I came across {company}'s opening for {job_title} and wanted to reach out directly.

With a strong foundation in Rust systems programming and 2+ years engineering high-scale, low-latency enterprise backend pipelines:

1. Low-Latency Systems in Rust: Engineered Voxa ({voxa_url}), utilizing Rust, CPAL, and on-device models to capture low-level audio streams and execute real-time local inference with minimal memory footprint and zero cloud latency.
2. Latency Optimization & Profiling: Reduced enterprise endpoint execution time from ~1 minute to consistently under 15 seconds by profiling system bottlenecks and optimizing query execution paths.
3. High-Throughput Rate Control: Architected custom rate-limiting algorithms with progressive backoff and jitter to maintain determinism and throughput under heavy concurrent load (10K+ DAU / 200K peak load).

Given {company}'s emphasis on performance, concurrency, and reliability, I would welcome the opportunity to discuss how my systems background can contribute to your team.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope all is well! I noticed the {job_title} role open at {company} and was really impressed by the engineering standards of your team.

I'm a systems engineer with experience building low-latency applications in Rust (Voxa: {voxa_url}) and 2+ years optimizing high-throughput enterprise pipelines at TCS.

Would you be open to submitting an internal referral for me? My LinkedIn profile is {li_url} and GitHub is {gh_url}.

Thanks so much!
Best,
Venu Gopal Potnuru
"""

    elif role_persona == "frontend":
        li_note = (
            f"Hi [Name], saw {company}'s {job_title} opening. With 2+ yrs building responsive, high-performance "
            f"React & Tailwind web apps and enterprise validation engines, I'd love to connect! - Venu"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s {job_title} role. I build responsive React/Tailwind web apps "
                f"and robust enterprise UI workflows. Would love to connect! - Venu"
            )

        email = f"""Subject: Application: {job_title} - Venu Gopal Potnuru (Frontend & UI Engineer)

Hi [Hiring Manager / Engineering Lead],

I came across {company}'s opening for {job_title} and wanted to share my interest.

Over the past 2+ years building enterprise applications at TCS and consumer-facing web products:
1. Modern Frontend Architecture: Built responsive web interfaces using React, Vite, Tailwind CSS, and JavaScript, including interactive showcase platforms ({voxa_live}).
2. Enterprise Validation & UX: Developed complex client-side validation logic, dynamic form state machines, and workflow triggers interfacing with enterprise APIs.
3. Performance & Cross-Browser Consistency: Optimized UI rendering performance, component reusability, and asset loading.

I have attached my resume and would welcome a brief conversation.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope you're having a great week! I saw the {job_title} opening at {company} and wanted to reach out.

I build modern React & Tailwind web applications with strong emphasis on UI performance and responsive component design (showcase: {voxa_live}).

Would you be open to providing an internal referral? My LinkedIn is {li_url} and GitHub is {gh_url}.

Thanks so much!
Best,
Venu Gopal Potnuru
"""

    elif role_persona == "backend":
        li_note = (
            f"Hi [Name], saw {company}'s {job_title} opening. With 2+ yrs building scalable Node/Python "
            f"APIs at TCS (reduced latency from 1m to <15s, rate-limiting jitter, 10K+ DAU), I'd love to connect! - Venu"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s {job_title} role. With 2+ yrs building scalable Node/Python "
                f"APIs and optimizing latency at TCS, I'd love to connect! - Venu"
            )

        email = f"""Subject: Application: {job_title} - Venu Gopal Potnuru (Backend & API Engineer)

Hi [Hiring Manager / Backend Lead],

I came across {company}'s opening for {job_title} and wanted to reach out directly.

With 2+ years as a Backend Developer at Tata Consultancy Services (TCS), I specialize in building resilient, high-throughput backend services and data workflows:

1. Performance Optimization: Reduced enterprise API load times from ~1 minute to consistently under 15 seconds by eliminating bottlenecks and profiling query performance.
2. Resilience & Concurrency: Built custom rate-limiting algorithms with progressive backoff and jitter, supporting 10K+ DAU and 200K peak load without system throttling.
3. Data Pipelines: Designed high-volume PostgreSQL and SQLite data processing workflows and automated ingestion engines.

I have attached my resume and look forward to discussing how I can deliver immediate backend impact for {company}.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope all is well! I noticed the {job_title} opening on your team at {company}.

I'm a Backend Engineer with 2+ years at TCS focusing on scalable Node.js/Python APIs, high-volume database automation, and cutting API latency (<15s).

Would you be open to referring me for this opening? My LinkedIn is {li_url} and GitHub is {gh_url}.

Thank you for your time!
Best,
Venu Gopal Potnuru
"""

    elif role_persona == "ai_engineer":
        li_note = (
            f"Hi [Name], saw {company}'s opening for {job_title}. I build local-first AI applications "
            f"in Rust, Python, and Tauri 2 with NVIDIA Parakeet speech pipelines, plus 2+ yrs backend experience at TCS. "
            f"Would love to connect and share ideas! - Venu"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s {job_title} role. I engineer local AI systems in Rust/Python "
                f"(NVIDIA Parakeet speech recognition) and scalable backends at TCS. Would love to connect! - Venu"
            )

        email = f"""Subject: Application: {job_title} - Venu Gopal Potnuru (AI & Systems Engineer)

Hi [Hiring Manager / Tech Lead],

I came across {company}'s opening for {job_title} and wanted to reach out directly.

With experience building local-first AI speech systems in Rust & Python, alongside 2+ years engineering high-scale enterprise backends at TCS:

1. Local-First AI Inference: Independently built Voxa (Rust + Tauri 2 + Python), a desktop AI voice-typing application integrating NVIDIA Parakeet and Qwen TTS for real-time speech recognition and text injection with zero cloud latency ({voxa_url}).
2. Acoustic & Diction Optimization: Implemented custom dictionary mappings, voice activation, and acoustic tuning specifically tailored for regional Indian diction and noisy environments.
3. High-Scale Engineering: Engineered backend REST APIs and automated data pipelines at TCS handling 10K+ DAU / 200K peak load, cutting latency from ~1m down to under 15s.

Given {company}'s focus on cutting-edge AI systems, I would love to contribute to your engineering efforts. My resume is attached, and I welcome a brief conversation.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope you're having a great week! I saw the {job_title} position open on your team at {company} and was really impressed by the work being done.

I'm an AI & Systems Engineer with experience building local-first speech recognition pipelines in Rust/Python (NVIDIA Parakeet, Qwen TTS) and 2+ years of enterprise backend engineering at TCS.

Would you be open to submitting a referral for me? You can check out my project at {voxa_url} and my profile at {li_url}.

Thank you so much!
Best,
Venu Gopal Potnuru
"""

    elif role_persona == "fde":
        li_note = (
            f"Hi [Name], noticed {company}'s Forward Deployed Engineer role. With 2+ yrs at TCS driving "
            f"direct client integrations, reducing enterprise API latency from 1m to <15s, and building AI tools in Rust, "
            f"I'd love to connect! - Venu"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s FDE role. At TCS, I partner directly with enterprise clients "
                f"to deploy scalable APIs (cut load time from 1m to <15s) and build AI tools. Would love to connect! - Venu"
            )

        email = f"""Subject: Forward Deployed Engineer ({job_title}) - Venu Gopal Potnuru

Hi [Hiring Manager / Solutions Lead],

I noticed {company}'s opening for {job_title}. As an engineer who thrives at the intersection of technical architecture, client collaboration, and high-velocity execution, I wanted to introduce myself.

Over the past 2+ years as a Full Stack Engineer at Tata Consultancy Services (TCS):
1. Client-Facing Problem Solving: Partnered directly with enterprise clients and business stakeholders to translate operational rules into robust software solutions and automated workflows.
2. Platform & API Integration: Built custom backend integrations connecting enterprise platforms (Cornerstone OnDemand / CSOD), reducing API latency from ~1 minute to under 15 seconds for 10K+ DAU / 200K peak volume.
3. Rapid Prototyping to Production: Engineered Voxa from scratch (Rust + Tauri 2 + local AI speech models), handling end-to-end SDLC through testing and public releases ({voxa_url}).

I thrive in forward deployed environments where solving ambiguous client challenges requires both strong engineering fundamentals and fast execution.

I've attached my resume and would welcome 10 minutes to discuss how I can deliver value for {company}'s clients.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope all is well! I noticed the Forward Deployed Engineer ({job_title}) opening at {company} and wanted to reach out.

I specialize in client solutions engineering and enterprise integrations, with 2+ years at TCS working directly with stakeholders to deliver high-performance APIs and data automation, alongside building local AI applications in Rust/Python.

Would you be open to providing an internal referral for this opening? My LinkedIn is {li_url} and my GitHub is {gh_url}.

Thanks for your time!
Best,
Venu Gopal Potnuru
"""

    elif role_persona == "sap_abap":
        li_note = (
            f"Hi [Name], saw {company}'s {job_title} opening. With 2+ yrs at TCS building enterprise "
            f"OData/REST integrations, high-volume PostgreSQL/SQLite data workflows, and rate-limiting controls, "
            f"I'd love to connect! - Venu"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s {job_title} role. With 2+ yrs at TCS delivering enterprise "
                f"OData/API integrations and high-volume data workflows, I'd love to connect! - Venu"
            )

        email = f"""Subject: Application: {job_title} - Venu Gopal Potnuru (Enterprise Integration Engineer)

Hi [Hiring Manager / Team Lead],

I am writing to express my interest in the {job_title} role at {company}.

With 2+ years of experience in enterprise application platforms and high-volume data integrations at Tata Consultancy Services (TCS):

1. Enterprise Platform & OData Integrations: Built and maintained mission-critical backend services interfacing with enterprise platforms (CSOD APIs, OData/REST services) for 10K+ DAU and 200K peak load.
2. High-Volume Data & Batch Processing: Designed data-processing solutions using PostgreSQL and SQLite; built automation to retrieve, validate, and load enterprise records, eliminating manual intervention.
3. Resilience & Rate-Control: Solved enterprise API rate-limiting issues using progressive delay, jitter, and backoff algorithms, reducing overall system latency from ~1 minute to under 15 seconds.

I have attached my resume and would welcome the opportunity to discuss how my enterprise background aligns with {company}'s integration needs.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope you're doing well! I came across the {job_title} opening at {company}.

I have 2+ years of experience at TCS specializing in enterprise platform integrations (OData/REST), high-volume database automation, and resilient rate-limiting architectures.

Would you be willing to refer me for this opening? Happy to share my resume (profile: {li_url}).

Thanks so much!
Best,
Venu Gopal Potnuru
"""

    else:
        # Standard Full Stack
        li_note = (
            f"Hi [Name], I noticed {company}'s opening for {job_title}. With 2+ yrs building high-scale "
            f"Node/Python APIs at TCS (reduced latency from 1m to <15s) and local-first AI apps in Rust, "
            f"I'd love to connect and contribute! - Venu Gopal"
        )
        if len(li_note) > 295:
            li_note = (
                f"Hi [Name], saw {company}'s {job_title} role. With 2+ yrs experience in Node.js, "
                f"Python, and scalable APIs at TCS, I'd love to connect and learn more about your team! - Venu"
            )

        email = f"""Subject: Application: {job_title} - Venu Gopal Potnuru (Full Stack & Systems Engineer)

Hi [Hiring Manager / Recruiter Name],

I came across the {job_title} role at {company} and wanted to reach out directly. 

With 2+ years of experience as a Full Stack Developer at Tata Consultancy Services (TCS), I specialize in building resilient backend systems, performance optimization, and platform integrations:

1. High-Scale API Performance: Engineered backend microservices and REST APIs supporting 10K+ DAU / 200K peak load, cutting latency from ~1 minute down to under 15 seconds.
2. Robust Engineering: Built custom rate-limiting algorithms with progressive backoff/jitter, and automated high-volume PostgreSQL/SQLite data pipelines.
3. AI & Systems Innovation: Independently built Voxa (Rust + Tauri + Python), a local-first AI voice-typing desktop app utilizing NVIDIA Parakeet and Qwen TTS for real-time inference ({voxa_url}).

Given your team's focus, I believe my background with {top_skills_str} would allow me to make an immediate impact from day one.

I have attached my resume and would welcome 10 minutes to discuss how my skillset aligns with {company}'s goals.

{sig_block}
"""

        referral = f"""Hi [First Name],

Hope you're doing well! I've been following {company}'s work and saw the {job_title} opening on your team.

I'm a Full Stack Developer with 2+ years at TCS working extensively with Node.js, Python, and PostgreSQL, along with Rust/Tauri for AI voice applications ({voxa_url}). In my current role, I optimized core enterprise APIs from 1-min load down to <15s and designed high-throughput rate-limiting solutions.

Would you be open to passing my resume along for a referral? My LinkedIn is {li_url} and GitHub is {gh_url}.

Thanks so much for your time!
Best,
Venu Gopal Potnuru
"""

    return {
        "linkedin_connection": li_note,
        "cold_email": email.strip(),
        "referral_pitch": referral.strip()
    }

async def generate_with_gemini(
    company: str,
    job_title: str,
    jd_text: str,
    api_key: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """
    Call Google Gemini 2.5 Flash API to generate hyper-personalized bullets and outreach
    if an API key is provided.
    """
    gemini_key = api_key or os.environ.get("GEMINI_API_KEY")
    if not gemini_key:
        return None

    profile = parse_resume()
    links = profile.get("links", {})
    li_url = links.get("linkedin", "https://www.linkedin.com/in/venu-gopal-potnuru-8b272b199")
    gh_url = links.get("github", "https://github.com/Rukutodo")
    voxa_url = links.get("voxa_github", "https://github.com/Rukutodo/voxa")

    prompt = f"""
You are an expert executive resume writer and career strategist. 
Write tailored job application materials for Venu Gopal Potnuru for the following role:

Target Company: {company}
Target Role: {job_title}
Job Description:
{jd_text[:3500]}

Candidate Resume Summary:
Name: Venu Gopal Potnuru
Experience: 2+ years at Tata Consultancy Services (TCS) as Assistant System Engineer / Full Stack Developer.
TCS Achievements:
- Supported enterprise platform with Cornerstone OnDemand (CSOD) integration, 10K DAU, 200K peak load.
- Reduced API/application load time from ~1 minute to under 15 seconds.
- Solved API rate limiting with custom jitter, progressive delays, and backoff algorithms.
- Designed high-volume PostgreSQL and SQLite data processing workflows and automated ingestion.
- Worked directly with clients and business stakeholders to clarify business rules; SIT/UAT validation.
Personal Project - Voxa:
- Local-first desktop AI voice typing application in Rust, Tauri 2, Python, SQLite ({voxa_url}).
- Used NVIDIA Parakeet and Qwen TTS for real-time speech-to-text inference with custom vocabulary tuning for Indian diction.
Verified Links:
LinkedIn: {li_url}
GitHub: {gh_url}
Voxa Project: {voxa_url}

Generate JSON with the following exact keys:
1. "bullets": Array of 3 tailored resume bullets formatted in Google X-Y-Z formula highlighting metrics.
2. "linkedin_connection": A warm, high-converting LinkedIn connection note STRICTLY under 295 characters.
3. "cold_email": A professional, high-impact cold email to the hiring manager including the verified links.
4. "referral_pitch": A polite, friendly note to an employee at {company} asking for a referral.

Output ONLY valid JSON.
"""

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.4, "responseMimeType": "application/json"}
        }
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json=payload, timeout=20.0)
            if resp.status_code == 200:
                data = resp.json()
                text_out = data["candidates"][0]["content"]["parts"][0]["text"]
                return json.loads(text_out)
    except Exception as e:
        print(f"[Warning] Gemini API error: {e}")
    return None
