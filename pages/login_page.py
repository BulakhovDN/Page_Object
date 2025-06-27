from datetime import time

from pages.base_page import BasePage
from pages.locators import LoginPageLocators, Register


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "Login URL is incorrect"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM not found"

    def register_new_user(self, email, password):
        self.browser.find_element(*Register.EMAIL).send_keys(email)
        self.browser.find_element(*Register.PASSWORD1).send_keys(password)
        self.browser.find_element(*Register.PASSWORD2).send_keys(password)
        self.browser.find_element(*Register.BUTTON).click()



