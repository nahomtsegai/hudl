import time

from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from utils.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    email_input = (By.CSS_SELECTOR, "[data-qa-id='email-input']")
    password_input = (By.CSS_SELECTOR, "[data-qa-id='password-input']")
    login_button = (By.CSS_SELECTOR, "[data-qa-id='login-btn']")
    remember_me_checkbox = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox']")
    remember_me_label = (By.CSS_SELECTOR, "[data-qa-id='remember-me-checkbox-label']")
    need_help_link = (By.CSS_SELECTOR, "[data-qa-id='need-help-link']")
    error_message = (By.CSS_SELECTOR, "[data-qa-id='error-display']")
    reset_email_input = (By.CSS_SELECTOR, "[data-qa-id='password-reset-input']")
    reset_password_button = (By.CSS_SELECTOR, "[data-qa-id='password-reset-submit-btn']")
    reset_invalid_message = (By.CSS_SELECTOR, "[data-qa-id='password-reset-error-display']")
    back_navigation_link = (By.CSS_SELECTOR, "a[class*='styles_backIconContainer']")
    signup_link = (By.CSS_SELECTOR, "a[href='/register/signup']")
    login_help_container = (By.CSS_SELECTOR, "[class*='loginHelpContainer'] h3")

    def get_email(self):
        return self.find_element_by_css_selector(LoginPage.email_input).text

    def set_email(self, email):
        self.set_element_value(LoginPage.email_input, email)

    def get_password(self):
        return self.find_element_by_css_selector(LoginPage.password_input).text

    def set_password(self, password):
        self.set_element_value(LoginPage.password_input, password)

    def click_remember_me_checkbox(self):
        self.find_element_by_css_selector(LoginPage.remember_me_label).click()

    def click_need_help_link(self):
        self.find_element_by_css_selector(LoginPage.need_help_link).click()
        self.find_element_by_link_text("support@hudl.com")

    def click_login_button(self):
        self.find_element_by_css_selector(LoginPage.login_button).click()
        return HomePage(self.driver)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def is_login_form_displayed(self):
        return self.find_element_by_css_selector(LoginPage.email_input).is_displayed()

    def click_fail_login_button(self):
        self.find_element_by_css_selector(LoginPage.login_button).click()
        self.text_to_be_present_in_element(LoginPage.error_message,
                                           "We didn't recognize that email and/or password.Need help?")

    def is_error_message_displayed(self):
        return self.find_element_by_css_selector(LoginPage.error_message).is_displayed()

    def is_reset_container_displayed(self):
        return self.find_element_by_css_selector(LoginPage.reset_password_button).is_displayed()

    def set_need_help_email(self, email):
        self.set_element_value(LoginPage.email_input, email)

    def get_need_help_email(self):
        return self.find_element_by_css_selector(LoginPage.reset_email_input).get_attribute("value")

    def set_need_help_email(self, email):
        self.set_element_value(LoginPage.reset_email_input, email)

    def is_reset_button_enabled(self):
        return self.find_element_by_css_selector(LoginPage.reset_password_button).is_enabled()

    def click_reset_invalid_email_button(self):
        self.find_element_by_css_selector(LoginPage.reset_password_button).click()
        self.text_to_be_present_in_element(LoginPage.reset_invalid_message, "That isn't a valid email address. Make "
                                                                            "sure to use the email@domain.com format.")

    def is_invalid_email_message_displayed(self):
        return self.find_element_by_css_selector(LoginPage.reset_invalid_message).is_displayed()

    def click_back_button(self):
        self.find_element_by_css_selector(LoginPage.back_navigation_link).click()
        self.find_element_by_link_text("Need help?")

    def click_signup_link(self):
        self.find_element_by_css_selector(LoginPage.signup_link).click()
