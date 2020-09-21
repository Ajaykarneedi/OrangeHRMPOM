from pages.PageJobtitles import Jobtitles


class OperationsAdmin:
    def __init__(self, driver):
        self.driver = driver


    def Add_Jobtitle(self):

        driver = self.driver
        jt = Jobtitles(driver)
        jt.clkAdd()
        jt.set_Jobtitle("Tester")
        jt.UploadFile("C:\\Users\\akash\\PycharmProjects\\pythonProject\\OrangeHRMPOM\\Data\\JobAtachment.txt")