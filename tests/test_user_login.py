import allure
import pytest
from configs.common_parsing import new_username, new_password, admin_link
from pages.Login_page import *


class TestLoginUser():

    @allure.feature('UI tests')
    @allure.story('Login new user in positive')
    @pytest.mark.positive
    def test_login_new_user(self, login_page, browser):
        with allure.step('Authorization steps in the UI by a new user'):
            login_new_user = LoginPage(browser)
            login_new_user.fill_username_field(new_username)
            login_new_user.fill_password_field(new_password)
            login_new_user.click_login_field()
            with allure.step('Checking for Successful Authorization'):
                assert login_new_user.current_url() == admin_link
