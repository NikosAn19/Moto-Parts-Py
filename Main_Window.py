import MySQLdb
import mysql.connector
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.uic.properties import QtGui
from PyQt5 import QtWidgets
from interface_2_Interface import Ui_MainWindow
from Query_Generator import Generator
from data import Piston
from db_procedures import connection
from duplicateEntryAlert_Window import Alert_Window
from Edit_Window import Edit_Panel
from Search_Window import Search_Panel
from entrySuccesfulAlert import Success_Alert_Window
from empty_input_alert_window import Empty_Input_Alert_Window
from Edit_SuccessFull_Window import Edit_Successfull_Alert
from Validator import Input_Validator
from Not_Numbers_Window import Not_Numbers_Alert
from Sure_Window import Sure_Alert
from Select_To_Edit import Select_To_Edit_Alert


class Main_Window(QMainWindow, Ui_MainWindow):
    clickPos = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.closeBtn.clicked.connect(lambda: QApplication.exit())
        self.minimizeBtn.clicked.connect(self.showMinimized)
        self.insertBtn.clicked.connect(self.insertion)
        self.fillTable()
        self.pistonTable.resizeColumnsToContents()
        self.searchBtn.clicked.connect(self.show_search_window)
        self.deleteBtn.clicked.connect(self.handle_delete)
        self.editBtn.clicked.connect(self.edit)
        self.pistonTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.search_window = Search_Panel()
        self.search_window.searchBtn.clicked.connect(self.search)
        self.sure_alert = Sure_Alert()
        self.sure_alert.yesBtn.clicked.connect(self.delete_row)
        self.sure_alert.noBtn.clicked.connect(self.sure_alert.close)
        # self.edit_window.saveEditBtn.clicked.connect(self.save_edit)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    def fillTable(self):
        conn = connection()
        result = conn.select_query("select * from pistons;")
        row = 0
        self.pistonTable.setRowCount(len(result))
        for piston in result:
            print(piston[1])
            self.pistonTable.setItem(row, 0, QTableWidgetItem(str(piston[0])))
            self.pistonTable.setItem(row, 1, QTableWidgetItem(str(piston[1])))
            self.pistonTable.setItem(row, 2, QTableWidgetItem(str(piston[2])))
            self.pistonTable.setItem(row, 3, QTableWidgetItem(str(piston[3])))
            self.pistonTable.setItem(row, 4, QTableWidgetItem(str(piston[4])))
            self.pistonTable.setItem(row, 5, QTableWidgetItem(str(piston[5])))
            self.pistonTable.setItem(row, 6, QTableWidgetItem(str(piston[6])))
            self.pistonTable.setItem(row, 7, QTableWidgetItem(str(piston[7])))
            self.pistonTable.setItem(row, 8, QTableWidgetItem(str(piston[8])))
            row = row + 1

    def insertion(self):

        code = self.pistonCodeLine.text().upper()
        brand = self.brandLine.text().upper()
        model = self.modelLine.text().upper()
        tact = self.tactLine.text().upper()
        pinDiameter = self.pinDiameterLine.text().upper()
        compression = self.compressionLine.text().upper()
        totalHeight = self.totalHeightLine.text().upper()
        oversize = self.oversizeLine.text().upper()
        diameter = self.diameterLine.text().upper()

        piston = Piston(brand, model, tact, code, diameter, totalHeight, pinDiameter, compression,
                        oversize)
        piston_data = (brand, model, tact, code, diameter, totalHeight, pinDiameter, compression,
                       oversize)
        inputs = []
        inputs.append(code)
        inputs.append(brand)
        inputs.append(model)
        inputs.append(tact)
        inputs.append(pinDiameter)
        inputs.append(compression)
        inputs.append(totalHeight)
        inputs.append(oversize)
        inputs.append(diameter)
        empty_input = False
        for input in inputs:
            if input is None or input == '':
                empty_input = True
                print('Empty input')

        if not empty_input:
            validator = Input_Validator(piston)
            is_valid = validator.result_only_numbers()
            if is_valid:
                try:
                    query = ("insert into pistons(brand, model, tact, pistonCode, diameter, totalHeight, pinDiameter, "
                             "compressionHeight, oversize) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    conn = connection()
                    conn.insert_query(query, piston_data)
                    print('Entered successfully')
                    self.show_success_alert()
                except mysql.connector.IntegrityError as e:
                    print(e)
                    self.show_duplicate_entry_alert()
                finally:
                    print(piston)
                    self.fillTable()
            else:
                self.show_not_numbers_alert()
        else:
            self.show_empty_input_alert()

    def show_duplicate_entry_alert(self):
        self.duplicate_pop_up = Alert_Window()
        self.duplicate_pop_up.show()

    def show_success_alert(self):
        self.success_pop_up = Success_Alert_Window()
        self.success_pop_up.show()

    def show_empty_input_alert(self):
        self.empty_input_pop_up = Empty_Input_Alert_Window()
        self.empty_input_pop_up.show()

    def show_not_numbers_alert(self):
        self.not_numbers_alert = Not_Numbers_Alert()
        self.not_numbers_alert.show()

    def show_select_to_edit_alert(self):
        self.select_to_edit_alert = Select_To_Edit_Alert()
        self.select_to_edit_alert.show()

    def show_edit_window(self):
        self.edit_window = Edit_Panel()
        self.edit_window.show()

    def show_search_window(self):
        self.search_window.show()
        self.search_window.move(100, 100)

    def search(self):
        brand = self.search_window.brandLine.text().upper()
        model = self.search_window.modelLine.text().upper()
        code = self.search_window.pistonCodeLine.text().upper()
        tact = self.search_window.tactLine.text().upper()
        compression = self.search_window.compressionLine.text().upper()
        total_height = self.search_window.totalHeightLine.text().upper()
        pin_diameter = self.search_window.pinDiameterLine.text().upper()
        diameter = self.search_window.diameterLine.text().upper()
        oversize = self.search_window.oversizeLine.text().upper()
        piston = Piston(brand, model, tact, code, diameter, total_height, pin_diameter, compression, oversize)
        generator = Generator(piston)
        query = generator.select_query()
        print(query)
        conn = connection()
        result = conn.select_query(query)
        row = 0
        self.pistonTable.setRowCount(len(result))
        for piston in result:
            print(piston[1])
            self.pistonTable.setItem(row, 0, QTableWidgetItem(str(piston[0])))
            self.pistonTable.setItem(row, 1, QTableWidgetItem(str(piston[1])))
            self.pistonTable.setItem(row, 2, QTableWidgetItem(str(piston[2])))
            self.pistonTable.setItem(row, 3, QTableWidgetItem(str(piston[3])))
            self.pistonTable.setItem(row, 4, QTableWidgetItem(str(piston[4])))
            self.pistonTable.setItem(row, 5, QTableWidgetItem(str(piston[5])))
            self.pistonTable.setItem(row, 6, QTableWidgetItem(str(piston[6])))
            self.pistonTable.setItem(row, 7, QTableWidgetItem(str(piston[7])))
            self.pistonTable.setItem(row, 8, QTableWidgetItem(str(piston[8])))
            row = row + 1

    def handle_delete(self):
        self.sure_alert.show()


    def delete_row(self):
        if self.pistonTable.rowCount() > 0:
            code = self.pistonTable.item(self.pistonTable.currentRow(), 3).text().upper()
            conn = connection()
            statement = 'DELETE FROM PISTONS WHERE pistonCode = ' + "'" + code + "'"
            print(statement)
            conn.delete_query(statement)
            self.pistonTable.removeRow(self.pistonTable.rowCount() - 1)
            self.fillTable()
            self.sure_alert.close()

    def edit(self):
        try:
            if self.pistonTable.rowCount() > 0:
                brand = self.pistonTable.item(self.pistonTable.currentRow(), 0).text().upper()
                model = self.pistonTable.item(self.pistonTable.currentRow(), 1).text().upper()
                tact = self.pistonTable.item(self.pistonTable.currentRow(), 2).text().upper()
                code = self.pistonTable.item(self.pistonTable.currentRow(), 3).text().upper()
                diameter = self.pistonTable.item(self.pistonTable.currentRow(), 4).text().upper()
                total_height = self.pistonTable.item(self.pistonTable.currentRow(), 5).text().upper()
                pin_diameter = self.pistonTable.item(self.pistonTable.currentRow(), 6).text().upper()
                compression = self.pistonTable.item(self.pistonTable.currentRow(), 7).text().upper()
                oversize = self.pistonTable.item(self.pistonTable.currentRow(), 8).text().upper()

                self.edit_window = Edit_Panel()
                self.edit_window.saveEditBtn.clicked.connect(self.save_edit)
                self.edit_window.brandPrevValue.setText(brand)
                self.edit_window.modelPrevValue.setText(model)
                self.edit_window.codePrevValue.setText(code)
                self.edit_window.tactPrevValue.setText(tact)
                self.edit_window.compressionPrevValue.setText(compression)
                self.edit_window.totalHeightPrevValue.setText(total_height)
                self.edit_window.pinDiameterPrevValue.setText(pin_diameter)
                self.edit_window.diameterPrevValue.setText(diameter)
                self.edit_window.oversizePrevValue.setText(oversize)
                self.edit_window.show()
        except:
            self.show_select_to_edit_alert()

    def save_edit(self):
        brand = self.edit_window.brandLine.text().upper()
        model = self.edit_window.modelLine.text().upper()
        tact = self.edit_window.tactLine.text().upper()
        code = self.edit_window.pistonCodeLine.text().upper()
        diameter = self.edit_window.diameterLine.text().upper()
        total_height = self.edit_window.totalHeightLine.text().upper()
        pin_diameter = self.edit_window.pinDiameterLine.text().upper()
        compression = self.edit_window.compressionLine.text().upper()
        oversize = self.edit_window.oversizeLine.text().upper()
        old_code = self.edit_window.codePrevValue.text().upper()
        piston = Piston(brand, model, tact, code, diameter, total_height, pin_diameter, compression, oversize)

        try:
            generator = Generator(piston)
            update_statement = generator.update_query(old_code)
            conn = connection()
            conn.update_query(update_statement)
            print('Piston successfully edited.')
            self.edit_success_alert = Edit_Successfull_Alert()
            self.edit_success_alert.show()
        except:
            print('Egine malakia')
        finally:
            self.fillTable()
