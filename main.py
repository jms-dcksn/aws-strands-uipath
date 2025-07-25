from contextlib import asynccontextmanager
import dataclasses
from mcp import ClientSession
from strands import Agent
import os
from dotenv import load_dotenv
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient

def configure_ssl_context() -> None:
    """Configure SSL context with proper certificate paths."""
    import os
    import ssl

    default_paths = ssl.get_default_verify_paths()
    if default_paths.cafile:
        os.environ["SSL_CERT_FILE"] = default_paths.cafile
    if not os.getenv("SSL_CERT_DIR", None):
        os.environ["SSL_CERT_DIR"] = default_paths.capath or "/etc/ssl/certs"

# Configure SSL context before loading environment variables
configure_ssl_context()

# Load environment variables from .env file
load_dotenv()

@dataclasses.dataclass
class AgentInput:
    message: str


streamable_http_mcp_client = MCPClient(lambda: streamablehttp_client(
    url=os.getenv("UIPATH_MCP_URL"),
    headers={"Authorization": f"Bearer {os.getenv('UIPATH_ACCESS_TOKEN')}"},
    timeout=60,
))

# Create a global agent variable
agent = None

def initialize_agent():
    """Initialize the agent with MCP tools"""
    global agent
    with streamable_http_mcp_client:
        # Get the tools from the MCP server
        tools = streamable_http_mcp_client.list_tools_sync()
        print(tools)
        # Create an agent with these tools
        agent = Agent(
            tools=tools,
            system_prompt="You are a helpful assistant that can use MCP tools. Use the WebSummaryAPIWF MCP tool to search the web for the user's query.",
            callback_handler=None
        )
    return agent

async def main(input: AgentInput):
    # Initialize the agent if not already done
    if agent is None:
        initialize_agent()
    
    # Ask the agent a question that uses the available tools
    message = input.message
    
    # Use the agent within the MCP client context
    with streamable_http_mcp_client:
        result = await agent.invoke_async(message)
        return result

# Alternative approach using async context manager
# @asynccontextmanager
# async def make_agent():
#     async with streamablehttp_client(
#         url=os.getenv("UIPATH_MCP_URL"),
#         headers={"Authorization": f"Bearer {os.getenv('UIPATH_ACCESS_TOKEN')}"},
#         timeout=60,
#     ) as (read, write, _):
#         async with ClientSession(read, write) as session:
#             await session.initialize()
#             tools = await session.list_tools()
#             print(tools)
#             agent = Agent(
#                 system_prompt="You are a helpful assistant that can use MCP tools. Use the WebSummary MCP tool to search the web for the user's query.",
#                 tools=tools,
#                 callback_handler=None
#             )
#             yield agent

# async def main_with_context_manager(input: AgentInput):
#     """Alternative main function using the async context manager approach"""
#     async with make_agent() as agent:
#         result = await agent.invoke_async(input.message)
#         return result

# Run the async function
# if __name__ == "__main__":
#     import asyncio
#     # Use the context manager approach for better resource management
#     asyncio.run(main(AgentInput(message="Tell me recent news about the stock market.")))