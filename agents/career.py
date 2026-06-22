from google.adk.agents import Agent
from google.adk.models import Gemini
from app.prompts.personas import CAREER_PROMPT
from app.tools.mcp_client import get_career_paths, get_skill_recommendations

career_agent = Agent(
    name="career_agent",
    description="Use this tool to perform a career skill gap analysis and find recommended certification tracks based on student interests and target roles.",
    model=Gemini(model="gemini-2.5-flash"),
    instruction=CAREER_PROMPT,
    tools=[get_career_paths, get_skill_recommendations]
)
