import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.data_loader import load_users_csv
from datetime import datetime
import pathlib
import pytest_html
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    user = load_users_csv()[0]
    login_page.login(user["username"], user["password"])
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            driver.save_screenshot(os.path.join(screenshot_dir, file_name))
