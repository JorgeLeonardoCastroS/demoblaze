from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    CART_LINK = (By.ID, "cartur")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.demoblaze.com/"

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def add_product_to_cart(self, product_name):
        """Selecciona un producto del catálogo y lo agrega al carrito"""
        product_locator = (By.LINK_TEXT, product_name)
        self.click(product_locator)
        
        # Botón 'Add to cart'
        add_btn = (By.LINK_TEXT, "Add to cart")
        self.click(add_btn)
        
        # Aceptar la alerta emergente de éxito
        self.accept_alert()
        
        # Regresar al inicio para el siguiente producto
        self.click((By.ID, "nava"))

    def go_to_cart(self):
        self.click(self.CART_LINK)