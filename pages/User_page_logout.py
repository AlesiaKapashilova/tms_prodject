from pages.Base_page import BasePage
from locators.User_add_locators import User_Add_Locators


class User_Page_Logout(BasePage):

    user_page = BasePage.url + 'admin/auth/user/'

    def open_user_page(self):
        self.open(self.user_page)

    def find_logout_field(self):
        field = self.find_element(User_Add_Locators.LOGOUT_LINK)
        return field

    def click_logout_field(self):
        field = self.find_logout_field()
        field.click()
        return field
