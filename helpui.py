import help
import sys
from PyQt5 import QtWidgets

class Help(QtWidgets.QMainWindow, help.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)
window = Help()
window.show()
app.exec_()