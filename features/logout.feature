@logout
Feature: Cierre de sesión

    Background:
        Given que el usuario está en la pagina de Login
        When ingresa el usuario 'standard_user' y la contreseña 'secret_sauce'
        And hace clic en el boton Login
        Then deberia ingresar al inventario

    @positivo
    Scenario: Logout exitoso
        Given que el usuario está en el inventario
        When abre el menú hamburguesa
        And hace clic en el boton Logout
        Then deberia volver a la pagina de Login

