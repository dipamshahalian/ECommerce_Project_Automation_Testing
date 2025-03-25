import pytest
from pageObjects.SearchPage import SearchPage
from utilities.ExcelUtils import ExcelUtils

# Initialize Excel utility
excel = ExcelUtils("testData/test_cases.xlsx")

def test_search_product(logged_in_driver):
    driver = logged_in_driver
    search_page = SearchPage(driver)

    try:
        # Step 1: Search for the product
        search_page.search_product("Fusion Backpack")
        search_page.click_search_icon()
        excel.update_status(3, "Pass")  # TC_003: Search Product

        # Step 2: Select the product from the collection page
        search_page.select_product()
        excel.update_status(4, "Pass")  # TC_004: Select Product

        # Step 3: Click 'Add to Cart'
        search_page.click_add_to_cart()
        excel.update_status(5, "Pass")  # TC_005: Add to Cart

    except Exception as e:
        # Mark test cases as Fail if any step fails
        excel.update_status(3, "Fail")
        excel.update_status(4, "Fail")
        excel.update_status(5, "Fail")
        print(f"Test failed due to: {str(e)}")
