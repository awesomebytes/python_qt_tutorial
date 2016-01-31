#!/usr/bin/env python
"""
Error showing example.
Author: Sammy Pfeiffer
"""

from PyQt4 import QtGui
import sys


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.execute_button = QtGui.QPushButton('Show error window')
        self.execute_button.clicked.connect(self.show_error)

        self.layout = QtGui.QVBoxLayout()
        self.layout.addWidget(self.execute_button)

        self.central_widget = QtGui.QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

    def show_error(self):
        QtGui.QMessageBox.warning(
            self, "Error", "Showing an error window is simple.")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()
