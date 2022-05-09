# - Створити тест на реєстрацію.
# Нюанс номер 1: Тест має проходити більше 1 разу, тобто данні в полях мають бути повністю або чатсково випадковими
# (Оскільки той самий юзер не може бути зареєстрований двічі)
# Нюанс номер 2: Вам потрібно самостійно придумати перевірку, що буде підверджувати успішність реєстрації.
# Це може бути перевірка наявності якогось поля, його значення, повідомлення або первірка URL.
import logging
import time
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestRegistrationPage():
    log = logging.getLogger()

    def test_registration(self):
        """
            - Create driver
            - Open start page
            - Find Username field
            - Clear Username field
            - Enter valid data
            - Find Email field
            - Clear Email field
            - Enter valid data
            - Find Password field
            - Clear Password field
            - Enter valid data
            - Click on 'Sing up for OurApp' button
            - Verify valid message about registration
        """

        # - Create driver
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")

        # - Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Start page is opened")

        # - Find Username field
        username_field = driver.find_element(
            by=By.XPATH,
            value='.//form[@id="registration-form"]//input[@id="username-register"]'
        )

        # - Clear Username field
        username_field.clear()
        self.log.info("Username field is clear")

        # - Enter valid data
        username_field.send_keys("John")
        self.log.info("Username data is entered")

        # - Find Email field
        email_field = driver.find_element(
            by=By.XPATH,
            value='.//form[@id="registration-form"]//input[@id="email-register"]'
        )

        # - Clear Email field
        email_field.clear()
        self.log.info("Email field is clear")

        # - Enter valid data
        email_field.send_keys("qwerty123@gmail.com")
        self.log.info("Email data is entered")

        # - Find Password field
        password_field = driver.find_element(
            by=By.XPATH,
            value='.//form[@id="registration-form"]//input[@id="password-register"]'
        )

        # - Clear Password field
        password_field.clear()
        self.log.info("Password field is clear")

        # - Enter valid data
        password_field.send_keys("12characters")
        self.log.info("Password data is entered")

        # - Click on 'Sing up for OurApp' button
        sleep(3)
        driver.find_element(by=By.XPATH, value=".//body//form//button[@type='submit']").click()
        # button.click()
        self.log.info("Button is clicked")
        # sleep(5)

        # - Verify valid registration by checking logout button
        check_registration = driver.find_element(by=By.XPATH, value='.//form[@id="chatForm"]')
        self.log.info("Sing Out button is found")

        assert check_registration.is_displayed(), "Registration is failed"

        # Close driver
        driver.close()
