#!/usr/bin/env python

import sys
from PyQt4 import QtGui, uic
import subprocess


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
        uic.loadUi('command_runner.ui', self)
        self.run_b.clicked.connect(self.run_command)
        self.show()

    def run_command(self):
        command = str(self.cmd_pte.toPlainText())
        # Note that shell=True is a very unsafe thing to do, but also easy
        try:
            output = subprocess.check_output(command, shell=True)
            self.output_te.setText(output)
        except subprocess.CalledProcessError as e:
            self.output_te.setText("Error:" + str(e))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    if not running_in_ipython():
        app.exec_()
