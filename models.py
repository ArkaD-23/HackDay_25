from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = AzureChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"), 
    api_version="2024-02-01", 
    azure_endpoint="https://models.inference.ai.azure.com",
    model="gpt-4o", 
)