import mysql.connector
import bcrypt
import threading
import time


class InvalidCredentialsError(Exception):
    pass


class NoUserFoundError(Exception):
    pass


class UserExistError(Exception):
    pass


class UsernameExistError(Exception):
    pass


class DatabaseCarSel:
    def __init__(self):
        self._mydb = mysql.connector.connect(host='103.82.242.16', port='5555', user='karel', passwd='32373')
        self._mydb.autocommit = True
        self._cursor = self._mydb.cursor(buffered=True)
        self._cursor.execute('use carsel')
        self._current_user = None

    def refresh(self):
        if not self._mydb.is_connected():
            self._mydb = mysql.connector.connect(host='103.82.242.16', port='5555', user='karel', passwd='32373')
            self._mydb.autocommit = True
            self._cursor = self._mydb.cursor(buffered=True)
            self._cursor.execute('use carsel')

    # RETRIEVING METHODS
    def retrieve_position(self, action='default'):
        self.refresh()
        self._cursor.execute("select * from Role order by role")
        if action == 'default':
            return list(self._cursor)
        else:
            return self._cursor

    def retrieve_manufacturer(self, action='default'):
        self.refresh()
        self._cursor.execute("select * from Manufacturer")
        if action == 'default':
            return list(self._cursor)
        else:
            return self._cursor

    def retrieve_employee_raw(self):
        self.refresh()
        self._cursor.execute("select * from Employee;")
        return self._cursor

    def retrieve_product_raw(self):
        self.refresh()
        self._cursor.execute("select * from Car")
        return self._cursor

    def retrieve_cartype(self, action='default'):
        self.refresh()
        self._cursor.execute("select * from CarType")
        if action == 'default':
            return list(self._cursor)
        else:
            return self._cursor

    def retrieve_branch(self, source='default'):
        self.refresh()
        self._cursor.execute("select * from Branch")
        if source == 'default':
            return list(self._cursor)
        else:
            return self._cursor

    # BRANCH METHODS
    def add_branch(self, branch_name: str, address: str, established: int):
        self.refresh()
        try:
            self._cursor.execute(f"insert into Branch(branchName, address, established) "
                                 f"values ('{branch_name}', '{address}', {established})")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def edit_branch(self, branch_id: int, branch_name: str, address: str, established: int):
        self.refresh()
        try:
            self._cursor.execute(
                f"update Branch set branchName = '{branch_name}', address = '{address}', established = {established} where branchID = {branch_id}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def delete_branch(self, branch_id: int):
        self.refresh()
        try:
            self._cursor.execute(f"delete from Branch where branchID = {branch_id}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def get_branch_by_name(self, branch_name: str):
        self._cursor.execute(f"select * from Branch where branchName={branch_name}")
        return list(self._cursor)

    def get_branch_by_id(self, branch_id: int):
        self._cursor.execute(f"select * from Branch where branchID={branch_id}")
        return list(self._cursor)

    # POSITION METHODS
    def add_position(self, index: int, branch_name: str):
        self.refresh()
        try:
            self._cursor.execute(f"insert into Role(role, roleName) values ({index}, '{branch_name}')")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def edit_position(self, role_id: int, role_name: str):
        self.refresh()
        try:
            self._cursor.execute(f"update Role set roleName='{role_name}' where role={role_id}")
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def delete_position(self, role_id: int):
        self.refresh()
        try:
            self._cursor.execute(f"delete from Role where role={role_id}")
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    # MANUFACTURER METHOD
    def add_manufacturer(self, manufacturer_name: str, country: str, established: int):
        self.refresh()
        try:
            self._cursor.execute(f"insert into Manufacturer(manufacturerName, country, established) "
                                 f"values "
                                 f"('{manufacturer_name}', '{country}', {established})")
            self._mydb.commit()
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def edit_manufacturer(self, m_id: int, manufacturer_name: str, country: str, established: int):
        self.refresh()
        try:
            self._cursor.execute(f"update Manufacturer set manufacturerName='{manufacturer_name}', "
                                 f"country='{country}', established={established} where "
                                 f"manufacturerID={m_id}")
            self._mydb.commit()
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def delete_manufacturer(self, manufacturer_id: int):
        self.refresh()
        try:
            self._cursor.execute(f"delete from Manufacturer where manufacturerID={manufacturer_id}")
            self._mydb.commit()
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    # CARTYPE METHODS
    def add_cartype(self, type_id: int, cartype_name: str):
        self.refresh()
        try:
            self._cursor.execute(f"insert into CarType(carType, typeName) "
                                 f"values ({type_id}, '{cartype_name}')")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def edit_cartype(self, type_id: int, cartype_name: str):
        self.refresh()
        try:
            self._cursor.execute(f"update CarType set typeName='{cartype_name}' where carType={type_id}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def delete_cartype(self, type_id: int):
        self.refresh()
        try:
            self._cursor.execute(f"delete from CarType where carType={type_id}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    # PRODUCT METHODS
    def add_product(self, manufacturer: int, branch: int, cartype: int, carname: str, year: int, topspeed: int,
                    horsepower: int, seatcount: int, length: float, width: float, price: float):
        self.refresh()
        try:
            self._cursor.execute(f"insert into Car(manufacturer, branch, carType, carName, yearReleased, topSpeed, "
                                 f"horsePower, seatCount, length, width, dateAdded, price) "
                                 f"values "
                                 f"({manufacturer}, {branch}, {cartype}, '{carname}', {year}, {topspeed}, "
                                 f"{horsepower}, {seatcount}, {length}, {width}, curdate(), {price})")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def edit_product(self, carid: int, manufacturer: int, branch: int, cartype: int, carname: str, year: int,
                     topspeed: int,
                     horsepower: int, seatcount: int, length: float, width: float, price: float):
        self.refresh()
        try:
            self._cursor.execute(f"update Car set manufacturer={manufacturer}, branch={branch}, carType={cartype}, "
                                 f"carName='{carname}', yearReleased={year}, topSpeed={topspeed}, "
                                 f"horsePower={horsepower}, seatCount={seatcount}, length={length}, "
                                 f"width={width}, price={price} where carID={carid}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def delete_product(self, carid: list):
        self.refresh()
        try:
            for ids in carid:
                self._cursor.execute(f"delete from Car where carID={ids}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            self._mydb.rollback()
            print(e)
            return e.errno

    # EMPLOYEE METHODS
    def employee_list(self, branch_name: str):
        if branch_name != "All":
            # self._cursor.execute(f"select * from Employee where branchID={branch_id}")
            self._cursor.execute(f"select "
                                 f"E.employeeID, "
                                 f"(select branchName from Branch where E.branchID = Branch.branchID), "
                                 f"E.firstName, "
                                 f"E.lastName, "
                                 f"E.gender, "
                                 f"E.born, "
                                 f"(select roleName from Role where E.role = Role.role) as role, "
                                 f"E.address, "
                                 f"E.phoneNo, "
                                 f"E.dateJoined "
                                 f"from Employee E "
                                 f"where (select branchName from Branch where E.branchID = Branch.branchID) = '{branch_name}'")
        else:
            self._cursor.execute("select "
                                 "E.employeeID, "
                                 "(select branchName from Branch where E.branchID=Branch.branchID), "
                                 "E.firstName, "
                                 "E.lastName, "
                                 "E.gender, "
                                 "E.born, "
                                 "(select roleName from Role where E.role=Role.role) as role, "
                                 "E.address, "
                                 "E.phoneNo, "
                                 "E.dateJoined "
                                 "from "
                                 "Employee E")
            # self._cursor.execute("select * from Employee")
        return list(self._cursor)

    def employee_pass(self, employee_id: int):
        self._cursor.execute(f"select password from Employee where employeeID={employee_id}")
        return list(self._cursor)

    def add_employee(self, branch: int, f_name: str, l_name: str, gender: str, born: str, position: int, address: str,
                     phone: int, password: str):
        try:
            self._cursor.execute(f"insert into Employee(branchID, firstName, lastName, gender, born, role, "
                                 f"address, phoneNo, dateJoined, password) "
                                 f"values "
                                 f"({branch}, '{f_name}', '{l_name}', '{gender}', '{born}', {position}, '{address}', {phone}, curdate(), '{password}')")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def edit_employee(self, employee_id: int, f_name: str, l_name: str, gender: str, born: str, position: int,
                      address: str, phone: int, password: str):
        try:
            self._cursor.execute(
                f"update Employee set firstName='{f_name}', lastName='{l_name}', gender='{gender}', born='{born}', "
                f"role={position}, address='{address}', phoneNo={phone}, password='{password}' "
                f"where employeeID={employee_id}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return e.errno

    def delete_employee(self, employee_to_delete: list):  # employee_id: int):
        # try:
        #     self._cursor.execute(f"delete from Employee where employeeID={employee_id}")
        #     self._mydb.commit()
        #     return True
        # except mysql.connector.Error as e:
        #     print(e)
        #     return e.errno
        # delete = ""
        try:
            # for index, employee in enumerate(employee_to_delete):
            #     if index == len(employee_to_delete)-1:
            #         delete += f"delete from Employee where employeeID={employee};"
            #     else:
            #         delete += f"delete from Employee where employeeID={employee};\n"
            # print(delete)
            for employee in employee_to_delete:
                self._cursor.execute(f"delete from Employee where employeeID={employee}")
            self._mydb.commit()
            return True
        except mysql.connector.Error as e:
            self._mydb.rollback()
            print(e)
            return e.errno

    # MANAGER SECTION METHODS
    def car_list(self, branch_name: str):
        if branch_name != "All":
            self._cursor.execute(f"select "
                                 f"car.carID, "
                                 f"(select manufacturerName from Manufacturer where car.manufacturer = Manufacturer.manufacturerID) as manufacturer, "
                                 f"(select branchName from Branch where car.branch = Branch.branchID) as branch, "
                                 f"(select typeName from CarType where car.carType = CarType.carType) as carType, "
                                 f"car.carName, "
                                 f"car.yearReleased, "
                                 f"car.topSpeed, "
                                 f"car.horsePower, "
                                 f"car.seatCount, "
                                 f"car.length, "
                                 f"car.width, "
                                 f"car.dateAdded, "
                                 f"car.price "
                                 f"from Car car "
                                 f"where (select branchName from Branch where car.branch = Branch.branchID) = '{branch_name}'")
        else:
            self._cursor.execute(f"select "
                                 f"car.carID, "
                                 f"(select manufacturerName from Manufacturer where car.manufacturer = Manufacturer.manufacturerID) as manufacturer, "
                                 f"(select branchName from Branch where car.branch = Branch.branchID) as branch, "
                                 f"(select typeName from CarType where car.carType = CarType.carType) as carType, "
                                 f"car.carName, "
                                 f"car.yearReleased, "
                                 f"car.topSpeed, "
                                 f"car.horsePower, "
                                 f"car.seatCount, "
                                 f"car.length, "
                                 f"car.width, "
                                 f"car.dateAdded, "
                                 f"car.price "
                                 f"from Car car")
        return list(self._cursor)

    def retrieve_type(self):
        self._cursor.execute("select * from CarType")
        return list(self._cursor)

    def update_password(self, user_id: int, hashed_password: str):
        try:
            self._cursor.execute(f"update Users set password='{hashed_password}' where userID={user_id}")
            self._mydb.commit()
            return True
        except:
            return False

    def get_password(self, useremail: str):
        self._cursor.execute(f"select password from Users where userName='{useremail}' or email='{useremail}'")
        self._mydb.commit()
        return self._cursor

    def register(self, username: str, email: str, firstname: str, lastname: str, password: str):
        self._cursor.execute(f"select * from Users where email='{email}'")
        if len(list(self._cursor)) == 0:
            self._cursor.execute(f"select * from Users where userName='{username.lower()}'")
            if len(list(self._cursor)) == 0:
                hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8')
                self._cursor.execute(
                    f"insert into Users(userName, email, firstName, lastName, dateRegistered, password)"
                    f"values ('{username}', '{email}', '{firstname}', '{lastname}', CURDATE(), '{hashed_pw}')")
                self._mydb.commit()
                return True
            else:
                raise UsernameExistError()
        else:
            raise UserExistError()

    def retrieve_maintainers(self):
        self._cursor.execute("select * from Employee where password is not null")
        return list(self._cursor)

    def login(self, name: list, password: str):
        self._cursor.execute(f"select "
                             f"E.employeeID, "
                             f"(select branchName from Branch where E.branchID=Branch.branchID), "
                             f"E.firstName, "
                             f"E.lastName, "
                             f"(select roleName from Role where E.role=Role.role) as role, "
                             f"E.password "
                             f"from Employee E "
                             f"where E.firstName='{name[0]}' and E.lastName='{name[1]}' and E.password is not null")
        user = list(self._cursor)
        print(user)
        if len(user) > 1:
            for maintainer in user:
                if maintainer[-1] == password:
                    return user
        else:
            if user[0][-1] == password:
                return user
            else:
                raise InvalidCredentialsError
        raise InvalidCredentialsError

    def logout(self):
        self._current_user = None
        return True
