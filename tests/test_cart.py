from selenium.webdriver.common.by import By
import pytest
from utils.logger import logger

def test_login_valido(driver):
    logger.info("Inicio del test: login válido")
    # tu lógica de test
    logger.info("Login válido finalizado correctamente")


@pytest.mark.smoke
def test_cart(driver_logged):
    driver = driver_logged

    # Agregar producto al carrito (primer botón encontrado)
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()

    # Verificar contador del carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert contador_cart.text == "1", "La cantidad de productos no se agregó correctamente"

    # Obtener nombre del primer producto
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar que el producto agregado coincide
    assert cart_item == product_name, "El producto agregado no coincide"
