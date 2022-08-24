import logging
import random

logging.basicConfig(filename='employee_company.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')



class Employee:
    def __init__(self, name, department, wage_per_hour, monthly_working_day, total_working_hour):
        self.name = name
        self.department = department
        self.wage_per_hour = wage_per_hour
        self.monthly_working_day = monthly_working_day
        self.total_working_hour = total_working_hour

    def check_employee_status(self, check):
        """
        Function used to check weather the employee present absent or in part time
        """
        try:
            if check == 0:
                daily_work_hour = 8
            elif check == 1:
                daily_work_hour = 4
            else:
                daily_work_hour = 0
            return daily_work_hour
        except Exception as e:
            logging.error(e)

    @property
    def calculating_wage(self):
        """
        Function used to calculate the daily wage an monthly wage of employee
        """
        logging.debug("Employee wage program is running perfectly.....")
        try:
            monthly_wage = 0
            no_of_working_days = 0
            working_hours = 0
            while no_of_working_days < self.monthly_working_day and working_hours <= self.total_working_hour:
                no_of_working_days += 1
                check = random.randint(0, 3)
                daily_work_hour = self.check_employee_status(check)
                working_hours += daily_work_hour
                daily_wage = self.wage_per_hour * daily_work_hour
                monthly_wage += daily_wage
            return monthly_wage
        except Exception as e:
            logging.error(e)

    def display_as_dict(self):
        """
        Function used to display the values in the form of dictionary
        """
        try:
            return {"Name": self.name, "department": self.department, "monthly_wage": self.calculating_wage}
        except Exception as e:
            logging.error(e)
    def as_string(self):
        """
        Function to display the values in the form of string
        """
        try:
            return "{:<10} {:<10} {:<10}".format(self.name, self.department,self.calculating_wage)

        except Exception as e:
            logging.error(e)


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
            print(self.employee_dict)
        except Exception as e:
            logging.error(e)

    def update_employee(self, name_, name, department):
        try:
            employee = self.get_employee(name_)
            if not employee:
                logging.info("key is not present")
                return

            employee.name = name
            employee.department = department
            logging.debug("updated successfully")
        except Exception as e:
            logging.error(e)


    def get_employee(self, name):
        """
        Function used to get the employee name from dictionary
        :param employee_name: to get the employee name from the dictionary
        :return: employee object contain values
        """
        try:
            print(self.employee_dict.keys())
            # employee_obj = self.employee_dict.get(name)
            employee_obj = self.employee_dict.keys()
            return employee_obj

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


    def display_employee(self):
        """
        Function to display the employee details
        """
        try:
            print("{:<10} {:<10} {:<10}".format('name', 'department', 'salary'))
            for employee_obj in self.employee_dict.values():
                print(employee_obj.as_string())
        except Exception as e:
            logging.error(e)

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

def add_employee_with_company():
    """
    Function to add the employee with the company name
    """
    try:
        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            company_exist = Company(company_name)
            comp_dict.update({company_exist.name: company_exist})
            print("company does not exist")
        name = input("Enter employee name : ")
        department = input("enter the department: ")
        emp = Employee(name, department, 30, 20, 120)
        company_exist.add_employee(emp)
    except Exception as e:
        logging.error(e)


def update_employee_with_company():
    """
    Function to update or edit the employee details who are present
    """
    try:
        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            company_exist = Company(company_name)
            comp_dict.update({company_exist.name: company_exist})
        key=input("enter the name u want to update")
        name = input("Enter employee name : ")
        department = input("enter the department: ")
        company=Company(company_name)
        company.update_employee(key, name, department)
    except Exception as e:
        logging.error(e)


def get_employee():
    try:

        company_name = input("Enter company name : ")
        company_exist = comp_dict.get(company_name)
        if company_exist is None:
            # print()
            return "Company doesn't exit "
        employee_name = input("Enter employee name : ")
        employee=company_exist.get_employee(employee_name)
        if not employee:
            print("employee not exist")
            return
        print(employee.as_string())

    except Exception as e:
        logging.error(e)




def delete_employee_with_company():
    company_name = input("Enter company name : ")
    company_exist = comp_dict.get(company_name)
    if company_exist is None:
        print("Company doesn't exit")
        return
    emp_name = input("Enter employee name : ")
    company_exist.delete_employee(emp_name)


def display_employees_with_company():
    company_name = input("Enter company name : ")
    company_obj = comp_dict.get(company_name)
    if company_obj is None:
        print("Company doesn't exit ")
        return None
    company_obj.display_employee()


if __name__ == "__main__":
    try:
        comp_dict = {}
        while True:
            print("1.add_company\n2.Display Company\n3.Add Employee \n4.Delete "
                  "Employee\n5.display_employees\n6.update_employee\n0.Exit")
            dict_e = {1: add_company,
                      2: display_company,
                      3: add_employee_with_company,
                      4: delete_employee_with_company,
                      5: display_employees_with_company,
                      6: update_employee_with_company}

            choice = int(input("Enter a number : "))
            if choice == 0:
                break
            dict_e.get(choice)()
            input("Press enter to continue ")
            print("--------------------- Choose Option ----------------------")

    except Exception as e:
        logging.error(e)
