from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from PyQt6 import uic

class Table_ls(QWidget):
    def __init__(self, main_w, obj):
        super(Table_ls,self).__init__()
        print("table list window создано")
        self.ui = uic.loadUi('gui_files/table_list.ui',self)
        self.main_w = main_w
        self.obj = obj
        cur = self.obj.cursor()
        cur.execute('SELECT * FROM rooms')
        data = cur.fetchall()
        if data:
            field_names = [i[0] for i in cur.description]
            self.ui.table.setRowCount(len(data))
            self.ui.table.setColumnCount(len(data[1]))
            self.ui.table.setHorizontalHeaderLabels(field_names)
            for i in range(len(data)):
                for j in range(len(data[1])):
                    cell = QTableWidgetItem('' if data[i][j] is None else str(data[i][j]))
                    self.ui.table.setItem(i, j, cell)

