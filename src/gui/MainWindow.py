import tkinter


class MainWindow():
    window: tkinter.Tk
    
    def __init__(self):
        self.window = tkinter.Tk()
        
        self.window.title("Python Timetable calculator")
        self.window.geometry("600x400")
        self.window.mainloop()
