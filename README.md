# AWS Strands Agent with UiPath MCP Tools

This project demonstrates how to create an AWS Strands Agent that integrates with UiPath MCP (Model Context Protocol) tools, enabling seamless automation workflows and the ability to publish the agent to UiPath Cloud for orchestration and governance.

## Overview

This example showcases:
- **AWS Strands Agent**: A powerful AI agent framework for building intelligent automation solutions
- **UiPath MCP Integration**: Connects to UiPath's Model Context Protocol tools for enterprise automation capabilities
- **Cloud Deployment**: Ability to publish and orchestrate the agent in UiPath Cloud with full governance controls

## Features

- 🤖 **Intelligent Agent**: Built with AWS Strands for advanced AI capabilities
- 🔧 **MCP Tool Integration**: Leverages UiPath MCP tools for enterprise automation
- ☁️ **Cloud Ready**: Designed for deployment and orchestration in UiPath Cloud
- 🔐 **Secure**: Uses environment-based authentication and secure token management
- 🚀 **Scalable**: Built for enterprise-scale automation workflows

## Prerequisites

- Python 3.10 or higher
- UiPath Cloud account with MCP access
- AWS Strands Agent credentials
- Environment variables configured for authentication

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd aws-strands
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or using uv (recommended)
uv sync
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

## Configuration

Create a `.env` file with the following variables:

```env
UIPATH_MCP_URL=your_uipath_mcp_endpoint
UIPATH_ACCESS_TOKEN=your_uipath_access_token
```

## Usage

### Basic Usage

```python
from main import main, AgentInput
import asyncio

async def run_agent():
    result = await main(AgentInput(message="Your query here"))
    print(result)

# Run the agent
asyncio.run(run_agent())
```

### Example Queries

The agent can handle various types of queries using the available MCP tools:

- "Search for recent news about AI automation"
- "Get information about UiPath platform updates"
- "Analyze current market trends in RPA"

## Publishing to UiPath Cloud

This agent is designed to be published to UiPath Cloud for enterprise orchestration and governance:

### Benefits of UiPath Cloud Deployment

- **Centralized Orchestration**: Manage and schedule agent workflows from a single platform
- **Enterprise Governance**: Full audit trails, compliance controls, and security management
- **Scalability**: Automatically scale based on demand and workload
- **Integration**: Seamless integration with existing UiPath automation workflows
- **Monitoring**: Real-time monitoring and alerting capabilities

### Deployment Steps

1. **Package the Agent**: The agent is ready for packaging with the current structure
2. **Configure Cloud Settings**: Set up authentication and permissions in UiPath Cloud
3. **Deploy**: Use UiPath's deployment tools to publish the agent
4. **Orchestrate**: Configure workflows and scheduling in UiPath Cloud
5. **Monitor**: Set up monitoring and alerting for the deployed agent

## Project Structure

```
aws-strands/
├── main.py              # Main agent implementation
├── pyproject.toml       # Project dependencies and metadata
├── README.md           # This file
├── .env                # Environment variables (create from .env.example)
└── requirements.txt    # Python dependencies
```

## Dependencies

- `strands-agents>=1.0.1`: AWS Strands Agent framework
- `strands-agents-builder>=0.1.7`: Agent building utilities
- `strands-agents-tools>=0.2.1`: Additional agent tools
- `uipath>=2.0.82`: UiPath SDK for MCP integration
- `python-dotenv>=1.0.0`: Environment variable management

