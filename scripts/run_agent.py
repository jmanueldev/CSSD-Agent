from langchain.agents import Tool
from cssd.agent.core import CSSDAgent
from tools.dummy_tool import dummy_tool

tools = [
    Tool(name="DummyTool", func=dummy_tool, description="Test tool")
]

agent = CSSDAgent(tools)

print(agent.run("Test query"))
