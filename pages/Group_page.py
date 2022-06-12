from pages.Base_page import BasePage
from locators.Group_page_locators import Group_Page_Locators


class GroupsPage(BasePage):

    groups_url = BasePage.url + 'admin/auth/group/'

    def open_groups_page(self):
        self.open(self.groups_url)

    def name_of_created_group(self):
        my_group = self.find_element(Group_Page_Locators.GROUP_FOR_USER)
        return my_group