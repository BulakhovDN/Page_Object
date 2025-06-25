from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")


class BookWasAddedToBasket:
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")


class NameBook:
    NAME = (By.XPATH, "//h1[1]")


class TheCostOfTheBasketIsNowField:
    COST_FIELD = (By.XPATH, "//div[@id='messages']//div[3]")


class TheCost:
    COST = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class='price_color']")
