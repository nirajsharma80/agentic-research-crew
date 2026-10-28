import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import SerperDevTool

def run_research(topic: str, audience: str) -> str:
    llm=LLM(model=os.getenv("CREWAI_MODEL","gemini/gemini-2.5-flash"),api_key=os.environ["GOOGLE_API_KEY"],temperature=0.2)
    search=SerperDevTool()
    researcher=Agent(role="Research analyst",goal="Find current, relevant evidence for {topic}",backstory="A careful analyst who searches several angles, records source URLs, and distinguishes facts from assumptions.",tools=[search],llm=llm,verbose=False,allow_delegation=False)
    editor=Agent(role="Research editor",goal="Turn verified evidence into a balanced decision brief for {audience}",backstory="An editor who values concise synthesis, explicit uncertainty, and traceable sources.",llm=llm,verbose=False,allow_delegation=False)
    gather=Task(description="Research this question: {topic}. Search for recent credible sources. Return a compact evidence log with source title, URL, date when available, key finding, and caveats. Do not invent sources.",expected_output="A source-linked evidence log with at least three distinct sources where available, plus any evidence gaps.",agent=researcher)
    brief=Task(description="Using only the researcher's evidence log, prepare a brief for {audience}. Include an executive summary, evidence table with links, practical implications, open questions, and a short confidence note. Flag anything that could not be verified.",expected_output="A polished Markdown research brief with links and explicit caveats.",agent=editor,context=[gather])
    crew=Crew(agents=[researcher,editor],tasks=[gather,brief],process=Process.sequential,verbose=False)
    result=crew.kickoff(inputs={"topic":topic,"audience":audience})
    return str(result)
