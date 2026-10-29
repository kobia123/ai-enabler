from core.base_agent import BaseAgent
from core.agent_metadata import AgentMetadata
from core.agent_dependency import AgentDependency
from core.execution_result import ExecutionResult

from roadmap_agent import build_roadmap


class RoadmapAgent(BaseAgent):

    @property
    def metadata(self):

        return AgentMetadata(
            agent_id="roadmap",
            agent_name="Roadmap Agent",
            version="1.0",
            agent_type="Planning",
            status="Active"
        )

    @property
    def dependencies(self):

        return AgentDependency(
            requires=[
                "function_ai_opportunities.json"
            ],
            produces=[
                "ai_roadmap.json"
            ]
        )

    @property
    def tools(self):

        return []

    def execute(self, context):

        insights = context["insights"]

        roadmap = build_roadmap(
            insights
        )

        print(
            "\nROADMAP GENERATED\n"
        )

        print(
            roadmap
        )

        return ExecutionResult(
            status="Completed",
            agent_id=self.metadata.agent_id,
            output_artifact="ai_roadmap.json",
            duration_seconds=0,
            errors=[]
        )