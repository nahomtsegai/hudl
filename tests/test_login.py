from pages.LoginPage import LoginPage
from utils.BaseClass import BaseClass


class TestLogin(BaseClass):
    def test_login_successful(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        home_page = login_page.click_login_button()
        is_displayed = home_page.is_homepage_link_displayed()
        assert is_displayed is True, "Expected to login successfully"

    def test_login_with_incorrect_password(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password("incorrect_password")
        login_page.click_fail_login_button()
        is_displayed = login_page.is_error_message_displayed()
        assert is_displayed is True, "Expected login failure message to be displayed"
