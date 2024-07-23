from dotenv import load_dotenv
from llama_index.llms.groq import Groq

load_dotenv()

llm = Groq(model="llama-3.1-70b-versatile")

response = llm.complete("Explain the importance of low latency LLMs")

print(response)
