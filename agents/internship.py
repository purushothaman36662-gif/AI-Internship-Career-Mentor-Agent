from google.adk.agents import Agent
from google.adk.models import Gemini
from app.prompts.personas import INTERNSHIP_PROMPT
from app.tools.mcp_client import get_internship_roles

internship_agent = Agent(
    name="internship_agent",
    description="Use this tool to map a student's tech background to specific internship roles and get positioning advice.",
    model=Gemini(model="gemini-flash-latest"),
    instruction=INTERNSHIP_PROMPT,
    tools=[get_internship_roles]
)
