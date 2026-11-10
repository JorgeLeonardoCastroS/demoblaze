from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Place Order']")
    NAME_INPUT = (By.ID, "name")
    COUNTRY_INPUT = (By.ID, "country")
    CITY_INPUT = (By.ID, "city")
    CARD_INPUT = (By.ID, "card")
    MONTH_INPUT = (By.ID, "month")
    YEAR_INPUT = (By.ID, "year")
    PURCHASE_BTN = (By.XPATH, "//button[text()='Purchase']")
    SUCCESS_CONFIRMATION = (By.CSS_SELECTOR, ".sweet-alert.showSweetAlert.visible")
    OK_BTN = (By.XPATH, "//button[text()='OK']")

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BTN)

    def fill_form_and_purchase(self, name, country, city, card, month, year):
        # Aseguramos que el modal de compra esté completamente visible antes de escribir
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.NAME_INPUT)
        )
        
        self.type(self.NAME_INPUT, name)
        self.type(self.COUNTRY_INPUT, country)
        self.type(self.CITY_INPUT, city)
        self.type(self.CARD_INPUT, card)
        self.type(self.MONTH_INPUT, month)
        self.type(self.YEAR_INPUT, year)
        self.click(self.PURCHASE_BTN)

    def is_purchase_successful(self):
        confirmation = self.find(self.SUCCESS_CONFIRMATION)
        return confirmation.is_displayed()

    def close_success_modal(self):
        self.click(self.OK_BTN)