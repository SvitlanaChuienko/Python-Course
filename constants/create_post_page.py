class CreatePostPageConstants:
    POST_TITLE_XPATH = './/input[@id="post-title"]'
    POST_CONTENT_XPATH = './/textarea[@id="post-body"]'
    SAVE_NEW_POST_BUTTON_XPATH = './/*//button[text()="Save New Post"]'
    MESSAGE_SUCCESS_CREATING_POST_XPATH = './/div[@class="alert alert-success text-center"]'
    MESSAGE_SUCCESS_CREATING_POST_TEXT = 'New post successfully created.'
    SAVE_UPDATES_BUTTON_XPATH = './/*//button[text()="Save Updates"]'
    MESSAGE_SUCCESS_UPDATING_POST_TEXT = 'Post successfully updated.'
