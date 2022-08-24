import random
import logging

logging.basicConfig(filename='employee.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Employee:

    def __init__(self, total_hr, daily_wage, max_working_hr, max_working_days, name, department, phone_number):
        self.total_hr = total_hr
        self.daily_wage = daily_wage
        self.max_working_hr = max_working_hr
        self.max_working_days = max_working_days
        self.name = name
        self.department = department
        self.phone_number = phone_number

    def calculate_wage(self, monthly_wage=0):
        try:
            while self.max_working_days <= 20 and self.max_working_hr <= 100:
                emp_check = random.randint(0, 2)
                if emp_check == 1:
                    self.total_hr = 8
                    # logging.debug('employee present')
                elif emp_check == 2:
                    self.total_hr = 4
                    # logging.debug('employee in part-time')
                else:
                    self.total_hr = 0
                    # logging.debug('employee absent')
                self.daily_Wage = int(20 * self.total_hr)
                monthly_wage += self.daily_Wage
                self.max_working_days += 1
                self.max_working_hr += 1
            logging.info('monthly wage: {}'.format(monthly_wage, ))
        except Exception as e:
            logging.error(e)
        finally:
            print("closed")

    def name(self):
        return self.name

    def details(self):
        """
        Function used to access the employee details
        :return: name,department,phone_number
        """
        return f"{self.name},{self.department},{self.phone_number}"


class Company:
    def __init__(self):
        self.employee_dict = {}

    def add_employee(self, employee):
        self.employee_dict.update({employee.name: employee})

    def update_employee(self, name_, name, department, phone_number):
        try:
            employee = self.get_contact(name_)
            if not employee:
                logging.info("key is not present")
                return

            employee.name = name
            employee.department = department
            employee.phone_number = phone_number
            logging.debug("updated successfully")
        except Exception as e:
            logging.error(e)

    def get_contact(self, name):
        """
        Function is used to get the name of the employee
        :param name:
        :return:
        """
        return self.employee_dict.get(name)

    def display_employee(self):
        # Iterate over all values of the dictionary
        for key, value in self.employee_dict.items():
            print(key, value.details())

    def delete_employee(self, name_):
        try:
            contact = self.get_contact(name_)
            if not contact:
                logging.debug("given name not exists")
                return
            self.employee_dict.pop(name_)

            logging.debug("contact deleted successfully")
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    company = Company()


    def choice1():
        print("enter ur name: ")
        name = input()
        print("enter ur department: ")
        department = input()
        print("enter ur phone number: ")
        phone_number = input()
        employee = Employee(0, 0, 0, 0, name, department, phone_number)
        company.add_employee(employee)


    def choice2():
        company.display_employee()


    def choice3():
        key = input("Enter key to check:")
        print("given name contact exists")
        print("Please enter the  name : ")
        name = input()
        print("Please enter the department : ")
        department = input()
        print("Please enter the phone_number : ")
        phone_number = input()
        company.update_employee(key, name, department, phone_number)


    def choice4():
        key = input("Enter key to check:")
        company.delete_employee(key)


    def default():
        print("Please choose correct option")


    switcher = {
        1: choice1,
        2: choice2,
        3: choice3,
        4: choice4,

    }
    while True:
        print("Enter the option : \n1)Add Contact \n2)Display contact\n3)update contact\n4)delete Contact")
        option = int(input())
        if option == 1:
            switcher.get(option)()

        elif option == 2:
            switcher.get(option)()

        elif option == 3:
            switcher.get(option)()

        elif option == 4:
            switcher.get(option)()

        else:
            default()
