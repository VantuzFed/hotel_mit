from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal, Slot
from gui_files.ui_new_book import Ui_Form
from models import *


class WindowBook(QWidget):
    def __init__(self, main_w, db):
        super(WindowBook,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.room_id = 0
        self.client_id = 0
        self.date_start = 0
        self.date_end = 0
        self.main_w = main_w
        self.obj = db
        self.ui.button_reg.clicked.connect(self.booking)
        rooms = self.obj.query(Rooms).filter(Rooms.available == 1).all()
        for col in rooms:
            self.ui.room_box.addItem(col.room_number, userData=col.id)
        clients = self.obj.query(Clients).all()
        for col in clients:
            self.ui.client_box.addItem(f'{col.first_name} {col.last_name}', userData=col.id)
        self.emp_id = None  # Изначально id не задано

    def set_user_id(self, emp_id):
        self.emp_id = emp_id


    def booking(self):
        self.room_id = self.ui.room_box.itemData(self.ui.room_box.currentIndex())
        self.client_id = self.ui.client_box.itemData(self.ui.client_box.currentIndex())
        self.date_start = self.ui.cal_start.selectedDate().toString("yyyy-MM-dd")
        self.date_end = self.ui.cal_end.selectedDate().toString("yyyy-MM-dd")
        day_start = self.ui.cal_start.selectedDate().toString("dd")
        day_end = self.ui.cal_end.selectedDate().toString("dd")
        total_days = int(day_end) - int(day_start)

        booking = self.obj.query(Booking).filter(Booking.room_id == self.room_id).first()
        if booking:
            if booking.room_id == self.room_id:
                QMessageBox.warning(self,'Сообщение', 'Такая бронь уже существует')
        else:
            new_book = Booking(room_id=self.room_id, book_start=self.date_start, book_end=self.date_end)
            self.obj.add(new_book)
            self.obj.commit()

            room_ = self.obj.query(Rooms).filter(Rooms.id == self.room_id).first()
            total_price = room_.price_per_day * total_days
            new_bill = Bill(book_id=new_book.id, emp_id=self.emp_id, client_id=self.client_id, price_total=total_price)
            self.obj.add(new_bill)
            self.obj.commit()

            self.ui.label_10.setText(f"Итоговая цена: {str(total_price)}")
            QMessageBox.information(self, 'Сообщение', 'Бронь успешно добавлена')


