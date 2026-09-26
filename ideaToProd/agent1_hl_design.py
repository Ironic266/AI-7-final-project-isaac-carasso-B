from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.google_drive import GoogleDriveTools
#from agno.tools.websearch import WebSearchTools
from agno.models.openai import OpenAIResponses
load_dotenv()

idea_name = "hourglass-B_1.0"
idea_description = "a lightweight desktop application written in Python that displays an hourglass animated GIF inside a small “messagebox-style” window. The user can choose a desired **cycle time** (the duration of a full GIF loop) using a dropdown or manual text input. The application adjusts playback timing to match the selected cycle time while enforcing bounds of **1–120 seconds**. A special playback rule applies: **the last 9 frames always play at 12 FPS**, regardless of the chosen cycle time. The UI provides real-time indicators including current frame index, selected cycle time, and computed effective frame rate."


agent = Agent(
    name="hl_design",
    tools=[
        GoogleDriveTools(),
        #WebSearchTools()
    ],
    model=OpenAIResponses(id="gpt-5.2"),
    instructions=[
        "You are Agent 1 in the Idea-To-Prod platform.",
        "Receive a product idea and produce a high-level design document in Markdown.",
        "Be concrete, implementation-aware, and structured.",
        "Do not write code.",
        "The document must include these sections: Title, Executive Summary, Product Goals, Users and Personas, Primary Use Cases, Functional Requirements, Non-Functional Requirements, Assumptions, Constraints, System Context, High-Level Architecture, Main Components, Data Model, External Integrations, Security and Privacy, Observability, Deployment Considerations, Risks, Open Questions, and Recommended Next Steps.",
        "Where the prompt is ambiguous, make reasonable assumptions and list them explicitly.",
        "Output only valid Markdown."
    ],
    markdown=True,
    description="High-level design agent for software ideas.",
)

prompt = (
    f"Create a complete high-level design document in Markdown for the following software idea.\n"
    f"Idea name: {idea_name}\n"
    f"Idea description: {idea_description}\n"
)

agent.print_response(prompt, stream=True)