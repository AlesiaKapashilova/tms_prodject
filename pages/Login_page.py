from pages.Base_page import BasePage
from locators.Login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    login_url = BasePage.url + 'admin/login/?next=/admin/'

    def open_login_page(self):
        self.open(self.login_url)

    def fill_username_field(self, username):
        field = self.find_element(LoginPageLocators.USERNAME)
        field.click()
        field.send_keys(username)
        return field

    def fill_password_field(self, password):
        field = self.find_element(LoginPageLocators.PASSWORD)
        field.click()
        field.send_keys(password)
        return field

    def click_login_field(self):
        field = self.find_element(LoginPageLocators.LOG_IN)
        field.click()
        return field

    def login(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_login_field()
