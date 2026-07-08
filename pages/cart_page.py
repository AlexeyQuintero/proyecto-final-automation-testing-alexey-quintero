from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def obtener_productos_carrito(self):
        productos = self.driver.find_elements(*self.cart_items)
        resultado = []
        for p in productos:
            nombre = p.find_element(By.CLASS_NAME, "inventory_item_name").text
            precio = p.find_element(By.CLASS_NAME, "inventory_item_price").text
            resultado.append({"nombre": nombre, "precio": precio})
        return resultado
