from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product_text = name_product.text
        name_product_alert = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ALERT)
        name_product_alert_text = name_product_alert.text
        assert name_product_text == name_product_alert_text, "Names of products are not the same"

    def should_be_cost_product(self):
        cost_product = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        cost_product_text = cost_product.text
        cost_product_alert = self.browser.find_element(*ProductPageLocators.COST_PRODUCT_ALERT)
        cost_product_alert_text = cost_product_alert.text
        assert cost_product_text == cost_product_alert_text, "Prices of products are not the same"  
    
    
