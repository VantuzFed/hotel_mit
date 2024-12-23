from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from gui_files.ui_log import Ui_Form
from sqlalchemy import and_
from models import *

class Login(QWidget):
    branch_signal = Signal(str)
    dataSent = Signal(int)
    def __init__(self, main_w, db):
        super(Login,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.log = 0
        self.passwd = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_log.clicked.connect(self.login)


    def login(self):
        self.log = self.ui.ent_login.text()
        self.passwd = self.ui.ent_passwd.text()
        user = self.obj.query(Employees.id, Employees.login, Employees.password_, JobHistory.occupation).join(JobHistory).filter(and_(Employees.login == self.log, Employees.password_ == self.passwd)).first()
        if user:
            if user.login == self.log or user.password_ == self.passwd:
                QMessageBox.information(self, 'Сообщение', f'Авторизация прошла успешно, {user.occupation}')
                self.branch_signal.emit(user.occupation)
                self.dataSent.emit(user.id)
        else:
            QMessageBox.warning(self,'Предупреждение', 'Неверное имя пользователя или пароль')
