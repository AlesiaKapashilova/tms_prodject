import pytest
import allure
from selenium import webdriver
from configs.common_parsing import username, password, new_username, new_password, group_name
from pages.Login_page import *
from pages.User_add_page import *
from pages.Group_page import *

class TestAllSteps():
    def test_user(self, login_page, browser):
        login_user = LoginPage(browser)
        login_user.fill_username_field(username)
        login_user.fill_password_field(password)
        login_user.click_login_field()
        assert login_user.current_url() == 'http://localhost:8000/admin/'

    def test_user_add(self, browser):
        new_user = User_add_page(browser)
        new_user.click_add_field()
        new_user.fill_username_field(new_username)
        new_user.fill_password_field(new_password)
        new_user.fill_confirm_passwd_field(new_password)
        new_user.click_save_field()
        new_user.click_staff_field()
        new_user.click_add_to_group_field()
        new_user.click_save_field()
        assert new_user.current_url() == 'http://localhost:8000/admin/auth/user/'

    def test_checked_groups(self, browser):
        user_groups = GroupsPage(browser)
        user_groups.groups_url()
        user_groups.name_of_created_group()
        assert user_groups == group_name



