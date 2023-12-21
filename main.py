from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from Main_Window import Main_Window
from duplicateEntryAlert_Window import Alert_Window
from Search_Window import Search_Panel
from Not_Numbers_Window import Not_Numbers_Alert

app = QApplication(sys.argv)
window = Main_Window()
window.show()
sys.exit(app.exec())
