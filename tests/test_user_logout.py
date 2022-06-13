import pytest
import allure
from selenium import webdriver
from configs.common_parsing import username, password, new_username, \
    new_password, group_name
from pages.Admin_page import AdminPage
from pages.Database_page import DataBasePage
from pages.Login_page import *
from pages.User_add_page import *
from pages.Group_page import *
from pages.User_page_logout import *
from pages.Base_page import *


class TestLogout():
    def test_logout(self, login_page, browser):
        login_user = LoginPage(browser)
        login_user.fill_username_field(username)
        login_user.fill_password_field(password)
        login_user.click_login_field()
        users_logout = User_Page_Logout(browser)
        users_logout.click_logout_field()
        assert (browser.current_url.startswith("http://localhost:8000/admin/logout/"))

