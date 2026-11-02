import json
import os
import time

from function_analysis import (
    analyze_function
)

from core.base_agent import BaseAgent
from core.agent_metadata import AgentMetadata
from core.agent_dependency import AgentDependency
from core.execution_result import ExecutionResult


class FunctionAnalysisAgent(BaseAgent):

    @property
    def metadata(self):

        return AgentMetadata(
            agent_id="function_analysis",
            agent_name="Function Analysis Agent",
            version="1.0",
            agent_type="Analysis",
            status="Active"
        )

    @property
    def dependencies(self):

        return AgentDependency(
            requires=[
                "organization_profile.json"
            ],
            produces=[
                "function_analysis.json"
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
                "organization_profile.json",
                "r",
                encoding="utf-8"
            ) as file:

                profile = json.load(
                    file
                )

        except Exception as ex:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    f"Unable to load organization_profile.json: {str(ex)}"
                ]
            )

        functions = profile.get(
            "business_functions",
            []
        )

        results = []

        total_tokens = 0

        for function in functions:

            analysis = analyze_function(
                function
            )

            usage = analysis.get(
                "usage",
                {}
            )

            total_tokens += (
                usage.get(
                    "total_tokens"
                ) or 0
            )

            results.append(
                {
                    "function_name":
                        function.get(
                            "name",
                            "Unknown Function"
                        ),
                    "analysis":
                        analysis["result"]
                }
            )

        final_result = {
            "function_insights":
                results
        }

        try:

            temp_file = (
                "function_analysis.json.tmp"
            )

            with open(
                temp_file,
                "w",
                encoding="utf-8"
            ) as output:

                json.dump(
                    final_result,
                    output,
                    ensure_ascii=False,
                    indent=2
                )

            os.replace(
                temp_file,
                "function_analysis.json"
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
            "\nFUNCTION ANALYSIS GENERATED\n"
        )

        return ExecutionResult(
            status="Completed",
            agent_id=self.metadata.agent_id,
            output_artifact="function_analysis.json",
            duration_seconds=duration,
            total_tokens=total_tokens,
            errors=[]
        )