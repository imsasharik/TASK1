import sys
from PyQt5.QtWidgets import *
import random
import sqlite3
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # загрузка файла uic
        self.con = sqlite3.connect("coffee.db")  # загрузка датабазы с данными об изображениях
        self.cur = self.con.cursor()

    def load_initial_data(self):
        self.cur.execute('''SELECT * FROM coffee ''')
        rows = self.cur.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.tableWidget_2.insertRow(inx)
            # add more if there is more columns in the database.
            self.tableWidget_2.setItem(inx, 0, QTableWidgetItem(row[1]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())