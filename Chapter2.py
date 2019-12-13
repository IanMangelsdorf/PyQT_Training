import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self):
        #Main Window Consctuctor
        super().__init__()
        #Main Code Goes Here

        #End Main Code

        self.show()


if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

