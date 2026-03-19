# 🤖 Selenium Automation Framework
### Python | Pytest | Page Object Model | GitHub Actions CI/CD

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-9.x-orange?logo=pytest)
![CI/CD](https://img.shields.io/badge/GitHub_Actions-Passing-brightgreen?logo=github)

---

## 📌 About This Project

This is a **Selenium WebDriver automation framework** built with Python using the **Page Object Model (POM)** design pattern. The framework automates end-to-end test scenarios on [SauceDemo](https://www.saucedemo.com) — a demo e-commerce website built for automation practice.

---

## 🌐 Website Under Test

| Detail | Value |
|--------|-------|
| URL | https://www.saucedemo.com |
| Username | `standard_user` |
| Password | `secret_sauce` |

---

## 🏗️ Project Structure

```
selenium_project/
│
├── pages/                        # Page Object Model classes
│   ├── login_page.py             # Login page locators & actions
│   ├── products_page.py          # Products page locators & actions
│   ├── cart_page.py              # Cart page locators & actions
│   └── checkout_page.py          # Checkout page locators & actions
│
├── tests/                        # Test files
│   ├── test_login.py             # Login test cases
│   ├── test_products.py          # Products page test cases
│   ├── test_cart.py              # Cart test cases
│   └── test_checkout.py          # Checkout test cases
│
├── utils/                        # Utility helpers
│   └── wait_helper.py            # Explicit wait methods
│
├── reports/                      # Generated reports
│   ├── report.html               # HTML test report
│   └── screenshots/              # Screenshots on failure
│
├── .github/
│   └── workflows/
│       └── selenium_tests.yml    # GitHub Actions CI/CD pipeline
│
├── conftest.py                   # Browser setup & teardown fixtures
├── pytest.ini                    # Pytest configuration
└── README.md                     # Project documentation
```

---

## 🧪 Test Cases

### 🔐 Login Tests (`test_login.py`)
| Test | Description |
|------|-------------|
| `test_valid_login` | Verify successful login with valid credentials |
| `test_invalid_login` | Verify error message with invalid credentials |

### 🛍️ Products Tests (`test_products.py`)
| Test | Description |
|------|-------------|
| `test_product_page` | Verify products page loads with title "Products" |
| `test_products_count` | Verify exactly 6 products are displayed |
| `test_click_product` | Verify clicking a product opens the detail page |

### 🛒 Cart Tests (`test_cart.py`)
| Test | Description |
|------|-------------|
| `test_cart_page` | Add product, verify cart count, remove product, verify cart empty |

### ✅ Checkout Tests (`test_checkout.py`)
| Test | Description |
|------|-------------|
| `test_checkout_page` | Full checkout flow — add product, go to cart, fill details, finish order |

---

## ⚙️ Prerequisites

- Python 3.13+
- Google Chrome browser
- Git

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/selenium_project.git
cd selenium_project
```

### 2. Install dependencies
```bash
pip install selenium pytest pytest-html webdriver-manager pytest-xdist
```

### 3. Run all tests
```bash
pytest
```

### 4. Run specific test file
```bash
pytest tests/test_login.py -v
```

### 5. Run in parallel
```bash
pytest -n 2
```

### 6. Run with HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 📊 Reports

After running tests, an HTML report is automatically generated at:
```
reports/report.html
```

Open it in your browser to see:
- ✅ Passed tests
- ❌ Failed tests
- ⏱️ Time taken per test
- 📸 Screenshots on failure

---

## 📸 Screenshots on Failure

When a test fails, a screenshot is automatically captured and saved to:
```
reports/screenshots/<test_name>.png
```

---

## 🔄 GitHub Actions CI/CD

This project uses **GitHub Actions** to automatically run tests on every push to the `main` branch.

### Pipeline Steps:
1. 📥 Checkout code
2. 🐍 Setup Python 3.13
3. 🌐 Setup Chrome browser
4. 📦 Install dependencies
5. 🧪 Run all tests in headless mode
6. 📊 Upload HTML report as artifact

### View Results:
Go to your GitHub repo → **Actions** tab → Click latest workflow run

---

## 🏗️ Framework Architecture

```
Test Files
    ↓ uses
Page Objects (POM)
    ↓ extends
Base Utilities (WaitHelper)
    ↓ uses
Selenium WebDriver
    ↓ controls
Chrome Browser
    ↓ opens
SauceDemo Website
```

---

## 🔧 Configuration (`pytest.ini`)

```ini
[pytest]
testpaths = tests
addopts = -v --html=reports/report.html --self-contained-html -n 2
```

---

## 💡 Key Concepts Used

| Concept | Description |
|---------|-------------|
| Page Object Model | Each page has its own class with locators and actions |
| Implicit Wait | Global wait of 10 seconds for all elements |
| Explicit Wait | Wait for specific element conditions |
| Fixtures | Browser setup and teardown via conftest.py |
| Parallel Execution | Run multiple tests simultaneously with pytest-xdist |
| Headless Mode | Run Chrome without display for CI/CD |

---

## 📚 Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.13 | Programming language |
| Selenium | 4.x | Browser automation |
| Pytest | 9.x | Test runner |
| pytest-html | 4.x | HTML reports |
| pytest-xdist | 3.x | Parallel execution |
| webdriver-manager | 4.x | Auto ChromeDriver management |
| GitHub Actions | - | CI/CD pipeline |

---

## 👨‍💻 Author

**Suman**
- GitHub: [@siddubashetti](https://github.com/siddubashetti)

---

## 📝 License

This project is for learning and practice purposes.

---

⭐ **If you found this helpful, give it a star on GitHub!** ⭐