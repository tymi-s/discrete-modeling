from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPainter, QColor, QPen

class BoardWidget(QWidget):

    def __init__(self, board, cell_size =3):
        super().__init__()
        self.board = board
        self.cell_size = cell_size # rozmiar komurki w pikselach

        self.setMinimumSize(
            board.width* cell_size ,
            board.height* cell_size
        )

    def sizeHint(self):
        return QSize(
            self.board.width * self.cell_size,
            self.board.height * self.cell_size
        )

    def paintEvent(self, event):

        painter = QPainter(self)

        #TŁO
        painter.fillRect(self.rect(), QColor(25,25,60))

        #ŻYWE
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(255,255,255))# czarny

        for y in range(self.board.height):
            for x in range(self.board.width):
                if self.board.grid[y,x] == 1:# czyli jeśli żywa
                    painter.drawRect(

                        x * self.cell_size,
                        y * self.cell_size,
                        self.cell_size,
                        self.cell_size
                    )

    def mousePressEvent(self, event):

        x = event.pos().x() // self.cell_size
        y = event.pos().y() // self.cell_size

        if 0 <= x < self.board.width and 0 <= y < self.board.height:
            self.board.toggle_cell(x, y)
            self.update()


