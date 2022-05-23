import logging

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        user = User()
        user.fill_properties()
        return user

    @pytest.fixture(scope="function")
    def registered_user(self, start_page, random_user):
        hello_user_page = start_page.sign_up(random_user)
        hello_user_page.profile_page.sign_out()
        return random_user

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

        # - Verify error message
        start_page.verify_sign_in_error()

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

        # - Verify error message
        start_page.verify_sign_in_error()

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
        start_page.sign_up_with_optional_variables(username=";%:?")
        # - Verify error message
        start_page.click_and_verify_validation_error_username_in_sigh_up()

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
        start_page.sign_up_with_optional_variables(username="User", email="estacc@gmail", password="Qwerty123456")
        # - Verify valid message
        start_page.click_and_verify_validation_error_email_in_sign_up()

    def test_success_registration(self, start_page, random_user):
        """"
        - Pre-conditions:
            - Create driver
            - Open start page
        - Steps:
            - Enter valid data in username, email and password fields
            - Click on 'Sing up for OurApp' button
            - Verify success registration
        """
        # - Enter valid data in username, email and password fields
        # - Click on 'Sing up for OurApp' button
        profile_page = start_page.success_sign_up(random_user)
        profile_page.verify_sign_out_button()
