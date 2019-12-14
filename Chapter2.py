import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self):
        #Main Window Consctuctor
        super().__init__()
        #Main Code Goes Here
        subwidgit = qtw.QWidget(self, toolTip= 'This is a Tool Tip Widget String')

        lable = qtw.QLabel('Hello Widgets!', self)
        lable.setText('Hi There Widgets')
        print (lable.text())

        line_edit = qtw.QLineEdit('Default Value', self)

        line_edit = qtw.QLineEdit(
            'default value',
            self,
            placeholderText = 'Type Here',
            clearButtonEndable= True,
            maxLength = 20
        )

        button = qtw.QPushButton('Push Me')
        button = qtw.QPushButton(
            'Push Me',
            self,
            checkable = True,
            checked = True,
            shortcut = qtg.QKeySequence('Ctrl+p')
        )

        combobox = qtw.QComboBox(self,
                                 editable = True,
                                 insertPolicy= qtw.QComboBox.InsertAtTop)
        combobox.addItem('Lemon',1)
        combobox.addItem('Peach','Oah I like Peaches',
        combobox.addItem('Strawberry', qtw.QWidget),
        combobox.insertItem(1,'Radish',2)
        )

        spinbox = qtw.QSpinBox(
            self,
            value =12,
            maximum =100,
            minimum = 10,
            prefix = '$',
            suffix = ' + Tax',
            singleStep = 5
        )

        datetimebox = qtw.QDateTimeEdit(
            self,
            date = qtc.QDate.currentDate(),
            time = qtc.QTime(12,30),
            calenderPopus = True,
            maximumDate = qtc.QDate(2030,1,1),
            maximumTime = qtc.QTime(17,0),
            dsplayFormat = 'yyy-MM-dd HH:mm'
        )


        #End Main Code
        self.show()


if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

