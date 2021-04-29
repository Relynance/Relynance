from PyQt5.QtWidgets import QTableWidget


class WindowTable(QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def resizeEvent(self, *args, **kwargs):
        e = args[0]
        old = e.oldSize().width()
        new = e.size().width()
        factor = new / old
        for column in range(self.columnCount()):
            self.setColumnWidth(
                column, self.columnWidth(column) * factor)
        super().resizeEvent(*args, **kwargs)

    def columnResized(self, column: int, oldWidth: int, newWidth: int) -> None:

        return super().columnResized(column, oldWidth, newWidth)
