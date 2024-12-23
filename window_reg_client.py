from PySide6.QtWidgets import QWidget, QMessageBox
from gui_files.ui_reg_client import Ui_Form
from models import *

class Register_client(QWidget):
    def __init__(self, main_w, db):
        super(Register_client,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.f_name = 0
        self.m_name = 0
        self.l_name = 0
        self.email = 0
        self.phone = 0
        self.doc_id = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_reg.clicked.connect(self.registration)

    def registration(self):
        self.f_name = self.ui.ent_fname.text()
        self.m_name = self.ui.ent_mname.text()
        self.l_name = self.ui.ent_lname.text()
        self.email = self.ui.ent_email.text()
        self.phone = self.ui.ent_phone.text()
        self.doc_id = self.ui.ent_doc_id.text()
        client = self.obj.query(Clients).filter(Clients.document_id == self.doc_id).first()
        if client:
            if client.document_id == self.doc_id:
                QMessageBox.warning(self,'Сообщение', 'Такой клиент уже существует')
        else:
            new_client = Clients(first_name=self.f_name, last_name=self.l_name, phone_number=self.phone, document_id=self.doc_id, middle_name=self.m_name, e_mail=self.email)
            self.obj.add(new_client)
            self.obj.commit()
            QMessageBox.information(self, 'Сообщение', 'Клиент успешно добавлен')
