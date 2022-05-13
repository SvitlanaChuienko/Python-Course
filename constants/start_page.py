class StartPageConstants:
    # SIgn In
    SIGN_IN_USERNAME_XPATH = ".//header//form//input[@name='username']"
    SIGN_IN_PASSWORD_XPATH = ".//header//form//input[@name='password']"
    SIGH_IN_BUTTON_XPATH = ".//header//form//button"
    SIGN_IN_ERROR_MESSAGE_XPATH = './/div[@class="alert alert-danger text-center"]'
    SIGN_IN_ERROR_MESSAGE_TEXT = "Invalid username / pasword"

    # Sign Up
    REGISTRATION_FORM_XPATH = './/form[@id="registration-form"]'
    SIGN_UP_USERNAME_XPATH = './/*[@id="username-register"]'
    SIGN_UP_EMAIL_XPATH = './/*[@id="email-register"]'
    SIGN_UP_PASSWORD_XPATH = './/*[@id="password-register"]'
    SIGN_UP_BUTTON_XPATH = './/body//form//button[@type="submit"]'
    SIGN_UP_VALIDATION_ERROR_USERNAME_XPATH = '//*[text()="Username can only contain letters and numbers."]'
    SIGN_UP_VALIDATION_ERROR_EMAIL_XPATH = './/*[text()="You must provide a valid email address."]'

    # Profile page
    SIGN_OUT_BUTTON_XPATH = ".//button[text()='Sign Out']"

    # Links
    LINK_IN_HEADER_XPATH = './/a[@class="text-white"]'
    LINK_IN_FOOTER_XPATH = './/a[@class="text-muted"]'
