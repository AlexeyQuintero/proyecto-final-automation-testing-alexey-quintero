@inventory
Feature: Inventario de productos

    Background:
        Given que el usuario está en la pagina de Login
        When ingresa el usuario 'standard_user' y la contreseña 'secret_sauce'
        And hace clic en el boton Login
        Then deberia ingresar al inventario

    @positivo
    Scenario: Validar que se muestran todos los productos
        Given que el usuario está en el inventario
        Then deberia ver 6 productos en el inventario
