from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtCore import Signal

class ManagPanel(QWidget):
    but_edt_sig = Signal()
    but_reg_m_sig = Signal()
    but_book_sig = Signal()
    def __init__(self, main_w, db):
        super(ManagPanel,self).__init__()
        loader = QUiLoader()
        ui_file = QFile('gui_files/manag_main.ui')
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
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
