from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocatorsOnProductPage:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")


class BookWasAddedToBasket:
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")


class NameBook:
    NAME = (By.XPATH, "//h1[1]")


class TheCostOfTheBasketIsNowField:
    COST_FIELD = (By.XPATH, "//div[@id='messages']//div[3]")


class TheCost:
    COST = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class='price_color']")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.XPATH, "//body/div[contains(@class,'container-fluid page')]/\
    div[contains(@class,'page_inner')]/div[@id='messages']/div[1]")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")


class ItemsInBasket:
    MESSAGE = (By.CSS_SELECTOR, ".col-sm-6.h3")


class Register:
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON = (By.CSS_SELECTOR, "button[value='Register']")
    GREETING_MESSAGE = (By.CSS_SELECTOR, "#wicon")


