import pytest
import allure
from configs.common_parsing import username, password, logout_link, admin_link
from pages.Login_page import *
from pages.User_page_logout import *


class TestLogout():
    @allure.feature('UI tests')
    @allure.story('Login new user in positive')
    @pytest.mark.positive
    def test_logout(self, login_page, browser):
        with allure.step('Шаги авторизации в UI'):
            login_user = LoginPage(browser)
            login_user.fill_username_field(username)
            login_user.fill_password_field(password)
            login_user.click_login_field()
            users_logout = User_Page_Logout(browser)
            users_logout.click_logout_field()
            with allure.step('Проверка logout'):
                assert (browser.current_url.startswith(logout_link))

    def test_login(self, login_page, browser):
        with allure.step('Шаги по авторизации админа'):
            login_user = LoginPage(browser)
            login_user.logout()
            login_user.fill_username_field(username)
            login_user.fill_password_field(password)
            login_user.click_login_field()
        with allure.step('Проверка перехода на страницу в админке'):
            assert login_user.current_url() == admin_link
