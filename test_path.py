from playwright.sync_api import sync_playwright
from buttons import LOGIN_BUTTON_SELECTOR


INVENTORY_PAGE_URL = 'https://www.saucedemo.com/inventory.html'
CART_PAGE_URL = 'https://www.saucedemo.com/cart.html'

def test_path():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.saucedemo.com')

        username_selector = '#user-name'
        password_selector = '#password'

        username_field = page.wait_for_selector(username_selector)
        username_field.fill('standard_user')

        password_field = page.wait_for_selector(password_selector)
        password_field.fill('secret_sauce')

        #button_selector = '#login-button'

        button = page.wait_for_selector(LOGIN_BUTTON_SELECTOR)
        button.click()

        button_id = 'react-burger-menu-btn'

        button = page.wait_for_selector(f'button#{button_id}')
        button.click()

        backpack_button_id = 'add-to-cart-sauce-labs-backpack'
        bike_light_button_id = 'add-to-cart-sauce-labs-bike-light'

        backpack_button = page.wait_for_selector(f'button#{backpack_button_id}')
        backpack_button.click()

        bike_light_button = page.wait_for_selector(f'button#{bike_light_button_id}')
        bike_light_button.click()

        shopping_cart_container = page.wait_for_selector('#shopping_cart_container')
        shopping_cart_container.click()

        assert page.url == CART_PAGE_URL

        checkout_button_selector = '.btn.btn_action.btn_medium.checkout_button'
        checkout_button = page.wait_for_selector(checkout_button_selector)
        checkout_button.click()

        first_name_field = page.wait_for_selector('#first-name')
        first_name_field.fill('Pawel')

        last_name_field = page.wait_for_selector('#last-name')
        last_name_field.fill('Gorski')

        postal_code_field = page.wait_for_selector('#postal-code')
        postal_code_field.fill('999')

        continue_button = page.wait_for_selector('#continue')
        continue_button.click()

        finish_button = page.wait_for_selector('#finish')
        finish_button.click()

        back_to_products_button = page.wait_for_selector('#back-to-products')
        back_to_products_button.click()


        current_url = page.url


        browser.close()

        assert current_url == INVENTORY_PAGE_URL


