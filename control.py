from PyQt6.QtWidgets import QApplication
from window_reg_client import Register_client
from window_auth import Login
from table_list import Table_ls
from main_window import MainWindow
from window_emp_panel import EmpPanel
from window_book import WindowBook
import sys
from sql import Con_base

class Control:
    def __init__(self, w, bd_obj):
        self.bd_obj = bd_obj
        self.w_reg_cli = Register_client(w, self.bd_obj)
        self.w_log = Login(w, self.bd_obj)
        self.w_t_ls = Table_ls(w, self.bd_obj)
        self.mw = w
        self.w_book = WindowBook(w, self.bd_obj)
        self.w_resep_panel = EmpPanel(w, self.bd_obj)
        # self.w_mngr_panel = ManagerPanel(w, self.bd_obj)
        self.mw.button_auth.clicked.connect(self.show_window_auth)
        self.w_log.branch_signal.connect(self.handle_emp_branch)
        self.w_resep_panel.but_tab_sig.connect(self.show_table_list)
        self.w_resep_panel.but_reg_sig.connect(self.show_window_reg_client)
        self.w_resep_panel.but_book_sig.connect(self.show_window_book)


    # registration
    def show_window_reg_client(self):
        # self.w_reg_cli.button.clicked.connect(self.show_main)
        self.w_resep_panel.hide()
        self.w_reg_cli.show()

    # login
    def show_window_auth(self):
        self.mw.hide()
        self.w_log.button.clicked.connect(self.show_main)
        self.w_log.show()

    def show_main(self):
        self.w_t_ls.hide()
        self.w_reg_cli.hide()
        self.w_log.hide()
        self.mw.show()

    def show_table_list(self):
        self.w_t_ls.but_back.clicked.connect(self.show_main)
        self.w_resep_panel.hide()
        self.w_t_ls.show()
        # self.w_t_ls.activateWindow()

    def show_window_book(self):
        self.w_resep_panel.hide()
        self.w_book.show()

    def handle_emp_branch(self, branch: str):
        """Обработка ветвления для открытия окна респепшена или менеджера."""
        self.w_log.hide()
        if branch == "Ресепшн":
            self.w_resep_panel.show()
        elif branch == "Менеджер":
            print('mgr')
            # self.w_mngr_panel.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    bd_obj = Con_base().connection()
    c = Control(w, bd_obj)
    sys.exit(app.exec())