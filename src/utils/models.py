from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
model = "qwen3.5:9b"
llm = ChatOllama(model=model,temperature=0)