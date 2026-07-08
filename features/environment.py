from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def before_scenario(context, scenario):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=chrome_options)

    # Inicializar Page Objects
    context.inventory_page = InventoryPage(context.driver)
    context.cart_page = CartPage(context.driver)
    context.checkout_page = CheckoutPage(context.driver)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
