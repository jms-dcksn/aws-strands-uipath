from contextlib import asynccontextmanager
import dataclasses
from mcp import ClientSession
from strands import Agent, tool
import os
from dotenv import load_dotenv
from mcp.client.streamable_http import streamablehttp_client

# Load environment variables from .env file
load_dotenv()

@dataclasses.dataclass
class AgentInput:
    message: str

@asynccontextmanager
async def make_agent():
    async with streamablehttp_client(
        url=os.getenv("UIPATH_MCP_URL"),
        headers={"Authorization": f"Bearer {os.getenv('UIPATH_ACCESS_TOKEN')}"},
        timeout=60,
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(tools)
            agent = Agent(
                system_prompt="You are a helpful assistant that can use MCP tools. Use your tools to search the web for the user's query.",
                tools=tools,
                callback_handler=None
            )
            yield agent

async def main(input: AgentInput):
    # Ask the agent a question that uses the available tools
    message = input.message
    async with make_agent() as agent:
        result = await agent.invoke_async(message)
        #print(result)
        return result

# # Run the async function
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main(AgentInput(message="Tell me recent news about the stock market.")))