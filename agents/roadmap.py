from google.adk.agents import Agent
from google.adk.models import Gemini
from app.prompts.personas import ROADMAP_PROMPT

roadmap_agent = Agent(
    name="roadmap_agent",
    description="Use this tool to structure a detailed 3, 6, or 12-month study and preparation timeline based on the student's background and previous analyses.",
    model=Gemini(model="gemini-2.5-flash"),
    instruction=ROADMAP_PROMPT,
    tools=[]
)
