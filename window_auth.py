from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

class Login(QWidget):
    branch_signal = pyqtSignal(str)
    def __init__(self, main_w, db):
        super(Login,self).__init__()
        self.ui = uic.loadUi('gui_files/log.ui',self)
        self.log = 0
        self.passwd = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_log.clicked.connect(self.login)

    def login(self):
        self.log = self.ui.ent_login.text()
        self.passwd = self.ui.ent_passwd.text()
        cur = self.obj.cursor(buffered=True)
        cur.execute('select * from employees where login = \'{}\' and password_ = \'{}\''.format(self.log, self.passwd))
        res = cur.fetchone()
        try:
            if res[1] == self.log and res[4] == self.passwd:
                cur.execute(f'select * from employees where login = \'{self.log}\'')
                res = cur.fetchone()
                user_id = res[0]
                cur.execute(f'select * from job_history where emp_id = \'{user_id}\'')
                res = cur.fetchone()
                occu = res[2]
                QMessageBox.information(self, 'Сообщение', f'Авторизация прошла успешно, {occu}')
                self.branch_signal.emit(occu)
        except:
            QMessageBox.warning(self,'Предупреждение', 'Неверное имя пользователя или пароль')
        cur.close()
