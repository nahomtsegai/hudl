from utils.BaseClass import BaseClass

from pages.LoginPage import LoginPage


class TestNeedHelp(BaseClass):
    def test_is_need_help_container_displayed(self):
        login_page = LoginPage(self.driver)
        login_page.click_need_help_link()
        is_displayed = login_page.is_reset_container_displayed()
        assert is_displayed is True, "Reset container is not displayed"

    def test_email_persists_in_help_form(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.click_need_help_link()
        email = login_page.get_need_help_email()
        is_enabled = login_page.is_reset_button_enabled()
        assert email == self.email
        assert is_enabled is True

    def test_set_valid_email(self):
        login_page = LoginPage(self.driver)
        login_page.click_need_help_link()
        login_page.set_need_help_email(self.email)
        email = login_page.get_need_help_email()
        assert email == self.email, "Email did not update"

    def test_invalid_email(self):
        login_page = LoginPage(self.driver)
        login_page.click_need_help_link()
        login_page.set_need_help_email("invalid_email_address")
        login_page.click_reset_invalid_email_button()
        is_message_displayed = login_page.is_invalid_email_message_displayed()
        assert is_message_displayed is True, "Error message did not display"

    def test_reset_button_disabled(self):
        login_page = LoginPage(self.driver)
        login_page.click_need_help_link()
        is_enabled = login_page.is_reset_button_enabled()
        assert is_enabled is False, "Password reset button is enabled"

        login_page.set_need_help_email(self.email)
        is_enabled = login_page.is_reset_button_enabled()
        assert is_enabled is True, "Password reset button is disabled"

    def test_back_button_directs_to_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.click_need_help_link()
        login_page.click_back_button()
        is_displayed = login_page.is_login_form_displayed()
        assert is_displayed is True, "Login form is not displayed"

