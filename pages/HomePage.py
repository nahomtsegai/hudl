from selenium.webdriver.common.by import By

from utils.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait_for_element_exists(HomePage.homepage_link)

    homepage_link = (By.CSS_SELECTOR, "[data-qa-id='webnav-globalnav-home']")
    user_profile_dropdown = (By.CSS_SELECTOR, "div.hui-globalusermenu")
    logout_button = (By.CSS_SELECTOR, "[data-qa-id='webnav-usermenu-logout']")

    def is_homepage_link_displayed(self):
        return self.find_element_by_css_selector(HomePage.homepage_link).is_displayed()

    def click_header_profile(self):
        self.find_element_by_css_selector(HomePage.user_profile_dropdown).click()

    def logout(self):
        self.click_header_profile()
        self.find_element_by_css_selector(HomePage.logout_button).click()
