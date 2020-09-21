from selenium import webdriver
import time
import unittest
import sys
from pages.PageHome import HomePage
from common.CommonMethods import commonMethods
from Operations.OpAdmin import OperationsAdmin
from pages.PageJobtitles import Jobtitles
from pages.PageApplyLeave import ApplyLeave
from selenium.webdriver.common.action_chains import ActionChains
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'E:\Selenium Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(2)
        cls.actions = ActionChains(cls.driver)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

    def test_loginTest(self):
        driver = self.driver
        actions = self.actions
        select = Select

        cm = commonMethods(driver, actions)
        cm.login()
        print("Before Try: ", datetime.now())

        cm.navigatetoApplyLeave()

        al = ApplyLeave(driver, select)

        al.SelectLeaveType()
        leaveBal = self.driver.find_element_by_id("applyleave_leaveBalance").text[0:4]

        # time.sleep(15)
        self.assertEqual('9.50', leaveBal)


        #element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "spanMessage")))
        # assertion
        #self.assertNotEqual("Invalid Logincredentials", element.text)
        #self.assertNotEqual(20*2, 40)


        # Exception Handling
        # try:
        #     # Explicit Wait
        #     element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "spanMessage")))
        #     # assertion
        #     self.assertEqual("Invalid Logincredentials", element.text)
        #     print("Try: ", datetime.now())
        # except Exception as e:
        #     # assertion
        #     #self.assertEqual("Dashboard", driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text)
        #     print("Except: ", datetime.now())
        #     print(e)
        # finally:
        #     print("Will Execute always")
        #     print("Finally: ", datetime.now())

        #cm.navigatetoAddEmployee()
        # cm.navigatetoJobtitle()
        #
        # OA = OperationsAdmin(driver)
        # OA.Add_Jobtitle()
        #
        #
        # time.sleep(15)
        #
        # homepage = HomePage(driver)
        # homepage.clkwelcome()
        # homepage.clklogout()


        time.sleep(2)


if __name__ == "__main__":
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'))
