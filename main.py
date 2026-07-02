from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(model="gpt-4o-mini")

content = "coding"

result = chat_model.invoke(f"Write a poem about {content}.")
print(result.content)
