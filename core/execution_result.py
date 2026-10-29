from dataclasses import dataclass, field
from typing import List


@dataclass
class ExecutionResult:

    status: str

    agent_id: str

    output_artifact: str

    duration_seconds: float

    errors: List[str] = field(default_factory=list)