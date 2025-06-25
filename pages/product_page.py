from pages.base_page import BasePage
from pages.locators import BasketPageLocators, BookWasAddedToBasket, NameBook, TheCostOfTheBasketIsNowField, TheCost


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        button.click()

    def check_that_book_was_added_to_basket(self):
        book_name_in_message = self.browser.find_element(*BookWasAddedToBasket.BOOK_NAME_IN_MESSAGE).text
        book_name = self.browser.find_element(*NameBook.NAME).text
        assert book_name == book_name_in_message, f"Different book: expected '{book_name}', got '{book_name_in_message}'"

    def check_that_cost_book_was_added_to_basket_is_write(self):
        element_cost = self.browser.find_element(*TheCostOfTheBasketIsNowField.COST_FIELD)
        text_element = element_cost.text
        book_cost = self.browser.find_element(*TheCost.COST)
        cost = book_cost.text
        assert cost in text_element, "Different cost"

