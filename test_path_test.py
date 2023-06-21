import pytest
import pytest
import re
import time
from playwright.sync_api import sync_playwright


def test_open_page(request):
    addopts = request.config.getini('addopts')
    addopts_str = ' '.join(addopts)  # Join the list elements into a single string
    browser_options = re.findall(r'--browser (\w+)', addopts_str)
    is_headless = '--headless' in addopts

    with sync_playwright() as playwright:
        for browser_type in browser_options:
            browser = getattr(playwright, browser_type).launch(headless=is_headless)
            page = browser.new_page()
            page.goto('https://www.saucedemo.com')


            browser.close()







