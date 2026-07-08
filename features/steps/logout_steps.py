from behave import when, then
from utils.logger import logger

@when("abre el menú hamburguesa")
def step_open_menu(context):
    logger.info("Usuario abre el menú hamburguesa")
    context.inventory_page.open_menu()

@when("hace clic en el boton Logout")
def step_click_logout(context):
    logger.info("Usuario hace clic en Logout")
    context.inventory_page.click_logout()

@then("deberia volver a la pagina de Login")
def step_validar_logout(context):
    # Verificar que la URL actual sea la de la página de login de SauceDemo
    assert context.driver.current_url == "https://www.saucedemo.com/", \
        f"No volvió a la página de login, URL actual: {context.driver.current_url}"
