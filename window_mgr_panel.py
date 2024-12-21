from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtCore import Signal

class MgrPanel(QWidget):
    but_edt_rm_sig = Signal()
    but_reg_emp_sig = Signal()
    but_edt_emp_sig = Signal()
    def __init__(self, main_w, db):
        super(MgrPanel,self).__init__()
        loader = QUiLoader()
        ui_file = QFile('gui_files/manag_main.ui')
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
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
