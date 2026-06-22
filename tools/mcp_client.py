from typing import List, Dict, Any
from app.server.mcp_server import (
    get_career_paths as direct_get_career_paths,
    get_skill_recommendations as direct_get_skill_recommendations,
    get_internship_roles as direct_get_internship_roles
)
from app.tools.security import validate_prompt

def get_career_paths(interests: List[str]) -> Dict[str, Any]:
    """
    Maps student technical interests to corresponding engineering domains.

    Args:
        interests: List of strings describing the student's technical interests.

    Returns:
        A dictionary with the original interests and the matched engineering domains.
    """
    # Apply security filter to inputs
    for interest in interests:
        validate_prompt(interest)
        
    return direct_get_career_paths(interests)


def get_skill_recommendations(target_role: str, current_skills: List[str] = None) -> Dict[str, Any]:
    """
    Looks up missing certifications and recommended skills based on a target role.

    Args:
        target_role: The role the student is aiming for (e.g., 'Cybersecurity Analyst').
        current_skills: Optional list of skills or certifications the student already has.

    Returns:
        A dictionary with recommended certifications and suggested skills.
    """
    # Apply security filter to inputs
    validate_prompt(target_role)
    if current_skills:
        for skill in current_skills:
            validate_prompt(skill)

    return direct_get_skill_recommendations(target_role, current_skills)


def get_internship_roles(background: List[str]) -> Dict[str, Any]:
    """
    Maps student tech backgrounds to specific internship roles.

    Args:
        background: List of keywords representing the student's tech background.

    Returns:
        A dictionary with the original background and matched internship roles.
    """
    # Apply security filter to inputs
    for bg in background:
        validate_prompt(bg)
        
    return direct_get_internship_roles(background)
