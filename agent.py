import os
from google.adk.apps import App
from app.agents.supervisor import root_agent

# Force Google AI Studio mode instead of Vertex AI
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

# Resolve path and load parent-level .env file dynamically
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base_dir, ".env")
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                parts = line.split("=", 1)
                if len(parts) == 2:
                    os.environ[parts[0].strip()] = parts[1].strip()

# Build the main ADK App
app = App(
    root_agent=root_agent,
    name="app",
)
