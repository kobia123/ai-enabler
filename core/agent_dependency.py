from dataclasses import dataclass
from typing import List


@dataclass
class AgentDependency:

    requires: List[str]

    produces: List[str]