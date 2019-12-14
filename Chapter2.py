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

        #line_edit = qtw.QLineEdit('Default Value', self)

        line_edit = qtw.QLineEdit(
            'default value',
            self,
            placeholderText = 'Type Here',
            clearButtonEnabled= True,
            maxLength = 20
        )

        #utton = qtw.QPushButton('Push Me')
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
        combobox.addItem('Peach','Oah I like Peaches')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1,'Radish',2)


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
            calendarPopup = True,
            maximumDate = qtc.QDate(2030,1,1),
            maximumTime = qtc.QTime(17,0),
            displayFormat = 'yyyy-MM-dd HH:mm'
        )


        #End Main Code
        self.show()

        textedit= qtw.QTextEdit(
            self,
            acceptRichText = False,
            lineWrapMode= qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth= 25,
            placeholderText = 'Enter Your Stuff Here'
        )

        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(lable)
        layout.addWidget(line_edit)

        subLayout = qtw.QHBoxLayout()
        layout.addLayout(subLayout)

        subLayout.addWidget(button)
        subLayout.addWidget(combobox)

        gridLayout = qtw.QGridLayout()
        layout.addLayout(gridLayout)
        gridLayout.addWidget(spinbox,0,0)
        gridLayout.addWidget(datetimebox,0,1)
        gridLayout.addWidget(textedit,1,0,2,2)

        form_layout = qtw.QFormLayout()
        layout.addLayout(form_layout)

        form_layout.addRow('Item 1', qtw.QLineEdit(self))
        form_layout.addRow('Item 2', qtw.QLineEdit(self))
        form_layout.addRow((qtw.QLabel('<b>This is a LAbel only Row </b>')))

        lable.setFixedSize(150, 40)
        line_edit.setMinimumSize(150,15)
        line_edit.setMaximumSize(500,15)
if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

