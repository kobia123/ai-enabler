import json
import os
import time

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

    def execute(
        self,
        context
    ):

        start_time = time.time()

        try:

            with open(
                "function_ai_opportunities.json",
                "r",
                encoding="utf-8"
            ) as file:

                insights = json.load(
                    file
                )

        except Exception as ex:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    f"Unable to load function_ai_opportunities.json: {str(ex)}"
                ]
            )

        roadmap = build_roadmap(
            insights
        )

        usage = roadmap.get(
            "usage",
            {}
        )

        roadmap_result = roadmap.get(
            "result"
        )

        if roadmap_result is None:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    "Roadmap result is missing"
                ]
            )

        try:

            temp_file = (
                "ai_roadmap.json.tmp"
            )

            with open(
                temp_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    roadmap_result,
                    file,
                    ensure_ascii=False,
                    indent=2
                )

            os.replace(
                temp_file,
                "ai_roadmap.json"
            )

        except Exception as ex:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    str(ex)
                ]
            )

        duration = round(
            time.time() - start_time,
            2
        )

        print(
            "\nROADMAP GENERATED\n"
        )

        return ExecutionResult(
            status="Completed",
            agent_id=self.metadata.agent_id,
            output_artifact="ai_roadmap.json",
            duration_seconds=duration,
            input_tokens=usage.get(
                "input_tokens"
            ),
            output_tokens=usage.get(
                "output_tokens"
            ),
            total_tokens=usage.get(
                "total_tokens"
            ),
            errors=[]
        )