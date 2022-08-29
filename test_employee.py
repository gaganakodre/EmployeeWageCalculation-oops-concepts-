import employeewage_json_pickel


def test_check_attendence():
    actuall=employeewage_json_pickel.Employee.check_attendance(rand=0)
    assert actuall==8
