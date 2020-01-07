from collections import OrderedDict
from controller import GroupController
from domain.group import Group


class MyView:
    def __init__(self):
        # self.__controller = Controller()  # type: IController
        self.__menu = OrderedDict()

        self.__menu["1"] = "  1 - Table Group"
        self.__menu["11"] = "  11 - Select Group"
        self.__menu["12"] = "  12 - Create Group"
        self.__menu["13"] = "  13 - Update Group"
        self.__menu["14"] = "  14 - Delete Group"
        self.__menu["15"] = "  15 - Find by ID Group"

        self.__menu["2"] = "  2 - Table Student"
        self.__menu["3"] = "  3 - Table Address"
        self.__menu["4"] = "  4 - Table Subject"
        self.__menu["Q"] = "  Q - exit"

        self.__menu_methods = dict()
        self.__menu_methods["11"] = self.__select_group
        self.__menu_methods["12"] = self.__create_group
        self.__menu_methods["13"] = self.__update_group
        self.__menu_methods["14"] = self.__delete_group
        self.__menu_methods["15"] = self.__find_by_id_group

    def __select_group(self):
        print "TABLE Group:"
        groups = GroupController().find_all()
        for group in groups:
            print group

    def __create_group(self):
        name = raw_input("Input Group->Name:")
        group = Group(name)
        GroupController().create(group)

    def __update_group(self):
        print "Into Method 'Update Group'"

    def __delete_group(self):
        print "Into Method 'Delete Group'"

    def __find_by_id_group(self):
        print "Into Method 'Find by ID Group'"
        key = raw_input("Input Group->ID:")
        group = GroupController().find_by_id(key)
        print group

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
