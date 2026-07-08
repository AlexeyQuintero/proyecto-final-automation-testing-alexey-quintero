@purchase
Feature: Compra de productos

  @positivo
  Scenario: Compra exitosa y generación de comprobante
    Given que el usuario está en la pagina de Login
    When ingresa el usuario 'standard_user' y la contreseña 'secret_sauce'
    And hace clic en el boton Login
    Then deberia ingresar al inventario
    When agrega el producto 'Sauce Labs Backpack' al carrito
    And navega al carrito
    And hace clic en el boton Checkout
    And completa los datos de envío:
      | FirstName | Alexey   |
      | LastName  | Quintero |
      | ZipCode   | 1234     |
    And hace clic en el boton Continue
    And hace clic en el boton Finish
    Then deberia ver el mensaje 'THANK YOU FOR YOUR ORDER'
    And deberia generarse el comprobante en PDF
