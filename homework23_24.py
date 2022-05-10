# 1. Клік на "Complex app for testing - QA" в хедері переводить на домашню сторінку
# 	*Steps to reproduce:*
# 	1. Відкрити сервіс https://qa-complex-app-for-testing.herokuapp.com/
# 	2. Клікнути на "Complex app for testing - QA" в хедері.
# 	3. Спостерігати результат в урлі.
# 	*Expected result:* відбувається перехід на домашню сторінку сервісу

import logging
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    def test_redirect_by_click_button_in_header(self):
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        driver.find_element(by=By.XPATH, value='.//a[@class="text-white"]').click()

        assert driver.find_element(by=By.XPATH, value='.//form[@id="registration-form"]')
        self.log.info("We are on the start page")
        driver.close()

    # 2. Клік на "OurApp" в футері переводить на домашню сторінку
    # 	*Steps to reproduce:*
    # 	1. Відкрити сервіс https://qa-complex-app-for-testing.herokuapp.com/
    # 	2. Клікнути на "OurApp" в футері.
    # 	3. Спостерігати результат в урлі.
    # 	*Expected result:* відбувається перехід на домашню сторінку сервісу

    def test_redirect_by_click_button_in_footer(self):
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        driver.find_element(by=By.XPATH, value='.//a[@class="text-muted"]').click()

        assert driver.find_element(by=By.XPATH, value='.//*[contains(text(),"Remember Writing?")]')
        self.log.info("Redirect is working")
        driver.close()

    # 3. Якшо в хедері при незаповненому полі "Username", клікнути кнопку "Sign In" - віддається помилка авторизації
    # 	*Steps to reproduce:*
    # 	1. Відкрити сервіс https://qa-complex-app-for-testing.herokuapp.com/
    # 	2. Заповнити поле "Password" данними (наприклад, Er45vhWq)
    # 	3. Поле "Username" залишити пустим.
    # 	4. Клікнути кнопку "Sign In".
    # 	5. Спостерігати результат в боді сторінки.
    # 	*Expected result:* віддається помилка авторизації з текстом "Invalid username / password"

    def test_message_with_empty_username(self):
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        password_value = driver.find_element(by=By.XPATH, value='.//header//form//input[@name="password"]')
        password_value.clear()
        password_value.send_keys("Er45vhWq")
        driver.find_element(by=By.XPATH, value='.//header//form//input[@name="username"]').clear()
        driver.find_element(by=By.XPATH, value='.//header//form//button').click()

        error_message = driver.find_element(by=By.XPATH, value='.//div[@class="alert alert-danger text-center"]')

        assert error_message.text == "Invalid username / pasword", "Text is not valid"
        self.log.info("Message is valid")
        driver.close()

    # 4. Якшо в формі реєстрації в поле "Username" ввести значення зі спецсимволів - віддається помилка валідації
    # 	*Steps to reproduce:*
    # 	1. Відкрити сервіс https://qa-complex-app-for-testing.herokuapp.com/
    # 	2. В формі реєстрації в поле "Username" ввести значення зі спецсимволів (наприклад, ;%:?)
    # 	3. Спостерігати результат над полем вводу.
    # 	*Expected result:* віддається помилка валідації "Username can only contain letters and numbers." над полем вводу

    def test_message_with_invalid_username(self):
        driver = WebDriver(executable_path="/home/svitlana/PycharmProjects/selenium-webdriver/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        username_value = driver.find_element(by=By.XPATH, value='.//*[@id="username-register"]')
        username_value.clear()
        username_value.send_keys(";%:?")
        sleep(2)

        assert driver.find_element(by=By.XPATH, value='//*[text()="Username can only contain letters and numbers."]')
        self.log.info("Validation message is present")
        driver.close()

    # 5. 	Перевірка повідомлення валідації, якшо передати невалідний email в формі реєстрації
    # 	*Steps to reproduce:*
    # 	1. Відкрити сервіс https://qa-complex-app-for-testing.herokuapp.com/
    # 	2. В формі реєстрації в поле "Username" ввести валідне значення (наприклад, John)
    # 	3. В поле "Email" ввести невалідне значення (наприклад, testacc@gmail)
    # 	4. В поле "Password" ввести валідне значення (наприклад, QWerty123456)
    # 	5. Клікнути кнопку "Sign up for OurApp"
    # 	6. Спостерігати результат на сторінці.
    # 	*Expected result:* відбувається перехід на особисту сторінку юзера.

    def test_message_with_invalid_email(self):
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

        assert driver.find_element(by=By.XPATH, value='.//form//div[@class="alert alert-danger small"]')
        self.log.info('Message "You must provide a valid email address." is present')
        driver.close()
