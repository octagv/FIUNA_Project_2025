import sys
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import (QPixmap)

class CreditWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Creditos de la Aplicación")
        self.setGeometry(100,100,500,500)
        self.setFixedSize(500,500)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreditWindow()
    sys.exit(app.exec())