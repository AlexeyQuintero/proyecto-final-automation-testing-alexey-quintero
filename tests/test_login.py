import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_users_csv
from utils.logger import logger

def test_login_valido(driver):
    logger.info("Inicio del test: login válido")
    # tu lógica de test
    logger.info("Login válido finalizado correctamente")


@pytest.mark.parametrize("user", load_users_csv())
def test_login(driver, user):
    login_page = LoginPage(driver)
    login_page.open()  # antes era load()
    login_page.ingresar_usuario(user["username"])
    login_page.ingresar_password(user["password"])
    login_page.click_login()

    # Validación simple: si el usuario es válido debería entrar a inventory
    if user["username"] == "standard_user":
        assert "inventory.html" in driver.current_url
    else:
        assert login_page.get_error_message() != ""
