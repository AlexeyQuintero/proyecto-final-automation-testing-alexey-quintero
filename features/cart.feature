@cart
Feature: Carrito de compras

    Background:
        Given que el usuario está en la pagina de Login
        When ingresa el usuario 'standard_user' y la contreseña 'secret_sauce'
        And hace clic en el boton Login
        Then deberia ingresar al inventario

    @positivo
    Scenario: Agregar un producto al carrito
        Given que el usuario está en el inventario
        When agrega el producto 'Sauce Labs Backpack' al carrito
        Then deberia ver el producto 'Sauce Labs Backpack' en el carrito

    @positivo
    Scenario: Agregar múltiples productos al carrito
        Given que el usuario está en el inventario
        When agrega los productos:
            | producto              |
            | Sauce Labs Backpack   |
            | Sauce Labs Bike Light |
        Then deberia ver 2 productos en el carrito
