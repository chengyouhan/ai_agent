from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()


def main():
    llm = ChatOpenAI(model="gemma3:27b",
    base_url="http://203.71.78.31:8000/v1",
    api_key="sk-12345678",temperature=0.0)
    with open("workspace/SOUL.md", "r", encoding="utf-8") as f:
        soul_content = f.read()
    with open("workspace/USER.md", "r", encoding="utf-8") as f:
        user_content = f.read()

    system_prompt = f"{soul_content}\n\n{user_content}"
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content="請自我介紹")
    ]

    for chunk in llm.stream(messages):
        print(chunk.content, end="", flush=True)
    # response = llm.invoke(messages)

    # print(response)
    # print(response.content)

if __name__ == "__main__":
    main()
