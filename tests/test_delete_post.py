from configs.common_parsing import username, password, data, time, new_date
from pages.Login_page import *
from pages.Main_page import MainPage
from pages.Post_page import PostsPage
import pytest
import allure


class TestDeletePost():

    def test_first_pic_is_deleted(self, browser):
        with allure.step('Log in with admin'):
            login_page = LoginPage(browser)
            login_page.open_login_page()
            login_page.login(username, password)
            with allure.step('Open page with pics posts'):
                posts_page = PostsPage(browser)
                posts_page.open_posts_page()
                with allure.step('Find first pic and set new data'):
                    posts_page.set_new_date_and_time(data, time)
                    with allure.step('Delete first pic'):
                        posts_page.delete_first_pic()
                        with allure.step('Go to main page '
                                         'and collect all pics dates'):
                            main_page = MainPage(browser)
                            main_page.open_main_page()
                            all_pic_data = main_page.find_all_pictures_data()
                            with allure.step('Check data of deleted pic is '
                                             'not in collected dates'):
                                assert new_date not in all_pic_data
