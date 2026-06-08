from google.adk.agents import Agent
from google.adk.models import Gemini
from rich.console import Console

console = Console()

def create_pm_agent(retry_config):
    return Agent(
        name = "PMagent",
        model=Gemini(
            model="gemini-2.5-flash-lite",
            retry_options=retry_config
        ),
        instruction = """You are a Senior Product Manager.

            The CEO has already defined the business vision {CEObrief}.

            Your responsibility is ONLY to define the product.

            Focus on:

            - MVP Features
            - Future Features
            - Feature Prioritization
            - Keep the response well-defined and clear.

            Do NOT:

            - Repeat business goals
            - Repeat target users
            - Ask business questions already answered by the CEO
            - Design APIs
            - Design databases
            - Choose technologies
            - Discuss infrastructure

            Return concise structured output.""",
        output_key = "PMfeatures"
    )

console.print("[bold green]PM Agent ready![/bold green]")