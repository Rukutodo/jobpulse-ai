"""
Curated directory of Top Product MNCs, HFT Firms, Fast-Growing Unicorns, Enterprise/SAP Hubs,
and AI Labs with 100% free, direct un-paywalled career boards (Greenhouse, Lever, Ashby, Direct ATS).
"""
from typing import List, Dict, Any
import urllib.parse

def make_google_jobs_url(company_name: str, keywords: str = "Software Engineer OR Developer") -> str:
    """Build a direct un-paywalled Google Jobs search query link."""
    query = f'{company_name} ({keywords}) ("Full Stack" OR "Backend" OR "Frontend" OR "AI" OR "Rust" OR "Python" OR "SAP")'
    return f"https://www.google.com/search?q={urllib.parse.quote(query)}&ibp=htl;jobs"

COMPANY_DIRECTORY: List[Dict[str, Any]] = [
    # ----------------------------------------------------
    # 1. HFT & Quantitative Trading Firms
    # ----------------------------------------------------
    {
        "id": "citadel",
        "name": "Citadel & Citadel Securities",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "World-leading market maker and quantitative trading powerhouse.",
        "locations": ["Gurugram", "Singapore", "London", "New York", "Remote"],
        "ats": "Direct",
        "careers_url": "https://www.citadel.com/careers/open-roles/",
        "google_jobs_url": make_google_jobs_url("Citadel", "Quantitative Developer OR Software Engineer"),
        "tech_stack": ["C++", "Rust", "Low Latency", "Python", "Distributed Systems"],
        "priority_roles": ["Software Engineer", "Quant Developer", "Systems Engineer"]
    },
    {
        "id": "jane_street",
        "name": "Jane Street",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "Quantitative trading firm operating around the clock and across globe.",
        "locations": ["Singapore", "Hong Kong", "London", "New York"],
        "ats": "Direct",
        "careers_url": "https://www.janestreet.com/join-jane-street/open-roles/",
        "google_jobs_url": make_google_jobs_url("Jane Street", "Software Engineer"),
        "tech_stack": ["OCaml", "C++", "Rust", "Low Latency", "Systems"],
        "priority_roles": ["Software Engineer", "Systems Architect"]
    },
    {
        "id": "tower_research",
        "name": "Tower Research Capital",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "High-frequency algorithmic trading pioneer with huge engineering presence in India.",
        "locations": ["Gurugram", "Bengaluru", "Singapore", "New York"],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/towerresearchcapital",
        "google_jobs_url": make_google_jobs_url("Tower Research Capital", "Software Engineer OR Systems Developer"),
        "tech_stack": ["C++", "Linux", "Low Latency", "Python", "Concurrency"],
        "priority_roles": ["Systems Engineer", "Quant Developer", "Core Trading Engineer"]
    },
    {
        "id": "jump_trading",
        "name": "Jump Trading",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "Global research-driven quantitative trading firm.",
        "locations": ["Singapore", "London", "Chicago", "Sydney"],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/jumptrading",
        "google_jobs_url": make_google_jobs_url("Jump Trading", "Software Engineer"),
        "tech_stack": ["C++", "Rust", "FPGA", "Low Latency", "High Throughput"],
        "priority_roles": ["Core Engineering", "Software Engineer"]
    },
    {
        "id": "hrt",
        "name": "Hudson River Trading (HRT)",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "Multi-asset class quantitative trading firm at the forefront of automated trading.",
        "locations": ["Singapore", "London", "New York", "Remote"],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/hudsonrivertrading",
        "google_jobs_url": make_google_jobs_url("Hudson River Trading", "Software Engineer"),
        "tech_stack": ["C++", "Python", "Linux Kernel", "Low Latency"],
        "priority_roles": ["Core Software Engineer", "Algorithm Engineer"]
    },
    {
        "id": "graviton",
        "name": "Graviton Research Capital",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "Leading algorithmic trading firm headquartered in India.",
        "locations": ["Gurugram", "Bengaluru"],
        "ats": "Direct",
        "careers_url": "https://www.gravitonresearch.com/careers",
        "google_jobs_url": make_google_jobs_url("Graviton Research Capital", "Software Engineer"),
        "tech_stack": ["C++", "Low Latency", "Linux", "Distributed Architecture"],
        "priority_roles": ["Quantitative Software Engineer", "Systems Developer"]
    },
    {
        "id": "de_shaw",
        "name": "D. E. Shaw & Co.",
        "category": "hft",
        "category_label": "HFT & Quant",
        "tagline": "Global investment and technology development firm with major Hyderabad hub.",
        "locations": ["Hyderabad", "Bengaluru", "New York", "London"],
        "ats": "Direct",
        "careers_url": "https://www.deshawindia.com/careers",
        "google_jobs_url": make_google_jobs_url("D. E. Shaw", "Member Technical OR Software Engineer"),
        "tech_stack": ["Python", "C++", "Java", "Distributed Systems", "Full Stack"],
        "priority_roles": ["Member Technical", "Senior Software Developer"]
    },

    # ----------------------------------------------------
    # 2. Tier-1 Product MNCs & Tech Giants
    # ----------------------------------------------------
    {
        "id": "google",
        "name": "Google",
        "category": "mnc",
        "category_label": "Top Tech MNC",
        "tagline": "Organizing world's information with hyper-scale systems and AI infrastructure.",
        "locations": ["Hyderabad", "Bengaluru", "Pune", "Gurugram", "Remote"],
        "ats": "Direct",
        "careers_url": "https://www.google.com/about/careers/applications/jobs/results/?location=India",
        "google_jobs_url": make_google_jobs_url("Google", "Software Engineer"),
        "tech_stack": ["Go", "C++", "Java", "Python", "Distributed Systems"],
        "priority_roles": ["Software Engineer (L3/L4)", "Application Engineer"]
    },
    {
        "id": "microsoft",
        "name": "Microsoft",
        "category": "mnc",
        "category_label": "Top Tech MNC",
        "tagline": "Empowering every person and organization on the planet to achieve more.",
        "locations": ["Hyderabad", "Bengaluru", "Noida", "Remote"],
        "ats": "Direct",
        "careers_url": "https://jobs.careers.microsoft.com/global/en/search?lc=India",
        "google_jobs_url": make_google_jobs_url("Microsoft", "Software Engineer"),
        "tech_stack": ["TypeScript", "C#", "Azure", "React", "Python"],
        "priority_roles": ["Software Engineer II", "Full Stack Developer"]
    },
    {
        "id": "amazon",
        "name": "Amazon",
        "category": "mnc",
        "category_label": "Top Tech MNC",
        "tagline": "Earth's most customer-centric company and AWS cloud platform provider.",
        "locations": ["Hyderabad", "Bengaluru", "Chennai", "Pune", "Remote"],
        "ats": "Direct",
        "careers_url": "https://www.amazon.jobs/en/locations/hyderabad-india",
        "google_jobs_url": make_google_jobs_url("Amazon", "Software Development Engineer"),
        "tech_stack": ["Java", "AWS", "Python", "Microservices", "React"],
        "priority_roles": ["SDE I", "SDE II", "Front End Engineer"]
    },
    {
        "id": "uber",
        "name": "Uber",
        "category": "mnc",
        "category_label": "Top Tech MNC",
        "tagline": "Reimagining mobility and logistics through high-throughput real-time systems.",
        "locations": ["Hyderabad", "Bengaluru", "Remote"],
        "ats": "Direct",
        "careers_url": "https://www.uber.com/in/en/careers/list/?location=IND--Hyderabad",
        "google_jobs_url": make_google_jobs_url("Uber", "Software Engineer"),
        "tech_stack": ["Go", "Java", "React", "Kafka", "Microservices"],
        "priority_roles": ["Software Engineer II", "Backend Engineer"]
    },
    {
        "id": "atlassian",
        "name": "Atlassian",
        "category": "mnc",
        "category_label": "Top Tech MNC",
        "tagline": "Building Jira, Confluence, and collaboration tools with a remote-first culture.",
        "locations": ["Bengaluru", "Remote (India)", "Sydney"],
        "ats": "Direct",
        "careers_url": "https://www.atlassian.com/company/careers/bengaluru",
        "google_jobs_url": make_google_jobs_url("Atlassian", "Software Engineer"),
        "tech_stack": ["React", "Node.js", "Java", "AWS", "Microservices"],
        "priority_roles": ["Full Stack Engineer", "Backend Developer"]
    },
    {
        "id": "meta",
        "name": "Meta",
        "category": "mnc",
        "category_label": "Top Tech MNC",
        "tagline": "Connecting billions across WhatsApp, Instagram, Facebook, and AI systems.",
        "locations": ["Hyderabad", "Bengaluru", "Gurugram", "London", "Remote"],
        "ats": "Direct",
        "careers_url": "https://www.metacareers.com/jobs/?locations[0]=India",
        "google_jobs_url": make_google_jobs_url("Meta", "Software Engineer"),
        "tech_stack": ["React", "Python", "C++", "GraphQL", "Distributed Systems"],
        "priority_roles": ["Software Engineer", "Solutions Engineer"]
    },

    # ----------------------------------------------------
    # 3. High-Growth Product Unicorns & Fintech
    # ----------------------------------------------------
    {
        "id": "stripe",
        "name": "Stripe",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "tagline": "Financial infrastructure for the internet powering millions of businesses.",
        "locations": ["Bengaluru", "Remote", "Singapore", "US"],
        "ats": "Direct",
        "careers_url": "https://stripe.com/jobs/search",
        "google_jobs_url": make_google_jobs_url("Stripe", "Software Engineer"),
        "tech_stack": ["Ruby", "TypeScript", "React", "Go", "Distributed APIs"],
        "priority_roles": ["Backend Engineer", "Full Stack Engineer"]
    },
    {
        "id": "razorpay",
        "name": "Razorpay",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "tagline": "Leading payments and financial services platform in India.",
        "locations": ["Bengaluru", "Remote"],
        "ats": "Direct",
        "careers_url": "https://razorpay.com/jobs/",
        "google_jobs_url": make_google_jobs_url("Razorpay", "Software Engineer"),
        "tech_stack": ["Node.js", "Go", "React", "PostgreSQL", "Kafka"],
        "priority_roles": ["Software Engineer II", "Full Stack Developer"]
    },
    {
        "id": "zepto",
        "name": "Zepto",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "tagline": "India's fastest-growing quick-commerce tech platform.",
        "locations": ["Bengaluru", "Mumbai"],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/zepto",
        "google_jobs_url": make_google_jobs_url("Zepto", "Software Engineer"),
        "tech_stack": ["Node.js", "Go", "React", "Microservices", "PostgreSQL"],
        "priority_roles": ["SDE II", "Backend Engineer", "Frontend Engineer"]
    },
    {
        "id": "swiggy",
        "name": "Swiggy",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "tagline": "Convenience platform delivering food, grocery, and dining experiences.",
        "locations": ["Bengaluru", "Hyderabad", "Remote"],
        "ats": "Direct",
        "careers_url": "https://careers.swiggy.com/",
        "google_jobs_url": make_google_jobs_url("Swiggy", "Software Engineer"),
        "tech_stack": ["Go", "Java", "React Native", "Kafka", "AWS"],
        "priority_roles": ["Software Development Engineer", "Backend Developer"]
    },
    {
        "id": "palantir",
        "name": "Palantir Technologies",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "tagline": "Pioneering enterprise data platforms and Forward Deployed Engineering (FDE).",
        "locations": ["London", "New York", "Remote", "Tokyo"],
        "ats": "Lever",
        "careers_url": "https://jobs.lever.co/palantir",
        "google_jobs_url": make_google_jobs_url("Palantir", "Forward Deployed Engineer OR Software Engineer"),
        "tech_stack": ["TypeScript", "Python", "Java", "React", "Enterprise Integrations"],
        "priority_roles": ["Forward Deployed Engineer (FDE)", "Software Engineer"]
    },
    {
        "id": "databricks",
        "name": "Databricks",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "tagline": "Unified data and AI company built on Apache Spark and Lakehouse.",
        "locations": ["Bengaluru", "Remote", "San Francisco"],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/databricks",
        "google_jobs_url": make_google_jobs_url("Databricks", "Software Engineer"),
        "tech_stack": ["Scala", "Python", "Go", "React", "Distributed Data"],
        "priority_roles": ["Software Engineer", "Solutions Architect"]
    },

    # ----------------------------------------------------
    # 4. Enterprise Tech, ERP & SAP Ecosystem
    # ----------------------------------------------------
    {
        "id": "sap_labs",
        "name": "SAP Labs",
        "category": "enterprise_sap",
        "category_label": "Enterprise / SAP",
        "tagline": "World market leader in enterprise software, ERP, S/4HANA, and BTP.",
        "locations": ["Bengaluru", "Gurugram", "Pune", "Hyderabad"],
        "ats": "Direct",
        "careers_url": "https://jobs.sap.com/search/?createNewAlert=false&q=developer&locationsearch=India",
        "google_jobs_url": make_google_jobs_url("SAP Labs", "Developer OR ABAP OR Cloud"),
        "tech_stack": ["SAP ABAP", "OData", "SAP BTP", "Node.js", "Java", "React"],
        "priority_roles": ["Developer Associate", "Senior Developer", "Integration Specialist"]
    },
    {
        "id": "jnj",
        "name": "Johnson & Johnson",
        "category": "enterprise_sap",
        "category_label": "Enterprise / SAP",
        "tagline": "Global healthcare enterprise with massive technology and LMS integrations.",
        "locations": ["Hyderabad", "Bengaluru", "Mumbai", "Remote"],
        "ats": "Workday",
        "careers_url": "https://jobs.jnj.com/en/jobs/?search=software&country=India",
        "google_jobs_url": make_google_jobs_url("Johnson & Johnson", "Software Engineer OR Technology Analyst"),
        "tech_stack": ["Node.js", "JavaScript", "CSOD", "REST APIs", "PostgreSQL"],
        "priority_roles": ["Software Engineer", "IT Analyst"]
    },
    {
        "id": "accenture",
        "name": "Accenture",
        "category": "enterprise_sap",
        "category_label": "Enterprise / SAP",
        "tagline": "Global professional services company with massive SAP & cloud practices.",
        "locations": ["Hyderabad", "Bengaluru", "Pune", "Chennai", "Noida"],
        "ats": "Direct",
        "careers_url": "https://www.accenture.com/in-en/careers/jobsearch?jk=software%20engineer&sb=1",
        "google_jobs_url": make_google_jobs_url("Accenture", "Software Engineer OR SAP Developer"),
        "tech_stack": ["SAP ABAP", "Full Stack", "Node.js", "Cloud Integrations"],
        "priority_roles": ["Application Developer", "Integration Consultant"]
    },
    {
        "id": "deloitte",
        "name": "Deloitte",
        "category": "enterprise_sap",
        "category_label": "Enterprise / SAP",
        "tagline": "Global enterprise consulting and digital transformation leader.",
        "locations": ["Hyderabad", "Bengaluru", "Mumbai", "Gurugram"],
        "ats": "Direct",
        "careers_url": "https://usijobs.deloitte.com/careersUSI/SearchJobs",
        "google_jobs_url": make_google_jobs_url("Deloitte", "Software Engineer OR Solutions Consultant"),
        "tech_stack": ["SAP S/4HANA", "Full Stack", "APIs", "Data Pipelines"],
        "priority_roles": ["Solutions Engineer", "Consultant"]
    },

    # ----------------------------------------------------
    # 5. Frontier AI Labs & Applied AI
    # ----------------------------------------------------
    {
        "id": "openai",
        "name": "OpenAI",
        "category": "ai",
        "category_label": "AI Labs",
        "tagline": "Creating safe, beneficial artificial general intelligence.",
        "locations": ["Remote", "San Francisco", "London", "Tokyo"],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/openai",
        "google_jobs_url": make_google_jobs_url("OpenAI", "Software Engineer"),
        "tech_stack": ["Python", "PyTorch", "Rust", "Distributed Systems", "TypeScript"],
        "priority_roles": ["Member of Technical Staff", "Full Stack Engineer"]
    },
    {
        "id": "anthropic",
        "name": "Anthropic",
        "category": "ai",
        "category_label": "AI Labs",
        "tagline": "AI safety and research company building reliable, steerable AI systems (Claude).",
        "locations": ["Remote", "San Francisco", "London"],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/anthropic",
        "google_jobs_url": make_google_jobs_url("Anthropic", "Software Engineer"),
        "tech_stack": ["Python", "Rust", "TypeScript", "Distributed Training"],
        "priority_roles": ["Systems Engineer", "Full Stack Engineer"]
    },
    {
        "id": "perplexity",
        "name": "Perplexity AI",
        "category": "ai",
        "category_label": "AI Labs",
        "tagline": "Where knowledge begins: AI-powered conversational answer engine.",
        "locations": ["San Francisco", "Remote"],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/perplexity",
        "google_jobs_url": make_google_jobs_url("Perplexity AI", "Software Engineer"),
        "tech_stack": ["Python", "React", "Rust", "FastAPI", "Vector Search"],
        "priority_roles": ["Full Stack Engineer", "Backend / AI Systems"]
    },
    {
        "id": "elevenlabs",
        "name": "ElevenLabs",
        "category": "ai",
        "category_label": "AI Labs",
        "tagline": "Voice AI research and deployment: realistic Text-to-Speech and voice models.",
        "locations": ["London", "Remote", "New York"],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/elevenlabs",
        "google_jobs_url": make_google_jobs_url("ElevenLabs", "Audio Engineer OR Software Engineer"),
        "tech_stack": ["Python", "C++", "Rust", "Audio Processing", "TTS/ASR"],
        "priority_roles": ["Speech AI Engineer", "Systems Engineer"]
    }
]

def get_companies(category: str = "all", search: str = "") -> List[Dict[str, Any]]:
    """Filter company directory by category and search term."""
    results = []
    search_lower = search.strip().lower()
    
    for comp in COMPANY_DIRECTORY:
        if category != "all" and comp["category"] != category:
            continue
            
        if search_lower:
            match_found = (
                search_lower in comp["name"].lower() or
                search_lower in comp["tagline"].lower() or
                any(search_lower in loc.lower() for loc in comp["locations"]) or
                any(search_lower in t.lower() for t in comp["tech_stack"]) or
                any(search_lower in r.lower() for r in comp["priority_roles"])
            )
            if not match_found:
                continue
                
        results.append(comp)
        
    return results
