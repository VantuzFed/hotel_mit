from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6 import uic

class WindowBook(QWidget):
    def __init__(self, main_w, db, emp_id):
        super(WindowBook,self).__init__()
        self.ui = uic.loadUi('gui_files/new_book.ui', self)
        self.room_id = 0
        self.emp_id = emp_id
        self.client_id = 0
        self.date_start = 0
        self.date_end = 0
        self.main_w = main_w
        self.obj = db
        self.emp_id = emp_id
        self.ui.button_reg.clicked.connect(self.booking)
        with self.obj.cursor() as cur:
            cur.execute('select id, room_number from rooms')
            res = cur.fetchall()
            for col in res:
                self.ui.room_box.addItem(str(col[1]), userData=col[0])
        with self.obj.cursor() as cur:
            cur.execute('select id, first_name, last_name from clients')
            res = cur.fetchall()
            for col in res:
                self.ui.client_box.addItem(f'{col[1]} {col[2]}', userData=col[0])

    def booking(self):
        self.room_id = self.ui.room_box.itemData(self.ui.room_box.currentIndex())
        self.client_id = self.ui.client_box.itemData(self.ui.client_box.currentIndex())
        self.date_start = self.ui.cal_start.selectedDate().toString("yyyy-MM-dd")
        self.date_end = self.ui.cal_end.selectedDate().toString("yyyy-MM-dd")
        day_start = self.ui.cal_start.selectedDate().toString("dd")
        day_end = self.ui.cal_end.selectedDate().toString("dd")
        total_days = int(day_end) - int(day_start)
        cur = self.obj.cursor()
        cur.execute(f'select * from booking where room_id = \'{self.room_id}\'')
        res = cur.fetchone()
        print(res)
        try:
            if res[1] == self.room_id:
                QMessageBox.warning(self,'Сообщение', 'Такая бронь уже существует')
        except:
            val = (self.room_id, self.date_start, self.date_end)
            sql = 'INSERT INTO booking (room_id, book_start, book_end) VALUES(%s,%s,%s)'
            cur.execute(sql, val)
            self.obj.commit()
            book_id = cur.lastrowid
            with self.obj.cursor() as cur1:
                cur1.execute(f'select price_per_day from rooms where id = \'{self.room_id}\'')
                price_day = cur1.fetchone()[0]
            total_price = price_day * total_days
            print(total_price)
            cur.execute(f'INSERT INTO bill (book_id, emp_id, client_id, price_total) VALUES({book_id},{self.emp_id},{self.client_id},{0})')
            QMessageBox.information(self, 'Сообщение', 'Бронь успешно добавлена')
        finally:
            cur.close()
