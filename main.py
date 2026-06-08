import asyncio
from google.adk.runners import Runner
from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.genai import types
from dotenv import load_dotenv

from orchestrator import create_company
from report_generator import generate_report
from rich.console import Console
from config import *

console = Console()
load_dotenv()

retry_config=types.HttpRetryOptions(
    attempts=MAX_RETRIES,
    exp_base=EXP_BASE,
    initial_delay=INITIAL_DELAY,
    http_status_codes=HTTP_STATUS_CODES,
)

company = create_company(retry_config)
session_service = InMemorySessionService()

runner = Runner(agent=company, app_name='default', session_service=session_service)

#helper function
async def run_session(
        runner_instance: Runner,
        user_queries : list[str] | str = None,
        session_name : str = "default",
):
    """Helper function to run queries in a session and display responses."""
    print(f"\nSession: {session_name}")
    final_response = ""

    app_name = runner_instance.app_name

    try:
        session = await session_service.create_session(
            app_name=app_name, user_id='DEFAULT', session_id=session_name
        )
    except:
        session = await session_service.get_session(
            app_name=app_name, user_id='DEFAULT', session_service=session_name
        )

    if user_queries:

        if type(user_queries) == str:
            user_queries = [user_queries]
        
        for query in user_queries:
            print(f"\nUSer >>> {query}")
            query_content = types.Content(role = 'User', parts=[types.Part(text=query)])

            async for event in runner_instance.run_async(
                user_id='DEFAULT', session_id=session.id, new_message=query_content
            ):
                if event.is_final_response() and event.content and event.content.parts:
                    text = event.content.parts[0].text
                    if text and text!=None:
                        final_response+='\n\n'+text
    
    return final_response

async def main():

    idea = input("Describe your idea:\n")
    response = await run_session(runner, idea, 'session-1')

    console.print(f"""
[bold green]
=================================
DEVCOUNCIL PROJECT BLUEPRINT
=================================
[/bold green]
{response}
[bold green]
=================================
END OF REPORT
=================================
[/bold green]
    """)
    generate_report(response)

asyncio.run(main())