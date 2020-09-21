
class Jobtitles():

    def __init__(self, driver):
        self.driver =  driver
        self.btn_Add_Id = "btnAdd"
        self.txt_JobTitle_Id = "jobTitle_jobTitle"
        self.btn_Fileupload_Id = "jobTitle_jobSpec"

    def set_Jobtitle(self, Jobtitle):
        self.driver.find_element_by_id(self.txt_JobTitle_Id).clear()
        self.driver.find_element_by_id(self.txt_JobTitle_Id).send_keys(Jobtitle)

    def UploadFile(self, FileToUpload):
        self.driver.find_element_by_id(self.btn_Fileupload_Id).clear()
        self.driver.find_element_by_id(self.btn_Fileupload_Id).send_keys(FileToUpload)

    def clkAdd(self):
        self.driver.find_element_by_id(self.btn_Add_Id).click()
