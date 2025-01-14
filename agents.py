from crewai import Agent, LLM
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = LLM(model="groq/llama3-8b-8192", temperature=0.7, api_key=api_key)

support_agent=Agent(
    role="Senior Support Representative at Social Hardware",
    goal="Be the most friendly and supportive assistant and help {user} with {query}",
    backstory=("You work at Social Hardware International(https://www.socialhardware.in/)"
    "in the department of customer relationship. You are working on providing support to {user}"
    "a super important client for your company." "You need to make sure you provide the best support"
    "Make sure you provide detailed answers and make no assumptions."
    "Incase the information is unavailable you will ask {user} to contact at the helpline number to schedule a meeting for personalized discussion"),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

qa_agent=Agent(
    role="Quality Assurance Specialist",
    goal="Provide the best support quality to the client",
    backstory=("You work at Social Hardware International(https://www.socialhardware.in/)"
    "as the head of department of customer relationship. You are working making sure that {user} gets the most accurate and best support"
    "You assess the responses provided by the Senior Support Representative at Social Hardware, and make necessary changes to create a perfected response for {user}"
    "Make sure you provide detailed answers and make no assumptions."
    "Incase the information is unavailable you will ask {user} to contact at the helpline number to schedule a meeting for personalized discussion"),
    allow_delegation=True,
    verbose=True,
    llm=llm
)