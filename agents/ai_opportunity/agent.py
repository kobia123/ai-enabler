import json
import os
import time

from ai_opportunity_agent import (
    discover_opportunities
)

from core.base_agent import BaseAgent
from core.agent_metadata import AgentMetadata
from core.agent_dependency import AgentDependency
from core.execution_result import ExecutionResult


class AiOpportunityAgent(BaseAgent):

    @property
    def metadata(self):

        return AgentMetadata(
            agent_id="ai_opportunity",
            agent_name="AI Opportunity Agent",
            version="1.0",
            agent_type="Analysis",
            status="Active"
        )

    @property
    def dependencies(self):

        return AgentDependency(
            requires=[
                "function_analysis.json"
            ],
            produces=[
                "function_ai_opportunities.json"
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

        total_input_tokens = 0
        total_output_tokens = 0
        total_tokens = 0

        try:

            with open(
                "function_analysis.json",
                "r",
                encoding="utf-8"
            ) as file:

                analysis_data = json.load(
                    file
                )

        except Exception as ex:

            return ExecutionResult(
                status="Failed",
                agent_id=self.metadata.agent_id,
                output_artifact="",
                duration_seconds=0,
                errors=[
                    f"Unable to load function_analysis.json: {str(ex)}"
                ]
            )

        function_insights = (
            analysis_data.get(
                "function_insights",
                []
            )
        )

        results = []

        for function in function_insights:

            opportunities = (
                discover_opportunities(
                    function["analysis"]
                )
            )

            usage = opportunities.get(
                "usage",
                {}
            )

            total_input_tokens += (
                usage.get(
                    "input_tokens"
                ) or 0
            )

            total_output_tokens += (
                usage.get(
                    "output_tokens"
                ) or 0
            )

            total_tokens += (
                usage.get(
                    "total_tokens"
                ) or 0
            )

            results.append(
                {
                    "function_name":
                        function[
                            "function_name"
                        ],

                    "analysis":
                        function[
                            "analysis"
                        ],

                    "ai_opportunities":
                        opportunities[
                            "result"
                        ][
                            "ai_opportunities"
                        ]
                }
            )

        final_result = {
            "function_insights":
                results
        }

        try:

            temp_file = (
                "function_ai_opportunities.json.tmp"
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
                "function_ai_opportunities.json"
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
            "\nAI OPPORTUNITIES GENERATED\n"
        )

        return ExecutionResult(
            status="Completed",
            agent_id=self.metadata.agent_id,
            output_artifact="function_ai_opportunities.json",
            duration_seconds=duration,
            input_tokens=total_input_tokens,
            output_tokens=total_output_tokens,
            total_tokens=total_tokens,
            errors=[]
        )