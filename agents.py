from crewai import Agent
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini",Temperature=0.6)

market_analyst=Agent(
    role="Market Analyst",
    goal="Analyze the market potential of the startup idea",
    backstory="You are a business expert with deep knowledge of trends, competitors, and demand forecasting.",
    llm=llm,
    verbose=True
)

tech_expert=Agent(
    role="Tech Expert",
    goal="Evaluate the technical feasibility of the startup idea",
    backstory="You are a tech expert with expertise in coding, algorithms, and software development.You have many years of building scalable software systems for startups and tech giants.",
    llm=llm,
    verbose=True
)

venture_capitalist=Agent(
    role="Venture Capitalist",
    goal="Evaluate the potential of the startup idea",
    backstory="You are a venture capitalist with a track record of investing in startups and tech companies.You have a deep understanding of the market and are looking for high-potential startups that have the potential to become successful businesses.Analyze the potential growth for the startup and thereby allocate funds by stating out improvements and features of the startup.",
    llm=llm,
    verbose=True
)



