"""
Curated directory of 130+ Top Product MNCs, HFT Desks, Fast-Growing Unicorns, 
Enterprise/SAP Hubs, Global GCCs, European Tech Giants, and Top IT Services paying 10 LPA+
with 100% free, direct un-paywalled career boards (Greenhouse, Lever, Ashby, Workday, Direct ATS).
"""
from typing import List, Dict, Any
import urllib.parse

def make_google_jobs_url(company_name: str, keywords: str = "Software Engineer OR Developer") -> str:
    """Build a direct un-paywalled Google Jobs search query link."""
    query = f'{company_name} ({keywords}) ("Full Stack" OR "Backend" OR "Frontend" OR "AI" OR "Cloud" OR "Python" OR "Java")'
    return f"https://www.google.com/search?q={urllib.parse.quote(query)}&ibp=htl;jobs"

COMPANY_DIRECTORY: List[Dict[str, Any]] = [
    {
        "id": "tcs",
        "name": "Tata Consultancy Services (TCS)",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 15+ LPA (Digital / Prime / Innovator)",
        "tagline": "India's largest IT multinational with specialized high-compensation Digital, Prime, and Innovator wings.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Mumbai",
            "Pune",
            "Chennai",
            "Kolkata"
        ],
        "ats": "Direct",
        "careers_url": "https://www.tcs.com/careers/india",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "React",
            "Python",
            "Cloud",
            "SAP",
            "Microservices"
        ],
        "priority_roles": [
            "Software Engineer",
            "Digital Specialist",
            "System Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Tata%20Consultancy%20Services%20%28TCS%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "infosys",
        "name": "Infosys",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9.5 - 16+ LPA (Power Programmer / SP)",
        "tagline": "Global consulting and next-generation services leader with elite Power Programmer and Specialist units.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Chennai",
            "Mysuru",
            "Chandigarh"
        ],
        "ats": "Direct",
        "careers_url": "https://www.infosys.com/careers/",
        "tech_stack": [
            "Java",
            "Python",
            "Go",
            "Cloud Native",
            "React",
            "Full Stack",
            "Spring Boot"
        ],
        "priority_roles": [
            "Specialist Programmer",
            "Power Programmer",
            "Tech Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Infosys%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "wipro",
        "name": "Wipro",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 15+ LPA (Turbo / Elite / Principal)",
        "tagline": "Leading technology services firm with specialized Digital & Cloud transformation practices.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Chennai",
            "Noida",
            "Kolkata"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.wipro.com/",
        "tech_stack": [
            "Cloud",
            "Java",
            "Microservices",
            "DevOps",
            "React",
            "Full Stack"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Full Stack Developer",
            "Technical Specialist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Wipro%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cognizant",
        "name": "Cognizant (CTS)",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "8.5 - 16+ LPA (GenC Next / Associate)",
        "tagline": "Global professional services giant modernizing business, operations, and IT models.",
        "locations": [
            "Chennai",
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Kolkata",
            "Coimbatore"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.cognizant.com/global/en",
        "tech_stack": [
            "React",
            "Node.js",
            "Spring Boot",
            "AWS",
            "Azure",
            "Microservices"
        ],
        "priority_roles": [
            "Associate Software Engineer",
            "Full Stack Developer",
            "Cloud Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Cognizant%20%28CTS%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "accenture",
        "name": "Accenture",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9.5 - 20+ LPA (Advanced Tech / Cloud)",
        "tagline": "Global professional services company with leading capabilities in digital, cloud, and security.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Mumbai",
            "Pune",
            "Gurugram",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://www.accenture.com/in-en/careers",
        "tech_stack": [
            "Cloud Transformation",
            "Java",
            "SAP BTP",
            "React",
            "Microservices",
            "Python"
        ],
        "priority_roles": [
            "Software Engineering Analyst",
            "Application Developer",
            "Technical Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Accenture%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "capgemini",
        "name": "Capgemini",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 18+ LPA (Digital / Senior Engineer)",
        "tagline": "Global leader in partnering with companies to transform and manage their business through technology.",
        "locations": [
            "Bengaluru",
            "Mumbai",
            "Hyderabad",
            "Pune",
            "Chennai",
            "Noida"
        ],
        "ats": "Direct",
        "careers_url": "https://www.capgemini.com/in-en/careers/",
        "tech_stack": [
            "Full Stack",
            "Cloud",
            "Java",
            "React",
            "Microservices",
            "Spring Boot"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Cloud Developer",
            "Consultant"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Capgemini%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "ltimindtree",
        "name": "LTIMindtree",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "10 - 18+ LPA (Specialist / Lead)",
        "tagline": "Global technology consulting and digital solutions company with enterprise scale.",
        "locations": [
            "Bengaluru",
            "Mumbai",
            "Pune",
            "Hyderabad",
            "Chennai",
            "Coimbatore"
        ],
        "ats": "Direct",
        "careers_url": "https://www.ltimindtree.com/careers/",
        "tech_stack": [
            "Cloud",
            "Microservices",
            "Java",
            "Python",
            "React",
            "Data Engineering"
        ],
        "priority_roles": [
            "Specialist Developer",
            "Tech Lead",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=LTIMindtree%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "hcltech",
        "name": "HCLTech",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 16+ LPA (Digital Engineering / Lead)",
        "tagline": "Global technology company supercharging digital progress across enterprise products and platforms.",
        "locations": [
            "Noida",
            "Bengaluru",
            "Chennai",
            "Hyderabad",
            "Pune",
            "Lucknow"
        ],
        "ats": "Direct",
        "careers_url": "https://www.hcltech.com/careers",
        "tech_stack": [
            "Product Engineering",
            "Cloud Native",
            "Java",
            "IoT",
            "Full Stack",
            "Python"
        ],
        "priority_roles": [
            "Lead Software Engineer",
            "Product Specialist",
            "Solutions Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=HCLTech%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "tech_mahindra",
        "name": "Tech Mahindra",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "8.5 - 16+ LPA (Makers Lab / Enterprise)",
        "tagline": "Digital transformation provider with Makers Lab innovation centers and next-gen telecom hubs.",
        "locations": [
            "Pune",
            "Hyderabad",
            "Bengaluru",
            "Noida",
            "Mumbai",
            "Chennai"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.techmahindra.com/",
        "tech_stack": [
            "5G",
            "Cloud",
            "Java",
            "Python",
            "AI",
            "React",
            "Enterprise ERP"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Full Stack Specialist",
            "Tech Consultant"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Tech%20Mahindra%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "epam",
        "name": "EPAM Systems",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "12 - 25+ LPA (Lead / Senior Engineer)",
        "tagline": "Global engineering consultancy renowned for high-end product development and top compensation.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Pune",
            "Gurugram",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.epam.com/careers",
        "tech_stack": [
            "Distributed Systems",
            "Java",
            "Python",
            "React",
            "Go",
            "AWS",
            "Docker"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Lead Developer",
            "Solution Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=EPAM%20Systems%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "thoughtworks",
        "name": "Thoughtworks",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "12 - 26+ LPA (Lead Consultant / Senior)",
        "tagline": "Pioneering global software consultancy celebrated for agile excellence, clean architecture, and TDD.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Chennai",
            "Gurugram",
            "Coimbatore"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.thoughtworks.com/en-in/careers",
        "tech_stack": [
            "Clean Architecture",
            "TDD",
            "Microservices",
            "Python",
            "React",
            "Go",
            "Kubernetes"
        ],
        "priority_roles": [
            "Senior Consultant Developer",
            "Lead Developer",
            "Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Thoughtworks%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "persistent",
        "name": "Persistent Systems",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "10 - 20+ LPA (Product Engineering / Lead)",
        "tagline": "High-growth product engineering and digital transformation partner for global tech leaders.",
        "locations": [
            "Pune",
            "Bengaluru",
            "Hyderabad",
            "Goa",
            "Nagpur"
        ],
        "ats": "Direct",
        "careers_url": "https://www.persistent.com/careers/",
        "tech_stack": [
            "Cloud Product Engineering",
            "Java",
            "Python",
            "React",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Lead Developer",
            "Cloud Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Persistent%20Systems%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "nagarro",
        "name": "Nagarro",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "10 - 22+ LPA (Senior / Principal Engineer)",
        "tagline": "Fluidic enterprise engineering services provider delivering digital breakthrough solutions.",
        "locations": [
            "Gurugram",
            "Bengaluru",
            "Pune",
            "Jaipur",
            "Dehradun",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.nagarro.com/en/careers",
        "tech_stack": [
            "Digital Engineering",
            "Java",
            ".NET",
            "React",
            "Cloud",
            "Python"
        ],
        "priority_roles": [
            "Senior Staff Engineer",
            "Principal Developer",
            "Full Stack Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Nagarro%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "publicis_sapient",
        "name": "Publicis Sapient",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "12 - 25+ LPA (Senior Associate / Specialist)",
        "tagline": "Digital business transformation company building agile, customer-centric modern platforms.",
        "locations": [
            "Bengaluru",
            "Gurugram",
            "Noida",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.publicissapient.com/",
        "tech_stack": [
            "Microservices",
            "React",
            "Node.js",
            "Spring Boot",
            "Cloud Native",
            "Java"
        ],
        "priority_roles": [
            "Senior Associate Technology",
            "Technical Specialist",
            "Lead Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Publicis%20Sapient%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "virtusa",
        "name": "Virtusa",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9.5 - 18+ LPA (Fintech / Cloud Specialist)",
        "tagline": "Global provider of digital engineering and information technology services across banking & telecom.",
        "locations": [
            "Hyderabad",
            "Chennai",
            "Bengaluru",
            "Pune"
        ],
        "ats": "Direct",
        "careers_url": "https://www.virtusa.com/careers",
        "tech_stack": [
            "Banking APIs",
            "Cloud Native",
            "Java",
            "Angular",
            "Full Stack",
            "Spring Boot"
        ],
        "priority_roles": [
            "Lead Engineer",
            "Senior Software Engineer",
            "Cloud Consultant"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Virtusa%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "hexaware",
        "name": "Hexaware Technologies",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 16+ LPA (Digital / Cloud Lead)",
        "tagline": "Fastest growing automation-led next-generation service provider.",
        "locations": [
            "Mumbai",
            "Chennai",
            "Bengaluru",
            "Pune",
            "Noida"
        ],
        "ats": "Direct",
        "careers_url": "https://hexaware.com/careers/",
        "tech_stack": [
            "Automation",
            "Cloud",
            "Full Stack",
            "Java",
            "Python",
            "Microservices"
        ],
        "priority_roles": [
            "Senior Software Developer",
            "Tech Lead",
            "Cloud Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Hexaware%20Technologies%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "coforge",
        "name": "Coforge",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9.5 - 17+ LPA (Senior Software Engineer)",
        "tagline": "Global digital services and solutions provider with deep domain depth in airlines and insurance.",
        "locations": [
            "Noida",
            "Bengaluru",
            "Hyderabad",
            "Pune"
        ],
        "ats": "Direct",
        "careers_url": "https://www.coforge.com/careers",
        "tech_stack": [
            "Cloud Services",
            "Full Stack",
            "Microservices",
            "Java",
            "Python"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Technical Specialist",
            "Cloud Consultant"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Coforge%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "dxc",
        "name": "DXC Technology",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 16+ LPA (Enterprise Cloud & Modernization)",
        "tagline": "Fortune 500 technology services leader managing mission-critical systems and modern operations.",
        "locations": [
            "Bengaluru",
            "Chennai",
            "Hyderabad",
            "Noida",
            "Pune"
        ],
        "ats": "Workday",
        "careers_url": "https://dxc.com/us/en/careers",
        "tech_stack": [
            "Enterprise Architecture",
            "Cloud",
            "DevOps",
            "Java",
            "Python"
        ],
        "priority_roles": [
            "Professional Software Engineer",
            "Cloud Specialist",
            "System Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=DXC%20Technology%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "deloitte",
        "name": "Deloitte USI (Tech & Engineering)",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "11 - 24+ LPA (Consultant / Senior Consultant)",
        "tagline": "Big 4 technological advisory and implementation powerhouse modernizing global Fortune 500 enterprises.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Mumbai",
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://www2.deloitte.com/ui/en/pages/careers/articles/careers-deloitte.html",
        "tech_stack": [
            "Full Stack",
            "Cloud",
            "Data Engineering",
            "SAP S/4HANA",
            "Salesforce",
            "Python"
        ],
        "priority_roles": [
            "Technology Consultant",
            "Software Engineer",
            "Solutions Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Deloitte%20USI%20%28Tech%20%26%20Engineering%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "pwc",
        "name": "PwC India SDC (Technology Consulting)",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "10 - 22+ LPA (Senior Associate / Tech Lead)",
        "tagline": "High-growth technology acceleration centers driving digital engineering, cloud, and security transformation.",
        "locations": [
            "Kolkata",
            "Bengaluru",
            "Hyderabad",
            "Gurugram",
            "Mumbai"
        ],
        "ats": "Workday",
        "careers_url": "https://www.pwc.in/careers.html",
        "tech_stack": [
            "Cloud Advisory",
            "Microservices",
            "Python",
            "React",
            "Cybersecurity",
            "Java"
        ],
        "priority_roles": [
            "Senior Associate Technology",
            "Full Stack Developer",
            "Tech Specialist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=PwC%20India%20SDC%20%28Technology%20Consulting%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "ey",
        "name": "EY GDS (Technology & Innovation)",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "10 - 22+ LPA (Senior Consultant / Lead)",
        "tagline": "Global delivery network developing innovative enterprise solutions, AI tools, and cloud platforms.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Gurugram",
            "Chennai",
            "Kochi"
        ],
        "ats": "Direct",
        "careers_url": "https://www.ey.com/en_gl/careers",
        "tech_stack": [
            "AI/ML",
            "Cloud Transformation",
            "Java",
            "Spring Boot",
            "React",
            "Python"
        ],
        "priority_roles": [
            "Senior Consultant Tech",
            "Full Stack Developer",
            "Data Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=EY%20GDS%20%28Technology%20%26%20Innovation%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "kpmg",
        "name": "KPMG Global Services (Digital Lighthouse)",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "10 - 20+ LPA (Data & Software Engineer)",
        "tagline": "Center of excellence for digital engineering, analytics, AI, and enterprise tech modernization.",
        "locations": [
            "Bengaluru",
            "Gurugram",
            "Mumbai",
            "Pune",
            "Kochi"
        ],
        "ats": "Direct",
        "careers_url": "https://kpmg.com/xx/en/home/careers.html",
        "tech_stack": [
            "Analytics",
            "Cloud",
            "Python",
            "React",
            "Enterprise Architecture"
        ],
        "priority_roles": [
            "Software Engineer",
            "Data Specialist",
            "Cloud Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=KPMG%20Global%20Services%20%28Digital%20Lighthouse%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "google",
        "name": "Google",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "25 - 65+ LPA",
        "tagline": "Global technology leader in search, cloud systems, generative AI, and distributed software engineering.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Gurugram",
            "Pune",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.google.com/about/careers/applications/jobs/results/",
        "tech_stack": [
            "C++",
            "Java",
            "Python",
            "Go",
            "Distributed Systems",
            "Kubernetes"
        ],
        "priority_roles": [
            "Software Engineer (SWE)",
            "Site Reliability Engineer (SRE)",
            "AI Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Google%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "microsoft",
        "name": "Microsoft",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "22 - 58+ LPA",
        "tagline": "Empowering every organization on the planet through Azure, GitHub, Office 365, and OpenAI partnerships.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Noida",
            "Pune",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.careers.microsoft.com/global/en/search",
        "tech_stack": [
            "C#",
            ".NET",
            "C++",
            "Python",
            "Azure",
            "TypeScript",
            "React"
        ],
        "priority_roles": [
            "Software Engineer",
            "Cloud Solutions Architect",
            "Research Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Microsoft%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "amazon",
        "name": "Amazon & AWS",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "22 - 52+ LPA",
        "tagline": "Earth's most customer-centric company, pioneering AWS cloud, global logistics, and distributed microservices.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Chennai",
            "Delhi NCR",
            "Pune"
        ],
        "ats": "Direct",
        "careers_url": "https://www.amazon.jobs/en/",
        "tech_stack": [
            "Java",
            "C++",
            "Python",
            "AWS",
            "DynamoDB",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Development Engineer (SDE I/II)",
            "Cloud Support Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Amazon%20%26%20AWS%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "meta",
        "name": "Meta",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "35 - 75+ LPA",
        "tagline": "Connecting billions of people worldwide through Instagram, WhatsApp, LLaMA open models, and Quest XR.",
        "locations": [
            "Bengaluru",
            "Gurugram",
            "Hyderabad",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.metacareers.com/jobs",
        "tech_stack": [
            "C++",
            "Python",
            "Hack/PHP",
            "React",
            "PyTorch",
            "High Throughput"
        ],
        "priority_roles": [
            "Software Engineer",
            "Production Engineer",
            "Research Scientist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Meta%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "apple",
        "name": "Apple",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "25 - 60+ LPA",
        "tagline": "Crafting the world's most innovative hardware, iOS/macOS software, silicon architecture, and digital services.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.apple.com/en-in/search",
        "tech_stack": [
            "Swift",
            "C++",
            "Rust",
            "Python",
            "Distributed Systems",
            "Objective-C"
        ],
        "priority_roles": [
            "Software Development Engineer",
            "Tools Engineer",
            "Systems Software Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Apple%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "nvidia",
        "name": "Nvidia",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "25 - 65+ LPA",
        "tagline": "Pioneering accelerated computing, CUDA, GPU architecture, and generative AI infrastructure globally.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Remote"
        ],
        "ats": "Workday",
        "careers_url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite",
        "tech_stack": [
            "C++",
            "CUDA",
            "Python",
            "Deep Learning",
            "Systems Software",
            "Linux Kernel"
        ],
        "priority_roles": [
            "System Software Engineer",
            "Deep Learning Engineer",
            "Core CUDA Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Nvidia%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "adobe",
        "name": "Adobe",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "20 - 48+ LPA",
        "tagline": "Creativity and digital marketing powerhouse powering Creative Cloud, Firefly Generative AI, and Acrobat.",
        "locations": [
            "Noida",
            "Bengaluru",
            "Remote"
        ],
        "ats": "Workday",
        "careers_url": "https://careers.adobe.com/us/en",
        "tech_stack": [
            "C++",
            "Java",
            "React",
            "TypeScript",
            "Python",
            "Cloud Platform"
        ],
        "priority_roles": [
            "Software Engineer",
            "Computer Scientist",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Adobe%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "salesforce",
        "name": "Salesforce",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "20 - 45+ LPA",
        "tagline": "World's #1 AI CRM connecting companies with customers through Agentforce and Einstein AI.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Mumbai",
            "Remote"
        ],
        "ats": "Workday",
        "careers_url": "https://salesforce.wd1.myworkdayjobs.com/External_Career_Site",
        "tech_stack": [
            "Java",
            "Apex",
            "React",
            "Node.js",
            "Python",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Engineering SMTS/MTS",
            "Platform Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Salesforce%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "oracle",
        "name": "Oracle & OCI",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "18 - 42+ LPA",
        "tagline": "Enterprise technology and Oracle Cloud Infrastructure (OCI) builder powering the world's transactional data.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Noida",
            "Pune",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.oracle.com/in/corporate/careers/",
        "tech_stack": [
            "Java",
            "C++",
            "Go",
            "OCI Cloud",
            "Distributed SQL",
            "Python"
        ],
        "priority_roles": [
            "Software Developer",
            "Cloud Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Oracle%20%26%20OCI%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cisco",
        "name": "Cisco Systems",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "16 - 38+ LPA",
        "tagline": "Worldwide leader in networking, enterprise security, Webex, and cloud infrastructure.",
        "locations": [
            "Bengaluru",
            "Chennai",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.cisco.com/",
        "tech_stack": [
            "Python",
            "C++",
            "Networking",
            "Kubernetes",
            "Go",
            "Linux"
        ],
        "priority_roles": [
            "Software Engineer",
            "Cloud Native Developer",
            "Network Systems Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Cisco%20Systems%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "intuit",
        "name": "Intuit",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "22 - 48+ LPA",
        "tagline": "Global financial technology platform powering TurboTax, QuickBooks, Mint, and Credit Karma.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.intuit.com/careers/",
        "tech_stack": [
            "Java",
            "React",
            "Spring Boot",
            "AWS",
            "GraphQL",
            "Python"
        ],
        "priority_roles": [
            "Software Engineer I/II",
            "Senior Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Intuit%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "uber",
        "name": "Uber",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "25 - 60+ LPA",
        "tagline": "Reimagining how the world moves for the better through massive distributed dispatch, mapping, and mobility systems.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.uber.com/in/en/careers/list/",
        "tech_stack": [
            "Go",
            "Java",
            "Kafka",
            "Microservices",
            "React",
            "Python"
        ],
        "priority_roles": [
            "Software Engineer II",
            "Backend Engineer",
            "Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Uber%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "atlassian",
        "name": "Atlassian",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "25 - 55+ LPA",
        "tagline": "Collaboration software leader behind Jira, Confluence, Bitbucket, and Trello with Remote-First culture.",
        "locations": [
            "Bengaluru",
            "Remote (India)"
        ],
        "ats": "Direct",
        "careers_url": "https://www.atlassian.com/company/careers",
        "tech_stack": [
            "Java",
            "Kotlin",
            "React",
            "TypeScript",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Software Engineer",
            "Full Stack Developer",
            "Site Reliability Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Atlassian%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "servicenow",
        "name": "ServiceNow",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "20 - 45+ LPA",
        "tagline": "The AI platform for digital transformation across global enterprise workflows.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.servicenow.com/careers.html",
        "tech_stack": [
            "Java",
            "JavaScript",
            "React",
            "Cloud Architecture",
            "Database Systems"
        ],
        "priority_roles": [
            "Software Engineer",
            "Full Stack Engineer",
            "System Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=ServiceNow%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "qualcomm",
        "name": "Qualcomm",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "18 - 42+ LPA",
        "tagline": "Wireless technology innovator transforming smartphones, automotive, computing, and on-device AI.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Chennai",
            "Noida"
        ],
        "ats": "Workday",
        "careers_url": "https://qualcomm.wd5.myworkdayjobs.com/External",
        "tech_stack": [
            "C",
            "C++",
            "Linux Kernel",
            "Embedded Systems",
            "Python",
            "DSP"
        ],
        "priority_roles": [
            "Software Engineer",
            "Embedded Software Developer",
            "Systems Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Qualcomm%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "databricks",
        "name": "Databricks",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "30 - 70+ LPA",
        "tagline": "Data and AI company pioneering the Data Lakehouse architecture, Apache Spark, and open foundation models.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/databricks",
        "tech_stack": [
            "Scala",
            "Java",
            "Python",
            "C++",
            "Distributed Systems",
            "Kubernetes"
        ],
        "priority_roles": [
            "Software Engineer - Platform",
            "Distributed Systems Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Databricks%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "snowflake",
        "name": "Snowflake",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "30 - 70+ LPA",
        "tagline": "The Data Cloud enabling organizations to mobilize data with near-infinite scale and high concurrency.",
        "locations": [
            "Bengaluru",
            "Pune",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/snowflake",
        "tech_stack": [
            "C++",
            "Java",
            "Go",
            "FoundationDB",
            "Distributed Query",
            "Python"
        ],
        "priority_roles": [
            "Software Engineer - Core",
            "Cloud Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Snowflake%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "walmart",
        "name": "Walmart Global Tech",
        "category": "fintech_gcc",
        "category_label": "GCC & Retail Tech",
        "pay_range": "18 - 40+ LPA",
        "tagline": "Technology innovation arm of Walmart engineering massive-scale omnichannel commerce and logistics.",
        "locations": [
            "Bengaluru",
            "Chennai",
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.walmart.com/technology",
        "tech_stack": [
            "Java",
            "Kafka",
            "Spring Boot",
            "React",
            "Cloud",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Engineer II/III",
            "Full Stack Developer",
            "Data Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Walmart%20Global%20Tech%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "target",
        "name": "Target Technology",
        "category": "fintech_gcc",
        "category_label": "GCC & Retail Tech",
        "pay_range": "15 - 32+ LPA",
        "tagline": "Global capability center designing supply chain automation, guest experiences, and e-commerce.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.target.com/category/technology-jobs/460/3932/1",
        "tech_stack": [
            "Java",
            "Kotlin",
            "React",
            "Kafka",
            "PostgreSQL",
            "Cloud Native"
        ],
        "priority_roles": [
            "Lead Engineer",
            "Senior Software Engineer",
            "Frontend Specialist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Target%20Technology%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "lowes",
        "name": "Lowe's India",
        "category": "fintech_gcc",
        "category_label": "GCC & Retail Tech",
        "pay_range": "14 - 30+ LPA",
        "tagline": "Retail technology hub delivering omnichannel solutions, inventory algorithms, and cloud infrastructure.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Workday",
        "careers_url": "https://talent.lowes.com/in/en",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "React",
            "GCP",
            "Microservices",
            "Python"
        ],
        "priority_roles": [
            "Software Engineer",
            "Staff Engineer",
            "Cloud Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Lowe%27s%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "goldman_sachs",
        "name": "Goldman Sachs",
        "category": "fintech_gcc",
        "category_label": "GCC & Global Bank",
        "pay_range": "20 - 45+ LPA",
        "tagline": "Leading global investment banking, securities, and investment management firm with massive tech engineering in India.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Direct",
        "careers_url": "https://www.goldmansachs.com/careers/",
        "tech_stack": [
            "Java",
            "C++",
            "Python",
            "React",
            "Slang/SecDb",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Engineer",
            "Quant Developer",
            "Systems Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Goldman%20Sachs%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "morgan_stanley",
        "name": "Morgan Stanley",
        "category": "fintech_gcc",
        "category_label": "GCC & Global Bank",
        "pay_range": "18 - 42+ LPA",
        "tagline": "Global financial services firm advising, originating, trading, and managing capital with technology at the core.",
        "locations": [
            "Bengaluru",
            "Mumbai"
        ],
        "ats": "Direct",
        "careers_url": "https://www.morganstanley.com/careers",
        "tech_stack": [
            "Java",
            "C++",
            "Python",
            "Angular",
            "Cloud",
            "High Throughput"
        ],
        "priority_roles": [
            "Associate Software Engineer",
            "Manager Developer",
            "Platform Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Morgan%20Stanley%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "jpmorgan",
        "name": "JPMorgan Chase & Co",
        "category": "fintech_gcc",
        "category_label": "GCC & Global Bank",
        "pay_range": "16 - 38+ LPA",
        "tagline": "World's preeminent financial institution operating at massive scale across payments, asset management, and banking APIs.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Mumbai"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.jpmorgan.com/global/en/home",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "React",
            "AWS",
            "Python",
            "Kubernetes"
        ],
        "priority_roles": [
            "Software Engineer",
            "Cloud Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=JPMorgan%20Chase%20%26%20Co%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "deshaw",
        "name": "D. E. Shaw & Co.",
        "category": "fintech_gcc",
        "category_label": "GCC & Quant Investment",
        "pay_range": "25 - 60+ LPA",
        "tagline": "Pioneering quantitative investment and technology development firm with huge engineering campus in Hyderabad.",
        "locations": [
            "Hyderabad"
        ],
        "ats": "Direct",
        "careers_url": "https://www.deshawindia.com/careers",
        "tech_stack": [
            "Python",
            "C++",
            "Java",
            "Distributed Systems",
            "Linux",
            "Low Latency"
        ],
        "priority_roles": [
            "Member Technical",
            "Systems Developer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=D.%20E.%20Shaw%20%26%20Co.%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "worldquant",
        "name": "WorldQuant",
        "category": "fintech_gcc",
        "category_label": "GCC & Quant Investment",
        "pay_range": "25 - 55+ LPA",
        "tagline": "Quantitative asset management firm developing and deploying systematic financial strategies across global markets.",
        "locations": [
            "Mumbai",
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://www.worldquant.com/careers/",
        "tech_stack": [
            "Python",
            "C++",
            "Algorithms",
            "Financial Modeling",
            "Data Engineering"
        ],
        "priority_roles": [
            "Quantitative Researcher",
            "Research Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=WorldQuant%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "barclays",
        "name": "Barclays",
        "category": "fintech_gcc",
        "category_label": "GCC & Global Bank",
        "pay_range": "14 - 32+ LPA",
        "tagline": "British universal bank providing personal, corporate, investment, and wealth banking technology.",
        "locations": [
            "Pune",
            "Noida",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://search.jobs.barclays/",
        "tech_stack": [
            "Java",
            "AWS",
            "Spring Boot",
            "React",
            "Microservices"
        ],
        "priority_roles": [
            "Developer",
            "Senior Developer",
            "Cloud Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Barclays%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "bny_mellon",
        "name": "BNY Mellon",
        "category": "fintech_gcc",
        "category_label": "GCC & Global Bank",
        "pay_range": "14 - 30+ LPA",
        "tagline": "Investments company touching approximately 20% of the world's investable assets.",
        "locations": [
            "Pune",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.bnymellon.com/",
        "tech_stack": [
            "Java",
            "Python",
            "Full Stack",
            "Spring",
            "Kafka",
            "Cloud"
        ],
        "priority_roles": [
            "Software Developer",
            "Specialist Developer",
            "Tech Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=BNY%20Mellon%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "wells_fargo",
        "name": "Wells Fargo India",
        "category": "fintech_gcc",
        "category_label": "GCC & Global Bank",
        "pay_range": "15 - 32+ LPA",
        "tagline": "Global capability centers powering financial services, digital banking, and payments security.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://www.wellsfargo.com/about/careers/",
        "tech_stack": [
            "Java",
            "React",
            "Spring Boot",
            "Microservices",
            "Python"
        ],
        "priority_roles": [
            "Software Senior Engineer",
            "Applications Systems Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Wells%20Fargo%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "flipkart",
        "name": "Flipkart",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 42+ LPA",
        "tagline": "India's homegrown e-commerce pioneer handling billions of transactions and massive scale logistics.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://www.flipkartcareers.com/",
        "tech_stack": [
            "Java",
            "Dropwizard",
            "React",
            "Node.js",
            "MySQL",
            "Distributed Systems"
        ],
        "priority_roles": [
            "SDE I/II/III",
            "Full Stack Engineer",
            "Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Flipkart%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "swiggy",
        "name": "Swiggy",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 42+ LPA",
        "tagline": "Leading on-demand convenience platform handling millions of daily food and grocery deliveries.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.swiggy.com/",
        "tech_stack": [
            "Go",
            "Java",
            "React Native",
            "Kafka",
            "AWS",
            "High Concurrency"
        ],
        "priority_roles": [
            "Software Development Engineer",
            "Backend Developer",
            "Staff Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Swiggy%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "zomato",
        "name": "Zomato & Blinkit",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "16 - 40+ LPA",
        "tagline": "Food delivery and 10-minute quick commerce powerhouse serving millions of customers every day.",
        "locations": [
            "Gurugram",
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://www.zomato.com/careers",
        "tech_stack": [
            "PHP",
            "Go",
            "Python",
            "React",
            "MySQL",
            "Redis"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Developer",
            "Product Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Zomato%20%26%20Blinkit%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "zepto",
        "name": "Zepto",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 42+ LPA",
        "tagline": "India's fastest-growing quick-commerce unicorn building hyper-optimized delivery algorithms.",
        "locations": [
            "Bengaluru",
            "Mumbai"
        ],
        "ats": "Lever",
        "careers_url": "https://jobs.lever.co/zepto",
        "tech_stack": [
            "Go",
            "Python",
            "React",
            "PostgreSQL",
            "Kafka",
            "AWS"
        ],
        "priority_roles": [
            "SDE-2 Backend",
            "Full Stack Developer",
            "Data Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Zepto%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "razorpay",
        "name": "Razorpay",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 40+ LPA",
        "tagline": "Full-stack financial services unicorn powering automated payments and banking for online businesses.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Lever",
        "careers_url": "https://jobs.lever.co/razorpay",
        "tech_stack": [
            "Go",
            "PHP",
            "Node.js",
            "React",
            "AWS",
            "Kubernetes"
        ],
        "priority_roles": [
            "Software Engineer - Payments",
            "Backend Engineer",
            "Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Razorpay%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "phonepe",
        "name": "PhonePe",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 42+ LPA",
        "tagline": "India's leading digital payments app processing billions of UPI transactions monthly.",
        "locations": [
            "Bengaluru",
            "Pune"
        ],
        "ats": "Direct",
        "careers_url": "https://www.phonepe.com/careers/",
        "tech_stack": [
            "Java",
            "Dropwizard",
            "HBase",
            "Aerospike",
            "React Native",
            "High Scale"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Specialist",
            "Platform Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=PhonePe%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cred",
        "name": "CRED",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "22 - 50+ LPA",
        "tagline": "Members-only fintech platform celebrated for pristine engineering, high compensation, and design.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Lever",
        "careers_url": "https://jobs.lever.co/cred",
        "tech_stack": [
            "Go",
            "Java",
            "Kafka",
            "PostgreSQL",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Backend Engineer",
            "Full Stack Engineer",
            "Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=CRED%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "groww",
        "name": "Groww",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "16 - 38+ LPA",
        "tagline": "India's premier investment platform for direct mutual funds, stocks, and wealth management.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://groww.in/careers",
        "tech_stack": [
            "Spring Boot",
            "Java",
            "Microservices",
            "React",
            "Kubernetes"
        ],
        "priority_roles": [
            "Software Engineer",
            "Full Stack Developer",
            "Backend Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Groww%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "zerodha",
        "name": "Zerodha",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "16 - 35+ LPA",
        "tagline": "India's largest stockbroker built on minimal, open-source technology, Python, Go, and PostgreSQL.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://zerodha.tech/careers/",
        "tech_stack": [
            "Python",
            "Go",
            "PostgreSQL",
            "Vue.js",
            "Redis",
            "Linux"
        ],
        "priority_roles": [
            "Software Developer",
            "Systems Administrator"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Zerodha%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "meesho",
        "name": "Meesho",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 40+ LPA",
        "tagline": "India's fastest growing social e-commerce platform democratizing internet commerce for everyone.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/meesho",
        "tech_stack": [
            "Java",
            "Python",
            "Go",
            "Kafka",
            "Spark",
            "Microservices"
        ],
        "priority_roles": [
            "SDE-II",
            "Backend Developer",
            "Data Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Meesho%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "postman",
        "name": "Postman",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "20 - 45+ LPA",
        "tagline": "The world's leading API platform used by over 30 million developers and 500,000 companies.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/postman",
        "tech_stack": [
            "Node.js",
            "TypeScript",
            "React",
            "Electron",
            "AWS",
            "Docker"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Developer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Postman%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "browserstack",
        "name": "BrowserStack",
        "category": "unicorn",
        "category_label": "Product Unicorn",
        "pay_range": "18 - 40+ LPA",
        "tagline": "The world's leading software testing platform powering 2+ million tests every day across cloud devices.",
        "locations": [
            "Mumbai",
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/browserstack",
        "tech_stack": [
            "Ruby",
            "Go",
            "React",
            "Docker",
            "Linux Kernel",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer",
            "Engineering Manager",
            "Product Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=BrowserStack%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "citadel",
        "name": "Citadel & Citadel Securities",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "60 LPA - 1.5 Cr+",
        "tagline": "World-leading market maker and quantitative trading powerhouse trading across all global markets.",
        "locations": [
            "Gurugram",
            "Singapore",
            "London",
            "New York",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://www.citadel.com/careers/open-roles/",
        "tech_stack": [
            "C++",
            "Rust",
            "Low Latency",
            "Python",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Engineer",
            "Quant Developer",
            "Systems Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Citadel%20%26%20Citadel%20Securities%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "jane_street",
        "name": "Jane Street",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "80 LPA - 2 Cr+",
        "tagline": "Quantitative trading firm operating around the clock and across globe with deep systems focus.",
        "locations": [
            "Singapore",
            "Hong Kong",
            "London",
            "New York"
        ],
        "ats": "Direct",
        "careers_url": "https://www.janestreet.com/join-jane-street/open-roles/",
        "tech_stack": [
            "OCaml",
            "C++",
            "Rust",
            "Low Latency",
            "Systems Software"
        ],
        "priority_roles": [
            "Software Engineer",
            "Systems Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Jane%20Street%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "tower_research",
        "name": "Tower Research Capital",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "45 LPA - 1.2 Cr+",
        "tagline": "High-frequency algorithmic trading pioneer with huge core engineering presence in India.",
        "locations": [
            "Gurugram",
            "Bengaluru",
            "Singapore",
            "New York"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/towerresearchcapital",
        "tech_stack": [
            "C++",
            "Linux",
            "Low Latency",
            "Python",
            "Concurrency",
            "Zero-Copy"
        ],
        "priority_roles": [
            "Systems Engineer",
            "Quant Developer",
            "Core Trading Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Tower%20Research%20Capital%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "jump_trading",
        "name": "Jump Trading",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "50 LPA - 1.3 Cr+",
        "tagline": "Global research-driven quantitative trading firm engineering hardware acceleration and high throughput.",
        "locations": [
            "Singapore",
            "London",
            "Chicago",
            "Sydney"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/jumptrading",
        "tech_stack": [
            "C++",
            "Rust",
            "FPGA",
            "Low Latency",
            "High Throughput"
        ],
        "priority_roles": [
            "Core Engineering",
            "Software Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Jump%20Trading%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "hrt",
        "name": "Hudson River Trading (HRT)",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "60 LPA - 1.4 Cr+",
        "tagline": "Multi-asset class quantitative trading firm at the forefront of automated algorithmic systems.",
        "locations": [
            "Singapore",
            "London",
            "New York",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/hudsonrivertrading",
        "tech_stack": [
            "C++",
            "Python",
            "Linux Kernel",
            "Low Latency",
            "Distributed Storage"
        ],
        "priority_roles": [
            "Core Software Engineer",
            "Algorithm Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Hudson%20River%20Trading%20%28HRT%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "graviton",
        "name": "Graviton Research Capital",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "50 LPA - 1.2 Cr+",
        "tagline": "India's premier quantitative trading firm executing high-frequency strategies on global exchanges.",
        "locations": [
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://gravitontrading.com/careers/",
        "tech_stack": [
            "C++",
            "Linux Kernel",
            "Low Latency",
            "Python",
            "Network Protocols"
        ],
        "priority_roles": [
            "Quantitative Software Engineer",
            "Systems Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Graviton%20Research%20Capital%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "nk_securities",
        "name": "NK Securities Research",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "45 LPA - 1 Cr+",
        "tagline": "Leading algorithmic trading firm deploying statistical arbitrage models and low latency execution.",
        "locations": [
            "Gurugram",
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://www.nksecurities.com/careers",
        "tech_stack": [
            "C++",
            "Python",
            "Multithreading",
            "FPGA",
            "Linux"
        ],
        "priority_roles": [
            "Low Latency Developer",
            "Quantitative Researcher"
        ],
        "google_jobs_url": "https://www.google.com/search?q=NK%20Securities%20Research%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "quadeye",
        "name": "Quadeye Securities",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "45 LPA - 90+ LPA",
        "tagline": "Proprietary algorithmic trading firm creating mathematically rigorous high-frequency engines.",
        "locations": [
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://quadeye.com/careers/",
        "tech_stack": [
            "C++",
            "Low Latency",
            "Concurrency",
            "Linux",
            "Algorithms"
        ],
        "priority_roles": [
            "Software Developer",
            "Quant Researcher"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Quadeye%20Securities%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "alphagrep",
        "name": "AlphaGrep Securities",
        "category": "hft",
        "category_label": "HFT & Quant Trading",
        "pay_range": "40 LPA - 85+ LPA",
        "tagline": "Global quantitative trading firm trading algorithmic strategies across major asset classes.",
        "locations": [
            "Mumbai",
            "Bengaluru",
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://alpha-grep.com/careers/",
        "tech_stack": [
            "C++",
            "Python",
            "Distributed Systems",
            "Low Latency"
        ],
        "priority_roles": [
            "Quantitative Developer",
            "Software Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=AlphaGrep%20Securities%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "sap_labs",
        "name": "SAP Labs",
        "category": "enterprise_sap",
        "category_label": "Enterprise & SAP",
        "pay_range": "14 - 35+ LPA",
        "tagline": "Enterprise resource planning market leader with cloud ERP, ABAP on HANA, and Business Technology Platform (BTP).",
        "locations": [
            "Bengaluru",
            "Gurugram",
            "Pune"
        ],
        "ats": "SuccessFactors",
        "careers_url": "https://jobs.sap.com/",
        "tech_stack": [
            "ABAP",
            "SAP HANA",
            "Java",
            "Node.js",
            "SAP BTP",
            "Cloud ERP"
        ],
        "priority_roles": [
            "Developer",
            "Senior Developer",
            "Development Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=SAP%20Labs%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "jnj",
        "name": "Johnson & Johnson (J&J)",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Healthcare",
        "pay_range": "12 - 28+ LPA",
        "tagline": "Global healthcare and medical technology leader utilizing enterprise systems and CSOD platforms.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Mumbai"
        ],
        "ats": "Workday",
        "careers_url": "https://www.careers.jnj.com/",
        "tech_stack": [
            "CSOD APIs",
            "Node.js",
            "Express",
            "SAP",
            "Full Stack",
            "Cloud"
        ],
        "priority_roles": [
            "Software Engineer",
            "Systems Analyst",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Johnson%20%26%20Johnson%20%28J%26J%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "siemens",
        "name": "Siemens Technology",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Industrial",
        "pay_range": "12 - 28+ LPA",
        "tagline": "Industrial software pioneer transforming manufacturing, infrastructure, and mobility systems.",
        "locations": [
            "Bengaluru",
            "Pune",
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://www.siemens.com/in/en/company/jobs.html",
        "tech_stack": [
            "Java",
            "C++",
            "Cloud",
            "IoT",
            "React",
            "Industrial Automation"
        ],
        "priority_roles": [
            "Software Developer",
            "Full Stack Engineer",
            "Platform Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Siemens%20Technology%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "schneider",
        "name": "Schneider Electric",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Energy",
        "pay_range": "12 - 26+ LPA",
        "tagline": "Global energy management and industrial automation leader driving digital IoT architectures.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Workday",
        "careers_url": "https://www.se.com/in/en/about-us/careers/overview.jsp",
        "tech_stack": [
            "Java",
            "C#",
            "Cloud",
            "IoT",
            "Angular",
            "Microservices"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Cloud Developer",
            "IoT Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Schneider%20Electric%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "honeywell",
        "name": "Honeywell Technology",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Aerospace",
        "pay_range": "12 - 28+ LPA",
        "tagline": "Software-industrial leader providing aerospace, building technologies, and performance materials software.",
        "locations": [
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Gurugram"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.honeywell.com/",
        "tech_stack": [
            "C++",
            "Java",
            "Python",
            "Cloud Platform",
            "React",
            "Embedded"
        ],
        "priority_roles": [
            "Advanced Software Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Honeywell%20Technology%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "bosch",
        "name": "Bosch Global Software Technologies (BGSW)",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Mobility",
        "pay_range": "10 - 24+ LPA",
        "tagline": "Pioneering technology and engineering services for automotive mobility, cloud, and IoT.",
        "locations": [
            "Bengaluru",
            "Coimbatore",
            "Hyderabad",
            "Pune"
        ],
        "ats": "SmartRecruiters",
        "careers_url": "https://www.bosch-softwaretechnologies.com/en/careers/",
        "tech_stack": [
            "Embedded C++",
            "Java",
            "Python",
            "Cloud",
            "AUTOSAR",
            "IoT"
        ],
        "priority_roles": [
            "Software Engineer",
            "Systems Architect",
            "Lead Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Bosch%20Global%20Software%20Technologies%20%28BGSW%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "philips",
        "name": "Philips HealthTech",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Healthcare",
        "pay_range": "12 - 28+ LPA",
        "tagline": "Health technology enterprise focusing on diagnostic imaging, connected care, and health informatics.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Workday",
        "careers_url": "https://www.careers.philips.com/",
        "tech_stack": [
            "C#",
            ".NET",
            "Java",
            "Cloud",
            "React",
            "Healthcare Informatics"
        ],
        "priority_roles": [
            "Software Development Engineer",
            "Senior Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Philips%20HealthTech%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "openai",
        "name": "OpenAI",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "40 LPA - 1 Cr+ (Global/Remote)",
        "tagline": "Creators of ChatGPT, GPT-4o, and advanced deep learning multimodal research.",
        "locations": [
            "San Francisco",
            "London",
            "Remote"
        ],
        "ats": "Ashby",
        "careers_url": "https://openai.com/careers/search/",
        "tech_stack": [
            "Python",
            "PyTorch",
            "Kubernetes",
            "TypeScript",
            "Distributed GPU"
        ],
        "priority_roles": [
            "Software Engineer",
            "Research Engineer",
            "Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=OpenAI%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "anthropic",
        "name": "Anthropic",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "40 LPA - 1 Cr+ (Global/Remote)",
        "tagline": "AI safety and research company developing Claude 3.5 Sonnet and frontier foundation models.",
        "locations": [
            "San Francisco",
            "London",
            "Remote"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.anthropic.com/careers#open-roles",
        "tech_stack": [
            "Python",
            "Rust",
            "TypeScript",
            "PyTorch",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Research Engineer",
            "Full Stack Engineer",
            "Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Anthropic%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "mistral",
        "name": "Mistral AI",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "35 - 75+ LPA (Global/Remote)",
        "tagline": "European frontier AI leader building state-of-the-art open weight models and efficient generative systems.",
        "locations": [
            "Paris",
            "London",
            "Remote"
        ],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/mistral",
        "tech_stack": [
            "Python",
            "C++",
            "PyTorch",
            "Triton",
            "Inference Optimization"
        ],
        "priority_roles": [
            "Inference Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Mistral%20AI%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "elevenlabs",
        "name": "ElevenLabs",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "35 - 70+ LPA (Global/Remote)",
        "tagline": "The world's leading voice AI research and deployment company generating ultra-realistic audio and speech.",
        "locations": [
            "London",
            "Warsaw",
            "Remote"
        ],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/elevenlabs",
        "tech_stack": [
            "Python",
            "C++",
            "Rust",
            "Audio Processing",
            "TTS/ASR"
        ],
        "priority_roles": [
            "Speech AI Engineer",
            "Systems Engineer",
            "Backend Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=ElevenLabs%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cohere",
        "name": "Cohere",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "35 - 70+ LPA (Global/Remote)",
        "tagline": "Enterprise AI platform developing state-of-the-art LLMs, RAG, and multilingual embeddings.",
        "locations": [
            "London",
            "Toronto",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://boards.greenhouse.io/cohere",
        "tech_stack": [
            "Python",
            "Go",
            "Kubernetes",
            "PyTorch",
            "FastAPI"
        ],
        "priority_roles": [
            "Platform Engineer",
            "Backend Software Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Cohere%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "scale_ai",
        "name": "Scale AI",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "30 - 65+ LPA (Global/Remote)",
        "tagline": "The data infrastructure foundation for generative AI and frontier model fine-tuning.",
        "locations": [
            "San Francisco",
            "Remote"
        ],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/scaleai",
        "tech_stack": [
            "Python",
            "TypeScript",
            "React",
            "Node.js",
            "Kubernetes"
        ],
        "priority_roles": [
            "Full Stack Engineer",
            "Backend Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Scale%20AI%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "hugging_face",
        "name": "Hugging Face",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "28 - 60+ LPA (Global/Remote)",
        "tagline": "The open-source AI platform and home of the world's largest repository of models and datasets.",
        "locations": [
            "Paris",
            "New York",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://huggingface.co/join-us",
        "tech_stack": [
            "Python",
            "Rust",
            "Transformers",
            "PyTorch",
            "TypeScript"
        ],
        "priority_roles": [
            "Machine Learning Engineer",
            "Full Stack Web Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Hugging%20Face%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "perplexity",
        "name": "Perplexity AI",
        "category": "ai",
        "category_label": "Frontier AI Lab",
        "pay_range": "35 - 75+ LPA (Global/Remote)",
        "tagline": "AI-powered conversational answer engine reinventing internet search and discovery.",
        "locations": [
            "San Francisco",
            "Remote"
        ],
        "ats": "Ashby",
        "careers_url": "https://jobs.ashbyhq.com/perplexity",
        "tech_stack": [
            "Python",
            "TypeScript",
            "React",
            "FastAPI",
            "High Scale Search"
        ],
        "priority_roles": [
            "Full Stack Engineer",
            "Search Systems Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Perplexity%20AI%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "mphasis",
        "name": "Mphasis",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 16+ LPA (NextLabs / Cloud Specialist)",
        "tagline": "Applied tech services giant specializing in cloud, cognitive computing, and banking platforms.",
        "locations": [
            "Bengaluru",
            "Pune",
            "Chennai",
            "Hyderabad",
            "Mumbai"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.mphasis.com/",
        "tech_stack": [
            "Cloud",
            "Java",
            "Python",
            "DevOps",
            "Microservices",
            "Fintech APIs"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Cloud Solutions Architect",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Mphasis%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "zensar",
        "name": "Zensar Technologies",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "8.5 - 15+ LPA (Digital Engineering / Lead)",
        "tagline": "RPG Group digital solutions firm building next-generation enterprise software.",
        "locations": [
            "Pune",
            "Bengaluru",
            "Hyderabad",
            "Kolkata"
        ],
        "ats": "Direct",
        "careers_url": "https://www.zensar.com/careers",
        "tech_stack": [
            "Cloud",
            "Java",
            "React",
            "Python",
            "Data Engineering"
        ],
        "priority_roles": [
            "Specialist Engineer",
            "Full Stack Developer",
            "Tech Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Zensar%20Technologies%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "birlasoft",
        "name": "Birlasoft",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "8.5 - 15+ LPA (Enterprise Digital Transformation)",
        "tagline": "CK Birla Group enterprise transformation partner across cloud and manufacturing tech.",
        "locations": [
            "Pune",
            "Noida",
            "Bengaluru",
            "Chennai"
        ],
        "ats": "Direct",
        "careers_url": "https://www.birlasoft.com/careers",
        "tech_stack": [
            "Enterprise Cloud",
            "Java",
            "SAP",
            "React",
            "Python"
        ],
        "priority_roles": [
            "Senior Consultant",
            "Software Engineer",
            "Technical Specialist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Birlasoft%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "happiest_minds",
        "name": "Happiest Minds Technologies",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 17+ LPA (Digital Business Services / AI)",
        "tagline": "Mindful IT company enabling digital transformation through disruptive technologies like AI and blockchain.",
        "locations": [
            "Bengaluru",
            "Pune",
            "Noida"
        ],
        "ats": "Direct",
        "careers_url": "https://www.happiestminds.com/careers/",
        "tech_stack": [
            "AI/ML",
            "IoT",
            "Cloud Native",
            "React",
            "Java",
            "Python"
        ],
        "priority_roles": [
            "Digital Solutions Architect",
            "Senior Developer",
            "Cloud Specialist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Happiest%20Minds%20Technologies%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cyient",
        "name": "Cyient",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "8.5 - 15+ LPA (Intelligent Engineering Services)",
        "tagline": "Global engineering, manufacturing, and digital technology solutions provider.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Pune",
            "Noida"
        ],
        "ats": "Direct",
        "careers_url": "https://www.cyient.com/careers",
        "tech_stack": [
            "Embedded Systems",
            "Cloud",
            "Python",
            "Java",
            "IoT",
            "C++"
        ],
        "priority_roles": [
            "Senior Software Developer",
            "Embedded Software Engineer",
            "DevOps Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Cyient%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "sonata",
        "name": "Sonata Software",
        "category": "service",
        "category_label": "IT Services & Consulting",
        "pay_range": "9 - 16+ LPA (Modernization Engineering / Lead)",
        "tagline": "Global modernization and digital engineering company with proprietary Platformation model.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Direct",
        "careers_url": "https://www.sonata-software.com/careers",
        "tech_stack": [
            "Cloud",
            "Microservices",
            "Java",
            "React",
            "Azure",
            "Python"
        ],
        "priority_roles": [
            "Technical Lead",
            "Senior Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Sonata%20Software%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "netflix",
        "name": "Netflix",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "45 - 85+ LPA (Senior Software Engineer)",
        "tagline": "Global entertainment streaming platform known for top-of-market compensation and freedom & responsibility culture.",
        "locations": [
            "Mumbai",
            "Remote",
            "Los Gatos",
            "California"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.netflix.com/",
        "tech_stack": [
            "Distributed Systems",
            "Java",
            "Node.js",
            "Python",
            "AWS",
            "Kafka",
            "React"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Distributed Systems Engineer",
            "UI Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Netflix%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "tesla",
        "name": "Tesla",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "30 - 65+ LPA (Autopilot & Platform Engineer)",
        "tagline": "Accelerating the world's transition to sustainable energy through cutting-edge EV hardware and AI autopilot software.",
        "locations": [
            "Pune",
            "Bengaluru",
            "Remote",
            "Austin"
        ],
        "ats": "Direct",
        "careers_url": "https://www.tesla.com/careers",
        "tech_stack": [
            "C++",
            "Python",
            "Embedded Systems",
            "React",
            "Kubernetes",
            "PyTorch"
        ],
        "priority_roles": [
            "Software Engineer",
            "Autopilot Software Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Tesla%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "stripe",
        "name": "Stripe",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "40 - 75+ LPA (Infrastructure & Payments)",
        "tagline": "Financial infrastructure platform for the internet, powering millions of businesses worldwide.",
        "locations": [
            "Bengaluru",
            "Remote",
            "San Francisco",
            "Dublin"
        ],
        "ats": "Direct",
        "careers_url": "https://stripe.com/jobs",
        "tech_stack": [
            "Ruby",
            "Go",
            "Java",
            "Distributed Systems",
            "React",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer - Infrastructure",
            "Backend Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Stripe%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "palantir",
        "name": "Palantir Technologies",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "35 - 70+ LPA (Foundry / Gotham Platforms)",
        "tagline": "Builds foundational data integration software platforms powering mission-critical government and enterprise decisions.",
        "locations": [
            "Remote",
            "London",
            "New York",
            "Denver"
        ],
        "ats": "Lever",
        "careers_url": "https://www.palantir.com/careers/",
        "tech_stack": [
            "Distributed Systems",
            "Java",
            "TypeScript",
            "React",
            "Python",
            "Kubernetes"
        ],
        "priority_roles": [
            "Forward Deployed Software Engineer",
            "Software Engineer",
            "Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Palantir%20Technologies%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "datadog",
        "name": "Datadog",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "35 - 65+ LPA (Cloud Observability & Scale)",
        "tagline": "Cloud monitoring and security platform delivering observability across infrastructure and applications.",
        "locations": [
            "Remote",
            "Paris",
            "New York",
            "Boston"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.datadoghq.com/careers/",
        "tech_stack": [
            "Go",
            "Python",
            "Kafka",
            "Kubernetes",
            "PostgreSQL",
            "React",
            "TypeScript"
        ],
        "priority_roles": [
            "Software Engineer - Systems",
            "Backend Engineer",
            "Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Datadog%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "airbnb",
        "name": "Airbnb",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "38 - 72+ LPA (Core Guest & Host Platform)",
        "tagline": "Global community marketplace for travel accommodations and experiences with top-tier product culture.",
        "locations": [
            "Gurugram",
            "Remote",
            "San Francisco"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://careers.airbnb.com/",
        "tech_stack": [
            "Java",
            "Kotlin",
            "React",
            "TypeScript",
            "GraphQL",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer",
            "Senior Full Stack Engineer",
            "Backend Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Airbnb%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "github",
        "name": "GitHub",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "32 - 62+ LPA (Developer Platform & Copilot)",
        "tagline": "The world's leading developer and AI platform empowering 100+ million developers.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://github.com/about/careers",
        "tech_stack": [
            "Ruby on Rails",
            "Go",
            "TypeScript",
            "React",
            "Azure",
            "Kubernetes",
            "AI Copilot"
        ],
        "priority_roles": [
            "Software Engineer",
            "Site Reliability Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=GitHub%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "gitlab",
        "name": "GitLab",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "30 - 60+ LPA (All-Remote DevSecOps)",
        "tagline": "Comprehensive all-remote DevSecOps platform delivered as a single application.",
        "locations": [
            "Remote Worldwide",
            "India Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://about.gitlab.com/jobs/",
        "tech_stack": [
            "Ruby on Rails",
            "Go",
            "Vue.js",
            "PostgreSQL",
            "Kubernetes",
            "GCP"
        ],
        "priority_roles": [
            "Backend Engineer",
            "Frontend Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=GitLab%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "elastic",
        "name": "Elastic",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "30 - 58+ LPA (Search & Observability)",
        "tagline": "Search-powered AI solutions platform behind Elasticsearch, Kibana, and Logstash.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.elastic.co/about/careers",
        "tech_stack": [
            "Java",
            "Go",
            "Python",
            "Distributed Search",
            "React",
            "TypeScript"
        ],
        "priority_roles": [
            "Software Engineer - Elasticsearch",
            "Full Stack Engineer",
            "Cloud Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Elastic%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "shopify",
        "name": "Shopify",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "35 - 65+ LPA (Global Commerce Engine)",
        "tagline": "Leading global commerce company providing trusted tools to start, grow, and market retail businesses.",
        "locations": [
            "Remote Worldwide",
            "Ottawa",
            "Toronto"
        ],
        "ats": "Direct",
        "careers_url": "https://www.shopify.com/careers",
        "tech_stack": [
            "Ruby",
            "Go",
            "React",
            "GraphQL",
            "MySQL",
            "Google Cloud",
            "Kafka"
        ],
        "priority_roles": [
            "Senior Backend Developer",
            "Full Stack Developer",
            "Production Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Shopify%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "twilio",
        "name": "Twilio",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "28 - 55+ LPA (Communications & Segment)",
        "tagline": "Customer engagement and communications platform powering SMS, voice, and data APIs.",
        "locations": [
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.twilio.com/en-us/company/jobs",
        "tech_stack": [
            "Java",
            "Go",
            "Python",
            "AWS",
            "Kafka",
            "React",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Engineer",
            "Cloud Infrastructure Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Twilio%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "pinterest",
        "name": "Pinterest",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "32 - 60+ LPA (Visual Search & Ad Engine)",
        "tagline": "Visual discovery engine for finding ideas like recipes, home and style inspiration.",
        "locations": [
            "Remote",
            "San Francisco",
            "Dublin"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.pinterestcareers.com/",
        "tech_stack": [
            "Python",
            "Java",
            "C++",
            "React",
            "Hadoop",
            "Kubernetes",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer",
            "Machine Learning Engineer",
            "Frontend Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Pinterest%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "doordash",
        "name": "DoorDash",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "35 - 68+ LPA (Logistics & Marketplace Engine)",
        "tagline": "Local commerce technology platform connecting consumers with their favorite local businesses.",
        "locations": [
            "Bengaluru",
            "Remote",
            "San Francisco"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://careers.doordash.com/",
        "tech_stack": [
            "Kotlin",
            "Go",
            "Python",
            "React Native",
            "PostgreSQL",
            "AWS",
            "gRPC"
        ],
        "priority_roles": [
            "Software Engineer - Logistics",
            "Backend Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=DoorDash%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "dropbox",
        "name": "Dropbox",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "32 - 62+ LPA (Virtual First Storage Platform)",
        "tagline": "Global collaboration platform providing smart workspace tools and secure cloud storage.",
        "locations": [
            "Remote Worldwide",
            "San Francisco"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://jobs.dropbox.com/",
        "tech_stack": [
            "Python",
            "Go",
            "Rust",
            "TypeScript",
            "React",
            "Distributed Storage"
        ],
        "priority_roles": [
            "Software Engineer",
            "Systems Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Dropbox%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "zoom",
        "name": "Zoom Video Communications",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "28 - 56+ LPA (Video Collaboration & AI)",
        "tagline": "Communications platform delivering video meetings, phone, chat, and AI Companion tools.",
        "locations": [
            "Bengaluru",
            "Remote",
            "San Jose"
        ],
        "ats": "Workday",
        "careers_url": "https://careers.zoom.us/",
        "tech_stack": [
            "C++",
            "Java",
            "Python",
            "WebRTC",
            "React",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Cloud Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Zoom%20Video%20Communications%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "hubspot",
        "name": "HubSpot",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "30 - 58+ LPA (Inbound Marketing & CRM)",
        "tagline": "Leading cloud CRM platform helping millions of scaling companies grow better.",
        "locations": [
            "Remote",
            "Cambridge",
            "Dublin",
            "Singapore"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.hubspot.com/careers",
        "tech_stack": [
            "Java",
            "React",
            "Python",
            "MySQL",
            "Kafka",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Software Engineer",
            "Senior Full Stack Engineer",
            "Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=HubSpot%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cloudflare",
        "name": "Cloudflare",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "35 - 70+ LPA (Edge Network & Workers)",
        "tagline": "Global connectivity cloud making everything connected to the internet secure, private, and fast.",
        "locations": [
            "Remote",
            "Austin",
            "San Francisco",
            "London",
            "Singapore"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.cloudflare.com/careers/",
        "tech_stack": [
            "Rust",
            "Go",
            "C",
            "TypeScript",
            "Edge Computing",
            "Distributed Networking"
        ],
        "priority_roles": [
            "Systems Engineer",
            "Software Engineer - Edge",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Cloudflare%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "coinbase",
        "name": "Coinbase",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "38 - 72+ LPA (Cryptocurrency Infrastructure)",
        "tagline": "Building the cryptoeconomy\u2014a more fair, accessible, and transparent financial system.",
        "locations": [
            "Hyderabad",
            "Bengaluru",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.coinbase.com/careers",
        "tech_stack": [
            "Go",
            "React",
            "React Native",
            "PostgreSQL",
            "AWS",
            "Ruby",
            "Cryptography"
        ],
        "priority_roles": [
            "Software Engineer - Platform",
            "Backend Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Coinbase%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "block",
        "name": "Block (Square & Cash App)",
        "category": "mnc",
        "category_label": "Tier-1 Product MNC",
        "pay_range": "36 - 68+ LPA (Payments & Financial Ecosystem)",
        "tagline": "Global technology company building economic empowerment tools: Square, Cash App, TIDAL, and TBD.",
        "locations": [
            "Remote",
            "San Francisco",
            "Melbourne"
        ],
        "ats": "SmartRecruiters",
        "careers_url": "https://block.xyz/careers",
        "tech_stack": [
            "Java",
            "Go",
            "Kotlin",
            "React",
            "AWS",
            "MySQL",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Block%20%28Square%20%26%20Cash%20App%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "visa",
        "name": "Visa",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "24 - 48+ LPA (Global Payment Processing)",
        "tagline": "World leader in digital payments connecting consumers, merchants, and financial institutions.",
        "locations": [
            "Bengaluru",
            "Mumbai"
        ],
        "ats": "SmartRecruiters",
        "careers_url": "https://www.visa.co.in/careers.html",
        "tech_stack": [
            "Java",
            "Distributed Transactions",
            "React",
            "Kafka",
            "Microservices",
            "Python"
        ],
        "priority_roles": [
            "Staff Software Engineer",
            "Senior Software Developer",
            "Platform Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Visa%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "mastercard",
        "name": "Mastercard",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "22 - 46+ LPA (Cyber & Payment Intelligence)",
        "tagline": "Global technology company in the payments industry using secure, simple, smart transactions.",
        "locations": [
            "Pune",
            "Gurugram",
            "Vadodara"
        ],
        "ats": "Workday",
        "careers_url": "https://careers.mastercard.com/",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "Cloud Native",
            "Angular",
            "Python",
            "Kubernetes"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Lead Developer",
            "Cloud Solutions Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Mastercard%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "amex",
        "name": "American Express (Amex)",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "20 - 42+ LPA (Global Digital Platform)",
        "tagline": "Globally integrated payments company providing customers with access to products and insights.",
        "locations": [
            "Bengaluru",
            "Gurugram"
        ],
        "ats": "Workday",
        "careers_url": "https://www.americanexpress.com/en-in/careers/",
        "tech_stack": [
            "Java",
            "Kotlin",
            "React",
            "Node.js",
            "Docker",
            "Distributed Architecture"
        ],
        "priority_roles": [
            "Engineer II",
            "Senior Software Engineer",
            "Technical Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=American%20Express%20%28Amex%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "paypal",
        "name": "PayPal",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "24 - 48+ LPA (Commerce Platforms & Risk)",
        "tagline": "Pioneering digital payments platform driving the financial digital transformation.",
        "locations": [
            "Bengaluru",
            "Chennai",
            "Hyderabad"
        ],
        "ats": "Workday",
        "careers_url": "https://careers.pypl.com/",
        "tech_stack": [
            "Java",
            "Node.js",
            "React",
            "Distributed Systems",
            "GCP",
            "Python"
        ],
        "priority_roles": [
            "Software Engineer - Platform",
            "MTS 1 Software Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=PayPal%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "capital_one",
        "name": "Capital One",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "25 - 50+ LPA (Cloud Banking & Machine Learning)",
        "tagline": "The bank that thinks and operates like a tech company, 100% on AWS cloud.",
        "locations": [
            "Bengaluru",
            "Remote",
            "McLean",
            "Virginia"
        ],
        "ats": "Workday",
        "careers_url": "https://www.capitalonecareers.com/",
        "tech_stack": [
            "Java",
            "Python",
            "AWS",
            "Serverless",
            "React",
            "Kubernetes",
            "Kafka"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Lead Software Engineer",
            "Data Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Capital%20One%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "fidelity",
        "name": "Fidelity Investments",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "18 - 38+ LPA (Asset Management Technology)",
        "tagline": "Global investment and asset management tech powerhouse driving institutional systems.",
        "locations": [
            "Bengaluru",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.fidelity.com/",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "Angular",
            "AWS",
            "Python",
            "Oracle"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Principal Software Engineer",
            "Cloud Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Fidelity%20Investments%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "citi",
        "name": "Citi (Citigroup Technology)",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "20 - 42+ LPA (Global Markets & Banking Tech)",
        "tagline": "Global banking partner managing institutional clients, algorithmic trading, and wealth systems.",
        "locations": [
            "Pune",
            "Chennai",
            "Bengaluru",
            "Mumbai"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.citi.com/",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "Microservices",
            "React",
            "Kafka",
            "Python",
            "Cloud"
        ],
        "priority_roles": [
            "Applications Development Senior Programmer",
            "VP Technology",
            "Full Stack Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Citi%20%28Citigroup%20Technology%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "standard_chartered",
        "name": "Standard Chartered GBS",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "18 - 36+ LPA (Global Business Services)",
        "tagline": "International banking group technology arm developing core corporate and retail platforms.",
        "locations": [
            "Bengaluru",
            "Chennai"
        ],
        "ats": "Direct",
        "careers_url": "https://www.sc.com/en/careers/",
        "tech_stack": [
            "Java",
            "Full Stack",
            "Spring Boot",
            "Cloud",
            "API Gateway",
            "Python"
        ],
        "priority_roles": [
            "Lead Software Engineer",
            "Full Stack Developer",
            "Tech Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Standard%20Chartered%20GBS%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "hsbc",
        "name": "HSBC Technology India",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "18 - 38+ LPA (Global IT & Digital Transformation)",
        "tagline": "Technology backbone of one of the world's largest banking and financial services organizations.",
        "locations": [
            "Pune",
            "Hyderabad"
        ],
        "ats": "Direct",
        "careers_url": "https://www.hsbc.com/careers",
        "tech_stack": [
            "Java",
            "Microservices",
            "GCP",
            "React",
            "Python",
            "Docker"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Technical Specialist",
            "Cloud Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=HSBC%20Technology%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "nike",
        "name": "Nike Technology Center",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "22 - 45+ LPA (Global Digital Commerce)",
        "tagline": "The world's leading athletic brand building direct-to-consumer digital commerce and apps.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.nike.com/",
        "tech_stack": [
            "Node.js",
            "React",
            "AWS",
            "Microservices",
            "Java",
            "Python",
            "Snowflake"
        ],
        "priority_roles": [
            "Lead Software Engineer",
            "Senior Full Stack Engineer",
            "Cloud Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Nike%20Technology%20Center%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "boeing",
        "name": "Boeing India Engineering (BIETC)",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "18 - 38+ LPA (Aerospace Digital & Embedded)",
        "tagline": "Advanced aerospace software and systems engineering center outside the United States.",
        "locations": [
            "Bengaluru",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.boeing.com/",
        "tech_stack": [
            "C++",
            "Python",
            "Java",
            "Avionics",
            "Cloud",
            "DevOps",
            "Embedded Systems"
        ],
        "priority_roles": [
            "Software Engineer",
            "Systems Integration Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Boeing%20India%20Engineering%20%28BIETC%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "mercedes",
        "name": "Mercedes-Benz R&D India (MBRDI)",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "18 - 36+ LPA (Automotive OS & Connected Cloud)",
        "tagline": "Largest R&D center for Mercedes-Benz outside Germany, engineering MB.OS and connected luxury.",
        "locations": [
            "Bengaluru",
            "Pune"
        ],
        "ats": "Direct",
        "careers_url": "https://www.mbrdi.co.in/careers",
        "tech_stack": [
            "C++",
            "Python",
            "Embedded Linux",
            "Java",
            "AWS",
            "Connected Car APIs"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Autonomous Driving Specialist",
            "Cloud Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Mercedes-Benz%20R%26D%20India%20%28MBRDI%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "intel",
        "name": "Intel India",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "22 - 48+ LPA (Silicon & AI Software)",
        "tagline": "Global semiconductor pioneer engineering processors, silicon drivers, and oneAPI AI software.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.intel.com/",
        "tech_stack": [
            "C",
            "C++",
            "Python",
            "Linux Kernel",
            "AI Frameworks",
            "Compilers"
        ],
        "priority_roles": [
            "Software Development Engineer",
            "Firmware Engineer",
            "AI Software Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Intel%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "amd",
        "name": "AMD India",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "22 - 48+ LPA (High-Performance Computing & GPU)",
        "tagline": "Semiconductor giant driving high-performance graphics, server processors, and ROCm open software.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Workday",
        "careers_url": "https://www.amd.com/en/corporate/careers.html",
        "tech_stack": [
            "C++",
            "Python",
            "CUDA / ROCm",
            "Linux",
            "Compilers",
            "Distributed Computing"
        ],
        "priority_roles": [
            "MTS Software Engineer",
            "GPU Software Developer",
            "Systems Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=AMD%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "texas_instruments",
        "name": "Texas Instruments (TI)",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "24 - 45+ LPA (Embedded Processing & DSP)",
        "tagline": "Global analog and embedded processing semiconductor manufacturer with storied Indian R&D.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://careers.ti.com/",
        "tech_stack": [
            "Embedded C",
            "C++",
            "Python",
            "DSP",
            "RTOS",
            "Hardware Acceleration"
        ],
        "priority_roles": [
            "Software Systems Engineer",
            "Embedded Software Developer",
            "Applications Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Texas%20Instruments%20%28TI%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "dell",
        "name": "Dell Technologies",
        "category": "fintech_gcc",
        "category_label": "Global FinTech & GCC",
        "pay_range": "18 - 38+ LPA (Infrastructure & Edge Cloud)",
        "tagline": "Global technology company transforming businesses through hybrid cloud and hardware platforms.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.dell.com/",
        "tech_stack": [
            "Java",
            "Python",
            "Go",
            "Kubernetes",
            "VMware / Virtualization",
            "React"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Principal Software Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Dell%20Technologies%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "figma",
        "name": "Figma",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "40 - 80+ LPA (WebAssembly & Collaboration Engine)",
        "tagline": "Leading collaborative web design and product development platform on modern web graphics.",
        "locations": [
            "Remote",
            "San Francisco",
            "London"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.figma.com/careers/",
        "tech_stack": [
            "TypeScript",
            "WebAssembly",
            "Rust",
            "C++",
            "WebGL",
            "React",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer",
            "Systems Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Figma%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "canva",
        "name": "Canva",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "35 - 70+ LPA (Visual Suite & Generative AI)",
        "tagline": "Global visual communications platform empowering the whole world to design anything.",
        "locations": [
            "Remote",
            "Sydney",
            "London"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.canva.com/careers/",
        "tech_stack": [
            "Java",
            "TypeScript",
            "React",
            "Rust",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Developer",
            "Frontend Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Canva%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "notion",
        "name": "Notion",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "40 - 75+ LPA (Connected Workspace & AI)",
        "tagline": "All-in-one workspace connecting notes, docs, wikis, and project management with Notion AI.",
        "locations": [
            "Remote",
            "San Francisco",
            "Dublin"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.notion.so/careers",
        "tech_stack": [
            "TypeScript",
            "React",
            "Node.js",
            "PostgreSQL",
            "AWS",
            "Generative AI"
        ],
        "priority_roles": [
            "Software Engineer - Core Product",
            "Infrastructure Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Notion%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "linear",
        "name": "Linear",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "38 - 70+ LPA (Issue Tracking & High-Craft Web)",
        "tagline": "The issue tracking tool you will actually enjoy using\u2014built for high-performing modern software teams.",
        "locations": [
            "Remote Worldwide"
        ],
        "ats": "Ashby",
        "careers_url": "https://linear.app/careers",
        "tech_stack": [
            "TypeScript",
            "React",
            "GraphQL",
            "Node.js",
            "Sync Engine",
            "WebSockets"
        ],
        "priority_roles": [
            "Full Stack Engineer",
            "Sync Engine Engineer",
            "Frontend Craft Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Linear%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "supabase",
        "name": "Supabase",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "35 - 65+ LPA (Open Source Firebase Alternative)",
        "tagline": "Open source Firebase alternative built on PostgreSQL with realtime subscriptions and Auth.",
        "locations": [
            "Remote Worldwide"
        ],
        "ats": "Ashby",
        "careers_url": "https://supabase.com/careers",
        "tech_stack": [
            "Elixir",
            "PostgreSQL",
            "TypeScript",
            "Go",
            "Rust",
            "Docker"
        ],
        "priority_roles": [
            "Software Engineer - Postgres",
            "Cloud Infrastructure Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Supabase%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "vercel",
        "name": "Vercel",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "38 - 72+ LPA (Next.js & Frontend Cloud)",
        "tagline": "The Frontend Cloud for Next.js, React, and Svelte, powering the best web experiences worldwide.",
        "locations": [
            "Remote Worldwide"
        ],
        "ats": "Ashby",
        "careers_url": "https://vercel.com/careers",
        "tech_stack": [
            "TypeScript",
            "Next.js",
            "React",
            "Rust",
            "Go",
            "Edge Networks"
        ],
        "priority_roles": [
            "Software Engineer - Platform",
            "Edge Systems Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Vercel%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "ramp",
        "name": "Ramp",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "42 - 80+ LPA (Finance Automation & Corporate Card)",
        "tagline": "Fastest growing corporate card and finance automation platform saving companies time and money.",
        "locations": [
            "Remote",
            "New York",
            "San Francisco"
        ],
        "ats": "Ashby",
        "careers_url": "https://ramp.com/careers",
        "tech_stack": [
            "Python",
            "React",
            "TypeScript",
            "PostgreSQL",
            "AWS",
            "Elixir"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Platform Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Ramp%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "retool",
        "name": "Retool",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "38 - 72+ LPA (Fast Internal Tools Platform)",
        "tagline": "The fastest way to build internal tools\u2014connecting databases, APIs, and modern UIs.",
        "locations": [
            "Remote",
            "San Francisco",
            "London"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://retool.com/careers",
        "tech_stack": [
            "TypeScript",
            "React",
            "Node.js",
            "PostgreSQL",
            "Docker",
            "Kubernetes"
        ],
        "priority_roles": [
            "Software Engineer",
            "Full Stack Engineer",
            "Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Retool%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "deel",
        "name": "Deel",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "35 - 65+ LPA (Global Payroll & Compliance)",
        "tagline": "All-in-one HR platform for global teams, managing international compliance and payroll.",
        "locations": [
            "Remote Worldwide"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.deel.com/careers",
        "tech_stack": [
            "Node.js",
            "React",
            "PostgreSQL",
            "TypeScript",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Senior Backend Developer",
            "Full Stack Developer",
            "Tech Lead"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Deel%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "rippling",
        "name": "Rippling",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "38 - 75+ LPA (Unified Workforce Platform)",
        "tagline": "Unified workforce management system managing HR, IT, and Finance on an integrated directory.",
        "locations": [
            "Bengaluru",
            "Remote",
            "San Francisco"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.rippling.com/careers",
        "tech_stack": [
            "Python",
            "Django",
            "React",
            "TypeScript",
            "MongoDB",
            "AWS"
        ],
        "priority_roles": [
            "Staff Software Engineer",
            "Backend Developer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Rippling%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "freshworks",
        "name": "Freshworks",
        "category": "unicorn",
        "category_label": "Product Unicorn / Scaleup",
        "pay_range": "20 - 45+ LPA (Cloud Customer Engagement SaaS)",
        "tagline": "Nasdaq-listed Indian SaaS success story building fresh, modern business software for IT and CRM.",
        "locations": [
            "Chennai",
            "Bengaluru"
        ],
        "ats": "SmartRecruiters",
        "careers_url": "https://www.freshworks.com/company/careers/",
        "tech_stack": [
            "Ruby on Rails",
            "Java",
            "Python",
            "Ember",
            "React",
            "AWS",
            "Kafka"
        ],
        "priority_roles": [
            "Lead Software Engineer",
            "Senior Software Developer",
            "Cloud Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Freshworks%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "spotify",
        "name": "Spotify",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "36 - 72+ LPA (Audio Streaming & Recommendations)",
        "tagline": "World's most popular audio streaming subscription service with legendary engineering culture.",
        "locations": [
            "Remote",
            "Stockholm",
            "London",
            "New York"
        ],
        "ats": "Direct",
        "careers_url": "https://www.lifeatspotify.com/jobs",
        "tech_stack": [
            "Java",
            "Python",
            "C++",
            "GCP",
            "Docker",
            "Kafka",
            "React"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Backend Developer",
            "Data Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Spotify%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "asml",
        "name": "ASML",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "32 - 65+ LPA (Lithography Systems & Nanometer Tech)",
        "tagline": "The world's leading semiconductor equipment maker producing extreme ultraviolet (EUV) photolithography machines.",
        "locations": [
            "Bengaluru",
            "Veldhoven (Netherlands)",
            "Remote"
        ],
        "ats": "Workday",
        "careers_url": "https://www.asml.com/en/careers",
        "tech_stack": [
            "C++",
            "Python",
            "Linux",
            "Mathematical Algorithms",
            "Embedded Real-Time",
            "Java"
        ],
        "priority_roles": [
            "Software Design Engineer",
            "Algorithm Developer",
            "Embedded Specialist"
        ],
        "google_jobs_url": "https://www.google.com/search?q=ASML%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "booking",
        "name": "Booking.com",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "30 - 62+ LPA (Travel E-commerce & High QPS)",
        "tagline": "Global travel e-commerce leader operating at massive global scale with thousands of microservices.",
        "locations": [
            "Bengaluru",
            "Amsterdam",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.booking.com/",
        "tech_stack": [
            "Java",
            "Perl / Python",
            "React",
            "Kafka",
            "MySQL",
            "Kubernetes",
            "AWS"
        ],
        "priority_roles": [
            "Software Engineer",
            "Full Stack Developer",
            "Machine Learning Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Booking.com%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "adyen",
        "name": "Adyen",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "36 - 70+ LPA (Single Payment Platform)",
        "tagline": "European fintech giant providing end-to-end payments infrastructure for top global brands.",
        "locations": [
            "Amsterdam",
            "London",
            "Singapore",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://careers.adyen.com/",
        "tech_stack": [
            "Java",
            "PostgreSQL",
            "React",
            "Distributed Architecture",
            "High Security"
        ],
        "priority_roles": [
            "Software Engineer - Payments",
            "Backend Developer",
            "Infrastructure Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Adyen%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "revolut",
        "name": "Revolut",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "32 - 65+ LPA (Global Neobank & Trading)",
        "tagline": "Global financial super-app with 45+ million customers managing currency exchange, stock, and crypto.",
        "locations": [
            "Bengaluru",
            "Remote",
            "London"
        ],
        "ats": "Lever",
        "careers_url": "https://www.revolut.com/careers/",
        "tech_stack": [
            "Java",
            "Kotlin",
            "React",
            "GCP",
            "PostgreSQL",
            "Docker"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Backend Developer",
            "Frontend Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Revolut%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "klarna",
        "name": "Klarna",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "30 - 60+ LPA (AI-Powered Commerce & BNPL)",
        "tagline": "AI-powered global payments network and shopping destination modernizing e-commerce.",
        "locations": [
            "Stockholm",
            "Berlin",
            "Remote"
        ],
        "ats": "Workday",
        "careers_url": "https://www.klarna.com/careers/",
        "tech_stack": [
            "JavaScript",
            "Node.js",
            "Java",
            "Python",
            "AWS",
            "React"
        ],
        "priority_roles": [
            "Software Engineer",
            "Full Stack Developer",
            "Data Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Klarna%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "delivery_hero",
        "name": "Delivery Hero",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "28 - 56+ LPA (Quick Commerce & Global Food)",
        "tagline": "World's leading local delivery platform operating in over 70 countries.",
        "locations": [
            "Berlin",
            "Remote",
            "Singapore"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://careers.deliveryhero.com/",
        "tech_stack": [
            "Python",
            "Go",
            "Kotlin",
            "React",
            "Kubernetes",
            "AWS",
            "Kafka"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Backend Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Delivery%20Hero%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "wise",
        "name": "Wise (TransferWise)",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "32 - 62+ LPA (Cross-Border Financial Engine)",
        "tagline": "Global tech company building the best way to move and manage money around the world without borders.",
        "locations": [
            "London",
            "Tallinn",
            "Singapore",
            "Remote"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.wise.jobs/",
        "tech_stack": [
            "Java",
            "Spring Boot",
            "React",
            "PostgreSQL",
            "AWS",
            "Microservices"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Developer",
            "Product Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Wise%20%28TransferWise%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "bytedance",
        "name": "ByteDance (TikTok)",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "40 - 80+ LPA (High QPS Algorithms & Feed)",
        "tagline": "Global tech giant operating TikTok, building billion-user recommendation engines and distributed systems.",
        "locations": [
            "Singapore",
            "San Jose",
            "London",
            "Remote"
        ],
        "ats": "Direct",
        "careers_url": "https://jobs.bytedance.com/en",
        "tech_stack": [
            "Go",
            "Python",
            "C++",
            "Distributed Systems",
            "Kubernetes",
            "High Scale Redis"
        ],
        "priority_roles": [
            "Software Engineer - Platform",
            "Backend Engineer",
            "Algorithm Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=ByteDance%20%28TikTok%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "grab",
        "name": "Grab",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "32 - 65+ LPA (Southeast Asia Superapp)",
        "tagline": "Southeast Asia's leading superapp providing deliveries, mobility, and financial services.",
        "locations": [
            "Bengaluru",
            "Singapore"
        ],
        "ats": "Workday",
        "careers_url": "https://grab.careers/",
        "tech_stack": [
            "Go",
            "Python",
            "React Native",
            "Kafka",
            "AWS",
            "MySQL"
        ],
        "priority_roles": [
            "Lead Software Engineer",
            "Senior Backend Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Grab%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "sea_group",
        "name": "Sea Group (Shopee & Garena)",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "32 - 62+ LPA (Gaming & E-commerce Hub)",
        "tagline": "Global consumer internet company operating Shopee e-commerce and Garena digital entertainment.",
        "locations": [
            "Bengaluru",
            "Singapore"
        ],
        "ats": "Direct",
        "careers_url": "https://career.sea.com/",
        "tech_stack": [
            "Go",
            "Python",
            "React",
            "C++",
            "MySQL",
            "Distributed Architecture"
        ],
        "priority_roles": [
            "Software Engineer",
            "Backend Developer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Sea%20Group%20%28Shopee%20%26%20Garena%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "rakuten",
        "name": "Rakuten India",
        "category": "europe_apac",
        "category_label": "European / APAC Tech Giant",
        "pay_range": "20 - 45+ LPA (Global Innovation Center)",
        "tagline": "Japanese internet and fintech giant's key global engineering center powering Rakuten ecosystem.",
        "locations": [
            "Bengaluru"
        ],
        "ats": "Direct",
        "careers_url": "https://rakuten.careers/",
        "tech_stack": [
            "Java",
            "Python",
            "Cloud Native",
            "React",
            "Kafka",
            "Data Engineering"
        ],
        "priority_roles": [
            "Senior Software Engineer",
            "Lead Developer",
            "Cloud Solutions Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Rakuten%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "two_sigma",
        "name": "Two Sigma",
        "category": "hft",
        "category_label": "HFT & Quantitative Trading",
        "pay_range": "60 LPA - 1.4 Cr+ (Quantitative Systems)",
        "tagline": "Financial sciences company using machine learning, distributed computing, and data science to trade globally.",
        "locations": [
            "Remote",
            "New York",
            "London",
            "Tokyo"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.twosigma.com/careers/",
        "tech_stack": [
            "C++",
            "Python",
            "Java",
            "Distributed Systems",
            "Linux Kernel",
            "Low Latency"
        ],
        "priority_roles": [
            "Quantitative Software Engineer",
            "Systems Engineer",
            "Data Platform Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Two%20Sigma%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "millennium",
        "name": "Millennium Management",
        "category": "hft",
        "category_label": "HFT & Quantitative Trading",
        "pay_range": "50 LPA - 1.2 Cr+ (Quantitative Tech)",
        "tagline": "Global alternative investment management firm with cutting-edge algorithmic execution platforms.",
        "locations": [
            "Bengaluru",
            "New York",
            "London",
            "Singapore"
        ],
        "ats": "Workday",
        "careers_url": "https://www.mlpm.com/careers/",
        "tech_stack": [
            "C++",
            "Python",
            "Low Latency",
            "KDB+",
            "Linux",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Quantitative Software Engineer",
            "Trading Systems Developer",
            "Cloud Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Millennium%20Management%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "point72",
        "name": "Point72",
        "category": "hft",
        "category_label": "HFT & Quantitative Trading",
        "pay_range": "50 LPA - 1.1 Cr+ (Cubist Systematic Strategies)",
        "tagline": "Global asset manager employing quantitative modeling and modern technology to trade public equity.",
        "locations": [
            "Remote",
            "New York",
            "London",
            "Singapore"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://point72.com/careers/",
        "tech_stack": [
            "C++",
            "Python",
            "Data Pipelines",
            "Linux",
            "Trading Infrastructure"
        ],
        "priority_roles": [
            "Quantitative Developer",
            "Software Engineer - Trading",
            "Systems Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Point72%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "optiver",
        "name": "Optiver",
        "category": "hft",
        "category_label": "HFT & Quantitative Trading",
        "pay_range": "65 LPA - 1.5 Cr+ (Market Making & Low Latency)",
        "tagline": "Leading global market maker improving financial markets with cutting-edge proprietary trading tech.",
        "locations": [
            "Amsterdam",
            "Sydney",
            "Singapore",
            "Chicago"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://optiver.com/working-at-optiver/career-opportunities/",
        "tech_stack": [
            "Modern C++ (C++20)",
            "FPGA",
            "Python",
            "Linux Kernel",
            "Hardware Acceleration"
        ],
        "priority_roles": [
            "Software Engineer - Execution",
            "FPGA Engineer",
            "Core Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Optiver%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "imc_trading",
        "name": "IMC Trading",
        "category": "hft",
        "category_label": "HFT & Quantitative Trading",
        "pay_range": "60 LPA - 1.4 Cr+ (Algorithmic Trading & FPGA)",
        "tagline": "Top algorithmic market maker trading on major exchanges worldwide with sub-microsecond latency.",
        "locations": [
            "Amsterdam",
            "Sydney",
            "Chicago",
            "Mumbai"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://www.imc.com/careers/",
        "tech_stack": [
            "C++",
            "FPGA",
            "Python",
            "Java",
            "Linux",
            "Low Latency Networking"
        ],
        "priority_roles": [
            "Software Engineer",
            "FPGA Developer",
            "Hardware Acceleration Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=IMC%20Trading%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "ge_vernova",
        "name": "GE Vernova / Healthcare",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Industrial Hub",
        "pay_range": "14 - 30+ LPA (Industrial IoT & Healthcare Tech)",
        "tagline": "Global industrial technology company pioneering digital energy grids and medical software systems.",
        "locations": [
            "Bengaluru",
            "Hyderabad"
        ],
        "ats": "Workday",
        "careers_url": "https://jobs.gecareers.com/",
        "tech_stack": [
            "Java",
            "Python",
            "Cloud",
            "IoT",
            "C++",
            "Kubernetes",
            "Microservices"
        ],
        "priority_roles": [
            "Staff Software Engineer",
            "Full Stack Developer",
            "Cloud Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=GE%20Vernova%20/%20Healthcare%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "abb",
        "name": "ABB India",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Industrial Hub",
        "pay_range": "12 - 28+ LPA (Industrial Automation & Robotics)",
        "tagline": "Technology leader in electrification and automation enabling a more sustainable and resource-efficient future.",
        "locations": [
            "Bengaluru",
            "Chennai"
        ],
        "ats": "Workday",
        "careers_url": "https://careers.abb/global/en",
        "tech_stack": [
            "C#",
            ".NET Core",
            "Cloud",
            "Python",
            "Industrial IoT",
            "React"
        ],
        "priority_roles": [
            "Senior Software Developer",
            "R&D Software Engineer",
            "Systems Architect"
        ],
        "google_jobs_url": "https://www.google.com/search?q=ABB%20India%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "john_deere",
        "name": "John Deere Technology Center (JDTCI)",
        "category": "enterprise_sap",
        "category_label": "Enterprise & Industrial Hub",
        "pay_range": "15 - 32+ LPA (Precision Ag & Cloud Platform)",
        "tagline": "Global agricultural and heavy machinery leader engineering autonomous tractors and precision cloud software.",
        "locations": [
            "Pune",
            "Bengaluru"
        ],
        "ats": "Workday",
        "careers_url": "https://www.deere.com/en/our-company/john-deere-careers/",
        "tech_stack": [
            "Java",
            "Python",
            "AWS",
            "IoT",
            "Embedded",
            "React"
        ],
        "priority_roles": [
            "Software Engineer",
            "Cloud Platform Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=John%20Deere%20Technology%20Center%20%28JDTCI%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "together_ai",
        "name": "Together AI",
        "category": "ai",
        "category_label": "Frontier AI & ML Research",
        "pay_range": "$150k - $380k+ / Remote (Cloud GPU & Inference)",
        "tagline": "Leading cloud platform for building and running generative AI models with state-of-the-art inference engines.",
        "locations": [
            "Remote Worldwide",
            "San Francisco"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.together.ai/careers",
        "tech_stack": [
            "PyTorch",
            "CUDA",
            "C++",
            "Python",
            "Kubernetes",
            "Distributed Training"
        ],
        "priority_roles": [
            "Inference Systems Engineer",
            "Cloud Infrastructure Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Together%20AI%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "groq",
        "name": "Groq",
        "category": "ai",
        "category_label": "Frontier AI & ML Research",
        "pay_range": "$160k - $400k+ / Remote (LPU Inference Engine)",
        "tagline": "Creator of the LPU (Language Processing Unit), setting world records for instantaneous real-time AI token generation.",
        "locations": [
            "Remote Worldwide",
            "Mountain View"
        ],
        "ats": "Greenhouse",
        "careers_url": "https://groq.com/careers/",
        "tech_stack": [
            "Compilers",
            "C++",
            "Python",
            "Silicon Architecture",
            "Distributed Systems"
        ],
        "priority_roles": [
            "Compiler Engineer",
            "Systems Software Engineer",
            "Cloud API Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Groq%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "anyscale",
        "name": "Anyscale",
        "category": "ai",
        "category_label": "Frontier AI & ML Research",
        "pay_range": "$150k - $360k+ / Remote (Ray Compute Platform)",
        "tagline": "The AI compute platform built by the creators of Ray, powering production training and LLM fine-tuning.",
        "locations": [
            "Remote",
            "San Francisco"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.anyscale.com/careers",
        "tech_stack": [
            "Ray",
            "Python",
            "C++",
            "Distributed Systems",
            "Kubernetes",
            "AWS"
        ],
        "priority_roles": [
            "Distributed Systems Engineer",
            "Backend Cloud Engineer",
            "Full Stack Engineer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Anyscale%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
    },
    {
        "id": "cursor",
        "name": "Cursor (Anysphere)",
        "category": "ai",
        "category_label": "Frontier AI & ML Research",
        "pay_range": "$180k - $450k+ / Remote (AI Code Editor)",
        "tagline": "The AI-first code editor built on VS Code, empowering millions of developers to write code 10x faster.",
        "locations": [
            "Remote Worldwide",
            "San Francisco"
        ],
        "ats": "Ashby",
        "careers_url": "https://www.cursor.com/careers",
        "tech_stack": [
            "TypeScript",
            "Rust",
            "C++",
            "VS Code Architecture",
            "Python",
            "PyTorch"
        ],
        "priority_roles": [
            "Core Editor Systems Engineer",
            "Model Training Engineer",
            "Full Stack Developer"
        ],
        "google_jobs_url": "https://www.google.com/search?q=Cursor%20%28Anysphere%29%20%28Software%20Engineer%20OR%20Developer%29%20%28%22Full%20Stack%22%20OR%20%22Backend%22%20OR%20%22Frontend%22%20OR%20%22AI%22%20OR%20%22Cloud%22%20OR%20%22Python%22%20OR%20%22Java%22%29&ibp=htl;jobs"
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
                search_lower in comp.get("pay_range", "").lower() or
                any(search_lower in loc.lower() for loc in comp.get("locations", [])) or
                any(search_lower in t.lower() for t in comp.get("tech_stack", [])) or
                any(search_lower in r.lower() for r in comp.get("priority_roles", []))
            )
            if not match_found:
                continue
                
        results.append(comp)
        
    return results
