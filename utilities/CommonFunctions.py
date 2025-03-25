import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.LoginPage import LoginPage
from utilities.ExcelUtils import ExcelUtils

# Load test data
with open("testData/testdata.json", "r") as file:
    test_data = json.load(file)

# Initialize Excel utility
excel = ExcelUtils("testData/test_cases.xlsx")


def login_to_magento(driver):
    """Reusable function to log in to Magento."""
    driver.get("https://magento.softwaretestingboard.com/")

    login_page = LoginPage(driver)

    # Perform login actions
    login_page.click_sign_in()
    login_page.enter_email(test_data["login_email"])
    login_page.enter_password(test_data["login_password"])
    login_page.click_login()

    # Verify login success
    wait = WebDriverWait(driver, 10)
    try:
        assert wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logged-in")))
        excel.update_status(3, "Pass")  # Update TC_002 status in Excel
    except:
        excel.update_status(3, "Fail")

    return driver  # Return the logged-in session
