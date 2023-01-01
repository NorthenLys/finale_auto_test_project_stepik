from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.NAME, "registration_submit")
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    NAME_PRODUCT_ALERT = (By.CSS_SELECTOR, "#messages>:nth-child(1)>.alertinner strong")
    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    COST_PRODUCT_ALERT = (By.CSS_SELECTOR, "#messages>:nth-child(3)>.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") 
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")