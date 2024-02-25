from typings.entities import student, specialities, options, langs
from typing import Tuple
import typings.ids

class Student:
    name: str
    level: typings.ids.level
    tc: str
    classid: str
    specialityClasses: Tuple[specialities, specialities, specialities]
    langsClasses: Tuple[langs, langs]
    optionsClasses: Tuple[options, options, options]
    apgroup: str
    edt: str

    def __init__(self, input: student = None):
        if input is not None:
            self.name = input[0]
            self.level = input[1]
            self.tc = input[2]
            self.classid = input[3]
            self.specialityClasses = (input[4], input[5], input[6])
            self.langsClasses = (input[7], input[8])
            self.optionsClasses = (input[9], input[10], input[11])
            self.apgroup = input[12]
            self.edt = input[13]
    
    def setName(self, name: str):
        self.name = name
        return self
    def setLevel(self, level: typings.ids.level):
        self.level = level
        return self
    def setTc(self, tc: str):
        self.tc = tc
        return self
    def setClassid(self, classid: str):
        self.classid = classid
        return self
    def setSpecialities(self, specialitiesList: Tuple[specialities, specialities, specialities]):
        self.specialityClasses = specialitiesList
        return self
    def setLangs(self, langsList: Tuple[langs, langs]):
        self.langsClasses = langsList
        return self
    def setOptions(self, optionsList: Tuple[options, options, options]):
        self.optionsClasses = optionsList
        return self
    def setApgroup(self, group: str):
        self.apgroup = group
        return self
    def setEdt(self, edt: str):
        self.edt = edt
        return self

    def toJSON(self) -> student:
        return [self.name, self.level, self.tc, self.classid, *self.specialityClasses, *self.langsClasses, *self.optionsClasses, self.apgroup, self.edt]

    @staticmethod
    def fromInput(input):
        false = [False, None]

        if not isinstance(input, dict):
            return false
        if not len(input.keys()) == 5:
            return false
        checks = (("name", str), ("level", str, typings.ids.levelStr), ("specialities", list, typings.ids.classesStr), ("langs", list, typings.ids.langStr), ("options", list, typings.ids.optionStr))

        valid = True

        for check in checks:
            if not valid:
                break
            if input.get(check[0]) is None:
                valid = False
                continue
            if not isinstance(input.get(check[0]), check[1]):
                valid = False
                continue
            hasThirdCheck = len(check) > 2

            if check[1] == list and hasThirdCheck:
                if len(list(filter(lambda x: not isinstance(x, str) or not x in check[2], input.get(check[0])))) > 0:
                    valid = False
                    continue
            elif hasThirdCheck:
                if not input.get(check[0]) in check[2]:
                    valid = False
                    continue
    
        if not valid:
            return false
        
        st = Student().setName(input.get('name')).setLevel(input.get('level')).setSpecialities(input.get('specialities')).setLangs(input.get('langs')).setOptions(input.get('options'))

        return [True, st]