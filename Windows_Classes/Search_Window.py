from Compiled_Interafaces.searchInterface import Ui_MainWindow
# from searchInterface import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore


class Search_Panel(QMainWindow, Ui_MainWindow):
    clickPos = None

    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closeBtn.clicked.connect(self.close)
        self.minimizeBtn.clicked.connect(self.showMinimized)
        # self.searchBtn.clicked.connect(self.search)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    # def search(self):
    #     brand = self.brandLine.text()
    #     model = self.modelLine.text()
    #     code = self.pistonCodeLine.text()
    #     tact = self.tactLine.text()
    #     compression = self.compressionLine.text()
    #     total_height = self.totalHeightLine.text()
    #     pin_diameter = self.pinDiameterLine.text()
    #     diameter = self.diameterLine.text()
    #     oversize = self.oversizeLine.text()
    #     piston = Piston(brand, model, tact, code, diameter, total_height, pin_diameter, compression, oversize)
    #     generator = Generator(piston)
    #     query = generator.select_query()
    #     print(query)
    #     conn = connection()
    #     result = conn.getQueryResult(query)
    #     return result
