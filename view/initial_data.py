from datetime import datetime

from controller import GroupController, StudentController
from domain import Group, Student

def to_date(str):
    return datetime.strptime(str, "%d-%m-%Y").date()

def load_data_to_db():
    group = Group("Python")
    GroupController().create(group)

    group = Group("Java")
    GroupController().create(group)

    group = Group("C++")
    GroupController().create(group)

    group = Group("C#")
    GroupController().create(group)

    group = Group("JavaScript")
    GroupController().create(group)

    # --------------------------------
    student = Student("Pavelchak", "Andrii", to_date("09-05-1976"), 1)
    StudentController().create(student)

    student = Student("Yatsuk", "Yuri", to_date("26-04-1983"), 1)
    StudentController().create(student)

    student = Student("Veres", "Zenovii", to_date("19-08-1984"), 2)
    StudentController().create(student)

    student = Student("Ivaniuk", "Oleh", to_date("02-09-1983"), 5)
    StudentController().create(student)

    student = Student("Lopachak", "Oleh", to_date("09-05-1976"), 3)
    StudentController().create(student)

    student = Student("Garaniuk", "Ihor", to_date("09-05-1953"), 2)
    StudentController().create(student)

    student = Student("Mokrenko", "Petro", to_date("09-12-1939"), 4)
    StudentController().create(student)

    student = Student("Kovela", "Ivan", to_date("09-05-1948"), 4)
    StudentController().create(student)
