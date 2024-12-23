from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from sqlalchemy import or_, and_, func
from gui_files.ui_emp_main import Ui_Form

class EmpPanel(QWidget):
    but_tab_sig = Signal()
    but_reg_sig = Signal()
    but_book_sig = Signal()
    but_book_edit_sig = Signal()
    def __init__(self, main_w, db):
        super(EmpPanel,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_w = main_w
        self.obj = db
        self.ui.but_tab.clicked.connect(self.but_tab_f)
        self.ui.but_reg_cli.clicked.connect(self.but_reg_cli_f)
        self.ui.but_book.clicked.connect(self.but_book_f)
        self.ui.but_book_edit.clicked.connect(self.but_book_edit_f)

    def but_tab_f(self):
        self.but_tab_sig.emit()

    def but_reg_cli_f(self):
        self.but_reg_sig.emit()

    def but_book_f(self):
        self.but_book_sig.emit()

    def but_book_edit_f(self):
        self.but_book_edit_sig.emit()