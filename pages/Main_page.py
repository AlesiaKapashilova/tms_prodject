from pages.Base_page import BasePage
from locators.Main_page_locators import Main_Page_Locators


class MainPage(BasePage):

    def main_page(self):
        self.open_main_page()

    def find_all_pictures_data(self):
        images_on_page = self.find_elements(Main_Page_Locators.IMAGES_ON_PAGE)
        data_text = [el.text for el in images_on_page]
        return data_text

    def find_admin_button_field(self):
        field = self.find_element(Main_Page_Locators.GO_TO_ADMIN)
        return field

    def get_text_admin_button(self):
        field = self.find_admin_button_field()
        return field.text
