class AgentRegistry:

    def __init__(self):

        self._agents = {
            "analyze_organization": "Organization Analysis Agent",
            "function_analysis": "Function Analysis Agent",
            "ai_opportunity": "AI Opportunity Agent",
            "roadmap": "Roadmap Agent",
            "executive_report": "Executive Report Agent"
        }

    def exists(self, agent_name):

        return agent_name in self._agents

    def get(self, agent_name):

        return self._agents.get(agent_name)

    def list_agents(self):

        return list(self._agents.keys())