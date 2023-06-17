from playwright.sync_api import sync_playwright
from buttons import LOGIN_BUTTON_SELECTOR, SHOPPING_CART_BUTTON, CHECKOUT_BUTTON, FINISH_STEP_TWO, BACK_HOME, BACKPACK_BUTTON_SELECTOR, BIKE_LIGHT_BUTTON_SELECTOR
from test_path_objects import LoginPage
from test_path_objects import InventoryPage

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



        inventory_page = InventoryPage()

        items = ["item1", "item2", "item3", "item4"]

        inventory_page.inventory(items)