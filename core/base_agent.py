from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @property
    @abstractmethod
    def metadata(self):
        """
        Returns AgentMetadata
        """
        pass

    @property
    @abstractmethod
    def dependencies(self):
        """
        Returns AgentDependency
        """
        pass

    @property
    @abstractmethod
    def tools(self):
        """
        Returns List[str]
        """
        pass

    @abstractmethod
    def execute(self, context):
        """
        Main execution method
        """
        pass