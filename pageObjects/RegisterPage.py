from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    def click_create_account(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create an Account"))).click()

    def enter_firstname(self, firstname):
        self.wait.until(EC.visibility_of_element_located((By.ID, "firstname"))).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.wait.until(EC.visibility_of_element_located((By.ID, "lastname"))).send_keys(lastname)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located((By.ID, "email_address"))).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)
        self.wait.until(EC.visibility_of_element_located((By.ID, "password-confirmation"))).send_keys(password)

    def click_register(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Create an Account']"))).click()
