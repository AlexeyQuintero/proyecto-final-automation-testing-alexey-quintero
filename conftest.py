import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.data_loader import load_users_csv
import pathlib
import pytest_html

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")

    # Detecta si está en GitHub Actions y usa Chromium
    chrome_path = os.getenv("CHROME_BIN", "/usr/bin/chromium-browser")
    driver_path = os.getenv("CHROMEDRIVER", "/usr/bin/chromedriver")

    options.binary_location = chrome_path
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)
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
            # Agregar screenshot al reporte HTML
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.png(os.path.join(screenshot_dir, file_name)))
