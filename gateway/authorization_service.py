class AuthorizationService:

    def __init__(self):

        self.permissions = {

            "BusinessAnalyst": [
                "analyze_organization",
                "function_analysis",
                "ai_opportunity"
            ],

            "SolutionArchitect": [
                "analyze_organization",
                "function_analysis",
                "ai_opportunity",
                "roadmap",
                "executive_report"
            ],

            "Executive": [
                "roadmap",
                "executive_report"
            ],

            "PlatformAdmin": [
                "analyze_organization",
                "function_analysis",
                "ai_opportunity",
                "roadmap",
                "executive_report"
            ]
        }

    def is_authorized(
        self,
        role,
        agent_name
    ):

        allowed_agents = self.permissions.get(
            role,
            []
        )

        return agent_name in allowed_agents