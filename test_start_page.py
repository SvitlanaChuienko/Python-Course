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
