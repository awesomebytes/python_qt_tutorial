#!/usr/bin/env python

import sys
from PyQt4 import QtGui, uic


def running_in_ipython():
    """Check if the interpreter is iPython as when debugging we don't want to
    execute app.exec_() to remain in the shell to do dynamic introspection"""
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('my_gui.ui', self)
        self.my_button.clicked.connect(self.on_my_button_push)
        self.show()

    def on_my_button_push(self):
        self.my_label.setText("Button Pushed!")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    if not running_in_ipython():
        app.exec_()
