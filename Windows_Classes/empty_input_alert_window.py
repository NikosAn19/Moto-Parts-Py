from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from Compiled_Interafaces.empty_input_Interface import Ui_alertWindow
# from empty_input_Interface import Ui_alertWindow


class Empty_Input_Alert_Window(QMainWindow, Ui_alertWindow):
    clickPos = None

    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closeBtn.clicked.connect(self.close)
        self.okBtn.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None