from test_path_objects import PageOpener, LoginPage
from playwright.sync_api import sync_playwright
from buttons import LOGIN_BUTTON_SELECTOR



with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False)
	page = browser.new_page()
	page.goto('https://www.saucedemo.com')
	inputs = LoginPage(page)
	inputs.login('standard_user', 'secret_sauce')


