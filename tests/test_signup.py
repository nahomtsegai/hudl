import pytest

from pages.LoginPage import LoginPage
from data.TestUrls import TestUrls
from utils.BaseClass import BaseClass


class TestSignup(BaseClass):
    def test_is_signup_displayed(self):
        login_page = LoginPage(self.driver)
        login_page.click_signup_link()
        current_url = login_page.get_current_url()
        assert current_url == TestUrls.signup_page
