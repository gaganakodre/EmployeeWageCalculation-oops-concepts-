from employeewage_json_pickel import Employee, Company


def test_check_attendence_for_fullday():
    emp = Employee("shree", "Hr", 10, 20, 30)
    attendence = emp.check_attendance(0)
    assert attendence == 8


def test_check_attendence_for_parttime():
    emp = Employee("shree", "Hr", 10, 20, 30)
    attendence = emp.check_attendance(1)
    assert attendence == 4


def test_add_employee():
    company = Company("tata")
    employee_dict = {"name": "shree", "department": "HR", "wage_per_hour": 20, "monthly_working_day": 20,
                     "total_working_hour": 100}
    employee = Employee(**employee_dict)
    assert len(company) == 0
    company.add_employee(employee)
    assert len(company) == 1


def test_update_employee():
    company = Company("tata")
    employee = Employee("shree", "HR", 10, 20, 30)
    company.add_employee(employee)
    company.update_employee("shree", "hr")
    assert employee.name == "shree"
    assert employee.department == "hr"


def test_delete_employee():
    company = Company("tata")
    employee_dict = {"name": "shree", "department": "HR", "wage_per_hour": 20, "monthly_working_day": 20,
                     "total_working_hour": 100}
    employee = Employee(**employee_dict)
    company.add_employee(employee)
    company.delete_employee(employee.name)
    assert len(company) == 0



