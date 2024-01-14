from typing import List

class Teacher():
    name: str
    ens: List[str]

    def __init__(self, *, name: str, ens: List[str]) -> None:
        self.name = name
        self.ens = ens