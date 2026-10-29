from agents.analyze_organization.agent import AnalyzeOrganizationAgent
from agents.function_analysis.agent import FunctionAnalysisAgent
from agents.ai_opportunity.agent import AiOpportunityAgent
from agents.roadmap.agent import RoadmapAgent
from agents.executive_report.agent import ExecutiveReportAgent


agents = [
    AnalyzeOrganizationAgent(),
    FunctionAnalysisAgent(),
    AiOpportunityAgent(),
    RoadmapAgent(),
    ExecutiveReportAgent()
]

for agent in agents:

    print("\n====================")

    print(agent.metadata)

    print(agent.dependencies)

    print(agent.execute({}))