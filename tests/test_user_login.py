from configs.common_parsing import new_username, new_password
from pages.Login_page import *

class TestLoginUser():
    def test_login_new_user(self, login_page, browser):
        login_new_user = LoginPage(browser)
        login_new_user.fill_username_field(new_username)
        login_new_user.fill_password_field(new_password)
        login_new_user.click_login_field()
        assert login_new_user.current_url() == 'http://localhost:8000/admin/'