from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-128k", api_key=api_key)

prompt = "Hello, how are you Ram?"
print(chat_model.invoke(prompt))


