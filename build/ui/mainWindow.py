import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow)
from mainMenubar import MainMenubar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,500)
        self.setMinimumSize(1000,500)
        self.setWindowTitle("Gestion Metereologica")
        MainMenubar(self)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())