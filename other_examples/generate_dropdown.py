#!/usr/bin/env python
"""
Playing with a dropdown / combo_box.
Author: Sammy Pfeiffer
"""

from PyQt4 import QtGui
import sys


class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        options = ['First option', 'Second option', 'Third option']
        default_option = 0
        self.combo_box = QtGui.QComboBox()
        for idx, option in enumerate(options):
            self.combo_box.insertItem(idx, option)
            if option == default_option:
                self.combo_box.setCurrentIndex(idx)

        # From http://doc.qt.io/qt-4.8/qcombobox.html#signals
        self.combo_box.currentIndexChanged.connect(self.on_dropdown_change)
        self.text_dropdown = QtGui.QLineEdit("")

        self.layout = QtGui.QHBoxLayout()
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.text_dropdown)

        self.central_widget = QtGui.QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

    def on_dropdown_change(self):
        option_text = self.combo_box.currentText()
        option_index = self.combo_box.currentIndex()
        self.text_dropdown.setText(str(option_index) + " " + option_text)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()
