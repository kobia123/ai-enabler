from core.agent_metadata import AgentMetadata
from core.agent_dependency import AgentDependency


metadata = AgentMetadata(
    agent_id="roadmap",
    agent_name="Roadmap Agent",
    version="1.0",
    agent_type="Planning",
    status="Active"
)

dependency = AgentDependency(
    requires=["function_ai_opportunities.json"],
    produces=["ai_roadmap.json"]
)

print(metadata)
print(dependency)