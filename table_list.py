from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from sqlalchemy import or_, and_, func

class Table_ls(QWidget):
    def __init__(self, main_w, obj):
        super(Table_ls,self).__init__()
        loader = QUiLoader()
        ui_file = QFile('gui_files/table_list.ui')
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()
        self.main_w = main_w
        # self.obj = obj
        # cur = self.obj.cursor()
        # cur.execute('SELECT room_number as \'Номер комнаты\', class as \'Класс\', price_per_day as \'Цена за день\', available as \'Занята\' FROM rooms')
        # data = cur.fetchall()
        # if data:
        #     field_names = [i[0] for i in cur.description]
        #     self.ui.table.setRowCount(len(data))
        #     self.ui.table.setColumnCount(len(data[0]))
        #     self.ui.table.setHorizontalHeaderLabels(field_names)
        #     for i in range(len(data)):
        #         for j in range(len(data[0])):
        #             if j==3:
        #                 cell = QTableWidgetItem('Да' if data[i][j] == 0 else 'Нет')
        #                 self.ui.table.setItem(i, j, cell)
        #             else:
        #                 cell = QTableWidgetItem(str(data[i][j]))
        #                 self.ui.table.setItem(i, j, cell)
        #
