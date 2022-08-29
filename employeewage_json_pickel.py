import json
import logging
import random
import pickle

logging.basicConfig(filename='employee_wage.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
JSON_FILE = "new_employee_wage.json"
PICKEL_FILE = "employee_pickel.pkl"


class Employee:
    def __init__(self, name, department, wage_per_hour, monthly_working_day, total_working_hour):
        self.name = name
        self.department = department
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day
        self.total_working_hour = total_working_hour

    def check_attendance(self, rand):
        """
        Function used to check weather the employee present absent or in part time
        """
        try:
            if rand == 0:
                daily_work_hour = 8
            elif rand == 1:
                daily_work_hour = 4
            else:
                daily_work_hour = 0
            return daily_work_hour
        except Exception as e:
            logging.error(e)

    def calculating_wage(self):
        """
        Function used to calculate the daily wage an monthly wage of employee
        """
        try:
            total_wage = 0
            no_of_working_days = 0
            working_hours = 0
            while no_of_working_days < self.monthly_working_day and working_hours <= self.total_working_hour:
                no_of_working_days += 1
                rand = random.randint(0, 2)
                daily_work_hour = self.check_attendance(rand)
                working_hours += daily_work_hour
                daily_wage = self.wage_per_hour * daily_work_hour
                total_wage += daily_wage
            return total_wage
        except Exception as e:
            logging.error(e)

    def as_dict(self):
        """
        Function used to display the values in the form of dictionary
        """
        try:
            return {"employee": {"Name": self.name,"department":self.department, "Total_wage": self.calculating_wage()}}
        except Exception as e:
            logging.error(e)

    def as_string(self):
        """
        Function to display the values in the form of string
        """
        try:
            return "{:<10} {:<10} {:<10}".format(self.name, self.department, self.calculating_wage())
        except Exception as e:
            logging.error(e)

    def details_from_user(self):
        try:
            return self.name, self.department, self.calculating_wage()
        except Exception as e:
            logging.error(e)


class JsonOperation:

    @staticmethod
    def read():
        with open(JSON_FILE) as f:
            data = json.load(f)
            return data

    @staticmethod
    def write(data):
        with open(JSON_FILE, 'w') as f:
            json.dump(data, f, indent=4)


class Company:
    def __init__(self, name):
        self.name = name
        self.employee_dict = {}

    def add_employee(self, emp):
        """
        Function used to add the employee and storing in the dictionary called employee_dict
        """
        try:
            self.employee_dict.update({emp.name: emp})
            return self.employee_dict
        except Exception as e:
            logging.error(e)

    def update_employee(self, name, department):
        """
        Function to update the employee
        """
        try:
            employee_name = input("Enter employee name you want to update: ")
            employee_exist = self.employee_dict.get(employee_name)
            if not employee_exist:
                print("name not present")
                return
            employee_exist.name = name
            employee_exist.department = department
            return self.employee_dict
        except Exception as e:
            logging.error(e)

    def get_employee(self, employee_name):
        """
        Function used to get the employee name from dictionary
        :param employee_name: to get the employee name from the dictionary
        :return: employee object contain values
        """
        try:
            emp_obj = self.employee_dict.get(employee_name)
            return emp_obj
        except Exception as e:
            logging.error(e)

    def delete_employee(self, emp_name):
        """
       Function used to delete the particular employee
       :param emp_name: to get the employee name
       """
        try:
            if not self.get_employee(emp_name):
                print("name dosen't exist")
                return

            self.employee_dict.pop(emp_name)
        except Exception as e:
            logging.error(e)

    def employee_details_view(self):
        """
        Function to display the employee details
        """
        try:

            # print(self.employee_dict)
            print("{:<10} {:<10} {:<10}".format('name', 'department', 'salary'))
            for i in self.employee_dict:
                emp_obj = self.employee_dict.get(i)
                print(emp_obj.as_string())
        except Exception as e:
            logging.error(e)

    def display_as_json(self):
        try:
            json_obj = JsonOperation.read()
            print(json_obj)
        except Exception as e:
            print(e)

    def write_json(self):
        name = input("enter ur name: ")
        department = input("entre ur department : ")
        emp = Employee(name, department, 30, 20, 120)
        # json_str = emp.details_from_user()
        json_str = emp.as_dict()
        with open(JSON_FILE, 'w') as f:
            json.dump(json_str, f, indent=4)
        # json_str = json.dump({"employee": emp.details_from_user()})
        # JsonOperation.write(json_str)
        print("data stored in", JSON_FILE, "file")
        # print(json_str)

    def write_as_pickle(self):
        name = input("enter ur name: ")
        department = input("entre ur department : ")
        emp = Employee(name, department, 30, 20, 120)
        pickel_str = emp.details_from_user()
        with open(PICKEL_FILE, 'wb') as file:
            pickle.dump(pickel_str, file)

    # A new file will be created serialize

    def read_as_pickel(self):
        with open(PICKEL_FILE, 'rb') as file:
            myvar = pickle.load(file)

            print(myvar)


def write_pickel():
    company = input("Enter company name : ")
    company_obj = Company(company)
    company_obj.write_as_pickle()


def read_pickel():
    company = input("Enter company name : ")
    company_obj = Company(company)
    company_obj.read_as_pickel()


def add_company():
    """
    Function to add the employee with the company name
    :return: company_dictionary
    """
    try:
        company = input("Enter company name : ")
        company_obj = Company(company)
        comp_dict.update({company_obj.name: company_obj})
        return comp_dict
    except Exception as e:
        logging.error(e)


def display_company():
    """
    Function to display the company with employee details
    """
    try:
        print(comp_dict)
    except Exception as e:
        logging.error(e)


def add_employee():
    """
    Function to add the employee with the company name
    """
    try:
        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            company_exist = Company(company_name)
            comp_dict.update({company_exist.name: company_exist})
        name = input("Enter employee name : ")
        department = input("enter the department")
        emp = Employee(name, department, 30, 20, 120)
        company_exist.add_employee(emp)
    except Exception as e:
        logging.error(e)


def get_employee():
    """
    Function to get the employee
    """
    try:
        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            print("Company doesn't exit ")
            return
        employee_name = input("Enter employee name : ")
        company_exist.get_employee(employee_name)
    except Exception as e:
        logging.error(e)


def update_employee():
    """
    Function to update or edit the employee details who are present
    """
    try:
        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            company_exist = Company(company_name)
            comp_dict.update({company_exist.name: company_exist})
        name = input("Enter employee new name : ")
        department = input("enter the department")
        company_exist.update_employee(name, department)
    except Exception as e:
        logging.error(e)


def delete_employee():
    """
    Function to delete employee
    """
    try:
        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            print("Company doesn't exit ")
            return
        emp_name = input("Enter employee name : ")
        company_exist.delete_employee(emp_name)
    except Exception as e:
        logging.error(e)


def display_employees():
    """
    Function to display employee
    """
    try:
        company_name = input("Enter company name : ")
        company_obj = comp_dict.get(company_name)
        if company_obj is None:
            print("Company doesn't exit ")
            return
        company_obj.employee_details_view()
    except Exception as e:
        logging.error(e)


def write_json():
    company_name = input("enter the company name : ")
    company = Company(company_name)
    company.write_json()



if __name__ == "__main__":
    try:
        comp_dict = {}
        while True:
            print("1.add_company\n2.Display Company\n3.Add Employee \n4.Get Employee\n5.Delete "
                  "Employee\n6.display_employees\n7.update_employees\n8.json_form\n9.json\n10.write_pickel\n11.read_pickel\n0.Exit")
            dict_e = {1: add_company,
                      2: display_company,
                      3: add_employee,
                      4: get_employee,
                      5: delete_employee,
                      6: display_employees,
                      7: update_employee,
                      # 8: write_as_json,
                      9: write_json,
                      10: write_pickel,
                      11: read_pickel
                      }

            choice = int(input("Enter a number : "))
            if choice == 0:
                break
            dict_e.get(choice)()
            input("Press enter to continue ")
            print("--------------------- Choose Option ----------------------")

    except Exception as e:
        print(e)
