from constants.profile_page import ProfilePageConstants

from pages.base_page import BasePage
from pages.utils import log_wrapper


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ProfilePageConstants()

    @log_wrapper
    def sign_out(self):
        """Sign out from current user profile"""
        self.click(self.constants.SIGN_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_wrapper
    def verify_sign_out_button(self):
        """Sing Out button is available for current user"""
        sign_out_button = self.wait_until_displayed(xpath=self.constants.SIGN_OUT_BUTTON_XPATH)
        assert sign_out_button.is_displayed()

    @log_wrapper
    def navigate_to_create_post(self):
        """Navigate to Create Post page"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    @log_wrapper
    def navigate_to_update_post(self):
        """Navigate to update exist post"""
        self.click(self.constants.EDIT_POST_BUTTON_XPATH)
        from pages.update_post_page import UpdatePostPage
        return UpdatePostPage(self.driver)
