import sys
import os
from typing import List
import PyQt5.QtGui as QtGui
from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore
from save import Save
from util import add_paths


Save.verify_path(None)
add_paths()

from Ui_table import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    # CONSTRUCTOR - this function gets called at the beginning
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.table.setAlternatingRowColors(True)
        self.show()

    def add_transaction(self, transaction_date, post_date, description, type, amount, category, memo):
        row = self.table.rowCount()
        # print(row)
        self.table.insertRow(row)
        values = [transaction_date, post_date,
                  description, type, amount, category, memo]
        for index, val in enumerate(values):
            self.table.setItem(row, index, QTableWidgetItem(val))


# ------ main section ------
if __name__ == "__main__":
    # the program was started directly
    # setup the graphical interface
    app = QApplication([])
    app.setApplicationName("Relynance")

    # start up the graphical interface
    window = MainWindow()
    with open("test_files\Chase4554_Activity20210320_20210419_20210424.CSV", "r") as f:
        for line in f.readlines()[1:]:
            transaction_date, post_date, description, category, type, amount, memo = line.split(
                ",")
            window.add_transaction(
                transaction_date, post_date, description, type, amount, category, memo)
    # execute the program until the window is closed
    sys.exit(app.exec_())
