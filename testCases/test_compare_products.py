import pytest
from pageObjects.CompareProductsPage import CompareProductsPage
from utilities.ExcelUtils import ExcelUtils

def test_compare_products(logged_in_driver, driver):
    driver = logged_in_driver
    excel = ExcelUtils("testData/test_cases.xlsx")

    try:
        compare_page = CompareProductsPage(driver)

        compare_page.click_homepage_banner()
        compare_page.go_to_second_page()
        compare_page.add_first_product_to_compare()
        compare_page.add_second_product_to_compare()
        compare_page.click_compare_button()

        # If everything runs till here, mark as Pass
        excel.update_status(6, "Pass")
        print("Product comparison successful.")

    except Exception as e:
        excel.update_status(6, "Fail")
        print(f"Test Failed: {str(e)}")

    input("Press Enter to close the browser...")
