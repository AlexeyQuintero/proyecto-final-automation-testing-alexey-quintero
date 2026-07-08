from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.add_buttons = (By.CLASS_NAME, "btn_inventory")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def agregar_producto_por_nombre(self, nombre):
        productos = self.driver.find_elements(*self.product_names)
        botones = self.driver.find_elements(*self.add_buttons)
        for i, producto in enumerate(productos):
            if producto.text == nombre:
                botones[i].click()
                break

    def ir_al_carrito(self):
        self.driver.find_element(*self.cart_link).click()

    def obtener_nombres_productos(self):
        return [p.text for p in self.driver.find_elements(*self.product_names)]

    def open_menu(self):
        self.driver.find_element(*self.menu_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logout_link)
        )

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
