from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.agent_tool import AgentTool
from app.prompts.personas import ADK_SUPERVISOR_INSTRUCTION
from app.agents.career import career_agent
from app.agents.internship import internship_agent
from app.agents.roadmap import roadmap_agent

# Wrap sub-agents as tools for the supervisor
career_tool = AgentTool(agent=career_agent)
internship_tool = AgentTool(agent=internship_agent)
roadmap_tool = AgentTool(agent=roadmap_agent)

# Supervisor root agent orchestration
root_agent = Agent(
    name="supervisor_agent",
    model=Gemini(model="gemini-flash-latest"),
    instruction=ADK_SUPERVISOR_INSTRUCTION,
    tools=[career_tool, internship_tool, roadmap_tool]
)
