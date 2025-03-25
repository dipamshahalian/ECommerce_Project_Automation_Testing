import pytest
from selenium import webdriver
from utilities.CommonFunctions import login_to_magento

@pytest.fixture
def driver():
    """Fixture to initialize WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    """Fixture to return a logged-in session."""
    return login_to_magento(driver)
