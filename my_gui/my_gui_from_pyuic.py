#!/usr/bin/env python

import sys
from PyQt4 import QtGui
from my_gui_class import Ui_MainWindow


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.my_button.clicked.connect(self.on_my_button_push)
        self.show()

    def on_my_button_push(self):
        self.ui.my_label.setText("Button pushed!")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
