import typing
from Teacher import Teacher
from Student import Student

class Session():
    __teachers: typing.List[Teacher]
    __students: typing.List[Student]

    def __init__(self) -> typing.NoReturn:
        self.__teachers = []
        self.__students = []
    
    @property
    def students(self) -> typing.List[Student]:
        return self.__students

    @property
    def teachers(self) -> typing.List[Teacher]:
        return self.__teachers

    def appendTeacher(self, teacher: Teacher) -> typing.Self:
        self.__teachers.append(teacher)
        return self
    def appendStudents(self, student: Student) -> typing.Self:
        self.__students.append(student)
        return self
