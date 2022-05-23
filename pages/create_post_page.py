from constants.create_post_page import CreatePostPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConstants()

    @log_wrapper
    def create_post(self, title, post_content):
        """Create post by using available values"""
        self.fill_field(self.constants.POST_TITLE_XPATH, title)
        self.fill_field(self.constants.POST_CONTENT_XPATH, post_content)
        self.click(xpath=self.constants.SAVE_NEW_POST_BUTTON_XPATH)

    @log_wrapper
    def verify_success_message_about_create_new_post(self):
        """Verify success message about creation the new post"""
        success_message = self.wait_until_displayed(self.constants.MESSAGE_SUCCESS_CREATING_POST_XPATH)
        assert success_message.text == self.constants.MESSAGE_SUCCESS_CREATING_POST_TEXT
