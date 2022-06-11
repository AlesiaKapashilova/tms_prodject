from selenium.webdriver.common.by import By


class Login_Page_Locators:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOG_IN = (By.XPATH, '//*[@id="login-form"]/div[3]/input')
