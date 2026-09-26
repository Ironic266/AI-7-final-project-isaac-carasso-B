from urllib import response

from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.google.drive import GoogleDriveTools
#from agno.tools.websearch import WebSearchTools
from agno.models.openai import OpenAIResponses
load_dotenv()

IDEA_NAME = "hourglass-B_1.0"
IDEA_DESCRIPTION = "a lightweight desktop application written in Python that displays an hourglass animated GIF inside a small “messagebox-style” window. The user can choose a desired **cycle time** (the duration of a full GIF loop) using a dropdown or manual text input. The application adjusts playback timing to match the selected cycle time while enforcing bounds of **1–120 seconds**. A special playback rule applies: **the last 9 frames always play at 12 FPS**, regardless of the chosen cycle time. The UI provides real-time indicators including current frame index, selected cycle time, and computed effective frame rate."


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

def _normalize_agent_output(response: object) -> str:
    if isinstance(response, str):
        return response.strip()

    for attribute in ("content", "text", "output", "message"):
        value = getattr(response, attribute, None)
        if isinstance(value, str) and value.strip():
            return value.strip()

    return str(response).strip()

def create_hl_design(
    idea_name: str,
    idea_description: str
) -> str:
    prompt = (
        f"Create a complete high-level design document in Markdown for the following software idea.\n"
        f"Idea name: {idea_name}\n"
        f"Idea description: {idea_description}\n"
    )
    
    # response = agent.print_response(prompt, stream=False)
    #agent.stream=True;
    response = agent.run(prompt)
    # generated = _normalize_agent_output(response)
    return _normalize_agent_output(response)

def main() -> None:
    hl_design = create_hl_design(
        idea_name=IDEA_NAME,
        idea_description=IDEA_DESCRIPTION
    )
    print(hl_design)

if __name__ == "__main__":
    main()