#!/usr/bin/env python
"""
Choose file example.
Author: Sammy Pfeiffer
"""

from PyQt4 import QtGui
import sys


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.execute_button = QtGui.QPushButton('Choose file')
        self.execute_button.clicked.connect(self.choose_file)

        self.path_text = QtGui.QLineEdit("")

        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(self.execute_button)
        self.layout.addWidget(self.path_text)

        self.central_widget = QtGui.QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

    def choose_file(self):
        # TODO: Filter by something? http://doc.qt.io/qt-4.8/qfiledialog.html#filter
        # QFileDialog(QWidget parent=None, QString caption=QString(), QString directory=QString(), QString filter=QString())
        path = QtGui.QFileDialog.getOpenFileName()
        if path != '':
            self.path_text.setText(path)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()
