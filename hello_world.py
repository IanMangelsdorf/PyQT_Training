from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import QtCore as qtc
app = QtWidgets.QApplication([])

window = QtWidgets.QWidget( windowTitle='Hello QT')
#window.setWindowFlag(qtc.Qt.Sheet|qtc.Qt.Popup)
window.show()
app.exec()