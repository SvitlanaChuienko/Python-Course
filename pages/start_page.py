from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from pages.utils import log_wrapper, wait_until_ok


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def sign_in(self, username="", password=""):
        """Sign in by using available values"""
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.click(xpath=self.constants.SIGH_IN_BUTTON_XPATH)
        return ProfilePage(self.driver)

    @log_wrapper
    def verify_sign_in_error(self):
        """Veryfiyng error message about invalid sign in"""
        error_message = self.wait_until_displayed(xpath=self.constants.SIGN_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SIGN_IN_ERROR_MESSAGE_TEXT, "Text is not valid"

    @log_wrapper
    def success_sign_up(self, user):
        """Sign up user by using available values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=user.email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=user.password)
        self.click_sing_up_and_verify()

        return ProfilePage(self.driver)

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def click_sing_up_and_verify(self):
        """Click Sign Up and verify that button 'Sign Up' doesn't exist anymore"""
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exist(xpath=self.constants.SIGN_UP_BUTTON_XPATH)

    @log_wrapper
    def sign_up_with_optional_variables(self, username="", email="", password=""):
        """"Sign up user by using optional values"""
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_XPATH, value=password)

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def click_and_verify_validation_error_email_in_sign_up(self):
        """Verifying error message about invalid email in registration form"""
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        validation_email_error = self.driver.find_element(by=By.XPATH, value=self.constants.
                                                          SIGN_UP_VALIDATION_ERROR_EMAIL_XPATH)
        assert validation_email_error.is_displayed()

    @log_wrapper
    def verify_success_redirect_by_header_link(self):
        """Verifying success redirect to start page by click in header link"""
        self.wait_until_clickable(xpath=self.constants.LINK_IN_HEADER_XPATH).click()
        start_page = self.wait_until_displayed(xpath=self.constants.REGISTRATION_FORM_XPATH)
        assert start_page.is_displayed()

    @log_wrapper
    def verify_success_redirect_by_footer_link(self):
        """Verifying success redirect to start page by click in footer link"""
        self.wait_until_clickable(xpath=self.constants.LINK_IN_FOOTER_XPATH).click()
        start_page = self.wait_until_displayed(xpath=self.constants.REGISTRATION_FORM_XPATH)
        assert start_page.is_displayed()

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def click_and_verify_validation_error_username_in_sigh_up(self):
        """Verifying error message about invalid username in registration form"""
        self.click(xpath=self.constants.SIGN_UP_BUTTON_XPATH)
        validation_username_error = self.driver.find_element(by=By.XPATH, value=self.constants.
                                                             SIGN_UP_VALIDATION_ERROR_USERNAME_XPATH)
        assert validation_username_error.is_displayed()
