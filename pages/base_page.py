from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=10)

    def wait_until_clickable(self, xpath):
        """Wait until element is clickable"""
        return self.waiter.until(method=expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    def wait_until_displayed(self, xpath):
        """Wait until element is displayed"""
        return self.waiter.until(method=expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    def is_element_exist(self, xpath):
        """Check is the element exist"""
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except(TimeoutError, NoSuchElementException):
            return False

    def fill_field(self, xpath, value):
        """Enter data into the field"""
        field = self.wait_until_clickable(xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath):
        """Find and click the element"""
        self.wait_until_clickable(xpath).click()
