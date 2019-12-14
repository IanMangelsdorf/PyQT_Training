import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self):
        #Main Window Consctuctor
        super().__init__()
        #Main Code Goes Here
        self.setWindowTitle('My Calendar App')
        self.resize(800,600)

        self.calendar = qtw.QCalendarWidget()
        self.event_list = qtw.QListWidget()
        self.event_title = qtw.QLineEdit()
        self.event_category = qtw.QComboBox()
        self.event_time = qtw.QTimeEdit(qtc.QTime(8,0))
        self.allday_check = qtw.QCheckBox('All Day')
        self.event_detail = qtw.QTextEdit()
        self.add_button = qtw.QPushButton('Add/Update')
        self.del_button = qtw.QPushButton('Delete')


        self.event_category.addItems(
            ['Select Category..','New','Work','Meeting','Doctor','Family']
        )
        self.event_category.model().item(0).setEnabled(False)

        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)

        self.calendar.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )

        right_layout =qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(qtw.QLabel('Events on Date'))
        right_layout.addWidget(self.event_list)

        self.event_list.setSizePolicy(
            qtw.QSizePolicy.Expanding,
            qtw.QSizePolicy.Expanding
        )

        event_form = qtw.QGroupBox('Event')
        right_layout.addWidget(event_form)
        event_form_layout = qtw.QGridLayout()
        event_form.setLayout(event_form_layout)

        event_form_layout.addWidget(self.event_title,1,1,1,3)
        event_form_layout.addWidget(self.event_category,2,1)
        event_form_layout.addWidget(self.event_time,2,2,)
        event_form_layout.addWidget(self.allday_check,2,3)
        event_form_layout.addWidget(self.event_detail,3,1,1,3)
        event_form_layout.addWidget(self.add_button,4,2)
        event_form_layout.addWidget(self.del_button,4,3)
        #End Main Code

        self.show()


if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())

