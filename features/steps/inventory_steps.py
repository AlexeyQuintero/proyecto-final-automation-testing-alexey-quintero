from behave import then
from pages.inventory_page import InventoryPage
from utils.logger import logger

@then("deberia ver {cantidad:d} productos en el inventario")
def step_validar_cantidad_productos(context, cantidad):
    productos = context.inventory_page.obtener_nombres_productos()
    logger.info(f"Validando cantidad de productos en inventario: {cantidad}")
    assert len(productos) == cantidad
