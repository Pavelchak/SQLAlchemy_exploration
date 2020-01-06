from mvc.controller.impl.controller import Controller
from mvc.controller.i_controller import IController


class MyView:
    def __init__(self):
        self.__controller = Controller()  # type: IController
        self.__menu = list()
        self.__menu.append("  1 - method1")
        self.__menu.append("  2 - method2")
        self.__menu.append("  3 - method3")
        self.__menu.append("  4 - method4")
        self.__menu.append("  Q - exit")

        self.__menu_methods = dict()
        self.__menu_methods["1"] = self.__launch_method1
        self.__menu_methods["2"] = self.__launch_method2
        self.__menu_methods["3"] = self.__launch_method3
        self.__menu_methods["4"] = self.__launch_method4

    def __launch_method1(self):
        print "Into Method 1"
        self.__controller.action1()

    def __launch_method2(self):
        print "Into Method 2"
        self.__controller.action2()

    def __launch_method3(self):
        print "Into Method 3"

    def __launch_method4(self):
        print "Into Method 4"

    def output_menu(self):
        print "MENU:"
        for value in self.__menu:
            print value

    def show(self):
        key_menu = ""
        while key_menu != "Q":
            self.output_menu()
            key_menu = str(raw_input()).upper()
            print key_menu
            if key_menu in self.__menu_methods:
                self.__menu_methods[key_menu]()
