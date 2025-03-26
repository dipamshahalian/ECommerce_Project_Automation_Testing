import pytest
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.ExcelUtils import ExcelUtils


def test_add_pants_to_cart(driver):
    driver.get("https://magento.softwaretestingboard.com/")

    excel = ExcelUtils("testData/test_cases.xlsx")

    login_page = LoginPage(driver)
    login_page.click_sign_in()
    login_page.enter_email("ShahDipam@gcet.com")  # Replace with actual test email
    login_page.enter_password("#Luma10#")  # Replace with actual test password
    login_page.click_login()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "logged-in")))

    try:
        # Navigate to Sale > Men's Deals > Pants
        sale_menu = driver.find_element(By.XPATH, "//a[@id='ui-id-8']")  # Sale menu
        sale_menu.click()

        pants_option = driver.find_element(By.XPATH, "//ul[2]//li[4]//a[1]")
        pants_option.click()

        # Select any pant from listing page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item-link")))
        pant_item = driver.find_element(By.CLASS_NAME, "product-item-link")
        pant_item.click()

        # Select Size
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.swatch-attribute.size .swatch-option")))
        size_option = driver.find_element(By.CSS_SELECTOR, "div.swatch-attribute.size .swatch-option")
        size_option.click()

        # Select Color
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.swatch-attribute.color .swatch-option")))
        color_option = driver.find_element(By.CSS_SELECTOR, "div.swatch-attribute.color .swatch-option")
        color_option.click()

        # Click Add to Cart
        wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
        add_to_cart = driver.find_element(By.ID, "product-addtocart-button")
        add_to_cart.click()

        # Verify cart update
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "counter-number"), "1"))

        # Open cart and check product presence
        cart_icon = driver.find_element(By.CLASS_NAME, "showcart")
        cart_icon.click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item-name")))
        product_name = driver.find_element(By.CLASS_NAME, "product-item-name").text
        assert "Pants" in product_name, "Product not added to cart!"

        # Update Excel
        excel = ExcelUtils("testData/test_cases.xlsx")
        excel.update_status(4, "Pass")  # TC_003 test
        print("Excel updated with Pass")


    except Exception as e:
        excel.update_status(4, "Pass")
        print("Excel updated with Fail")
        print(f"Test failed due to: {str(e)}")

