from google.adk.agents import SequentialAgent

from agents.ceo import create_ceo_agent
from agents.pm import create_pm_agent
from agents.uiux import create_uiux_agent
from agents.techLead import create_tech_agent

def create_company(retry_config):
    ceo = create_ceo_agent(retry_config)
    pm = create_pm_agent(retry_config)
    uiux = create_uiux_agent(retry_config)
    techLead = create_tech_agent(retry_config)

    return SequentialAgent(
        name = 'flow',
        sub_agents= [ceo]
    )

