from dataclasses import dataclass


@dataclass
class Padding:
    left: float = 0.1
    bottom: float = 0.1
    right: float = 0.1
    top: float = 0.1
