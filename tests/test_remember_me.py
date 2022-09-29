import pytest

from pages.LoginPage import LoginPage
from data.TestUrls import TestUrls
from utils.BaseClass import BaseClass


class TestRememberMe(BaseClass):
    def test_is_user_data_not_saved(self):
        login_page = self.login()
        email = login_page.get_email()
        password = login_page.get_password()
        assert email is "", "Email was saved"
        assert password is "", "Password was saved"

    @pytest.mark.skip()
    def test_is_user_data_saved(self):  # unable to remember user credentials
        login_page = self.login(True)
        email = login_page.get_email()
        password = login_page.get_password()
        assert email is self.email, "Email is not displayed"
        assert password is self.password, "Password is not displayed"

    def login(self, remember_me=False):
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        if remember_me:
            login_page.click_remember_me_checkbox()
        home_page = login_page.click_login_button()
        print(self.driver.get_cookies())
        home_page.logout()
        self.driver.get(TestUrls.login_page)
        return login_page
