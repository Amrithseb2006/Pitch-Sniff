from crewai import Task
from agents import market_analyst, tech_expert, venture_capitalist

from crewai import Task
from agents import market_analyst, tech_expert, venture_capitalist

def define_tasks(idea: str):
    market_task = Task(
        description=f"Analyze the market potential for the following startup idea: {idea}",
        expected_output="Detailed market analysis, including size, growth trends, target demographics, and competition.",
        agent=market_analyst
    )

    tech_task = Task(
        description=f"Evaluate how technically feasible the following startup idea is: {idea}",
        expected_output="Assessment of technical implementation, possible challenges, and required tech stack.",
        agent=tech_expert
    )

    vc_task = Task(
        description=f"As a VC, assess whether this startup idea is fundable, with reasons: {idea}",
        expected_output="Funding score (1-10) with explanation based on market, team, and product.",
        agent=venture_capitalist
    )

    return [market_task, tech_task, vc_task]
