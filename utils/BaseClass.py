import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.usefixtures("setup", "user_data")
class BaseClass:

    def find_element_by_css_selector(self, locator):
        self.wait_for_element_exists(locator)
        element = self.driver.find_element(*locator)
        return element

    def set_element_value(self, locator, value):
        element = self.find_element_by_css_selector(locator)
        element.clear()
        element.send_keys(value)

    def wait_for_element_exists(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(locator), "Element not found")

    def find_element_by_link_text(self, text):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)), "Link not found")

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    def get_current_url(self):
        return self.driver.current_url
