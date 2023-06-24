from buttons import LOGIN_BUTTON_SELECTOR
import re
from playwright.sync_api import sync_playwright


class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        username_field = self.page.wait_for_selector('#user-name')
        username_field.fill(username)

        password_field = self.page.wait_for_selector('#password')
        password_field.fill(password)

        self.page.wait_for_selector(LOGIN_BUTTON_SELECTOR).click()


class SetUp:

