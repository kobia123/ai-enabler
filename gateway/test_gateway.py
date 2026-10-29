from agent_gateway import AgentGateway

gateway = AgentGateway()

gateway.execute(
    "roadmap",
    "BusinessAnalyst"
)

gateway.execute(
    "roadmap",
    "SolutionArchitect"
)

gateway.execute(
    "executive_report",
    "Executive"
)

gateway.execute(
    "unknown_agent",
    "PlatformAdmin"
)