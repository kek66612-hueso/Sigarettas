from dataclasses import dataclass
from typing import Optional

@dataclass
class Warehouse:
    id: Optional[int] = None
    weight: float = 0.0
    box: str = ""