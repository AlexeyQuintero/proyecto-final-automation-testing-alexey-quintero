from behave import when, then
from PIL import Image
import os
from datetime import datetime

@when("navega al carrito")
def step_go_to_cart(context):
    context.cart_page.go_to_cart()

@when("hace clic en el boton Checkout")
def step_checkout(context):
    context.cart_page.click_checkout()

@when("completa los datos de envío:")
def step_fill_shipping(context):
    context.checkout_page.fill_shipping("Alexey", "Quintero", "1234")

@when("hace clic en el boton Continue")
def step_continue(context):
    context.checkout_page.click_continue()

@when("hace clic en el boton Finish")
def step_finish(context):
    context.checkout_page.click_finish()

@then("deberia ver el mensaje 'THANK YOU FOR YOUR ORDER'")
def step_verify_order(context):
    message = context.checkout_page.get_confirmation_message()
    assert "Thank you for your order!" in message, f"Mensaje inesperado: {message}"

@then("deberia generarse el comprobante en PDF")
def step_generate_pdf(context):
    folder = "ordenes_pdf"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(folder, f"orden_{timestamp}.png")
    pdf_path = os.path.join(folder, f"orden_{timestamp}.pdf")

    context.driver.save_screenshot(screenshot_path)
    img = Image.open(screenshot_path)
    img.save(pdf_path, "PDF", resolution=100.0)
    print(f"✅ Comprobante guardado en: {pdf_path}")
