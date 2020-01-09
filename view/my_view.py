from collections import OrderedDict
from datetime import datetime
from controller import GroupController, StudentController
from domain import Student, Group
import initial_data as in_data
from orm_config import OrmConfig as Cfg


class MyView:
    def __init__(self):
        if Cfg.LOAD_DATA_TO_DB:
            in_data.load_data_to_db()
        self.__menu = OrderedDict()

        self.__menu["1"] = "  1 - Table Group"
        self.__menu["11"] = "  11 - Select Group"
        self.__menu["12"] = "  12 - Find by ID Group"
        self.__menu["13"] = "  13 - Create Group"
        self.__menu["14"] = "  14 - Update Group"
        self.__menu["15"] = "  15 - Patch Group"
        self.__menu["16"] = "  16 - Delete Group"

        self.__menu["2"] = "  2 - Table Student"
        self.__menu["21"] = "  21 - Select Student"
        self.__menu["22"] = "  22 - Find by ID Student"
        self.__menu["23"] = "  23 - Create Student"
        self.__menu["24"] = "  24 - Update Student"
        self.__menu["25"] = "  25 - Patch Student"
        self.__menu["26"] = "  26 - Delete Student"

        self.__menu["3"] = "  3 - Table Address"
        self.__menu["4"] = "  4 - Table Subject"
        self.__menu["Q"] = "  Q - exit"

        self.__menu_methods = dict()
        self.__menu_methods["11"] = self.__select_group
        self.__menu_methods["12"] = self.__find_by_id_group
        self.__menu_methods["13"] = self.__create_group
        self.__menu_methods["14"] = self.__update_group
        self.__menu_methods["15"] = self.__patch_group
        self.__menu_methods["16"] = self.__delete_group

        self.__menu_methods["21"] = self.__select_student
        self.__menu_methods["22"] = self.__find_by_id_student
        self.__menu_methods["23"] = self.__create_student
        self.__menu_methods["24"] = self.__update_student
        self.__menu_methods["25"] = self.__patch_student
        self.__menu_methods["26"] = self.__delete_student

    def __select_group(self):
        print "TABLE Group:"
        groups = GroupController().find_all()
        for group in groups:
            print group

    def __create_group(self):
        name = raw_input("Input Group->Name:")
        group = Group(name)
        GroupController().create(group)
        print group.id

    def __update_group(self):
        key = int(raw_input("Input Group->ID:"))
        name = raw_input("Input Group->new NAME:")
        group = Group(name)
        GroupController().update(key, group)

    def __delete_group(self):
        key = int(raw_input("Input Group->ID:"))
        GroupController().delete(key)

    def __find_by_id_group(self):
        key = int(raw_input("Input Group->ID:"))
        group = GroupController().find_by_id(key)
        print group

    def __patch_group(self):
        key = int(raw_input("Input Group->ID:"))
        field_name = raw_input("Input Group->field name:")
        value = raw_input("Input Group->new VALUE:")
        GroupController().patch(key, field_name, value)

    # ---------------------------------------------------

    def __select_student(self):
        print "TABLE Student:"
        students = StudentController().find_all()
        for student in students:
            print student

    def __create_student(self):
        surname = raw_input("Input Student->SURNAME:")
        name = raw_input("Input Student->Name:")
        date_str = raw_input("Input Student->BIRTHDAY ('24-05-2010'):")
        birthday = datetime.strptime(date_str, "%d-%m-%Y").date()
        group_id = int(raw_input("Input Student->GROUP_ID:"))
        student = Student(surname, name, birthday, group_id)
        StudentController().create(student)
        print student.id

    def __update_student(self):
        key = int(raw_input("Input Student->ID:"))
        surname = raw_input("Input Student->new SURNAME:")
        name = raw_input("Input Student->new Name:")
        date_str = raw_input("Input Student->new BIRTHDAY ('24-05-2010'):")
        birthday = datetime.strptime(date_str, "%d-%m-%Y").date()
        group_id = int(raw_input("Input Student->new GROUP_ID:"))
        student = Student(surname, name, birthday, group_id)
        StudentController().update(key, student)

    def __delete_student(self):
        key = int(raw_input("Input Student->ID:"))
        StudentController().delete(key)

    def __find_by_id_student(self):
        key = int(raw_input("Input Student->ID:"))
        student = StudentController().find_by_id(key)
        print student

    def __patch_student(self):
        key = int(raw_input("Input Student->ID:"))
        field_name = raw_input("Input Student->field name:")
        value = raw_input("Input Student->new VALUE:")
        StudentController().patch(key, field_name, value)

    # ---------------------------------------------------

    def output_menu(self):
        print "MENU:"
        for key in self.__menu.keys():
            if len(key) == 1:
                print self.__menu.get(key)

    def output_sub_menu(self, fig):
        print "SubMENU:"
        for key in self.__menu.keys():
            if len(key) != 1 and key[0] == fig:
                print self.__menu.get(key)

    def show(self):
        key_menu = ""
        while key_menu != "Q":
            self.output_menu()
            key_menu = str(raw_input()).upper()

            if key_menu.isdigit():
                self.output_sub_menu(key_menu)
                print "Please, select menu point."
                key_menu = str(raw_input()).upper()
            if key_menu in self.__menu_methods:
                self.__menu_methods[key_menu]()
