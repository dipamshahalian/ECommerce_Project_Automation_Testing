from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage

class CompareProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, email, password):
        login_page = LoginPage(self.driver)
        login_page.click_sign_in()
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_login()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logged-in")))

    def click_homepage_banner(self):
        banner = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='https://magento.softwaretestingboard.com/pub/media/wysiwyg/home/home-main.jpg']")))
        banner.click()

    def go_to_second_page(self):
        page_2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[4]//div[2]//ul[1]//li[2]//a[1]//span[2]")))
        page_2.click()

    def add_first_product_to_compare(self):
        compare1_xpath = "//li[9]//div[1]//div[1]//div[3]//div[1]//div[2]//a[2]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, compare1_xpath)))
        element = self.driver.find_element(By.XPATH, compare1_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, compare1_xpath)))
        self.driver.execute_script("arguments[0].click();", element)

    def add_second_product_to_compare(self):
        compare2_xpath = "//li[10]//div[1]//div[1]//div[3]//div[1]//div[2]//a[2]"
        self.wait.until(EC.presence_of_element_located((By.XPATH, compare2_xpath)))
        element = self.driver.find_element(By.XPATH, compare2_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, compare2_xpath)))
        self.driver.execute_script("arguments[0].click();", element)

    def click_compare_button(self):
        compare_btn_xpath = "//span[normalize-space()='Compare']"
        self.wait.until(EC.presence_of_element_located((By.XPATH, compare_btn_xpath)))
        element = self.driver.find_element(By.XPATH, compare_btn_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, compare_btn_xpath)))
        self.driver.execute_script("arguments[0].click();", element)
