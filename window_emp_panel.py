from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

class EmpPanel(QWidget):
    branch_signal = pyqtSignal(str)
    def __init__(self, main_w, db):
        super(EmpPanel,self).__init__()
        self.ui = uic.loadUi('gui_files/emplo_main.ui',self)
        self.log = 0
        self.passwd = 0
        self.main_w = main_w
        self.obj = db
        # self.ui.button_log.clicked.connect(self.login)
