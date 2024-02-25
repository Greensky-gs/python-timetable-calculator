import typing
from typings.ids import allClasses, allClassesStr
from typings.entities import disponibilities as disps, teacher


class Teacher:
    name: str
    classes: typing.Tuple[allClasses, ...]
    disponibilities: disps
    edt: str
    studentGroups: typing.Tuple[str, ...]

    def __init__(self, input: teacher=None):
        if not input is None:
            self.name = input[0]
            self.classes = input[1]
            self.disponibilities = input[2]
            self.edt = input[3]
            self.studentGroups = input[4]
    
    def setName(self, name: str):
        self.name = name
        return self

    def setClasses(self, classes: typing.Tuple[allClasses, ...]):
        self.classes = classes
        return self

    def setDisponibilities(self, disponibilities: disps):
        self.disponibilities = disponibilities
        return self

    def setEdt(self, edt: str):
        self.edt = edt
        return self

    def setStudentGroups(self, groups: typing.Tuple[str, ...]):
        self.studentGroups = groups
        return self

    def toJSON(self):
        return [self.name, self.classes, self.disponibilities, self.edt, self.studentGroups]

    @staticmethod
    def fromInput(input):
        false = [False, None]

        if not isinstance(input, dict):
            return false
        if len(input.keys()) != 3:
            return false
        if not input.get('name') or not input.get('disponibilities') or not input.get('classes'):
            return false
        if not isinstance(input.get('name'), str):
            return false
        if not isinstance(input.get('disponibilities'), list):
            return false
        if not isinstance(input.get('classes'), list):
            return false
        if not len(input.get('classes')):
            return false
        matieres = []
        for x in input.get('classes'):
            if isinstance(x, str) and x in allClassesStr:
                matieres.append(x)
        if not len(matieres):
            return false
        disps = input.get('disponibilities')
        if len(disps) != 5:
            return false
        for d in disps:
            if not isinstance(d, list):
                return false
            if len(list(filter(lambda x: not isinstance(x, int) or x < 1 or x > 12, d))) > 0:
                return false

        t = Teacher()
        disponibilities = []

        for i, x in enumerate(disps):
            disponibilities.append((i + 1, tuple(x)))
        t.setName(input.get('name')).setDisponibilities(disponibilities)

        return [True, t]
