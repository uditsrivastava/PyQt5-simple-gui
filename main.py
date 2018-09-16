
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi
import sys


class Udit(QDialog):
    def __init__(self):
        super(Udit,self).__init__()
        loadUi('Udit.ui',self)

app=QApplication(sys.argv)
window=Udit()
window.setWindowTitle('Udit first ui')
window.show()
sys.exit(app.exec_())  
