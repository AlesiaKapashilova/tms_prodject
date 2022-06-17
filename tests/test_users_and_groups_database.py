import pytest
import allure
from configs.database_parsing import user_name, group_name
from pages.Database_page import DataBasePage


class TestDatabase():
    db = DataBasePage()

    @allure.feature('DB tests')
    @allure.story('Checking the created user in the database')
    @pytest.mark.positive
    def test_user_from_bd(self):
        with allure.step('Check for creation in the user database'):
            assert self.db.user_from_db(user_name)

    @allure.feature('DB tests')
    @allure.story('Checking the created user in the database')
    @pytest.mark.positive
    def test_delete_user_from_bd(self):
        with allure.step(
                'Steps to remove user from auth_user_groups table and group from database'):
            self.db.delete_user_from_auth_user_groups(user_name, group_name)
            self.db.delete_user_from_db(user_name)
            with allure.step(
                    'Checking if a user has been deleted from the database'):
                assert self.db.checked_user_from_db('')

    @allure.feature('DB tests')
    @allure.story('Steps to delete a group from the database')
    @pytest.mark.positive
    def test_delete_group_from_bd(self):
        with allure.step(''):
            self.db.delete_group_from_db(group_name)
            with allure.step(
                    'Checking if a group has been deleted from the database'):
                assert self.db.checked_group_from_db(group_name)
