from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "search")
        self.search_icon = (By.XPATH, "//button[@title='Search']")
        self.product = (By.XPATH, "//img[@alt='Fusion Backpack']")  # Select product
        self.add_to_cart = (By.XPATH, "//button[@title='Add to Cart']")  # Add to Cart

    def search_product(self, product_name):
        """Enter product name into the search box."""
        search_box = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_box)
        )
        search_box.clear()
        search_box.send_keys(product_name)

    def click_search_icon(self):
        """Click the search icon."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_icon)
        ).click()

    def select_product(self):
        """Click on the Fusion Backpack product from the collection page."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product)
        ).click()

    def click_add_to_cart(self):
        """Click the 'Add to Cart' button."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart)
        ).click()
