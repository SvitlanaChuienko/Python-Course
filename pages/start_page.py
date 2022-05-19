from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username="", password=""):
        """Sign in by using available values"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.click(xpath=self.constants.SIGH_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Veryfiyng error message about invalid sign in"""

        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, "Text is not valid"

    def sign_up(self, username="", email="", password=""):
        """"Sign up user by using available values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=password)
        sleep(2)
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    def verify_sign_out_button(self):
        sign_out_button = self.driver.find_element(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)
        assert sign_out_button

    def verify_success_redirect_by_header_link(self):
        self.click(xpath=self.constants.LINK_IN_HEADER_XPATH)
        start_page = self.driver.find_element(by=By.XPATH, value=self.constants.REGISTRATION_FORM_XPATH)
        assert start_page.is_displayed()

    def verify_success_redirect_by_footer_link(self):
        self.click(xpath=self.constants.LINK_IN_FOOTER_XPATH)
        start_page = self.driver.find_element(by=By.XPATH, value=self.constants.REGISTRATION_FORM_XPATH)
        assert start_page.is_displayed()

    def verify_validation_error_username_in_sigh_up(self):
        validation_username_error = self.driver.find_element(by=By.XPATH, value=self.constants.
                                                             SIGN_UP_VALIDATION_ERROR_USERNAME_XPATH)
        assert validation_username_error.is_displayed()

    def verify_validation_error_email_in_sign_up(self):
        validation_email_error = self.driver.find_element(by=By.XPATH,
                                                          value=self.constants.SIGN_UP_VALIDATION_ERROR_EMAIL_XPATH)
        assert validation_email_error.is_displayed
