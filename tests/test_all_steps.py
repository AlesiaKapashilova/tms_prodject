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


class TestAllSteps():
    db = DataBasePage()

    def test_user(self, login_page, browser):
        login_user = LoginPage(browser)
        login_user.fill_username_field(username)
        login_user.fill_password_field(password)
        login_user.click_login_field()
        assert login_user.current_url() == 'http://localhost:8000/admin/'

    def test_grop_from_ui(self, login_page, browser):
        self.db.add_group("Privat_group")
        groups = GroupsPage()
        groups.open_groups_page()
        groups.name_of_created_group()
        assert groups == "Privat_group"


    def test_user_add(self,login_page, browser):
        new_user = User_add_page(browser)
        new_user.click_add_field()
        new_user.fill_username_field(new_username)
        new_user.fill_password_field(new_password)
        new_user.fill_confirm_passwd_field(new_password)
        new_user.click_save_field()
        new_user.click_staff_field()
        new_user.click_add_to_group_field()
        new_user.click_save_field()

        assert self.db.user_from_group('Alesia', 'Privat_group')

    # def test_logout(self, login_page, browser):
    #     users_logout = User_Page_Logout(browser)
    #     page_logout = BasePage(browser)
    #     users_logout.click_logout_field()
    #     assert page_logout.current_url == 'http://localhost:8000/admin/logout/'
