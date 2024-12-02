from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingredient in samosa are ")
    print(response.content)