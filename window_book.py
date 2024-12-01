from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

class WindowBook(QWidget):
    def __init__(self, main_w, db):
        super(WindowBook,self).__init__()
        self.ui = uic.loadUi('gui_files/emplo_main.ui', self)
        self.log = 0
        self.passwd = 0
        self.username = 0
        self.main_w = main_w
        self.obj = db

