from buttons import LOGIN_BUTTON_SELECTOR
import re
LOGIN_BUTTON_SELECTOR = '#login-button'
import playwright
import time
from playwright.sync_api import sync_playwright
from buttons import LOGIN_BUTTON_SELECTOR

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username: str, password: str) -> None:
        username_field = self.page.wait_for_selector('#user-name')
        username_field.fill(username)

        password_field = self.page.wait_for_selector('#password')
        password_field.fill(password)

        self.page.wait_for_selector(LOGIN_BUTTON_SELECTOR).click()


class PageOpener:
    def __init__(self):
        self.page = None
        self.browser = None

    def open_page(self):
        #playwright = sync_playwright()
        with sync_playwright() as playwright:
            self.browser = playwright.chromium.launch(headless=False)
            self.page = self.browser.new_page()
            self.page.goto('https://www.saucedemo.com')


    def close(self):
        # Close the page
        if self.page is not None:
            self.page.close()

        # Close the browser
        if self.browser is not None:
            self.browser.close()

    def login(self, username: str, password: str) -> None:
        username_field = self.page.wait_for_selector('#user-name')
        username_field.fill(username)

        password_field = self.page.wait_for_selector('#password')
        password_field.fill(password)

        self.page.wait_for_selector(LOGIN_BUTTON_SELECTOR).click()