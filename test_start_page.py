import logging
from time import sleep

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    def test_sign_in_with_empty_fields(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Clear login field
            - Clear password field
            - Click on 'Sing In' button
            - Verify error message
        """
        # Clear login field
        # Clear password field
        # Click on 'Sing In' button
        start_page.sign_in()
        self.log.info("Empty fields of user are trying to sign in")

        # - Verify error message
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_invalid_login_on_start_page(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter invalid data in login field
            - Enter valid data in password field
            - Click on 'Sing In' button
            - Verify error message
        """

        # - Enter invalid data in login field
        # - Enter valid data in password field
        # - Click on 'Sing In' button
        start_page.sign_in(username='Qwerty', password='Qwerty123456')
        self.log.info("Fields with invalid data of user are trying to sign in")

        # - Verify error message
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_redirect_by_click_button_in_header(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Find 'Complex app for testing - QA' link and click on it
            - Verify redirect on the start page
        """
        # - Find 'Complex app for testing - QA' link and click on it
        # - Verify redirect on the start page
        start_page.verify_success_redirect_by_header_link()

    def test_redirect_by_click_button_in_footer(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Find 'OurApp' link in footer and click on it
            - Verify redirect on the start page
        """
        # - Find 'OurApp' link in footer and click on it
        # - Verify redirect on the start page
        start_page.verify_success_redirect_by_footer_link()

    def test_message_with_empty_username(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter valid data in password field
            - Find username field and clear it
            - Click on 'Sing In' button
            - Verify error message
        """
        # - Enter valid data in password field
        # - Find username field and clear it
        # - Click on 'Sing In' button
        start_page.sign_in(password='Qwerty123456')
        # - Verify error message
        start_page.verify_sign_in_error()
        self.log.info("Message is valid")

    def test_message_with_invalid_username_in_registration_form(self, start_page):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter invalid data in username field
            - Verify error message
        """
        # - Enter invalid data in username field
        start_page.sign_up(username=";%:?")
        # - Verify error message
        start_page.verify_validation_error_username_in_sigh_up()
        self.log.info("Validation message is present")

    def test_message_with_invalid_email_in_registration_form(self, start_page):
        """"
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter valid data in username field
            - Enter invalid data in email field
            - Enter valid data in password field
            - Click on 'Sing up for OurApp' button
            - Verify valid message
        """
        # - Enter valid data in username field
        # - Enter invalid data in email field
        # - Enter valid data in password field
        # - Click on 'Sing up for OurApp' button

        username_value = start_page.random_str()
        password_value = f"QWERTY{start_page.random_num()}"
        start_page.sign_up(username=username_value, email="estacc@gmail", password=password_value)
        # - Verify valid message
        start_page.verify_validation_error_email_in_sign_up()
        self.log.info('Message "You must provide a valid email address." is present')
