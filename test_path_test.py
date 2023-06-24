import pytest
import re
import time
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chromium', help='Browser option: chromium, firefox, or webkit')
    parser.addoption('--headed', action='store_true', help='Run the test in headed mode')


@pytest.fixture(scope="module")
def playwright_page(request):
    browser_option = request.config.getoption('--browser')
    is_headed = request.config.getoption('--headed')

    if isinstance(browser_option, list):
        browser_option = browser_option[0]

    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_option).launch(headless=not is_headed)

        if not browser:
            raise ValueError(f"Invalid browser option: {browser_option}")

        page = browser.new_page()
        page.goto('https://www.saucedemo.com')

        yield page

        browser.close()


def test_open_page(playwright_page):
    page = playwright_page

    time.sleep(3)






