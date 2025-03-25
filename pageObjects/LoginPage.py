from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))).click()

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pass"))).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "send2"))).click()

    def is_login_successful(self):
        return self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logged-in")))
