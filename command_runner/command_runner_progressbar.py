#!/usr/bin/env python

import sys
from PyQt4 import QtGui, uic, QtCore
import subprocess
import tempfile
import os
import signal


# Helper class to run commands
class ShellCmd:

    def __init__(self, cmd):
        self.outf = tempfile.NamedTemporaryFile(mode="w")
        self.errf = tempfile.NamedTemporaryFile(mode="w")
        self.inf = tempfile.NamedTemporaryFile(mode="r")
        self.process = subprocess.Popen(cmd, shell=True, stdin=self.inf,
                                        stdout=self.outf, stderr=self.errf,
                                        preexec_fn=os.setsid, close_fds=True)

    def __del__(self):
        if not self.is_done():
            self.kill()
        self.outf.close()
        self.errf.close()
        self.inf.close()

    def get_stdout(self):
        with open(self.outf.name, "r") as f:
            return f.read()

    def get_stderr(self):
        with open(self.errf.name, "r") as f:
            return f.read()

    def get_retcode(self):
        """get retcode or None if still running"""
        return self.process.poll()

    def is_done(self):
        return self.process.poll() is not None

    def kill(self):
        os.killpg(self.process.pid, signal.SIGTERM)
        self.process.wait()


class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('command_runner.ui', self)
        self.run_b.clicked.connect(self.run_command_with_progressbar)
        self.show()

    def run_command_with_progressbar(self):
        # Note: toPlainText returns a QString which you cannot feed the shell
        # with it or you'll get the error:
        # CalledProcessError: Command 'XXX' returned non-zero exit status 127
        command = str(self.cmd_pte.toPlainText())

        feedback_msg = "Command '" + command + "' is being executed..."
        cancel_button_text = "Cancel"
        self.progressbar = QtGui.QProgressDialog(feedback_msg,
                                                 cancel_button_text,
                                                 # min 0, max 0 makes
                                                 # progressbar just move from
                                                 # left to right
                                                 0, 0)
        self.timer = QtCore.QTimer()
        # For a one time timer use
        # QTimer.singleShot(200, self.do_this_thing)
        self.timer.timeout.connect(self.progressbar_update)
        self.progressbar.canceled.connect(self.progressbar_cancel)
        self.timer.start(1000)
        self.progressbar.show()

        self.process = ShellCmd(command)

    def progressbar_update(self):
        # If using a progressbar with max and min (0-100 for example)
        # Use setValue to set the progressbar
        # self.progressbar.setValue()
        if not self.process.is_done():
            self.progressbar.show()
        else:
            output = self.process.get_stdout()
            err_output = self.process.get_stderr()
            self.output_te.setText(output + err_output)
            self.timer.stop()
            self.progressbar.hide()

    def progressbar_cancel(self):
        self.timer.stop()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()
