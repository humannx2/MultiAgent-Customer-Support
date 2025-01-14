from crewai import Crew
from agents import qa_agent, support_agent
from tasks import quality_assurance_review, inquiry_resolution

crew = Crew(
  agents=[support_agent, qa_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=True,
  memory=True
)

inputs={
    "user":"Aditya",
    "query":"Can you help me understand what Social Hardware does?",
}

result=crew.kickoff(inputs=inputs)
print(result)