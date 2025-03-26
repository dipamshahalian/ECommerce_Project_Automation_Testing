import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.LoginPage import LoginPage
from utilities.ExcelUtils import ExcelUtils


def test_proceed_to_checkout(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)  # Increased wait time
    excel = ExcelUtils("testData/test_cases.xlsx")
    actions = ActionChains(driver)

    try:
        # Click on the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "showcart")))
        cart_icon.click()

        # Click on 'Proceed to Checkout'
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout")))
        checkout_button.click()

        # Fill in necessary shipping details
        wait.until(EC.presence_of_element_located((By.NAME, "street[0]"))).send_keys("123 Main Street")
        driver.find_element(By.NAME, "city").send_keys("Los Angeles")
        driver.find_element(By.NAME, "region_id").send_keys("California")
        driver.find_element(By.NAME, "postcode").send_keys("90001")
        driver.find_element(By.NAME, "telephone").send_keys("1234567890")

        # Select shipping method
        shipping_methods = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='radio'][name^='ko_unique_']")))
        if shipping_methods:
            shipping_methods[0].click()

        # Click 'Next' to proceed
        next_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "continue")))
        actions.move_to_element(next_button).click().perform()

        # Check 'My billing and shipping address are the same' checkbox
        same_address_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, "billing-address-same-as-shipping")))
        same_address_checkbox.click()

        # Place order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "action.primary.checkout")))
        actions.move_to_element(place_order_button).click().perform()

        # Ensure order confirmation message appears
        confirmation_message_locator = (By.CLASS_NAME, "checkout-success")
        order_message = wait.until(EC.presence_of_element_located(confirmation_message_locator)).text
        assert "Thank you for your purchase!" in order_message, "Order confirmation message not found!"

        # Update Excel with Pass
        excel.update_status(5, "Pass")
        print("Test Passed: Order placed successfully.")

    except Exception as e:
        excel.update_status(5, "Fail")
        print(f"Test Failed: {str(e)}")
