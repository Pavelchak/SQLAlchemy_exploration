from mvc.controller.i_controller import IController


class Controller(IController):
    def __init__(self):
        pass

    def action1(self):
        print "Controller-action1"

    def action2(self):
        print "Controller-action2"

