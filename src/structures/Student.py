from typing import List

class Student():
    name: str
    ens: List[str]
    grade: str

    def __init__(self, *, name: str, ens: List[str], grade: str):
        self.name = name
        self.ens = ens
        self.grade = grade