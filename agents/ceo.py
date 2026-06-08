from google.adk.agents import Agent
from google.adk.models import Gemini
from rich.console import Console

console = Console()

def create_ceo_agent(retry_config):
    return Agent(
        name = "CEOagent",
        model=Gemini(
            model="gemini-2.5-flash",
            retry_options=retry_config
        ),
        instruction = """You are the CEO of an AI software company.

            Your responsibility is to convert
            a user's software idea into a clear project brief.

            You should:

            - Understand the business problem.
            - Identify target users.
            - Define business goals.
            - Determine project scope.
            - Keep the response well-defined and clear.

            Do NOT design APIs.
            Do NOT design databases.
            Do NOT choose technologies.
            DO NOT generate long response.

            Leave implementation decisions
            to specialist agents.

            Return structured output.""",
        output_key = "CEObrief"
    )

console.print("[bold green]CEO Agent ready![/bold green]")