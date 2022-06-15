from pages.Base_page import BasePage
from locators.Post_page_locators import Posts_Page_Locators


class PostsPage(BasePage):

    posts_url = BasePage.url + 'admin/app/post/'

    def open_posts_page(self):
        self.open(self.posts_url)

    def find_first_pic_field(self):
        field = self.find_elements(Posts_Page_Locators.ALL_IMAGE)
        return field

    def click_first_pic_field(self):
        field = self.find_first_pic_field()
        field.click()
        return field

    def find_date_field(self):
        field = self.find_element(Posts_Page_Locators.DATE)
        return field

    def find_time_field(self):
        field = self.find_element(Posts_Page_Locators.TIME)
        return field

    def set_new_date(self, date):
        field = self.find_date_field()
        field.clear()
        field.send_keys(date)
        return field

    def set_new_time(self, time):
        field = self.find_time_field()
        field.clear()
        field.send_keys(time)
        return field

    def find_delete_field(self):
        field = self.find_element(Posts_Page_Locators.DELETE)
        return field

    def click_delete_field(self):
        field = self.find_delete_field()
        field.click()
        return field

    def find_sure_field(self):
        field = self.find_element(Posts_Page_Locators.SURE)
        return field

    def click_sure_field(self):
        field = self.find_sure_field()
        field.click()
        return field

    def set_new_date_and_time(self, data, time):
        self.click_first_pic_field()
        self.set_new_date(data)
        self.set_new_time(time)
        self.click_delete_field()

    def delete_first_pic(self):
        self.click_sure_field()
