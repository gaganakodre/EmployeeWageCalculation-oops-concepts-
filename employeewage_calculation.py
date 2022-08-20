import random
import logging

logging.basicConfig(filename='employee_wage.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Employee:
    def employee_wage(self):
        try:
            emp_check = random.randint(0, 2)
            if emp_check == 1:
                logging.debug('employee present')
            else:
                logging.debug('employee absent')
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    employee=Employee()
    employee.employee_wage()