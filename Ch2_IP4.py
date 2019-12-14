import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class IPv4Validator(qtg.QValidator):
    '''Enforce Entry of IPv4 Addresses'''

    def validate(self,string, index):
        octets = string.split('.')
        if len(octets)>4:
            state = qtg.QValidator.Invalid
        elif not all([x.isdigit() for x in octets if x!='']):
            state= qtg.QValidator.Invalid
        elif not all([0<= int(x) <=255 for x  in octets if x !='']):
            state =  qtg.QValidator.Invalid
        elif len(octets)<4 :
            state = qtg.QValidator.Intermediate
        else:
            state = qtg.QValidator.Acceptable
        return (state, string, index)

class MainWindow(qtw.QWidget):

    def __init__(self):
        #Main Window Consctuctor
        super().__init__()
        #Main Code Goes Here
        line_edit = qtw.QLineEdit(
            'default value',
            self,
            placeholderText='Type Here',
            clearButtonEnabled=True,
            maxLength=20
        )



        line_edit.setText('0.0.0.0')
        line_edit.setValidator(IPv4Validator())

        layout = qtw.QHBoxLayout()
        self.setLayout(layout)

       #End Main Code

        self.show()


if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

