from agents import tech_expert,market_analyst,venture_capitalist
from tasks import define_tasks
from crewai import Crew
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    startup_idea=input("Enter your startup idea: ")


    tasks=define_tasks(startup_idea)
    
    crew=Crew(
        agents=[tech_expert,market_analyst,venture_capitalist],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("Evaluation Results:",result)