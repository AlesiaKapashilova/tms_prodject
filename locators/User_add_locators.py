from selenium.webdriver.common.by import By

class User_Add_Locators():
    USER_ADD = (By.XPATH, '//*[@id="content-main"]/div[2]/table/tbody/tr[2]/td[1]/a')
    USERNAME = (By.NAME, 'username')
    PASSWORD = (By.NAME, 'password1')
    PASSWORD_CONFIRMATION = (By.NAME, 'password2')
    SAVE_BUTTON = (By.NAME, '_save')
    LOGOUT_LINK = (By.XPATH, '//*[@id="user-tools"]/a[3]')
    STAFF_STATUS = (By.ID, "id_is_staff")
    ADD_TO_GROUP = (By.ID, "id_groups_add_all_link")
