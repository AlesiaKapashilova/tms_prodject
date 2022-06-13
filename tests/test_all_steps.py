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

    @allure.feature('UI tests')
    @allure.story('Login in positive')
    @pytest.mark.positive
    def test_user(self, login_page, browser):
        with allure.step('Шаги по авторизации админа'):
            login_user = LoginPage(browser)
            login_user.fill_username_field(username)
            login_user.fill_password_field(password)
            login_user.click_login_field()
            with allure.step('Проверка перехода на страницу в админке'):
                assert login_user.current_url() == 'http://localhost:8000/admin/'

    @allure.feature('UI tests ')
    @allure.story('Проверка на UI созданной группы в БД')
    @pytest.mark.positive
    def test_group_from_ui(self, login_page, browser):
        with allure.step('Шаги по подключению к БД и сравнения с UI'):
            self.db.add_group("Privat_group")
            groups = GroupsPage(browser)
            groups.open_group_page()
        with allure.step('Проверка созданной группы на UI'):
            assert groups.check_group_exist("Privat_group")

    @allure.feature('UI and DB tests ')
    @allure.story('Проверка в БД созданного юзера в группе')
    @pytest.mark.positive
    def test_user_add(self, login_page, browser):
        with allure.step(
                'Подключение к БД и Шаги по созданию пользователя с группой в UI'):
            new_user = User_add_page(browser)
            new_user.open_add_user_page()
            new_user.fill_username_field(new_username)
            new_user.fill_password_field(new_password)
            new_user.fill_confirm_passwd_field(new_password)
            new_user.click_save_field()
            new_user.click_staff_field()
            new_user.click_add_to_group_field()
            new_user.click_save_field()
        with allure.step('Проверка на создание в БД пользователя в группе'):
            assert self.db.user_from_group('Alesia', 'Privat_group')

    @allure.feature('DB tests ')
    @allure.story('Проверка созданного пользователя в БД')
    @pytest.mark.positive
    def test_user_from_bd(self):
        with allure.step('Проверка на создание в БД пользователя в группе'):
         assert self.db.user_from_db('Alesia')
