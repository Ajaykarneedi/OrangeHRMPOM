import time

class ApplyLeave:

    def __init__(self, driver, select):
        self.driver = driver
        self.Select = select
        self.select_LeaveType_Id = "applyleave_txtLeaveType"

    def  SelectLeaveType(self):
        sel = self.Select(self.driver.find_element_by_id('applyleave_txtLeaveType'))
        sel.select_by_value('2')
        time.sleep(3)


