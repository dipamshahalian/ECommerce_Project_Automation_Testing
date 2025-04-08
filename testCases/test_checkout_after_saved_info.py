import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.LoginPage import LoginPage
from utilities.ExcelUtils import ExcelUtils


def test_proceed_to_checkout(logged_in_driver, driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 15)  # Increased wait time
    excel = ExcelUtils("testData/test_cases.xlsx")
    actions = ActionChains(driver)

    try:
        # Click on the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "showcart")))
        cart_icon.click()

        # Click on 'Proceed to Checkout'
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout")))
        checkout_button.click()

        # Click 'Next' to proceed
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button action continue primary']")))
        actions.move_to_element(next_button).click().perform()

        # Place order
        place_order_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "action.primary.checkout")))
        actions.move_to_element(place_order_button).click().perform()

        # Ensure order confirmation message appears
        confirmation_message_locator = (By.CLASS_NAME, "checkout-success")
        order_message = wait.until(EC.presence_of_element_located(confirmation_message_locator)).text
        assert "Thank you for your purchase!" in order_message, "Order confirmation message not found!"

        # Update Excel with Pass
        excel.update_status(6, "Pass")
        print("Test Passed: Order placed successfully.")

    except Exception as e:
        excel.update_status(5, "Fail")
        print(f"Test Failed: {str(e)}")

