import pytest
import allure
from configs.database_parsing import user_name, group_name
from pages.Database_page import DataBasePage


class TestDatabase():
    db = DataBasePage()

    @allure.feature('DB tests ')
    @allure.story('Проверка созданного пользователя в БД')
    @pytest.mark.positive
    def test_user_from_bd(self):
        with allure.step('Проверка на создание в БД пользователя'):
            assert self.db.user_from_db(user_name)

    def test_delete_user_from_bd(self):
        with allure.step('Проверка на удаление пользователя из БД'):
            self.db.delete_user_from_auth_user_groups(user_name, group_name)
            self.db.delete_user_from_db(user_name)
            assert self.db.checked_user_from_db('')

    def test_delete_group_from_bd(self):
        with allure.step('Проверка на удаление группы из БД'):
            self.db.delete_group_from_db(group_name)
            assert self.db.checked_group_from_db(group_name)