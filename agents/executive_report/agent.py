import json
import os
import time

from core.base_agent import BaseAgent
from core.agent_metadata import AgentMetadata
from core.agent_dependency import AgentDependency
from core.execution_result import ExecutionResult

from executive_report_agent import (
    create_executive_report
)


class ExecutiveReportAgent(BaseAgent):

    @property
    def metadata(self):

        return AgentMetadata(
            agent_id="executive_report",
            agent_name="Executive Report Agent",
            version="1.0",
            agent_type="Reporting",
            status="Active"
        )

    @property
    def dependencies(self):

        return AgentDependency(
            requires=[
                "ai_roadmap.json"
            ],
            produces=[
                "executive_report.json"
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
                "ai_roadmap.json",
                "r",
                encoding="utf-8"
            ) as file:

                roadmap = json.load(
                    file
                )

        except Exception as ex:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    f"Unable to load ai_roadmap.json: {str(ex)}"
                ]
            )

        report = create_executive_report(
            roadmap
        )

        usage = report.get(
            "usage",
            {}
        )

        report_result = report.get(
            "result"
        )

        if report_result is None:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    "Executive report result is missing"
                ]
            )

        try:

            temp_file = (
                "executive_report.json.tmp"
            )

            with open(
                temp_file,
                "w",
                encoding="utf-8"
            ) as output:

                json.dump(
                    report_result,
                    output,
                    ensure_ascii=False,
                    indent=2
                )

            os.replace(
                temp_file,
                "executive_report.json"
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
            "\nEXECUTIVE REPORT GENERATED\n"
        )

        return ExecutionResult(
            status="Completed",
            agent_id=self.metadata.agent_id,
            output_artifact="executive_report.json",
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