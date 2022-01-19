import ctypes
import datetime
import math
import os
import signal
import subprocess
import sys

from PySide2 import QtGui
from PySide2.QtCore import (Qt, QTimer, QDate)
from PySide2.QtWidgets import *

import database
from gui import Ui_MainWindow

_database = database.DatabaseCarSel()

myappid = u'wolf.wolf.carsel.1.0.0'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self._splash = subprocess.Popen('python splash.py', shell=True,
                                        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._employee_table_column = ["First Name", "Last Name", "Gender", "Age", "Position", "Address",
                                       "Phone number", "Date joined"]
        self._product_table_column = ['Type', 'Name', 'Year released', 'Top speed (km/h)', 'Horse power',
                                      'Seat count', 'Length (cm)', 'Width (cm)', 'Date added', 'Price (million Rp)']
        self._branches = []
        self._branches_it = []
        self._cartypes = []
        self._cartypes_it = []
        self._position = []
        self._manufacturer = []
        self._employee_list = []
        self._employee_list_raw = []
        self._maintainer_list = []
        self._product_list = []
        self._product_list_raw = []
        self._previous_search = ""
        self._previous_product_search = ""
        self._current_employee_age = 0
        self._employee_count = 0
        self._product_count = 0
        self._current_user = [[1, 1, 'Debug', 'Account']]  # change this to None later
        self._grant_all = True  # change this to false later
        self._grant_manager = False
        self._grant_it = False
        self._grant_db = False
        self._app_icon = QtGui.QIcon('data/img/icon.ico')

        # setting the app icon to show on the taskbar
        self.setWindowIcon(self._app_icon)

        # login page
        self.ui.signinbutton.clicked.connect(lambda: self.login())
        self.ui.password.returnPressed.connect(lambda: self.login())

        # manager page
        self.ui.refreshbuttonmanager.clicked.connect(lambda: self.set_widget(self.ui.manager))
        self.ui.profilebuttonmanager.clicked.connect(lambda: self.set_widget(self.ui.profile))

        # manager page -- employee
        self.ui.displayageframe_manager.hide()
        self.ui.displaygenderframe_manager.hide()
        self.ui.displaypositionframe_manager.hide()
        self.ui.employeetableframe_manager.hide()
        self.ui.employeecountframe_manager.hide()
        self.ui.maxagechoose_manager.setValue(999)
        self._table = self.ui.employeetable_manager
        self._table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.submitbuttonemployee_manager.clicked.connect(lambda: self.show_employee_table(
            self.ui.firstnamecheckboxemployee_manager.isChecked(),
            self.ui.lastnamecheckboxemployee_manager.isChecked(),
            self.ui.gendercheckboxemployee_manager.isChecked(),
            self.ui.agecheckboxemployee_manager.isChecked(),
            self.ui.positioncheckboxemployee_manager.isChecked(),
            self.ui.addresscheckboxemployee_manager.isChecked(),
            self.ui.phonenocheckboxemployee_manager.isChecked(),
            self.ui.datecheckboxemployee_manager.isChecked()
        ))
        self.ui.branchchoose_manager.currentIndexChanged.connect(self.change_branch_description)
        self.ui.gendercheckboxemployee_manager.stateChanged.connect(self.enable_gender)
        self.ui.agecheckboxemployee_manager.stateChanged.connect(self.enable_age)
        self.ui.positioncheckboxemployee_manager.stateChanged.connect(self.enable_position)

        # manager page -- product
        self.ui.cartypeframe_manager.hide()
        self.ui.yearreleasedframe_manager.hide()
        self.ui.topspeedframe_manager.hide()
        self.ui.horsepowerframe_manager.hide()
        self.ui.seatcountframe_manager.hide()
        self.ui.lengthframe_manager.hide()
        self.ui.widthframe_manager.hide()
        self.ui.priceframe_manager.hide()
        self.ui.producttableframe_manager.hide()
        self.ui.productcountframe_manager.hide()
        self.ui.branchchoose_manager_2.currentIndexChanged.connect(self.change_branch_desc_product)
        self.ui.cartype_manager.stateChanged.connect(self.enable_car_type)
        self.ui.yearreleased_manager.stateChanged.connect(self.enable_year_released)
        self.ui.topspeed_manager.stateChanged.connect(self.enable_top_speed)
        self.ui.horsepower_manager.stateChanged.connect(self.enable_horse_power)
        self.ui.seatcount_manager.stateChanged.connect(self.enable_seat_count)
        self.ui.length_manager.stateChanged.connect(self.enable_length)
        self.ui.width_manager.stateChanged.connect(self.enable_width)
        self.ui.price_manager.stateChanged.connect(self.enable_price)
        self._product_table = self.ui.producttable_manager
        self._product_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._product_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.submitbuttonproduct_manager.clicked.connect(lambda: self.show_product_table(
            self.ui.cartype_manager.isChecked(),
            self.ui.carname_manager.isChecked(),
            self.ui.yearreleased_manager.isChecked(),
            self.ui.topspeed_manager.isChecked(),
            self.ui.horsepower_manager.isChecked(),
            self.ui.seatcount_manager.isChecked(),
            self.ui.length_manager.isChecked(),
            self.ui.width_manager.isChecked(),
            self.ui.dateadded_manager.isChecked(),
            self.ui.price_manager.isChecked()
        ))

        # manager page -- counts
        self.ui.branchchoosecount_counts.currentIndexChanged.connect(lambda: self.refresh_counts(segment='branch'))
        self.ui.positionchoose_counts.currentIndexChanged.connect(lambda: self.refresh_counts(segment='position'))
        self.ui.manufacturerchoose_counts.currentIndexChanged.connect(
            lambda: self.refresh_counts(segment='manufacturer'))
        self.ui.cartypechoose_counts.currentIndexChanged.connect(lambda: self.refresh_counts(segment='cartype'))

        # IT page
        self.ui.refrehsbuttonit.clicked.connect(lambda: self.set_widget(self.ui.it))
        self.ui.profilebuttonit.clicked.connect(lambda: self.set_widget(self.ui.profile))

        # IT page - branch
        self.ui.addbranchbt_it.hide()
        self.ui.editbranchbt_it.hide()
        self.ui.deletebranchbt_it.hide()
        self.ui.newbranchframe_it.hide()
        self.ui.selectbranchframe_it.hide()
        self.ui.addressframe_it.hide()
        self.ui.establishedframe_edit.hide()
        self.ui.branchactionchoose_it.currentIndexChanged.connect(self.branch_it)
        self.ui.addbranchbt_it.clicked.connect(lambda: self.add_branch())
        self.ui.selectbranch_it.currentIndexChanged.connect(self.set_branch_fields)
        self.ui.editbranchbt_it.clicked.connect(lambda: self.edit_branch())
        self.ui.deletebranchbt_it.clicked.connect(lambda: self.delete_branch())

        # IT page - position
        self.ui.addpositionbt_it.hide()
        self.ui.editpositionbt_it.hide()
        self.ui.deletepositionbt_it.hide()
        self.ui.selectpositionframe.hide()
        self.ui.newpositionnameframe.hide()
        self.ui.positionchoose.currentIndexChanged.connect(self.position_it)
        self.ui.addpositionbt_it.clicked.connect(lambda: self.add_position())
        self.ui.selectposition.currentIndexChanged.connect(self.position_fields)
        self.ui.editpositionbt_it.clicked.connect(lambda: self.edit_position())
        self.ui.deletepositionbt_it.clicked.connect(lambda: self.delete_position())

        # IT page - employee
        self.ui.addemployeebtt_it.hide()
        self.ui.editemployeebtt_it.hide()
        self.ui.deleteemployeebtt_it.hide()
        self.ui.employee_addedit_it.hide()
        self.ui.loginpassframe_it.hide()
        self.ui.employeetableframe_editdel_it.hide()
        self.ui.employeeactionchoose_it.currentIndexChanged.connect(self.employee_it)
        self.ui.position_addedit_it.currentIndexChanged.connect(self.show_pass_field)
        self.ui.addemployeebtt_it.clicked.connect(lambda: self.add_edit_employee(1))
        self.ui.editemployeebtt_it.clicked.connect(lambda: self.add_edit_employee(2))
        self.ui.getemployeebt_it.clicked.connect(lambda: self.get_employee_list())
        self.ui.employeetable_editdelete_it.itemDoubleClicked.connect(self.set_employee_fields)
        self.ui.employeetable_editdelete_it.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.deleteemployeebtt_it.clicked.connect(lambda: self.delete_employee())
        self.ui.searchbox_it.returnPressed.connect(lambda: self.filter_employee())
        self.ui.searchbutton_it.clicked.connect(lambda: self.filter_employee())

        # IT page - manufacturer
        self.ui.addmanufacturerbt.hide()
        self.ui.editmanufacturerbt.hide()
        self.ui.deletemanufacturerbt.hide()
        self.ui.selectmanufacturerframe.hide()
        self.ui.newmanufacturerframe.hide()
        self.ui.countryframe_it.hide()
        self.ui.yearframe_it.hide()
        self.ui.manufacturerchoose.currentIndexChanged.connect(self.manufacturer_it)
        self.ui.addmanufacturerbt.clicked.connect(lambda: self.add_edit_manufacturer(1))
        self.ui.selectmanufacturer.currentIndexChanged.connect(self.set_manufacturer_fields)
        self.ui.editmanufacturerbt.clicked.connect(lambda: self.add_edit_manufacturer(2))
        self.ui.deletemanufacturerbt.clicked.connect(lambda: self.delete_manufacturer())

        # IT page - car type
        self.ui.selectcartypeframe.hide()
        self.ui.newcartypenameframe.hide()
        self.ui.addcartypebt.hide()
        self.ui.editcartypebt.hide()
        self.ui.deletecartypebt.hide()
        self.ui.cartypechoose.currentIndexChanged.connect(self.cartype_it)
        self.ui.addcartypebt.clicked.connect(lambda: self.add_edit_cartype(1))
        self.ui.selectcartype.currentIndexChanged.connect(self.set_cartype_fields)
        self.ui.editcartypebt.clicked.connect(lambda: self.add_edit_cartype(2))
        self.ui.deletecartypebt.clicked.connect(lambda: self.delete_cartype())

        # IT page - product
        self.ui.productframe_it.hide()
        self.ui.addproduct_it.hide()
        self.ui.editproduct_it.hide()
        self.ui.deleteproduct_it.hide()
        self.ui.producttableframe_it.hide()
        self.ui.productchoose.currentIndexChanged.connect(self.product_it)
        self.ui.getproductbt_it_2.clicked.connect(lambda: self.get_product_list())
        self.ui.producttable_editdelete_it_2.itemDoubleClicked.connect(self.set_product_field)
        self.ui.producttable_editdelete_it_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.searchproductfield_2.returnPressed.connect(lambda: self.filter_product())
        self.ui.searchproductbutton_2.clicked.connect(lambda: self.filter_product())
        self.ui.addproduct_it.clicked.connect(lambda: self.add_edit_product(1))
        self.ui.editproduct_it.clicked.connect(lambda: self.add_edit_product(2))
        self.ui.deleteproduct_it.clicked.connect(lambda: self.delete_product())

        # profile page
        self.ui.managersectionbutton.clicked.connect(lambda: self.check_access(self.ui.managersectionbutton))
        self.ui.itsectionbutton.clicked.connect(lambda: self.check_access(self.ui.itsectionbutton))
        self.ui.dbtestbutton_profile.clicked.connect(lambda: self.check_access(self.ui.dbtestbutton_profile))
        self.ui.logoutbutton.clicked.connect(lambda: self.logout())

        # database page
        self.ui.submitquerybranch.hide()
        self.ui.submitpositionquery_2.hide()
        self.ui.manufacturerquerybt_2.hide()
        self.ui.cartypequerybt_2.hide()
        self.ui.employeequerybt_2.hide()
        self.ui.productquerybt_2.hide()
        # self.ui.querytable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # self.ui.querytable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.querytable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.profilebuttondbtest.clicked.connect(lambda: self.set_widget(self.ui.profile))
        self.ui.submitquerybranch.clicked.connect(lambda: self.test_database())
        self.ui.selecttable_dbtest.currentIndexChanged.connect(self.test_set)
        self.ui.submitquerybranch.clicked.connect(lambda: self.test_database())
        self.ui.submitpositionquery_2.clicked.connect(lambda: self.test_database())
        self.ui.manufacturerquerybt_2.clicked.connect(lambda: self.test_database())
        self.ui.cartypequerybt_2.clicked.connect(lambda: self.test_database())
        self.ui.employeequerybt_2.clicked.connect(lambda: self.test_database())
        self.ui.productquerybt_2.clicked.connect(lambda: self.test_database())

        # setting the widget to login page
        self.set_widget(self.ui.login)
        # self.ui.stackedWidget.setCurrentWidget(self.ui.profile)  # debug

        # showing the main window
        os.kill(self._splash.pid, signal.CTRL_BREAK_EVENT)
        if not self._splash.poll():
            print("Splash correctly halted")
        # self._splash.send_signal(signal.CTRL_BREAK_EVENT)
        self.show()
        self.set_status("OK")

    def show_message_box(self, message: str):
        self._info = QMessageBox()
        self._info.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        self._info.setWindowIcon(self._app_icon)
        self._info.information(self, "CarSel Co., Ltd", message)
        # return self._info.show()

    def set_status(self, status: str):
        self.ui.status_main.setText(f"Status: {status}")
        if status == "OK" or status == "Failed":
            timer = QTimer(self)
            self.ui.loading_icon.hide()
            timer.singleShot(2000, self.ui.status_main.hide)
        else:
            self.ui.status_main.show()
            self.ui.loading_icon.show()

    # MANAGER SECTION - COUNTS SECTION METHOD
    def refresh_counts(self, segment: str):
        if segment == 'branch':
            index = self.ui.branchchoosecount_counts.currentIndex()
            self.ui.employeecount_counts.setText(f"Employee count: {self._branches[index][-1]}")
            self.ui.productcount_counts.setText(f"Product count: {self._branches[index][-2]}")
        elif segment == 'position':
            index = self.ui.positionchoose_counts.currentIndex()
            self.ui.employeenrolled.setText(f"Employee enrolled: {self._position[index][-1]}")
        elif segment == 'manufacturer':
            index = self.ui.manufacturerchoose_counts.currentIndex()
            self.ui.manu_onsale_counts.setText(f"Product on sale: {self._manufacturer[index][-1]}")
        else:
            index = self.ui.cartypechoose_counts.currentIndex()
            self.ui.cartype_onsale_counts.setText(f"Product on sale: {self._cartypes[index][-1]}")

    # MANAGER SECTION - ENABLER METHODS
    def enable_gender(self, int):
        if self.ui.gendercheckboxemployee_manager.isChecked():
            self.ui.displaygenderframe_manager.show()
        else:
            self.ui.genderchoose_manager.setCurrentIndex(0)
            self.ui.displaygenderframe_manager.hide()

    def enable_age(self, int):
        if self.ui.agecheckboxemployee_manager.isChecked():
            self.ui.displayageframe_manager.show()
        else:
            self.ui.minagechoose_manager.setValue(0)
            self.ui.maxagechoose_manager.setValue(999)
            self.ui.displayageframe_manager.hide()

    def enable_position(self, int):
        if self.ui.positioncheckboxemployee_manager.isChecked():
            self.ui.displaypositionframe_manager.show()
        else:
            self.ui.displaypositionframe_manager.hide()

    # MANAGER SECTION - EMPLOYEE METHODS
    def show_employee_table(self, first_name: bool, last_name: bool, gender: bool, age: bool, position: bool,
                            address: bool, phoneno: bool, datejoined: bool):
        employee_count = 0
        self.set_status("Querying and adding employees to table...")
        # clear the table
        while self._table.rowCount() > 0:
            self._table.removeRow(0)

        # showing the table and employee count which is previously hidden
        self.ui.employeetableframe_manager.show()
        self.ui.employeecountframe_manager.show()

        # acquiring employee list from the database, based on the current selected branch
        self._employee_list = _database.employee_list(self.ui.branchchoose_manager.currentText())

        # determining which attributes are going to be added into the table, Branch and Employee ID
        # will always be shown else the table would not make sense
        values = [first_name, last_name, gender, age, position, address, phoneno, datejoined]
        final_list = [self._employee_table_column[index] for index, yes in enumerate(values) if yes]
        final_list_index = [index for index, yes in enumerate(values) if yes]
        final_list.insert(0, "Branch")
        final_list.insert(0, "Employee ID")

        # setting the column count based on user's choice
        self._table.setColumnCount(len(final_list))
        self._table.setHorizontalHeaderLabels(final_list)

        # appending employees into the table
        for employee in self._employee_list:
            # reset employee count
            self._employee_count = 0

            # checker booleans
            show_gender = True
            show_age = True
            show_position = True

            # inserting new row and setting the first and second column to be filled
            # with Branch and Employee ID attributes
            row = self._table.rowCount()
            self._table.insertRow(row)
            self._table.setItem(row, 0, QTableWidgetItem(str(employee[0])))
            self._table.setItem(row, 1, QTableWidgetItem(str(employee[1])))

            # filtering the data, all below are j+2 to skip the first and second column of the table, but the 2
            # isn't directly defined in the range function to avoid the last two attributes being skipped
            for j in range(len(final_list_index)):

                # if the value going to be inserted is age then convert it from datetime.date to int, else append
                # other attributes into the table unconditionally
                if final_list[j + 2] == "Age":
                    self._current_employee_age = math.floor(
                        (datetime.date.today() - employee[final_list_index[j] + 2]).days / 365)
                    self._table.setItem(row, j + 2, QTableWidgetItem(str(self._current_employee_age)))
                else:
                    self._table.setItem(row, j + 2, QTableWidgetItem(str(employee[final_list_index[j] + 2])))

            # if gender and/or age and/or position are True then check the conditions as defined by user's choice,
            # else pass and unconditionally append them to the table
            if gender:
                if self.ui.genderchoose_manager.currentText() != "All":
                    if self.ui.genderchoose_manager.currentText() != employee[4]:
                        show_gender = False
                    else:
                        show_gender = True
                else:
                    show_gender = True
            if age:
                min_age = self.ui.minagechoose_manager.value()
                max_age = self.ui.maxagechoose_manager.value()
                if min_age <= self._current_employee_age <= max_age:
                    show_age = True
                else:
                    show_age = False
            if position:
                if self.ui.positionchooser_manager.currentText() != "All":
                    if employee[-4] != self.ui.positionchooser_manager.currentText():
                        show_position = False
                    else:
                        show_position = True
                else:
                    show_position = True

            # finally, check all the checker booleans. If all are True then append them to the table, else skip them
            if show_gender and show_age and show_position:
                self._table.showRow(row)
                employee_count += 1
            else:
                self._table.hideRow(row)
        self.ui.employeecount_manager.setText(f'Employee count: {employee_count}')
        self.set_status("OK")

    # MANAGER SECTION - BRANCH METHODS
    def refresh_branch(self):
        self.set_status("Refreshing branch...")
        branch = _database.retrieve_branch()
        self.ui.branchchoose_manager.setCurrentIndex(0)
        self.ui.branchchoose_manager_2.setCurrentIndex(0)
        self.ui.branchchoosecount_counts.setCurrentIndex(0)
        self.change_branch_desc_product(0)
        if self._branches != branch:
            self._branches = branch
            self.ui.branchchoose_manager.clear()
            self.ui.branchchoose_manager_2.clear()
            self.ui.branchchoosecount_counts.clear()
            self.ui.branchchoose_manager.addItems(["All"])
            self.ui.branchchoose_manager_2.addItems(["All"])
            for place in branch:
                self.ui.branchchoose_manager.addItems([place[1]])
                self.ui.branchchoose_manager_2.addItems([place[1]])
                self.ui.branchchoosecount_counts.addItems([place[1]])
        self.set_status("OK")

    def change_branch_description(self, int):
        self.set_status("Changing branch description...")
        # subtract by one to avoid out of range index, since self._branches doesn't contain the "All" value,
        # therefore to ease the operation, "All" is assigned as -1
        index = int - 1
        try:
            if index == -1:
                self.ui.addresslabel_manager.setText("Address: ")
                self.ui.establishedlabel_manager.setText("Established: ")
                self.ui.employeecount_manager_2.setText("Employee count in branch: ")
            else:
                self.ui.addresslabel_manager.setText(f"Address: {self._branches[index][2]}")
                self.ui.establishedlabel_manager.setText(f"Established: {self._branches[index][3]}")
                self.ui.employeecount_manager_2.setText(f"Employee count in branch: {self._branches[index][-1]}")
        except IndexError:
            pass
        self.set_status("OK")

    # IT SECTION - REFRESHES FOR DROPDOWNS
    def refresh_branch_it(self):
        self.set_status("Refreshing branch...")
        branch = _database.retrieve_branch()
        self.ui.branchactionchoose_it.setCurrentIndex(0)
        self.ui.selectbranch_it.setCurrentIndex(0)
        self.ui.branchchoose_addedit_it.setCurrentIndex(0)
        self.ui.branchchooseproduct.setCurrentIndex(0)
        if branch != self._branches_it:
            self.ui.selectbranch_it.clear()
            self.ui.branchchoose_addedit_it.clear()
            self.ui.branchchooseproduct.clear()
            for place in branch:
                self.ui.selectbranch_it.addItems([place[1]])
                self.ui.branchchoose_addedit_it.addItems([place[1]])
                self.ui.branchchooseproduct.addItems([place[1]])
            self._branches_it = branch
        self.set_status("OK")

    def refresh_position_it(self):
        self.set_status("Refreshing position...")
        position = _database.retrieve_position()
        self.ui.positionchoose.setCurrentIndex(0)
        self.ui.selectposition.setCurrentIndex(0)
        self.ui.position_addedit_it.setCurrentIndex(0)
        self.ui.positionchoose_counts.setCurrentIndex(0)
        if position != self._position:
            self._position = position
            self.ui.selectposition.clear()
            self.ui.position_addedit_it.clear()
            self.ui.positionchoose_counts.clear()
            for pos in position:
                self.ui.selectposition.addItems([pos[1]])
                self.ui.position_addedit_it.addItems([pos[1]])
                self.ui.positionchoose_counts.addItems([pos[1]])
        # self._position = position
        self.set_status("OK")

    def refresh_manufacturer(self):
        self.set_status("Refreshing manufacturers...")
        manufacturers = _database.retrieve_manufacturer()
        self.ui.manufacturerchoose.setCurrentIndex(0)
        self.ui.selectmanufacturer.setCurrentIndex(0)
        self.ui.manufacturerchooseproduct.setCurrentIndex(0)
        self.ui.manufacturerchoose_counts.setCurrentIndex(0)
        self.ui.manuselect_manager.setCurrentIndex(0)
        if manufacturers != self._manufacturer:
            self._manufacturer = manufacturers
            self.ui.selectmanufacturer.clear()
            self.ui.manufacturerchooseproduct.clear()
            self.ui.manufacturerchoose_counts.clear()
            self.ui.manuselect_manager.clear()
            self.ui.manuselect_manager.addItems(["All"])
            for manufacturer in manufacturers:
                self.ui.selectmanufacturer.addItems([manufacturer[1]])
                self.ui.manufacturerchooseproduct.addItems([manufacturer[1]])
                self.ui.manufacturerchoose_counts.addItems([manufacturer[1]])
                self.ui.manuselect_manager.addItems([manufacturer[1]])

        # self._manufacturer = manufacturers
        self.set_status("OK")

    def refresh_cartype_it(self):
        self.set_status("Refreshing car types...")
        types = _database.retrieve_type()
        self.ui.cartypechoose.setCurrentIndex(0)
        self.ui.selectcartype.setCurrentIndex(0)
        self.ui.cartypechooseproduct.setCurrentIndex(0)
        if types != self._cartypes_it:
            self.ui.selectcartype.clear()
            self.ui.cartypechooseproduct.clear()
            for tipe in types:
                self.ui.selectcartype.addItems([tipe[1]])
                self.ui.cartypechooseproduct.addItems([tipe[1]])
        self._cartypes_it = types
        self.set_status("OK")

    # MANAGER SECTION - REFRESH CARTYPE METHOD
    def refresh_cartype(self):
        self.set_status("Refreshing car type...")
        types = _database.retrieve_type()
        self.ui.cartypechoose_manager.setCurrentIndex(0)
        if types != self._cartypes:
            self._cartypes = types
            self.ui.cartypechoose_manager.clear()
            self.ui.cartypechoose_manager.addItems(["All"])
            self.ui.cartypechoose_counts.clear()
            for tipe in self._cartypes:
                self.ui.cartypechoose_manager.addItems([tipe[1]])
                self.ui.cartypechoose_counts.addItems([tipe[1]])
        self.set_status("OK")

    # MANAGER SECTION - ENABLER METHODS
    def enable_car_type(self, int):
        if self.ui.cartype_manager.isChecked():
            self.ui.cartypeframe_manager.show()
        else:
            self.ui.cartypeframe_manager.hide()

    def enable_year_released(self, int):
        if self.ui.yearreleased_manager.isChecked():
            self.ui.yearreleasedframe_manager.show()
        else:
            self.ui.yearreleasedframe_manager.hide()

    def enable_top_speed(self, int):
        if self.ui.topspeed_manager.isChecked():
            self.ui.topspeedframe_manager.show()
        else:
            self.ui.topspeedframe_manager.hide()

    def enable_horse_power(self, int):
        if self.ui.horsepower_manager.isChecked():
            self.ui.horsepowerframe_manager.show()
        else:
            self.ui.horsepowerframe_manager.hide()

    def enable_seat_count(self, int):
        if self.ui.seatcount_manager.isChecked():
            self.ui.seatcountframe_manager.show()
        else:
            self.ui.seatcountframe_manager.hide()

    def enable_length(self, int):
        if self.ui.length_manager.isChecked():
            self.ui.lengthframe_manager.show()
        else:
            self.ui.lengthframe_manager.hide()

    def enable_width(self, int):
        if self.ui.width_manager.isChecked():
            self.ui.widthframe_manager.show()
        else:
            self.ui.widthframe_manager.hide()

    def enable_price(self, int):
        if self.ui.price_manager.isChecked():
            self.ui.priceframe_manager.show()
        else:
            self.ui.priceframe_manager.hide()

    def show_product_table(self, cartype: bool, carname: bool, year_released: bool, top_speed: bool, horse_power: bool,
                           seat_count: bool, length: bool, width: bool, date_added: bool, price: bool):
        self.set_status("Querying and adding products to table...")
        product_count = 0

        # clear the table
        while self._product_table.rowCount() > 0:
            self._product_table.removeRow(0)

        # showing the table and product count
        self.ui.producttableframe_manager.show()
        self.ui.productcountframe_manager.show()

        # acquiring product list from the database, based on the current selected branch
        self._product_list = _database.car_list(self.ui.branchchoose_manager_2.currentText())

        values = [cartype, carname, year_released, top_speed, horse_power, seat_count, length, width, date_added, price]
        final_list = [self._product_table_column[index] for index, add in enumerate(values) if add]
        final_list_index = [index for index, add in enumerate(values) if add]
        final_list.insert(0, "Branch")
        final_list.insert(0, "Manufacturer")
        final_list.insert(0, "Car ID")

        # setting the column count based on user's choice
        self._product_table.setColumnCount(len(final_list))
        self._product_table.setHorizontalHeaderLabels(final_list)

        # appending products into the table
        for car in self._product_list:
            # checker booleans
            show_manufacturer = True
            show_type = True
            show_year_released = True
            show_top_speed = True
            show_horse_power = True
            show_seat_count = True
            show_length = True
            show_width = True
            show_price = True

            # inserting new row and setting the first, second, and third column to be filled
            # with Car ID, Manufacturer, and Branch attributes
            row = self._product_table.rowCount()
            self._product_table.insertRow(row)
            self._product_table.setItem(row, 0, QTableWidgetItem(str(car[0])))
            self._product_table.setItem(row, 1, QTableWidgetItem(str(car[1])))
            self._product_table.setItem(row, 2, QTableWidgetItem(str(car[2])))

            # filtering the data, all below are j+3 to skip the first and second column of the table, but the 3
            # isn't directly defined in the range function to avoid the last two attributes being skipped
            for data in range(len(final_list_index)):
                self._product_table.setItem(row, data + 3, QTableWidgetItem(str(car[final_list_index[data] + 3])))

            if cartype:
                if self.ui.cartypechoose_manager.currentText() != "All":
                    if self.ui.cartypechoose_manager.currentText() != car[3]:
                        show_type = False
                    else:
                        show_type = True
                else:
                    show_type = True
            if year_released:
                if self.ui.minyear_manager.value() < car[5] < self.ui.maxyear_manager.value():
                    show_year_released = True
                else:
                    show_year_released = False
            if top_speed:
                if self.ui.mintopspeed_manager.value() < car[6] < self.ui.maxtopspeed_manager.value():
                    show_top_speed = True
                else:
                    show_top_speed = False
            if horse_power:
                if self.ui.minhorsepower_manager.value() < car[7] < self.ui.maxhorsepower_manager.value():
                    show_horse_power = True
                else:
                    show_horse_power = False
            if seat_count:
                if self.ui.minseatcount_manager.value() < car[-5] < self.ui.maxseatcount_manager.value():
                    show_seat_count = True
                else:
                    show_seat_count = False
            if length:
                if self.ui.minlength_manager.value() < car[-4] < self.ui.maxlength_manager.value():
                    show_length = True
                else:
                    show_length = False
            if width:
                if self.ui.minwidth_manager.value() < car[-3] < self.ui.maxwidth_manager.value():
                    show_width = True
                else:
                    show_width = False
            if price:
                if self.ui.minprice_manager.value() < car[-1] < self.ui.maxprice_manager.value():
                    show_price = True
                else:
                    show_price = False
            if self.ui.manuselect_manager.currentText() != "All":
                if self.ui.manuselect_manager.currentText() != car[1]:
                    show_manufacturer = False

            if (show_manufacturer and show_type and show_year_released and show_top_speed and show_horse_power and show_seat_count and
                    show_length and show_width and show_price):
                self._product_table.showRow(row)
                product_count += 1
            else:
                self._product_table.hideRow(row)
        self.ui.productcount_manager.setText(f'Product count: {product_count}')
        self.set_status("OK")

    def change_branch_desc_product(self, int):
        self.set_status("Changing branch description...")
        # subtract by one to avoid out of range index, since self._branches doesn't contain the "All" value,
        # therefore to ease the operation, "All" is assigned as -1
        index = int - 1
        try:
            if index == -1:
                self.ui.addresslabel_manager_2.setText("Address: ")
                self.ui.establishedlabel_manager_2.setText("Established: ")
                self.ui.productcount_branch.setText("Product count in branch: ")
            else:
                self.ui.addresslabel_manager_2.setText(f"Address: {self._branches[index][2]}")
                self.ui.establishedlabel_manager_2.setText(f"Established: {self._branches[index][3]}")
                self.ui.productcount_branch.setText(f"Product count in branch: {self._branches[index][-1]}")
        except IndexError:
            pass
        self.set_status("OK")

    # IT SECTION - BRANCH METHODS
    def branch_it(self, index):
        self.set_status("Refreshing branch...")
        self.ui.newbranchframe_it.hide()
        self.ui.selectbranchframe_it.hide()
        self.ui.addressframe_it.hide()
        self.ui.establishedframe_edit.hide()
        self.ui.addbranchbt_it.hide()
        self.ui.editbranchbt_it.hide()
        self.ui.deletebranchbt_it.hide()
        if index == 0:  # add
            self.ui.newbranchframe_it.show()
            self.ui.addbranchbt_it.show()
            self.ui.addressframe_it.show()
            self.ui.establishedframe_edit.show()
        elif index == 1:  # edit
            self.ui.selectbranchframe_it.show()
            self.ui.newbranchframe_it.show()
            self.ui.editbranchbt_it.show()
            self.ui.addressframe_it.show()
            self.ui.establishedframe_edit.show()
        else:  # delete
            self.ui.selectbranchframe_it.show()
            self.ui.deletebranchbt_it.show()
        self.set_status("OK")

    def add_branch(self):
        self.set_status("Adding branch to database...")
        branch_name = self.ui.branchname_addedit_it.text().strip()
        address = self.ui.address_addedit_it.toPlainText().strip()
        established = self.ui.established_addedit_it.value()
        if int(established) < 2000:
            self.show_message_box("Please enter a valid year")
            self.set_status("Failed")
        elif branch_name == "":
            self.show_message_box("Please enter a valid name")
            self.set_status("Failed")
        elif address == "":
            self.show_message_box("Please enter a valid address")
            self.set_status("Failed")
        else:
            add = _database.add_branch(branch_name, address, established)
            if add == 1062:
                self.show_message_box(f"A branch with existing name and/or address has been recorded in the "
                                      f"database. [{branch_name}], [{address}]")
                self.set_status("Failed")
            elif add == 2013:
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                self.ui.branchname_addedit_it.clear()
                self.ui.address_addedit_it.clear()
                self.ui.established_addedit_it.setValue(0)
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")

    def set_branch_fields(self, index):
        try:
            self.ui.branchname_addedit_it.setText(self._branches_it[index][1])
            self.ui.address_addedit_it.setText(self._branches_it[index][2])
            self.ui.established_addedit_it.setValue(self._branches_it[index][3])
        except IndexError:
            pass

    def edit_branch(self):
        index = self.ui.selectbranch_it.currentIndex()
        if (self.ui.selectbranch_it.currentText() != self.ui.branchname_addedit_it.text() or
                self.ui.address_addedit_it.toPlainText() != self._branches_it[index][-2] or
                int(self.ui.established_addedit_it.value()) != self._branches_it[index][-1]):
            if _database.edit_branch(self._branches_it[index][0],
                                     self.ui.branchname_addedit_it.text(),
                                     self.ui.address_addedit_it.toPlainText(),
                                     self.ui.established_addedit_it.value()) == 2013:
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")

    def delete_branch(self):
        self.set_status("Deleting branch...")
        index = self.ui.selectbranch_it.currentIndex()
        del_branch = _database.delete_branch(self._branches_it[index][0])
        if del_branch == 1451:
            self.show_message_box(f"Cannot delete branch as there are still some products left there. If you want "
                                  f"to delete this branch, make sure to remove any existing products that are still "
                                  f"registered in branch [{self._branches_it[index][1]}].")
            self.set_status("Failed")
        elif del_branch == 2013:
            self.show_message_box("Connection error. Please check your network connection and try again. "
                                  "If the problem still persists, restart the application.")
            self.set_status("Failed")
        else:
            self.show_message_box("Success!")
            self.set_widget(self.ui.it)
            self.set_status("OK")

    # IT SECTION - POSITION METHODS
    def position_it(self, index):
        self.set_status("Refreshing positions...")
        self.ui.selectpositionframe.hide()
        self.ui.newpositionnameframe.hide()
        self.ui.posdescframe_it.hide()
        self.ui.addpositionbt_it.hide()
        self.ui.editpositionbt_it.hide()
        self.ui.deletepositionbt_it.hide()
        if index == 0:
            self.ui.newpositionnameframe.show()
            self.ui.posdescframe_it.show()
            self.ui.addpositionbt_it.show()
        elif index == 1:
            self.ui.selectpositionframe.show()
            self.ui.newpositionnameframe.show()
            self.ui.posdescframe_it.show()
            self.ui.editpositionbt_it.show()
        else:
            self.ui.selectpositionframe.show()
            self.ui.deletepositionbt_it.show()
        self.set_status("OK")

    def position_fields(self, index):
        try:
            self.ui.newposname.setText(self._position[index][1])
            self.ui.positiondesc_it.setText(self._position[index][2])
        except IndexError:
            pass

    def add_position(self):
        self.set_status("Adding position...")
        position_name = self.ui.newposname.text().strip()
        pos_description = self.ui.positiondesc_it.toPlainText().strip()
        if position_name == "":
            self.show_message_box("Please enter a valid name")
        elif pos_description == "":
            self.show_message_box("Please enter a valid description")
        else:
            index_insert = -1
            for j, i in enumerate(self._position):
                if j == 0:
                    previous = i[0]
                else:
                    if previous + 1 != i[0]:
                        index_insert = previous + 1
                        break
                    else:
                        previous = i[0]
            if index_insert == -1:
                index_insert = len(self._position) + 1
            publish = _database.add_position(index_insert, position_name, pos_description)
            if publish == 1062:
                self.show_message_box(f"A branch with existing name and/or address has been recorded in the "
                                      f"database. [{position_name}]")
                self.set_status("Failed")
            elif publish == 2013:
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                self.ui.newposname.clear()
                self.ui.positionchoose.setCurrentIndex(0)
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")

    def edit_position(self):
        self.set_status("Editing position...")
        position_name = self.ui.newposname.text().strip()
        pos_description = self.ui.positiondesc_it.toPlainText().strip()
        if position_name == "":
            self.show_message_box("Please enter a valid name")
        elif pos_description == "":
            self.show_message_box("Please enter a valid description")
        else:
            update_pos = _database.edit_position(self._position[self.ui.selectposition.currentIndex()][0],
                                                 position_name, pos_description)
            if update_pos == 1062:
                self.show_message_box(f"A branch with existing name and/or address has been recorded in the "
                                      f"database. [{position_name}]")
                self.set_status("Failed")
            elif update_pos == 2013:
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                self.ui.newposname.clear()
                self.ui.positionchoose.setCurrentIndex(0)
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")

    def delete_position(self):
        self.set_status("Deleting position...")
        index = self.ui.selectposition.currentIndex()
        del_pos = _database.delete_position(self._position[index][0])
        if del_pos == 1451:
            self.show_message_box(f"Cannot delete position as there are still some employees with such position. "
                                  f"If you want to continue the delete process, make sure to remove any records "
                                  f"of employees with position [{self._position[index][1]}].")
            self.set_status("Failed")
        elif del_pos == 2013:
            self.show_message_box("Connection error. Please check your network connection and try again. "
                                  "If the problem still persists, restart the application.")
            self.set_status("Failed")
        else:
            self.show_message_box("Success!")
            self.set_widget(self.ui.it)
            self.set_status("OK")

    # IT SECTION - EMPLOYEE METHODS
    def employee_it(self, index):
        self.ui.employee_addedit_it.hide()
        self.ui.addemployeebtt_it.hide()
        self.ui.editemployeebtt_it.hide()
        self.ui.deleteemployeebtt_it.hide()
        self.ui.employeetableframe_editdel_it.hide()
        if index != 2:
            self.ui.employee_addedit_it.show()
            if index == 0:
                self.ui.addemployeebtt_it.show()
            elif index == 1:
                self.ui.editemployeebtt_it.show()
                self.ui.employeetableframe_editdel_it.show()
        else:
            self.ui.deleteemployeebtt_it.show()
            self.ui.employeetableframe_editdel_it.show()

    def show_pass_field(self, index):
        pos = self.ui.position_addedit_it.currentText()
        if pos == 'Manager' or pos == 'IT' or pos == 'CEO' or pos == 'Co-Founder':
            self.ui.loginpassframe_it.show()
        else:
            self.ui.loginpassframe_it.hide()

    def set_employee_fields(self, item: QTableWidgetItem):
        print(self._employee_list)
        print(item.text())
        self.ui.employeetable_editdelete_it.selectRow(item.row())
        for index, i in enumerate(self._branches_it):
            if i[1] == self._employee_list[item.row()][1]:
                self.ui.branchchoose_addedit_it.setCurrentIndex(index)
                break
        self.ui.firstname_addedit_it.setText(self._employee_list[item.row()][2])
        self.ui.lastname_addedit_it.setText(self._employee_list[item.row()][3])
        if self._employee_list[item.row()][4] == "Male":
            self.ui.gender_addedit_it.setCurrentIndex(0)
        else:
            self.ui.gender_addedit_it.setCurrentIndex(1)
        self.ui.born_addedit_it.setDate(QDate(self._employee_list[item.row()][5]))
        for index, j in enumerate(self._position):
            if j[-1] == self._employee_list[item.row()][6]:
                self.ui.position_addedit_it.setCurrentIndex(index)
                break
        self.ui.password_addedit_it.setText(_database.employee_pass(self._employee_list[item.row()][0])[0][0])
        self.ui.phonenumber_addedit_it.setText(str(self._employee_list[item.row()][-2]))
        self.ui.addressemp_addedit_it.setText(self._employee_list[item.row()][-3])
        print(self._employee_list[item.row()][-3])

    def filter_employee(self):
        search = self.ui.searchbox_it.text().lower()
        if search != self._previous_search:
            for index, term in enumerate(self._employee_list):
                emp_id = str(term[0])
                branch = term[1].lower()
                fname = term[2].lower()
                lname = term[3].lower()
                gender = term[4].lower()
                born = term[5].strftime("%m-%d-%Y")
                position = term[-4].lower()
                address = term[-3].lower()
                phone = str(term[-2])
                joined = term[-1].strftime("%m-%d-%Y")
                if (search in emp_id) or (search in branch) or (search in fname) or (search in lname) \
                        or (search in gender) or (search in born) or (search in position) \
                        or (search in address) or (search in phone) or (search in joined) or (search == ""):
                    self.ui.employeetable_editdelete_it.setRowHidden(index, False)
                else:
                    self.ui.employeetable_editdelete_it.setRowHidden(index, True)
            self._previous_search = search

    def get_employee_list(self):
        while self.ui.employeetable_editdelete_it.rowCount() > 0:
            self.ui.employeetable_editdelete_it.removeRow(0)

        employees = _database.employee_list('All')

        if employees != self._employee_list:
            self._employee_list = employees

        for employee in self._employee_list:
            row = self.ui.employeetable_editdelete_it.rowCount()
            self.ui.employeetable_editdelete_it.insertRow(row)

            for index, j in enumerate(employee):
                self.ui.employeetable_editdelete_it.setItem(row, index, QTableWidgetItem(str(j)))
        self.ui.employeecount_it.setText(f"Employee count: {self.ui.employeetable_editdelete_it.rowCount()}")

    def add_edit_employee(self, action: int):
        firstn = self.ui.firstname_addedit_it
        lastn = self.ui.lastname_addedit_it
        born = self.ui.born_addedit_it
        phone = self.ui.phonenumber_addedit_it
        addr = self.ui.addressemp_addedit_it
        passw = self.ui.password_addedit_it
        pos = self.ui.position_addedit_it.currentText()
        index = self.ui.employeetable_editdelete_it.currentRow()
        try:
            if firstn == "" or lastn == "" or addr == "":
                self.show_message_box("Please enter valid values in the fields above.")
            elif math.floor((datetime.date.today() - datetime.date(born.date().year(), born.date().month(),
                                                                   born.date().day())).days / 365) < 17:
                self.show_message_box("Employee age must be 17 or more.")
            elif int(phone.text()) < 1000:
                self.show_message_box("Phone number length cannot be shorter than 4 digits.")
            elif (pos == 'Manager' or pos == 'IT' or pos == 'CEO' or pos == 'Co-Founder') and passw == "":
                self.show_message_box(f"Please enter a pssword for the new {pos}")
            else:
                add_emp = edit_emp = 0
                if action == 1:  # add
                    self.set_status("Adding employee...")
                    add_emp = _database.add_employee(
                        self._branches_it[self.ui.branchchoose_addedit_it.currentIndex()][0],
                        firstn.text(), lastn.text(),
                        self.ui.gender_addedit_it.currentText(),
                        f'{born.date().year()}-{born.date().month()}-{born.date().day()}',
                        self._position[self.ui.position_addedit_it.currentIndex()][0],
                        addr.toPlainText(), int(phone.text()), passw.text()
                    )
                elif action == 2:  # edit
                    self.set_status("Editing employee...")
                    edit_emp = _database.edit_employee(
                        self._employee_list[index][0], firstn.text(), lastn.text(),
                        self.ui.gender_addedit_it.currentText(),
                        f'{born.date().year()}-{born.date().month()}-{born.date().day()}',
                        self._position[self.ui.position_addedit_it.currentIndex()][0],
                        addr.toPlainText(), int(phone.text()), passw.text()
                    )
                if add_emp == 2013 or edit_emp == 2013:
                    self.show_message_box("Connection error. Please check your network connection and try again. "
                                          "If the problem still persists, restart the application.")
                    self.set_status("Failed")
                else:
                    firstn.clear()
                    lastn.clear()
                    born.setDate(QDate(2000, 1, 1))
                    phone.clear()
                    addr.clear()
                    passw.clear()
                    self.ui.employeeactionchoose_it.setCurrentIndex(0)
                    self.ui.branchchoose_addedit_it.setCurrentIndex(0)
                    self.ui.position_addedit_it.setCurrentIndex(0)
                    self.ui.gender_addedit_it.setCurrentIndex(0)
                    self.show_message_box("Success!")
                    self.set_widget(self.ui.it)
                    self.set_status("OK")
        except ValueError:
            self.show_message_box("Please enter valid numbers.")

    def delete_employee(self):
        self.set_status("Deleting employee...")
        indexes = []
        employee_to_delete = []
        message = ""
        selected = self.ui.employeetable_editdelete_it.selectedItems()
        for item in selected:
            if item.row() not in indexes:
                indexes.append(item.row())
        for number, rows in enumerate(indexes):
            message += f"{number + 1}.\tName: {self._employee_list[rows][2]} {self._employee_list[rows][3]}\n\tPosition: {self._employee_list[rows][6]}\n\n"
            employee_to_delete.append(self._employee_list[rows][0])
        self._confirmation = QMessageBox()
        self._confirmation.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        # self._confirmation.setWindowIcon(self._app_icon)
        question = self._confirmation.question(self, 'CarSel Co., Ltd',
                                               f"Are you sure you want to delete these employees? Once executed, "
                                               f"it cannot be undone.\n\n{message}",
                                               self._confirmation.Yes | self._confirmation.No)
        if question == self._confirmation.Yes:
            delete = _database.delete_employee(employee_to_delete)
            if delete == 2013:
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                self.ui.employeeactionchoose_it.setCurrentIndex(0)
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")
        else:
            self.set_status("OK")
            pass

    # IT SECTION - MANUFACTURER METHODS
    def manufacturer_it(self, index):
        self.ui.selectmanufacturerframe.hide()
        self.ui.newmanufacturerframe.hide()
        self.ui.countryframe_it.hide()
        self.ui.yearframe_it.hide()
        self.ui.addmanufacturerbt.hide()
        self.ui.editmanufacturerbt.hide()
        self.ui.deletemanufacturerbt.hide()
        if index == 0:
            self.ui.newmanufacturerframe.show()
            self.ui.addmanufacturerbt.show()
            self.ui.countryframe_it.show()
            self.ui.yearframe_it.show()
        elif index == 1:
            self.ui.selectmanufacturerframe.show()
            self.ui.newmanufacturerframe.show()
            self.ui.countryframe_it.show()
            self.ui.yearframe_it.show()
            self.ui.editmanufacturerbt.show()
        else:
            self.ui.selectmanufacturerframe.show()
            self.ui.deletemanufacturerbt.show()

    def set_manufacturer_fields(self, index):
        try:
            self.ui.newmanufacturername.setText(self._manufacturer[index][1])
            self.ui.mcountry_it.setText(self._manufacturer[index][2])
            self.ui.yearestablished_it.setValue(self._manufacturer[index][3])
        except IndexError:
            pass

    def add_edit_manufacturer(self, action: int):
        manufacturer_name = self.ui.newmanufacturername
        country = self.ui.mcountry_it
        established = self.ui.yearestablished_it
        if manufacturer_name == "":
            self.show_message_box("Please enter a valid name")
        else:
            if action == 1:  # add
                self.set_status("Adding manufacturer...")
                add = _database.add_manufacturer(manufacturer_name.text(), country.text(), established.value())
                if add == 1062:
                    self.show_message_box(f"A manufacturer  with existing name and/or address has been recorded in the "
                                          f"database. [{manufacturer_name.text()}], [{country.text()}]")
                    self.set_status("Failed")
                elif add == 2013:
                    self.show_message_box("Connection error. Please check your network connection and try again. "
                                          "If the problem still persists, restart the application.")
                    self.set_status("Failed")

                else:
                    manufacturer_name.clear()
                    country.clear()
                    established.setValue(0)
                    self.show_message_box("Success!")
                    self.set_widget(self.ui.it)
                    self.set_status("OK")
            else:  # edit
                m_id = self._manufacturer[self.ui.selectmanufacturer.currentIndex()][0]
                edit = _database.edit_manufacturer(m_id, manufacturer_name.text(), country.text(), established.value())
                if edit == 1062:
                    self.show_message_box(f"A manufacturer with existing name has been recorded in the "
                                          f"database. [{manufacturer_name}]")
                    self.set_status("Failed")
                elif edit == 2013:
                    self.show_message_box("Connection error. Please check your network connection and try again. "
                                          "If the problem still persists, restart the application.")
                    self.set_status("Failed")
                else:
                    manufacturer_name.clear()
                    country.clear()
                    established.setValue(0)
                    self.ui.manufacturerchoose.setCurrentIndex(0)
                    self.show_message_box("Success!")
                    self.set_widget(self.ui.it)
                    self.set_status("OK")

    def delete_manufacturer(self):
        self.set_status("Deleting manufacturer...")
        index = self.ui.selectmanufacturer.currentIndex()
        m_id = self._manufacturer[index][0]
        delete = _database.delete_manufacturer(m_id)
        if delete == 1451:
            self.show_message_box(
                f"Cannot delete manufacturer as there are still some products with said manufacturer. "
                f"If you want to continue the delete process, make sure to remove any records "
                f"of products with manufacturer [{self._manufacturer[index][1]}].")
            self.set_status("Failed")
        elif delete == 2013:
            self.show_message_box("Connection error. Please check your network connection and try again. "
                                  "If the problem still persists, restart the application.")
            self.set_status("Failed")
        else:
            self.show_message_box("Success!")
            self.set_widget(self.ui.it)
            self.set_status("OK")

    # IT SECTION - CARTYPE METHODS
    def cartype_it(self, index):
        self.ui.selectcartypeframe.hide()
        self.ui.newcartypenameframe.hide()
        self.ui.inventedframe_it.hide()
        self.ui.addcartypebt.hide()
        self.ui.editcartypebt.hide()
        self.ui.deletecartypebt.hide()
        if index == 0:
            self.ui.newcartypenameframe.show()
            self.ui.inventedframe_it.show()
            self.ui.addcartypebt.show()
        elif index == 1:
            self.ui.selectcartypeframe.show()
            self.ui.newcartypenameframe.show()
            self.ui.inventedframe_it.show()
            self.ui.editcartypebt.show()
        else:
            self.ui.selectcartypeframe.show()
            self.ui.deletecartypebt.show()

    def set_cartype_fields(self, index):
        try:
            self.ui.newcartypename.setText(self._cartypes_it[index][1])
            self.ui.invented_it.setValue(self._cartypes_it[index][2])
        except IndexError:
            pass

    def add_edit_cartype(self, action: int):
        cartype_name = self.ui.newcartypename
        year_invented = self.ui.invented_it
        if cartype_name.text() == "":
            self.show_message_box("Please enter a valid name")
        elif year_invented.value() <= 0:
            self.show_message_box("Please enter a valid year")
        else:
            if action == 1:  # add
                self.set_status("Adding a new car type...")
                index_insert = -1
                for index, cartype in enumerate(self._cartypes_it):
                    if index == 0:
                        previous = cartype[0]
                    else:
                        if previous + 1 != cartype[0]:
                            index_insert = previous + 1
                            break
                        else:
                            previous = cartype[0]
                if index_insert == -1:
                    index_insert = len(self._cartypes_it) + 1
                add = _database.add_cartype(index_insert, cartype_name.text(), year_invented.value())
                if add == 1062:
                    self.show_message_box(f"A car type with existing name has been recorded in the "
                                          f"database. [{cartype_name.text()}]")
                    self.set_status("Failed")
                elif add == 2013:
                    self.show_message_box("Connection error. Please check your network connection and try again. "
                                          "If the problem still persists, restart the application.")
                    self.set_status("Failed")
                else:
                    cartype_name.clear()
                    year_invented.setValue(0)
                    self.show_message_box("Success!")
                    self.set_widget(self.ui.it)
                    self.set_status("OK")
            else:  # edit
                self.set_status("Editing car type...")
                index = self.ui.selectcartype.currentIndex()
                type_id = self._cartypes_it[index][0]
                edit = _database.edit_cartype(type_id, cartype_name.text(), year_invented.value())
                if edit == 1062:
                    self.show_message_box(f"A car type with existing name has been recorded in the "
                                          f"database. [{cartype_name.text()}]")
                    self.set_status("Failed")
                elif edit == 2013:
                    self.show_message_box("Connection error. Please check your network connection and try again. "
                                          "If the problem still persists, restart the application.")
                    self.set_status("Failed")
                else:
                    cartype_name.clear()
                    self.ui.cartypechoose.setCurrentIndex(0)
                    self.show_message_box("Success!")
                    self.set_widget(self.ui.it)
                    self.set_status("OK")

    def delete_cartype(self):
        self.set_status("Deleting car type...")
        index = self.ui.selectcartype.currentIndex()
        m_id = self._cartypes_it[index][0]
        delete = _database.delete_cartype(m_id)
        if delete == 1451:
            self.show_message_box(
                f"Cannot delete car type as there are still some products associated with said type. "
                f"If you want to continue the delete process, make sure to remove any records "
                f"of products with type [{self._cartypes_it[index][1]}].")
            self.set_status("Failed")
        elif delete == 2013:
            self.show_message_box("Connection error. Please check your network connection and try again. "
                                  "If the problem still persists, restart the application.")
            self.set_status("Failed")
        else:
            self.show_message_box("Success!")
            self.set_widget(self.ui.it)
            self.set_status("OK")

    # IT SECTION - PRODUCT METHODS
    def product_it(self, index):
        self.ui.productframe_it.hide()
        self.ui.addproduct_it.hide()
        self.ui.editproduct_it.hide()
        self.ui.deleteproduct_it.hide()
        self.ui.producttableframe_it.hide()
        if index != 2:
            self.ui.productframe_it.show()
            if index == 0:
                self.ui.addproduct_it.show()
            elif index == 1:
                self.ui.editproduct_it.show()
                self.ui.producttableframe_it.show()
        else:
            self.ui.producttableframe_it.show()
            self.ui.deleteproduct_it.show()

    def set_product_field(self, item: QTableWidgetItem):
        print(self._product_list)
        self.ui.producttable_editdelete_it_2.selectRow(item.row())
        self.ui.carname.setText(self._product_list[item.row()][4])
        for index, manufacturer in enumerate(self._manufacturer):
            if manufacturer[1] == self._product_list[item.row()][1]:
                self.ui.manufacturerchooseproduct.setCurrentIndex(index)
                break
        for index, branch in enumerate(self._branches_it):
            if branch[1] == self._product_list[item.row()][2]:
                self.ui.branchchooseproduct.setCurrentIndex(index)
                break
        for index, cartype in enumerate(self._cartypes_it):
            if cartype[1] == self._product_list[item.row()][3]:
                self.ui.cartypechooseproduct.setCurrentIndex(index)
                break
        self.ui.yeareleased.setValue(self._product_list[item.row()][5])
        self.ui.topspeed.setValue(self._product_list[item.row()][6])
        self.ui.horsepower.setValue(self._product_list[item.row()][-6])
        self.ui.seatcount.setValue(self._product_list[item.row()][-5])
        self.ui.length.setValue(self._product_list[item.row()][-4])
        self.ui.width.setValue(self._product_list[item.row()][-3])
        self.ui.price.setValue(self._product_list[item.row()][-1])

    def filter_product(self):
        search = self.ui.searchproductfield_2.text().lower()
        if search != self._previous_product_search:
            for index, term in enumerate(self._product_list):
                carid = str(term[0])
                manufacturer = term[1].lower()
                branch = term[2].lower()
                cartype = term[3].lower()
                name = term[4].lower()
                year = str(term[5])
                topspeed = str(term[6])
                hp = str(term[-6])
                seatcount = str(term[-5])
                length = str(term[-4])
                width = str(term[-3])
                added = str(term[-2].strftime("%m-%d-%Y"))
                price = str(term[-1])
                if (search in carid) or (search in manufacturer) or (search in branch) or (search in cartype) \
                        or (search in name) or (search in year) or (search in topspeed) or (search in hp) \
                        or (search in seatcount) or (search in length) or (search in width) or (search in added) \
                        or (search in price) or (search == ""):
                    self.ui.producttable_editdelete_it_2.setRowHidden(index, False)
                else:
                    self.ui.producttable_editdelete_it_2.setRowHidden(index, True)
            self._previous_product_search = search

    def get_product_list(self):
        while self.ui.producttable_editdelete_it_2.rowCount() > 0:
            self.ui.producttable_editdelete_it_2.removeRow(0)

        products = _database.car_list('All')

        if products != self._product_list:
            self._product_list = products

        for product in self._product_list:
            row = self.ui.producttable_editdelete_it_2.rowCount()
            self.ui.producttable_editdelete_it_2.insertRow(row)

            for index, j in enumerate(product):
                self.ui.producttable_editdelete_it_2.setItem(row, index, QTableWidgetItem(str(j)))
        self.ui.productcount_it.setText(f"Products count: {self.ui.producttable_editdelete_it_2.rowCount()}")

    def add_edit_product(self, action: int):
        name = self.ui.carname
        manufacturer = self.ui.manufacturerchooseproduct
        branch = self.ui.branchchooseproduct
        cartype = self.ui.cartypechooseproduct
        year = self.ui.yeareleased
        speed = self.ui.topspeed
        hp = self.ui.horsepower
        seat = self.ui.seatcount
        length = self.ui.length
        width = self.ui.width
        price = self.ui.price
        index = self.ui.producttable_editdelete_it_2.currentRow()
        print(year.value(), speed.value(), hp.value(), seat.value(), length.value(), width.value(), price.value())
        if name.text() == "" \
                or 0.0 in (year.value(), speed.value(), hp.value(), seat.value(),
                           length.value(), width.value(), price.value()):
            self.show_message_box("Please enter valid values in the fields above.")
        elif year.value() < 1886:
            self.show_message_box("Please enter a valid year (cars were first invented in 1886, duh).")
        else:
            add = edit = 0
            if action == 1:  # add
                self.set_status("Adding a new product...")
                add = _database.add_product(
                    self._manufacturer[manufacturer.currentIndex()][0],
                    self._branches_it[branch.currentIndex()][0],
                    self._cartypes_it[cartype.currentIndex()][0], name.text(), year.value(),
                    speed.value(), hp.value(), seat.value(), length.value(),
                    width.value(), price.value())
            elif action == 2:
                self.set_status("Editing product...")
                edit = _database.edit_product(
                    self._product_list[index][0], self._manufacturer[manufacturer.currentIndex()][0],
                    self._branches_it[branch.currentIndex()][0],
                    self._cartypes_it[cartype.currentIndex()][0], name.text(), year.value(),
                    speed.value(), hp.value(), seat.value(), length.value(),
                    width.value(), price.value())
            if 2013 in (add, edit):
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                name.clear()
                manufacturer.setCurrentIndex(0)
                branch.setCurrentIndex(0)
                cartype.setCurrentIndex(0)
                year.setValue(0)
                speed.setValue(0)
                hp.setValue(0)
                seat.setValue(0)
                length.setValue(0)
                width.setValue(0)
                price.setValue(0)
                self.ui.productchoose.setCurrentIndex(0)
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")

    def delete_product(self):
        self.set_status("Deleting product...")
        indexes = []
        products_to_delete = []
        message = ""
        selected = self.ui.producttable_editdelete_it_2.selectedItems()
        for product in selected:
            if product.row() not in indexes:
                indexes.append(product.row())
        for number, rows in enumerate(indexes):
            message += f"{number + 1}.\tCar Name: {self._product_list[rows][4]}\n" \
                       f"\tManufacturer: {self._product_list[rows][1]}\n" \
                       f"\tBranch: {self._product_list[rows][2]}\n"
            products_to_delete.append(self._product_list[rows][0])
        print(indexes)
        print(products_to_delete)
        self._confirmation = QMessageBox()
        self._confirmation.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)
        # self._confirmation.setWindowIcon(self._app_icon)
        question = self._confirmation.question(self, 'CarSel Co., Ltd',
                                               f"Are you sure you want to delete these products? Once executed, "
                                               f"it cannot be undone.\n\n{message}",
                                               self._confirmation.Yes | self._confirmation.No)
        if question == self._confirmation.Yes:
            delete = _database.delete_product(products_to_delete)
            if delete == 2013:
                self.show_message_box("Connection error. Please check your network connection and try again. "
                                      "If the problem still persists, restart the application.")
                self.set_status("Failed")
            else:
                self.ui.productchoose.setCurrentIndex(0)
                self.show_message_box("Success!")
                self.set_widget(self.ui.it)
                self.set_status("OK")
        else:
            self.set_status("OK")
            pass

    # DATABASE TESTING SECTION
    def test_set(self, index):
        self.ui.submitquerybranch.hide()
        self.ui.submitpositionquery_2.hide()
        self.ui.manufacturerquerybt_2.hide()
        self.ui.cartypequerybt_2.hide()
        self.ui.employeequerybt_2.hide()
        self.ui.productquerybt_2.hide()
        if index == 0:
            self.ui.submitquerybranch.show()
        elif index == 1:
            self.ui.submitpositionquery_2.show()
        elif index == 2:
            self.ui.manufacturerquerybt_2.show()
        elif index == 3:
            self.ui.cartypequerybt_2.show()
        elif index == 4:
            self.ui.employeequerybt_2.show()
        else:
            self.ui.productquerybt_2.show()

    def test_database(self):
        index = self.ui.selecttable_dbtest.currentIndex()
        if index == 0:
            branch = _database.retrieve_branch('test')
        elif index == 1:
            branch = _database.retrieve_position('test')
        elif index == 2:
            branch = _database.retrieve_manufacturer('test')
        elif index == 3:
            branch = _database.retrieve_cartype('test')
        elif index == 4:
            branch = _database.retrieve_employee_raw()
        else:
            branch = _database.retrieve_product_raw()
        names = [i[0] for i in branch.description]
        while self.ui.querytable.rowCount() > 0:
            self.ui.querytable.removeRow(0)
        self.ui.querytable.setColumnCount(len(names))
        self.ui.querytable.setHorizontalHeaderLabels(names)
        for items in branch:
            row = self.ui.querytable.rowCount()
            self.ui.querytable.insertRow(row)
            for index, store in enumerate(items):
                self.ui.querytable.setItem(row, index, QTableWidgetItem(str(store)))
        self.ui.itemcount_dbtest.setText(f"Item count in table: {self.ui.querytable.rowCount()}")

    # METHODS FOR GENERAL FUNCTIONS
    def retrieve_maintainers(self):
        self._maintainer_list = _database.retrieve_maintainers()
        self.ui.loginaschoose.clear()
        for maintainer in self._maintainer_list:
            self.ui.loginaschoose.addItems([f"{maintainer[2]} {maintainer[3]}"])

    def login(self):
        self.set_status("Logging in...")
        try:
            self._current_user = _database.login(self.ui.loginaschoose.currentText().split(sep=' '),
                                                 self.ui.password.text())
            print(self._current_user)
            self.set_widget(self.ui.profile)
            self.ui.loginaschoose.setCurrentIndex(0)
            self.ui.password.clear()
            if self._current_user[0][-2] == 'CEO' or self._current_user[0][-2] == 'Co-Founder':
                self._grant_all = True
                self._grant_manager = True
                self._grant_it = True
                self._grant_db = True
            elif self._current_user[0][-2] == 'Manager':
                self._grant_all = False
                self._grant_manager = True
                self._grant_it = False
                self._grant_db = False
            else:
                self._grant_all = False
                self._grant_manager = False
                self._grant_it = True
                self._grant_db = True
            self.set_status("OK")
        except database.InvalidCredentialsError:
            self.show_message_box("Wrong password, please try loggin in again")
            self.set_status("Failed")

    def logout(self):
        self.set_status("Logging out...")
        self._current_user = None
        _database.logout()
        self.set_widget(self.ui.login)
        self.set_status("OK")

    def check_access(self, button: object):
        self.set_status("Checking access...")
        button_name = str(button)[str(button).find('"'):str(button).rfind(')')].replace('"', '')
        if button_name == 'managersectionbutton':
            if self._grant_manager or self._grant_all:
                self.set_widget(self.ui.manager)
                self.set_status("OK")
            else:
                self.show_message_box("You do not have the permission to view this section: Manager Section")
                self.set_status("Failed")
        elif button_name == 'itsectionbutton':
            if self._grant_it or self._grant_all:
                self.set_widget(self.ui.it)
                self.set_status("OK")
            else:
                self.show_message_box("You do not have the permission to view this section: IT Section")
                self.set_status("Failed")
        elif button_name == 'dbtestbutton_profile':
            if self._grant_db or self._grant_all:
                self.set_widget(self.ui.databasetest)
                self.set_status("OK")
            else:
                self.show_message_box("You do not have the permission to view this section: Database Testing Section")
                self.set_status("Failed")

    def set_widget(self, widget: object):
        widget_name = str(widget)[str(widget).find('"'):str(widget).rfind(')')].replace('"', '')
        if widget_name == 'manager':
            self.refresh_branch()
            self.refresh_cartype()
            self.refresh_manufacturer()
            self.refresh_position_it()
            self.ui.stackedWidget.setCurrentWidget(widget)

        elif widget_name == 'login':
            self.retrieve_maintainers()
            self.ui.loginaschoose.setCurrentIndex(0)
            self.ui.password.clear()
            self.ui.stackedWidget.setCurrentWidget(widget)

        elif widget_name == 'it':
            self.branch_it(0)
            self.position_it(0)
            self.employee_it(0)
            self.manufacturer_it(0)
            self.cartype_it(0)
            self.product_it(0)
            self.refresh_branch_it()
            self.refresh_cartype_it()
            self.refresh_position_it()
            self.refresh_manufacturer()
            self.ui.newmanufacturername.clear()
            self.ui.mcountry_it.clear()
            self.ui.yearestablished_it.setValue(0)
            self.ui.newposname.clear()
            self.ui.positiondesc_it.clear()
            self.ui.stackedWidget.setCurrentWidget(widget)

        elif widget_name == 'profile':
            self.ui.employeename_profile.setText(f"{self._current_user[0][2]} {self._current_user[0][3]}")
            self.ui.position_profile.setText(self._current_user[0][-2])
            self.ui.stackedWidget.setCurrentWidget(widget)

        elif widget_name == 'databasetest':
            self.test_set(0)
            self.ui.stackedWidget.setCurrentWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("CarSel Co., Ltd.")
    sys.exit(app.exec_())
