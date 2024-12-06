from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

class MgrPanel(QWidget):
    but_edt_rm_sig = pyqtSignal()
    but_reg_emp_sig = pyqtSignal()
    but_edt_emp_sig = pyqtSignal()
    def __init__(self, main_w, db):
        super(MgrPanel,self).__init__()
        self.ui = uic.loadUi('gui_files/manag_main.ui',self)
        self.main_w = main_w
        self.obj = db
        self.ui.but_edt_rm.clicked.connect(self.but_edt_rm_f)
        self.ui.but_reg_emp.clicked.connect(self.but_reg_emp_f)
        self.ui.but_edt_emp.clicked.connect(self.but_edt_emp_f)

    def but_edt_rm_f(self):
        self.but_edt_rm_sig.emit()

    def but_reg_emp_f(self):
        self.but_reg_emp_sig.emit()

    def but_edt_emp_f(self):
        self.but_edt_emp_sig.emit()
