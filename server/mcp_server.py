from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any

# Initialize FastMCP Server
mcp = FastMCP("AI-Internship-Career-Mentor-Tools")

@mcp.tool()
def get_career_paths(interests: List[str]) -> Dict[str, Any]:
    """
    Maps student technical interests to corresponding engineering domains.

    Args:
        interests: List of strings describing the student's technical interests.

    Returns:
        A dictionary with the original interests and the matched engineering domains.
    """
    matched_domains = set()
    interests_lower = [interest.lower() for interest in interests]

    for interest in interests_lower:
        if any(keyword in interest for keyword in ["security", "cyber", "hacking", "networking", "cryptography"]):
            matched_domains.add("Cybersecurity Engineering")
        if any(keyword in interest for keyword in ["database", "db", "sql", "nosql", "postgres", "mysql", "oracle", "data engineering"]):
            matched_domains.add("Database Administration & Data Engineering")
        if any(keyword in interest for keyword in ["ai", "ml", "machine learning", "deep learning", "neural", "nlp", "vision", "data science"]):
            matched_domains.add("Artificial Intelligence & Machine Learning Engineering")
        if any(keyword in interest for keyword in ["web", "frontend", "backend", "fullstack", "app", "software", "coding", "programming", "react", "javascript"]):
            matched_domains.add("Software / Web Development")
        if any(keyword in interest for keyword in ["cloud", "devops", "aws", "azure", "gcp", "kubernetes", "docker", "infrastructure"]):
            matched_domains.add("Cloud & DevOps Engineering")

    if not matched_domains:
        matched_domains.add("General Software Engineering")

    return {
        "interests": interests,
        "engineering_domains": sorted(list(matched_domains))
    }


@mcp.tool()
def get_skill_recommendations(target_role: str, current_skills: List[str] = None) -> Dict[str, Any]:
    """
    Looks up missing certifications and recommended skills based on a target role.

    Args:
        target_role: The role the student is aiming for (e.g., 'Cybersecurity Analyst').
        current_skills: Optional list of skills or certifications the student already has.

    Returns:
        A dictionary with recommended certifications and suggested skills.
    """
    target = target_role.lower()
    current = [skill.lower() for skill in current_skills] if current_skills else []

    certifications = []
    skills = []

    if any(keyword in target for keyword in ["cyber", "security", "network security", "soc", "pentest"]):
        certifications = [
            "IBM Cybersecurity Analyst Professional Certificate",
            "CompTIA Security+",
            "Certified Information Systems Security Professional (CISSP) Prep"
        ]
        skills = [
            "Network Security Protocols",
            "Incident Response",
            "Vulnerability Assessment",
            "Linux Command Line",
            "Wireshark / Packet Analysis"
        ]
    elif any(keyword in target for keyword in ["database", "db", "sql", "dba", "data engineer", "data analyst"]):
        certifications = [
            "TCS Database Administration Track",
            "Google Data Analytics Professional Certificate",
            "Oracle Database SQL Certified Associate"
        ]
        skills = [
            "SQL Query Optimization",
            "Relational Database Management Systems (RDBMS)",
            "Database Schema Design",
            "ETL (Extract, Transform, Load) Processes",
            "NoSQL Databases (e.g., MongoDB)"
        ]
    elif any(keyword in target for keyword in ["ai", "ml", "machine learning", "deep learning", "nlp", "computer vision", "data scientist"]):
        certifications = [
            "DeepLearning.AI TensorFlow Developer Professional Certificate",
            "AWS Certified Machine Learning - Specialty"
        ]
        skills = [
            "Python Programming",
            "TensorFlow & PyTorch",
            "Data Preprocessing & Feature Engineering",
            "Supervised and Unsupervised Learning",
            "Model Deployment & FastAPI"
        ]
    else:
        certifications = [
            "AWS Certified Developer - Associate",
            "Meta Back-End Developer Professional Certificate"
        ]
        skills = [
            "Data Structures & Algorithms",
            "Git & GitHub Version Control",
            "RESTful API Design",
            "System Design Principles",
            "Unit Testing & CI/CD"
        ]

    # Filter out skills/certifications the student already possesses (case-insensitive check)
    filtered_certs = [cert for cert in certifications if cert.lower() not in current]
    filtered_skills = [skill for skill in skills if skill.lower() not in current]

    return {
        "target_role": target_role,
        "recommended_certifications": filtered_certs,
        "suggested_skills_to_learn": filtered_skills
    }


@mcp.tool()
def get_internship_roles(background: List[str]) -> Dict[str, Any]:
    """
    Maps student tech backgrounds to specific internship roles.

    Args:
        background: List of keywords representing the student's tech background, coursework, or projects.

    Returns:
        A dictionary with the original background and matched internship roles.
    """
    background_combined = " ".join(background).lower()
    recommended = set()

    if any(keyword in background_combined for keyword in ["security", "cyber", "cryptography", "firewall", "network"]):
        recommended.add("Cybersecurity Analyst Intern")
        recommended.add("Information Security Intern")
    if any(keyword in background_combined for keyword in ["database", "sql", "db", "oracle", "mysql", "postgres", "nosql"]):
        recommended.add("Database Intern")
        recommended.add("Data Engineer Intern")
    if any(keyword in background_combined for keyword in ["ai", "ml", "machine learning", "deep learning", "tensorflow", "pytorch", "python"]):
        recommended.add("AI/ML Engineer Intern")
        recommended.add("Data Science Intern")
    if any(keyword in background_combined for keyword in ["web", "frontend", "backend", "fullstack", "react", "javascript", "node", "html", "css"]):
        recommended.add("Software Engineer Intern")
        recommended.add("Web Developer Intern")
    if any(keyword in background_combined for keyword in ["cloud", "devops", "aws", "azure", "docker", "kubernetes"]):
        recommended.add("Cloud Engineer Intern")
        recommended.add("DevOps Intern")

    if not recommended:
        recommended.add("Software Engineer Intern")
        recommended.add("IT Support Intern")

    return {
        "background": background,
        "recommended_roles": sorted(list(recommended))
    }

# Create FastAPI wrapper
app = FastAPI(
    title="AI Career Mentor MCP Service",
    description="Standards-compliant Model Context Protocol server exposing career planning tools.",
    version="1.0.0"
)

# Mount FastMCP streamable http endpoints
app.mount("/mcp", mcp.streamable_http_app())
