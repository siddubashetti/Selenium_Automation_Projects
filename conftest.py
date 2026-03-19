import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

@pytest.fixture()
def driver():
    chrome_options = Options()
    
    # Use a fresh temporary profile - no saved passwords!
    temp_profile = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_profile}")
    
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--no-default-browser-check")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    yield
    # Take screenshot only if test failed
    if request.node.rep_call.failed:
        # Create screenshots folder if not exists
        import os
        os.makedirs("reports/screenshots", exist_ok=True)
        
        # Save screenshot with test name
        screenshot_name = f"reports/screenshots/{request.node.name}.png"
        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved: {screenshot_name}")
