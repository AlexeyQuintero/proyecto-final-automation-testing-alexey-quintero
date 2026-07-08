import pytest
from pages.inventory_page import InventoryPage
from utils.logger import logger

def test_login_valido(driver):
    logger.info("Inicio del test: login válido")
    # tu lógica de test
    logger.info("Login válido finalizado correctamente")


@pytest.mark.smoke
def test_inventory(driver_logged):
    inventory_page = InventoryPage(driver_logged)

    # Obtener todos los nombres de productos en la página
    productos = inventory_page.obtener_nombres_productos()

    # Validar que haya al menos un producto
    assert len(productos) > 0, "No se encontraron productos en el inventario"

    # Validar que los nombres no estén vacíos
    for nombre in productos:
        assert nombre.strip() != "", "Se encontró un producto sin nombre"
