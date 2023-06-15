# Test for correct login and password using page object pattern

from playwright.sync_api import sync_playwright
from buttons import LOGIN_BUTTON_SELECTOR, SHOPPING_CART_BUTTON, CHECKOUT_BUTTON, FINISH_STEP_TWO, BACK_HOME, BACKPACK_BUTTON_SELECTOR, BIKE_LIGHT_BUTTON_SELECTOR
from test_path_objects import LoginPage

def test_correct_login():
    with sync_playwright() as playwright:
        #it's on headless false because I wanted to see what is happening. Normally it would not be on
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.saucedemo.com')

        assert page.url == 'https://www.saucedemo.com/'

        login_page = LoginPage(page)
        login_page.login('standard_user', 'secret_sauce')

        # Assertion to check if the login is successful
        assert page.url == 'https://www.saucedemo.com/inventory.html'

        browser.close()

#test for correct login incorrect password
def test_failed_login():
    with sync_playwright() as playwright:
        # it's on headless false because I wanted to see what is happening. Normally it would not be on
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.saucedemo.com')

        assert page.url == 'https://www.saucedemo.com/'

        login_page = LoginPage(page)
        login_page.login('standard_user', 'incorrect_password')

        # Assertion to check if the login fails and user remains on the login page
        assert page.url == 'https://www.saucedemo.com/'

        browser.close()