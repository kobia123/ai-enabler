from agents.analyze_organization.agent import AnalyzeOrganizationAgent
from agents.function_analysis.agent import FunctionAnalysisAgent
from agents.ai_opportunity.agent import AiOpportunityAgent
from agents.roadmap.agent import RoadmapAgent
from agents.executive_report.agent import ExecutiveReportAgent


class AgentRegistry:

    def __init__(self):

        self._agents = {}

        self.register(
            AnalyzeOrganizationAgent()
        )

        self.register(
            FunctionAnalysisAgent()
        )

        self.register(
            AiOpportunityAgent()
        )

        self.register(
            RoadmapAgent()
        )

        self.register(
            ExecutiveReportAgent()
        )

    def register(
        self,
        agent
    ):

        self._agents[
            agent.metadata.agent_id
        ] = agent

    def get(
        self,
        agent_id
    ):

        return self._agents.get(
            agent_id
        )

    def list_agents(
        self
    ):

        return list(
            self._agents.values()
        )

    def exists(
        self,
        agent_id
    ):

        return (
            agent_id in self._agents
        )