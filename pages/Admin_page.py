from locators.Admin_page_locators import AdminPageLocators
from pages.Base_page import BasePage


class AdminPage(BasePage):

    admin_url = BasePage.url + '/admin/'

    def open_admin_page(self):
        self.open(self.admin_url)

    def find_welcome_name_field(self):
        field = self.find_element(AdminPageLocators.WELCOME_NAME)
        return field

    def get_welcome_name_text(self):
        name = self.find_welcome_name_field()
        return name.text
