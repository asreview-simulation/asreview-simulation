from typing import Optional
from dataclasses import dataclass


@dataclass
class Model:
    model: Optional[str] = None
    params: Optional[dict] = None
