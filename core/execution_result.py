from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ExecutionResult:

    status: str
    agent_id: str

    output_artifact: str

    duration_seconds: float = 0.0

    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None

    errors: list[str] = field(
        default_factory=list
    )