from pages.Base_page import BasePage
from locators.User_add_locators import *


class User_add_page(BasePage):
    add_user_page = BasePage.url + 'admin/auth/user/add/'

    def open_add_user_page(self):
        self.open(self.add_user_page)

    def click_add_field(self):
        field = self.find_element(User_Add_Locators.USER_ADD)
        field.click()
        return field

    def fill_username_field(self, username):
        field = self.find_element(User_Add_Locators.USERNAME)
        field.click()
        field.send_keys(username)
        return field

    def fill_password_field(self, password):
        field = self.find_element(User_Add_Locators.PASSWORD)
        field.click()
        field.send_keys(password)
        return field

    def fill_confirm_passwd_field(self, password):
        field = self.find_element(User_Add_Locators.PASSWORD_CONFIRMATION)
        field.click()
        field.send_keys(password)
        return field

    def click_save_field(self):
        field = self.find_element(User_Add_Locators.SAVE_BUTTON)
        field.click()
        return field

    def click_staff_field(self):
        field = self.find_element(User_Add_Locators.STAFF_STATUS)
        field.click()
        return field

    def click_add_to_group_field(self):
        field = self.find_element(User_Add_Locators.ADD_TO_GROUP)
        field.click()
        return field

    def user_creation(self, new_username, new_password):
        self.click_add_field
        self.fill_username_field(new_username)
        self.fill_password_field(new_password)
        self.fill_confirm_passwd_field(new_password)
        self.click_save_field()
        self.click_staff_field()
        self.click_add_to_group_field()
        self.click_save_field()
