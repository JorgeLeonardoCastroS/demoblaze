import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    # Descarga el driver y asegura la ruta correcta del ejecutable .exe en Windows
    driver_path = ChromeDriverManager().install()
    
    if "THIRD_PARTY_NOTICES" in driver_path:
        driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")
    
    # Si por alguna razón sigue apuntando mal, buscamos el .exe en la caché de wdm
    if not driver_path.endswith("chromedriver.exe"):
        wdm_dir = os.path.join(os.path.expanduser("~"), ".wdm")
        for root, dirs, files in os.walk(wdm_dir):
            if "chromedriver.exe" in files:
                driver_path = os.path.join(root, "chromedriver.exe")
                break

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_e2e_purchase_demoblaze(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    # 1. Abrir la página principal de Demoblaze
    home_page.open()

    # 2. Agregar dos productos al carrito
    home_page.add_product_to_cart("Samsung galaxy s6")
    home_page.add_product_to_cart("Nokia lumia 1520")

    # 3. Visualizar el carrito de compras
    home_page.go_to_cart()

    # 4. Completar el formulario de compra
    cart_page.click_place_order()
    cart_page.fill_form_and_purchase(
        name="Jorge Leonardo Castro",
        country="Colombia",
        city="Bogotá",
        card="1234567890123456",
        month="11",
        year="2028"
    )

    # 5. Validar que la compra fue exitosa y cerrar modal
    assert cart_page.is_purchase_successful() == True, "La compra no se completó correctamente"
    cart_page.close_success_modal()