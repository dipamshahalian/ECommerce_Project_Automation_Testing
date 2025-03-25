import json
import pytest
from pageObjects.RegisterPage import RegisterPage
from utilities.ExcelUtils import ExcelUtils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load test data
with open("testData/testdata.json", "r") as file:
    test_data = json.load(file)

# Initialize Excel utility
excel = ExcelUtils("testData/test_cases.xlsx")

def test_create_account(driver):
    driver.get("https://magento.softwaretestingboard.com/")

    register_page = RegisterPage(driver)

    # Perform actions
    register_page.click_create_account()
    register_page.enter_firstname(test_data["firstname"])
    register_page.enter_lastname(test_data["lastname"])
    register_page.enter_email(test_data["email"])
    register_page.enter_password(test_data["password"])
    register_page.click_register()

    # Verify account creation
    wait = WebDriverWait(driver, 10)
    try:
        assert wait.until(EC.title_contains("My Account"))
        excel.update_status(2, "Pass")  # Update TC_001 status in Excel
    except:
        excel.update_status(2, "Fail")
