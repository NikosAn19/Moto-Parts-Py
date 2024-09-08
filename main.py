from PyQt5.QtWidgets import QApplication
import sys
from Windows_Classes.Main_Window import Main_Window
import os

print(os.path.exists("/icons/search.svg"))
print(os.getcwd())
app = QApplication(sys.argv)
window = Main_Window()
window.show()
sys.exit(app.exec())
