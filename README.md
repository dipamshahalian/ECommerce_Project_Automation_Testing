# 🛒 ECommerce Project - Automation Testing Suite

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Framework-yellow)

A robust, scalable, and hybrid automation testing framework built using **Selenium**, **Python**, and **Pytest** to ensure high-quality assurance for a Magento-based E-Commerce platform.

---

## 🚀 Key Features

- 🔑 **Login Automation** — Verifies secure login functionality.
- 🛍️ **Product Search & Navigation** — Automates the search and selection of products like *Fusion Backpack*.
- 🛒 **Add to Cart Flow** — Validates the add-to-cart functionality with UI assertions.
- 📊 **Excel-Based Test Data** — Test cases are dynamically driven by Excel files.
- ✅ **Pass/Fail Result Logging** — Updates test status (Pass/Fail) in Excel after execution.
- 🧩 **Hybrid Framework** — Combines the best of keyword, data-driven, and modular frameworks.
- 📁 **Organized Folder Structure** — Easy to scale and maintain.
- 🪵 **Logging** — Detailed log capture for easy debugging.
- ⚙️ **Config-Driven Execution** — Credentials and URLs maintained separately in `config.ini`.

---

## 🗂️ Project Structure

```
ECommerce_Project_Automation_Testing/
│
├── configurations/
│   └── config.ini                # Stores base URL and login credentials
│
├── logs/
│   └── automation.log            # Log file for test execution
│
├── page_objects/
│   ├── login_page.py            # Page class for login functionalities
│   └── add_to_cart_page.py      # Page class for product search and add-to-cart
│
├── test_cases/
│   ├── test_login.py            # Test case for login
│   └── test_add_to_cart.py      # Test case for adding product to cart
│
├── utilities/
│   ├── excel_utils.py           # Read/write to Excel
│   └── logger.py                # Logging utility
│
├── TestData/
│   └── testdata.xlsx            # Excel file with test cases
│
├── conftest.py                  # Common fixtures and setup
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🧪 How to Run Tests

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Update Config:**
   - Add base URL, username, and password in `configurations/config.ini`.

3. **Run Test Cases:**
   ```bash
   pytest test_cases/test_login.py
   pytest test_cases/test_add_to_cart.py
   ```

---

## 📈 Excel Test Case Format

| TC_ID   | Test_Step              | Expected_Result         | Actual_Result | Status |
|---------|------------------------|--------------------------|----------------|--------|
| TC_001  | Login with valid user  | Dashboard should appear  | Dashboard seen | Pass   |

Excel is automatically updated after test execution with **Pass/Fail** status.

---

## 🔧 Tools & Technologies

- Python 3.10+
- Selenium WebDriver
- Pytest
- openpyxl (Excel Handling)
- WebDriverWait for synchronization
- Custom Logger
- Page Object Model (POM)

---

## 💡 Future Enhancements

- 🔍 Add Allure Reporting
- 🌐 Cross-browser testing
- 📦 Jenkins CI/CD Integration
- 📱 Mobile responsiveness checks

---

## 🤝 Contribution

Feel free to fork this project, raise issues, or contribute enhancements. Let’s build quality automation together!
