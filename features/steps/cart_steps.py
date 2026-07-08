from behave import given, when, then
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

@given("que el usuario está en el inventario")
def step_usuario_en_inventario(context):
    context.inventory_page = InventoryPage(context.driver)
    assert "/inventory.html" in context.driver.current_url

@when("agrega el producto '{producto}' al carrito")
def step_agregar_producto(context, producto):
    context.inventory_page.agregar_producto_por_nombre(producto)

@when("agrega los productos:")
def step_agregar_multiples_productos(context):
    for row in context.table:
        producto = row["producto"]
        context.inventory_page.agregar_producto_por_nombre(producto)

@then("deberia ver el producto '{producto}' en el carrito")
def step_validar_producto_en_carrito(context, producto):
    context.inventory_page.ir_al_carrito()
    context.cart_page = CartPage(context.driver)
    productos = context.cart_page.obtener_productos_carrito()
    nombres = [p["nombre"] for p in productos]
    assert producto in nombres

@then("deberia ver {cantidad:d} productos en el carrito")
def step_validar_cantidad_productos(context, cantidad):
    context.inventory_page.ir_al_carrito()
    context.cart_page = CartPage(context.driver)
    productos = context.cart_page.obtener_productos_carrito()
    assert len(productos) == cantidad
