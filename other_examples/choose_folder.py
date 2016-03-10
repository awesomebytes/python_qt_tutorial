#!/usr/bin/env python
"""
Choose folder example.
Author: Sammy Pfeiffer
"""

from PyQt4 import QtGui
import sys


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.execute_button = QtGui.QPushButton('Choose folder')
        self.execute_button.clicked.connect(self.choose_folder)

        self.path_text = QtGui.QLineEdit("")

        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(self.execute_button)
        self.layout.addWidget(self.path_text)

        self.central_widget = QtGui.QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

    def choose_folder(self):
        path = QtGui.QFileDialog.getExistingDirectory()
        if path != '':
            self.path_text.setText(path)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()
