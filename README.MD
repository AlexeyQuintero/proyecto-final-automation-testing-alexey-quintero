# Proyecto Final - Automation Testing
Autor: Alexey Quintero

## 📌 Propósito
Framework de automatización de pruebas que combina **UI Testing con Selenium WebDriver**, **API Testing con Requests**, y generación de **reportes HTML con Pytest**.  
Se aplican buenas prácticas de programación y el patrón **Page Object Model (POM)** para mantener el código organizado y escalable.

---

## 🛠️ Tecnologías
- Python 3.13
- Selenium WebDriver
- Pytest
- Requests
- Pytest-HTML (reportes visuales)
- Pytest-Check (validaciones suaves)
- Behave (BDD, escenarios Gherkin)
- Git + GitHub (control de versiones)
- Logging personalizado (`utils.logger`)

---

## 📂 Estructura
- **pages/** → Page Objects (LoginPage, InventoryPage, CartPage, CheckoutPage)
- **tests/** → Casos de prueba (UI, API, parametrizados con CSV/JSON)
- **features/** → Escenarios BDD (login, carrito, inventario, logout, purchase)
- **features/steps/** → Definiciones de steps
- **utils/** → Funciones auxiliares (logger, lectura de datos)
- **data/** → Datos externos (users.csv, products.json)
- **ordenes_pdf/** → Comprobantes PDF generados
- **reports/** → Reportes HTML y screenshots
- **logs/** → Archivos de logging
- **environment.py** → Configuración Behave
- **pytest.ini** → Configuración Pytest
- **requirements.txt** → Dependencias
- **README.md** → Documentación

---

## 🚀 Instalación
Clonar el repositorio y ejecutar:

```bash
git clone https://github.com/[usuario]/proyecto-final-automation-testing-alexey-quintero.git
cd proyecto-final-automation-testing-alexey-quintero
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt
▶️ Ejecución de pruebas
Con Pytest
Ejecutar todas las pruebas:

bash
pytest
Generar reporte HTML:

bash
pytest --html=report.html
Con Behave (BDD)
Ejecutar escenarios de compra:

bash
behave --tags=@purchase
📊 Reportes
Se genera automáticamente un archivo report.html en la raíz del proyecto.

Incluye estado de cada test, duración y detalles.

Los comprobantes de compra se guardan en ordenes_pdf/.

📌 Funcionalidades implementadas
UI Tests (Selenium): login, inventario, carrito, logout, compra completa.

API Tests (Requests): login válido/erróneo, crear usuario, eliminar usuario, obtener usuario.

Parametrización: datos de prueba desde CSV y JSON.

Capturas de pantalla: PDF generado en compra exitosa.

Reportes HTML: con Pytest-HTML.

Logging: registro de pasos clave.

📂 Entrega
Repositorio GitHub:
proyecto-final-automation-testing-alexey-quintero