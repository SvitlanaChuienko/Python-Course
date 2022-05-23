import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User, text_example


class TestProfilePage:

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
        profile_page = start_page.success_sign_up(random_user)
        profile_page.sign_out()

        return random_user

    def test_update_exist_post_without_changing(self, start_page, registered_user):
        """
        - Pre-conditions:
            - Create driver
            - Open start page
            - Sing up as a user
            - Logout
        Steps:
            - Sign in as existing user
            - Click button 'Create Post'
            - Create post
            - Verify success message about create
            - Click on 'Edit Post' button
            - Enter the same data into fields, save updates
            - Verify success message about update
        """
        # - Sign in as existing user
        profile_page = start_page.sign_in(username=registered_user.username, password=registered_user.password)
        # - Click button 'Create Post'
        create_post_page = profile_page.navigate_to_create_post()
        # - Create post
        title = text_example(4)
        post_content = text_example(100)
        create_post_page.create_post(title, post_content)
        # - Verify success message about create
        create_post_page.verify_success_message_about_create_new_post()
        # - Click on 'Edit Post' button
        update_post_page = profile_page.navigate_to_update_post()
        # - Enter the same data into fields, save updates
        update_post_page.update_post(title, post_content)
        # - Verify success message about update
        update_post_page.verify_success_message_about_update_post()
