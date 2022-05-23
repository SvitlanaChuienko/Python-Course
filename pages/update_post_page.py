from constants.update_post_page import UpdatePostPageConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class UpdatePostPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = UpdatePostPageConstants()

    @log_wrapper
    def update_post(self, title, post_content):
        """Update exist post"""
        self.fill_field(self.constants.POST_TITLE_XPATH, title)
        self.fill_field(self.constants.POST_CONTENT_XPATH, post_content)
        self.click(xpath=self.constants.SAVE_UPDATES_BUTTON_XPATH)

    @log_wrapper
    def verify_success_message_about_update_post(self):
        """Verify success message about updating an exist post"""
        success_message = self.wait_until_displayed(self.constants.MESSAGE_SUCCESS_UPDATING_POST_XPATH)
        assert success_message.text == self.constants.MESSAGE_SUCCESS_UPDATING_POST_TEXT
