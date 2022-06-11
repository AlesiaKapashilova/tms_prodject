from selenium.webdriver.common.by import By

class User_Add_Locators():
    USERNAME = (By.CLASS_NAME, 'username')
    PASSWORD = (By.CLASS_NAME, 'password1')
    PASSWORD_CONFIRMATION = (By.CLASS_NAME, 'password2')
    SAVE_BUTTON = (By.CLASS_NAME, 'default')
    LOGOUT_LINK = (By.XPATH, '//*[@id="user-tools"]/a[3]')
    STAFF_STATUS = (By.ID, "id_is_staff")
    ADD_TO_GROUP = (By.ID, "id_groups_add_all_link")
