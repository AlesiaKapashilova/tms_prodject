from pages.Base_page import BasePage
from locators.Group_page_locators import Group_Page_Locators
from selenium.webdriver.common.by import By


class GroupsPage(BasePage, Group_Page_Locators):
    group_url = BasePage.url + 'admin/auth/group/'

    def open_group_page(self):
        self.open(self.group_url)


    def check_group_exist(self, group):
        groups = self.find_elements((By.LINK_TEXT, group))
        if groups is not None:
            return True

        return False
