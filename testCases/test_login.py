def test_login(logged_in_driver):
    """Test login using the reusable function."""
    driver = logged_in_driver
    assert "logged-in" in driver.page_source  # Simple check
