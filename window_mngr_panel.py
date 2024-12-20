from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

class ManagPanel(QWidget):
    but_edt_sig = pyqtSignal()
    but_reg_m_sig = pyqtSignal()
    but_book_sig = pyqtSignal()
    def __init__(self, main_w, db):
        super(ManagPanel,self).__init__()
        self.ui = uic.loadUi('gui_files/manag_main.ui',self)
        self.main_w = main_w
        self.obj = db
        self.ui.but_tab.clicked.connect(self.but_tab_f)
        self.ui.but_reg_cli.clicked.connect(self.but_reg_cli_f)
        self.ui.but_book.clicked.connect(self.but_book_f)

    def but_tab_f(self):
        self.but_tab_sig.emit()

    def but_reg_cli_f(self):
        self.but_tab_sig.emit()

    def but_book_f(self):
        self.but_tab_sig.emit()
