from PyQt6.QtWidgets import (QMainWindow)

class MainMenubar():
    def __init__(self,parent:QMainWindow):
        self.main_menu =parent.menuBar()
        file_menu = self.main_menu.addMenu("&Archivo")
        view_menu = self.main_menu.addMenu("&Vista")
        log_menu = self.main_menu.addMenu("&Terminal")
        data_menu = self.main_menu.addMenu("&Datos")
        credits_menu = self.main_menu.addMenu("&Creditos")