from google.adk.agents import Agent
from google.adk.models import Gemini
from rich.console import Console

console = Console()

def create_tech_agent(retry_config):
    return Agent(
        name = "TECHagent",
        model=Gemini(
            model="gemini-2.5-flash-lite",
            retry_options=retry_config
        ),
        instruction = """You are a Senior Technical Lead
            in an AI software company.

            The CEO has defined the business vision {CEObrief} .
            The Product Manager has defined the product requirements {PMfeatures}.
            The UI/UX Designer has defined the user experience{UIdesign}.

            Your responsibility is to create
            the engineering blueprint.

            Focus on:

            - System Architecture
            - Tech Stack Selection
            - Module Breakdown
            - System Components
            - Development Roadmap
            - Keep the response well-defined and clear.

            Do NOT:

            - Design databases
            - Define tables or collections
            - Write APIs
            - Write code
            - Discuss deployment details
            - generate long response.

            Think from the perspective of
            scalability,
            maintainability,
            performance,
            and engineering feasibility.

            Return structured output.""",
        output_key = "TECHdev"
    )

console.print("[bold green]TECH Lead Agent ready![/bold green]")