from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

class WindowBookEdit(QWidget):
    def __init__(self, main_w, db):
        super(WindowBookEdit,self).__init__()
        self.ui = uic.loadUi('gui_files/book_edit.ui', self)
        self.log = 0
        self.passwd = 0
        self.username = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_reg.clicked.connect(self.registration)

    def registration(self):
        self.fname = self.ui.ent_fname.text()
        self.mname = self.ui.ent_mname.text()
        self.lname = self.ui.ent_lname.text()
        self.email = self.ui.ent_email.text()
        self.phone = self.ui.ent_phone.text()
        self.doc_id = self.ui.ent_doc_id.text()
        cur = self.obj.cursor()
        cur.execute(
            f'select * from clients where first_name = \'{self.fname}\' and last_name = \'{self.lname}\' and document_id = \'{self.doc_id}\'')
        res = cur.fetchone()
        print(res)
        try:
            if res[1] == self.fname and res[3] == self.lname and res[6] == self.doc_id:
                QMessageBox.warning(self, 'Сообщение', 'Такой клиент уже существует')
        except:
            val = (self.fname, self.mname, self.lname, self.email, self.phone, self.doc_id)
            sql = 'INSERT INTO clients (first_name, middle_name, last_name, e_mail, phone_number, document_id) VALUES(%s,%s,%s,%s,%s,%s)'
            cur.execute(sql, val)
            self.obj.commit()
            QMessageBox.information(self, 'Сообщение', 'Клиент успешно добавлен')
        finally:
            cur.close()

