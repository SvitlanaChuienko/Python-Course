import logging
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_start_page(self):
        """
        - Create driver
        - Open start page
        - Clear login field
        - Clear password field
        - Click on 'Sing In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Start page is opened")

        # Find login element
        login_field = driver.find_element(by=By.XPATH, value=".//header//form//input[@name='username']")

        # Clear login field
        self.log.info("Clearing login field...")
        login_field.clear()

        # Find password element
        password_field = driver.find_element(by=By.XPATH, value=".//header//form//input[@name='password']")

        # Clear password field
        self.log.info("Clearing password field...")
        password_field.clear()

        # Click on 'Sing In' button
        driver.find_element(by=By.XPATH, value=".//header//form//button").click()
        self.log.info("Button is clicked")
        sleep(1)

        # Verify error message
        error_message = driver.find_element(by=By.XPATH, value='.//div[@class="alert alert-danger text-center"]')
        self.log.info("Verifying error message")
        assert error_message.text == "Invalid username / pasword", "Text is not valid"

        # Close driver
        driver.close()

    # Створити тест (поглядаючи на існуючий), який буде первіряти інвалід логін.
    # Тобто заповнювати поля та первіряти помилку.

    def test_invalid_login_on_start_page(self):
        """
        - Create driver
        - Open start page
        - Find login field
        - Clear login field
        - Enter invalid data in login field
        - Find password field
        - Clear password field
        - Enter valid data in password field
        - Click on 'Sing In' button
        - Verify error message
        """
        # - Create driver
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")

        # - Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Start page is opened")

        # - Find login field
        login_field = driver.find_element(by=By.XPATH, value=".//header//form//input[@name='username']")

        # - Clear login field
        self.log.info("Clearing login field...")
        login_field.clear()

        # - Enter invalid data in login field
        login_field.send_keys('Qwerry1234')
        self.log.info("Login data is entered")
        sleep(1)

        # - Find password field
        password_field = driver.find_element(by=By.XPATH, value=".//header//form//input[@name='password']")

        # - Clear password field
        password_field.clear()
        self.log.info("Clearing password field...")

        # - Enter valid data in password field
        password_field.send_keys("test@gmail.com")
        self.log.info("Password data is entered")

        # - Click on 'Sing In' button
        driver.find_element(by=By.XPATH, value=".//header//form//button").click()
        self.log.info("Button is clicked")

        # - Verify error message
        error_message = driver.find_element(by=By.XPATH, value=".//*[text()='Invalid username / pasword']")
        self.log.info("Verifying error message...")

        assert error_message.text == "Invalid username / pasword", "Text is not valid"

        # Close driver
        driver.close()

    def test_redirect_by_click_button_in_header(self):
        """
        - Create driver
        - Open start page
        - Find 'Complex app for testing - QA' link and click on it
        - Verify redirect on the start page
        """
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        driver.find_element(by=By.XPATH, value='.//a[@class="text-white"]').click()

        assert driver.find_element(by=By.XPATH, value='.//form[@id="registration-form"]')
        self.log.info("We are on the start page")
        driver.close()

    def test_redirect_by_click_button_in_footer(self):
        """
        - Create driver
        - Open start page
        - Find 'OurApp' link in footer and click on it
        - Verify redirect on the start page
        """
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        driver.find_element(by=By.XPATH, value='.//a[@class="text-muted"]').click()

        assert driver.find_element(by=By.XPATH, value='.//*[contains(text(),"Remember Writing?")]')
        self.log.info("Redirect is working")
        driver.close()

    def test_message_with_empty_username(self):
        """
        - Create driver
        - Open start page
        - Find password field
        - Clear password field
        - Enter valid data in password field
        - Find username field and clear it
        - Click on 'Sing In' button
        - Verify error message
        """
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        password_value = driver.find_element(by=By.XPATH, value='.//header//form//input[@name="password"]')
        password_value.clear()
        password_value.send_keys("Er45vhWq")
        driver.find_element(by=By.XPATH, value='.//header//form//input[@name="username"]').clear()
        driver.find_element(by=By.XPATH, value='.//header//form//button').click()

        error_message = driver.find_element(by=By.XPATH,
                                            value='.//div[@class="alert alert-danger text-center"]')

        assert error_message.text == "Invalid username / pasword", "Text is not valid"
        self.log.info("Message is valid")
        driver.close()

    def test_message_with_invalid_username(self):
        """
        - Create driver
        - Open start page
        - Find username field in registration form
        - Clear username field
        - Enter invalid data in username field
        - Verify error message
        """
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username_value = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username_value.clear()
        username_value.send_keys(";%:?")
        sleep(2)

        assert driver.find_element(by=By.XPATH,
                                   value='//*[text()="Username can only contain letters and numbers."]')
        self.log.info("Validation message is present")
        driver.close()

    def test_message_with_invalid_email(self):
        """"
        - Create driver
        - Open start page
        - Find username field
        - Clear username field
        - Enter valid data in username field
        - Find email field
        - Clear email field
        - Enter invalid data in email field
        - Find password field
        - Clear password field
        - Enter valid data in password field
        - Click on 'Sing up for OurApp' button
        - Verify valid message
        """
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username_field = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username_field.clear()
        username_field.send_keys("John123")
        email_field = driver.find_element(by=By.XPATH, value='.//*[@id="email-register"]')
        email_field.clear()
        email_field.send_keys("testacc@gmail")
        password_field = driver.find_element(by=By.XPATH, value='.//*[@id="password-register"]')
        password_field.clear()
        password_field.send_keys("QWerty123456")
        sleep(2)
        driver.find_element(by=By.XPATH, value='.//body//form//button[@type="submit"]').click()

        assert driver.find_element(by=By.XPATH, value='.//*[text()="You must provide a valid email address."]')
        self.log.info('Message "You must provide a valid email address." is present')
        driver.close()
