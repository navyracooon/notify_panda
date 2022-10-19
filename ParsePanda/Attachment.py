from dataclasses import dataclass

@dataclass(frozen=True)
class Attachment:
    name: str
    ref: str
    size: int
    type: str
    url: str
