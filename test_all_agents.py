import os

from agents.function_analysis.agent import FunctionAnalysisAgent
from agents.ai_opportunity.agent import AiOpportunityAgent
from agents.roadmap.agent import RoadmapAgent
from agents.executive_report.agent import ExecutiveReportAgent

total_time = 0
total_tokens = 0
pipeline = [
    FunctionAnalysisAgent(),
    AiOpportunityAgent(),
    RoadmapAgent(),
    ExecutiveReportAgent()
]


for agent in pipeline:

    print("\n====================")

    print(
        f"Running: {agent.metadata.agent_name}"
    )

    result = agent.execute({})

    print(result)
    total_time += (
      result.duration_seconds
    )

    total_tokens += (
     result.total_tokens or 0
   )
    print(
    f"Time: "
    f"{result.duration_seconds} sec"
   )

    print(
     f"Tokens: "
     f"{result.total_tokens}"
     )
    if result.status != "Completed":

        print(
            f"Pipeline stopped at "
            f"{agent.metadata.agent_id}"
        )

        break


artifacts = [
    "function_analysis.json",
    "function_ai_opportunities.json",
    "ai_roadmap.json",
    "executive_report.json"
]

print("\n=== ARTIFACTS ===")

for artifact in artifacts:

    print(
        artifact,
        os.path.exists(artifact)
    )
print("\n=== PIPELINE SUMMARY ===")

print(
     f"Total Time: "
     f"{round(total_time,2)} sec"
)

print(
     f"Total Tokens: "
     f"{total_tokens}"
)
