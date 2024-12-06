from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from PyQt6 import uic

class WindowRoomEdit(QWidget):
    def __init__(self, main_w, db):
        super(WindowRoomEdit,self).__init__()
        self.ui = uic.loadUi('gui_files/table_edit.ui', self)
        self.log = 0
        self.passwd = 0
        self.username = 0
        self.main_w = main_w
        self.obj = db
        # self.ui.but_cle.clicked.connect(self.table.clear)
        # self.ui.but_ent.clicked.connect(self.insert_in_table)
        cur = self.obj.cursor()
        cur.execute('SELECT room_number as \'Номер комнаты\', class as \'Класс\', price_per_day as \'Цена за день\', available as \'Занята\' FROM rooms')
        data = cur.fetchall()
        if data:
            field_names = [i[0] for i in cur.description]
            self.ui.table.setRowCount(len(data))
            self.ui.table.setColumnCount(len(data[0]))
            self.ui.table.setHorizontalHeaderLabels(field_names)
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if j==3:
                        cell = QTableWidgetItem('Да' if data[i][j] == 0 else 'Нет')
                        self.ui.table.setItem(i, j, cell)
                    else:
                        cell = QTableWidgetItem(str(data[i][j]))
                        self.ui.table.setItem(i, j, cell)



