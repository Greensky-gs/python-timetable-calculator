import typing
from Teacher import Teacher
from Student import Student

class Session():
    __teachers: typing.List[Teacher]
    __students: typing.List[Student]
    __options: typing.List[str]

    def __init__(self) -> typing.NoReturn:
        self.__teachers = []
        self.__students = []
        self.__options = []
    
    # Getters
    @property
    def students(self) -> typing.List[Student]:
        return self.__students

    @property
    def teachers(self) -> typing.List[Teacher]:
        return self.__teachers

    @property
    def options(self) -> typing.List[str]:
        return self.__options

    # Methods

    def appendTeacher(self, teacher: Teacher):
        self.__teachers.append(teacher)
        return self
    def appendStudents(self, student: Student):
        self.__students.append(student)
        return self
    def addOption(self, option: str):
        self.__options.append(option)
        return self
