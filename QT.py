import sys
from PyQt4 import QtCore, QtGui, uic 

app = QtGui.QApplication(sys.argv)

window = uic.loadUi("untitled.ui") # type: <class 'PyQt4.QtGui.QWidget'>
QtCore.QObject.connect(window.butQuit,QtCore.SIGNAL("clicked()"),
                       QtGui.qApp.quit)


window.show()
sys.exit(app.exec_())
