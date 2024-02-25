from tkinter import filedialog
import tkinter
import json
import os.path
from structures.Teacher import Teacher
from structures.Student import Student
import typing


class MainWindow():
    window: tkinter.Tk
    cache: typing.Any
    __state: str
    changed = True
    dimens = [1200, 800]
    WIDTH = dimens[0]
    HEIGHT = dimens[1]

    teachers: typing.Tuple[Teacher, ...]
    students: typing.Tuple[Student, ...]
    
    def __init__(self):
        self.window = tkinter.Tk()
        
        self.window.title("Python Timetable calculator")
        self.window.geometry('x'.join(map(lambda x: str(x), self.dimens)))
        self.__state = 'init'

        self.__clock()
        self.window.mainloop()
    
    def __clock(self):
        if self.changed:
            self.__update()
            self.changed = False

        self.window.after(100, self.__clock)

    def __clear(self):
        for x in self.window.winfo_children():
            x.destroy()

    def __mainFrame(self):
        return self.window.children.get('mainFrame')

    def errorMessage(self, message):
        self.__clear()
        self.__addTeacherInput()

        frame = self.__mainFrame()

        msg = tkinter.Message(frame, text=message, width=self.WIDTH, bg="orangered2")
        msg.grid(row=3, column=1)

    def __teacherCall(self):
        file = filedialog.askopenfile(mode='r', filetypes=(("json files", "*.json"), ("CSV files", "*.csv")))

        if not file or file is None:
            return self.errorMessage("Veuillez sélectionner un fichier")
        
        ext = os.path.splitext(file.name)[1]
        
        if ext == ".json":
            try:
                with open(file.name, 'r') as read_file:
                    loads = json.loads(read_file.read())

                    if not isinstance(loads, list):
                        return self.errorMessage("Veuillez envoyer un fichier json qui possède une liste de professeurs")

                    teachers: typing.Tuple[Teacher, ...] = []
                    for x in loads:
                        valid, t = Teacher.fromInput(x)

                        if valid:
                            teachers.append(t)
                    if not len(teachers):
                        return self.errorMessage("Aucun professeur n'a été trouvé")
                    
                    self.teachers = teachers
                    self.setState("students")
            except Exception as err:
                print(err)
                self.errorMessage("Une erreur est survenue")

    def __studentsCall(self):
        file = filedialog.askopenfilename(filetypes=(("json files", "*.json"), ("CSV files", "*.csv")))

        if not file or file is None:
            return self.errorMessage("Veuillez sélectionner un fichier")

        ext = os.path.splitext(file)[1]

        if ext == ".json":
            try:
                with open(file) as read_file:
                    loads = json.loads(read_file.read())

                    if not isinstance(loads, list):
                        return self.errorMessage("Veuillez sélectionner un fichier json qui possède une liste d'élèves")
                    
                    students: typing.Tuple[Teacher, ...] = []
                    for x in loads:
                        valid, s = Student.fromInput(x)

                        if valid:
                            students.append(s)
                    
                    if not len(students):
                        return self.errorMessage("Aucun élève n'a été trouvé")
                    
                    self.students = students
                    self.errorMessage(f"This is not an error. We found {str(len(students))} students")
            except Exception as err:
                print(err)
                self.errorMessage("Une erreur est survenue")

    def setMainFrame(self):
        return tkinter.Frame(self.window, name="mainFrame", width=self.WIDTH, height=self.HEIGHT)
    def __addTeacherInput(self):
        frame = self.setMainFrame()

        btn = tkinter.Button(frame, text="Importer les professeurs", command=self.__teacherCall)
        btn.grid(row=1, column=1)

        frame.pack()

    def __studentsInput(self):
        frame = self.setMainFrame()

        btn = tkinter.Button(frame, text="Importer les élèves", command=self.__studentsCall)
        btn.grid(row=1, column=1)

        frame.pack()
    
    def setCache(self, cache: typing.Any):
        self.cache = cache
        return self
    
    def setState(self, state: str):
        self.__state = state
        self.changed = True

    def __update(self):
        self.__clear()
        match self.__state:
            case 'init':
                self.__addTeacherInput()
            case 'second':
                self.__clear()
            case 'students':
                self.__studentsInput()
