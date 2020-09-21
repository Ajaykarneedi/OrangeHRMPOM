from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from datetime import datetime



cm = commonMethods(driver, actions)
cm.login()
print("Before Try: ", datetime.now())
# Exception Handling
try:
    #Explicit Wait
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "spanMessage")))
    # assertion
    self.assertEqual("Invalid credentials", element.text)
    print("Try: ", datetime.now())
except Exception as e:
    #assertion
    self.assertEqual("Dashboard", driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/h1').text)
    print("Except: ", datetime.now())
    #print(e)
finally:
    print ("Will Execute always")
    print("Finally: ", datetime.now())