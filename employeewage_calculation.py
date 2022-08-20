import random
import logging

logging.basicConfig(filename='employee_wage.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Employee:
    def __init__(self,total_hr):
        self.total_hr = total_hr

    def employee_wage(self):
        try:
            emp_check = random.randint(0, 2)
            if emp_check == 1:
                total_hr = 8
                logging.debug('employee present')
            elif emp_check == 2:
                total_hr = 4
                logging.debug('employee in part-time')
            else:
                total_hr = 0
                logging.debug('employee absent')
            dailyWage = int(20 * total_hr)
            logging.debug(dailyWage)
            logging.debug("dailywage: {}".format(dailyWage))
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    employee = Employee(0)
    employee.employee_wage()
