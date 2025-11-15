from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QPushButton,
                             QScrollArea)
from PyQt6.QtCore import Qt, QTimer
import sys

#from PyQt6.QtWidgets.QWidget import setWindowFlag

from board import Board
from board_widget import BoardWidget
from patterns import Patterns

class GameOfLifeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Game of Life")


        self.board = Board(width= 260, height= 210)# plansza

        self.board_widget = BoardWidget(self.board, cell_size = 3)# widget do rysowania planszy

        # Timer do symulacji
        self.timer = QTimer()
        self.timer.timeout.connect(self.step_simulation)
        self.is_running = False
        self.boundary_type = 'periodic'  # domyślnie periodyczny
        self.generation = 0  # licznik generacji

        #Scroll do przewijania plnaszy
        scroll = QScrollArea()
        scroll.setWidget(self.board_widget)
        scroll.setWidgetResizable(False)


        #panel z przyciskami
        button_panel = QWidget()
        button_layout = QHBoxLayout()

        # Przyciski kontrolne
        self.btn_start = QPushButton("Start")
        self.btn_start.clicked.connect(self.toggle_simulation)

        self.btn_step = QPushButton("Krok")
        self.btn_step.clicked.connect(self.step_simulation)

        self.btn_clear = QPushButton("Wyczyść") # przycisk do czyszcenia
        self.btn_clear.clicked.connect(self.clear_board)# co jak klikne przycisk czyszczenia

        #przycisk do glidera:
        self.btn_glider = QPushButton("Glider")
        self.btn_glider.clicked.connect(self.add_glider)

        #przycisk do bloku
        self.btn_block = QPushButton("Block")
        self.btn_block.clicked.connect(self.add_block)

        #przycisk do blinkera:
        self.btn_blinker = QPushButton("Blinker")
        self.btn_blinker.clicked.connect(self.add_blinker)

        button_layout.addWidget(self.btn_start)
        button_layout.addWidget(self.btn_step)
        button_layout.addWidget(self.btn_clear)
        button_layout.addWidget(QWidget())  # separator
        button_layout.addWidget(self.btn_glider)
        button_layout.addWidget(self.btn_block)
        button_layout.addWidget(self.btn_blinker)
        button_layout.addStretch()

        button_panel.setLayout(button_layout)

        #glowny layout:
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(button_panel)
        main_layout.addWidget(scroll)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        #rozmiar okna
        self.resize(800, 700)


    def clear_board(self):
        self.board.clear()
        self.board_widget.update()

    def add_glider(self):

        self.board.clear()
        center_x = self.board.width // 2
        center_y = self.board.height // 2
        self.board.set_pattern(Patterns.glider(), center_x, center_y)
        self.board_widget.update()

    def add_block(self):

        self.board.clear()
        center_x = self.board.width // 2
        center_y = self.board.height // 2
        self.board.set_pattern(Patterns.block(), center_x, center_y)
        self.board_widget.update()

    def add_blinker(self):

        self.board.clear()
        center_x = self.board.width // 2
        center_y = self.board.height // 2
        self.board.set_pattern(Patterns.blinker(), center_x, center_y)
        self.board_widget.update()

    def toggle_simulation(self):
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.btn_start.setText("Start")

        else:
            self.timer.start(1)
            self.is_running = True
            self.btn_start.setText("Stop")
            self.generation =0

    def step_simulation(self):
        self.board.next_generation(boundery=self.boundary_type)
        self.board_widget.update()
        self.generation +=1
        print(f"Generacja: {self.generation}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameOfLifeWindow()
    window.show()
    sys.exit(app.exec())