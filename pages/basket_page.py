from pages.base_page import BasePage
from pages.locators import ItemsInBasket, MessageAboutBasketIsEmpty


class BasketPage(BasePage):
    def should_not_be_book_in_basket(self):
        assert self.is_not_element_present(*ItemsInBasket.MESSAGE)

    def should_be_text_that_basket_empty(self):
        assert self.is_element_present(*MessageAboutBasketIsEmpty.MESSAGE)
