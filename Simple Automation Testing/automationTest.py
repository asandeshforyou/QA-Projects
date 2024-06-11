from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

#setting up  the driver function
def driverSetup():
    chrome_driver_path = 'D:/Coding stuffs/ecom_tests/chromedriver.exe'
    service =Service(chrome_driver_path)
    driver=webdriver.Chrome(service=service)
    return driver
#driver teardown function
def driverTeardown(driver):
    driver.quit()

#toautomateloginpagefrom“BasicAuth”pageandvalidate.User:admin Password:admin

def basciAuth(driver):
    driver.get('https://the-internet.herokuapp.com/basic_auth')      
    time.sleep(2)
    driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    time.sleep(2)
    if 'Congratulations! You must have the proper credentials.' in driver.page_source:
        print("Test case A passed")
    else: print("Test case A failed")
def checkboxesValidation(driver):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    checkbox1=driver.find_element(By.XPATH,'//*[@id="checkboxes"]/input[1]')
    checkbox1.click()
    if checkbox1.is_selected():
        print('Test case B passed')
    else: print("Test case B failed")

driver=driverSetup()
basciAuth(driver)
checkboxesValidation(driver)
driverTeardown(driver)
