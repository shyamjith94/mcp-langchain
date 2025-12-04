from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from dotenv import load_dotenv
load_dotenv()
import os
import asyncio


async def main():
    print("Starting client...")
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    print("GROQ_API_KEY set")
    client = MultiServerMCPClient(
       {
           "math":{
               "command": "python",
               "args": ["math_response"],
               "transport": "stdio",
           },
           "whether":{
               "url": "http://localhost:8000/mcp",
               "transport": "streamable-http",
           }
       }
    )


    tools = await client.get_tools()
    print(f"tools: {tools}")
    model = ChatGroq(model="qwen/qwen3-32b")
    agent = create_react_agent(model, tools)
    prompt = "What is 10 + 20?"
    llm_response = await model.ainvoke(
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"raw llm response: {llm_response}")

    agent_response = await agent.ainvoke({"input": prompt})
    print(f"agent response: {agent_response}")

# if __name__ == "__main__":
asyncio.run(main())