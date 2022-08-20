import random
import logging

logging.basicConfig(filename='employee.log', level='DEBUG', format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


class Employee:
    def __init__(self, total_hr, daily_wage, max_working_hr, max_working_days):
        self.total_hr = total_hr
        self.daily_wage = daily_wage
        self.max_working_hr = max_working_hr
        self.max_working_days = max_working_days

    def employee_wage(self, monthly_wage=0):
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
                # logging.debug("dailywage: {}".format(self.daily_Wage))
                monthly_wage +=self.daily_Wage #self.daily_Wage
                self.max_working_days+=1
                self.max_working_hr+=1
            logging.debug('monthly wage: {}'.format(monthly_wage))
        except Exception as e:
            logging.error(e)
        finally:
            print("closed")


if __name__ == '__main__':
    employee = Employee(0, 0, 0, 0)
    employee.employee_wage()
