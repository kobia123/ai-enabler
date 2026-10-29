from dataclasses import dataclass


@dataclass
class AgentMetadata:

    agent_id: str

    agent_name: str

    version: str

    agent_type: str

    status: str