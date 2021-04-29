from PyQt5.QtWidgets import QTableWidget


class WindowTable(QTableWidget):
    def __init__(self, *args, col_width=100, **kwargs):
        self.col_sizes = []
        self.col_width = col_width
        self.size = 0
        super().__init__(*args, **kwargs)
        self.horizontalHeader().sectionResized.connect(self.columnResized)

    def resizeEvent(self, *args, **kwargs):
        e = args[0]
        old = e.oldSize().width()
        new = e.size().width()
        self.size = new
        #factor = new / old
        self.check_sizes()
        for column in range(self.columnCount()):
            self.setColumnWidth(column, self.col_sizes[column] * new)
            #self.setColumnWidth(column, self.columnWidth(column) * factor)
        super().resizeEvent(*args, **kwargs)

    def columnResized(self, column: int, oldWidth: int, newWidth: int) -> None:
        self.check_sizes()
        self.col_sizes[column] = newWidth / self.size
        return super().columnResized(column, oldWidth, newWidth)

    def check_sizes(self):
        while len(self.col_sizes) < self.columnCount():
            self.col_sizes.append(self.col_width / self.size)
