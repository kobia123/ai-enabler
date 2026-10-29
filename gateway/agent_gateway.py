from agent_registry import AgentRegistry
from authorization_service import AuthorizationService


class AgentGateway:

    def __init__(self):

        self.registry = AgentRegistry()

        self.authorization = AuthorizationService()

    def execute(
        self,
        agent_name,
        role
    ):

        print("\n=== AGENT-CORE-GW ===")

        print(
            f"Role: {role}"
        )

        print(
            f"Agent: {agent_name}"
        )

        #
        # Step 1
        # Registry Validation
        #

        if not self.registry.exists(
            agent_name
        ):

            print(
                "DENY - Agent not registered"
            )

            return

        #
        # Step 2
        # Authorization
        #

        if not self.authorization.is_authorized(
            role,
            agent_name
        ):

            print(
                "DENY - Unauthorized"
            )

            return

        #
        # Step 3
        # Execute
        #

        print(
            "ALLOW - Executing agent"
        )

        print(
            f"Agent [{agent_name}] executed successfully"
        )