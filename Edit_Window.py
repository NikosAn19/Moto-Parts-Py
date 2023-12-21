from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtCore
from editInterface import Ui_MainWindow
from db_procedures import connection
import mysql.connector
from duplicateEntryAlert_Window import Alert_Window


class Edit_Panel(QMainWindow, Ui_MainWindow):
    clickPos = None

    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closeBtn.clicked.connect(self.close)
        self.minimizeBtn.clicked.connect(self.showMinimized)
        # self.saveEditBtn.clicked.connect()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    def save(self):
        code = self.pistonCodeLine.text()
        brand = self.brandLine.text()
        model = self.modelLine.text()
        tact = self.tactLine.text()
        pinDiameter = self.pinDiameterLine.text()
        compression = self.compressionLine.text()
        totalHeight = self.totalHeightLine.text()
        oversize = self.oversizeLine.text()
        diameter = self.diameterLine.text()
        piston = (brand, model, tact, code, diameter, totalHeight, pinDiameter, compression,
                  oversize)
        conn = connection()
        try:
            query = ("insert into pistons(brand, model, tact, pistonCode, diameter, totalHeight, "
                     "pinDiameter, compressionHeight, oversize) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            conn.insert_query(query, piston)
            print('Entered successfully')
        except mysql.connector.IntegrityError as e:
            print(e)
            self.show_pop_up()
        finally:
            print(piston)


    def show_pop_up(self):
        self.pop_up = Alert_Window()
        self.pop_up.show()
