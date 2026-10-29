from agents.registry import AgentRegistry


registry = AgentRegistry()

print(
    "\n=== AGENTS ==="
)

for agent in registry.list_agents():

    print(
        agent.metadata.agent_id
    )

print(
    "\n=== LOOKUP ==="
)

roadmap = registry.get(
    "roadmap"
)

print(
    roadmap.metadata
)

print(
    "\n=== EXISTS ==="
)

print(
    registry.exists(
        "executive_report"
    )
)

print(
    registry.exists(
        "fake_agent"
    )
)