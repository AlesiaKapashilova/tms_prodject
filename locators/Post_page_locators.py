from selenium.webdriver.common.by import By


class Posts_Page_Locators:

    CHECKBOXES = (By.CLASS_NAME, "action-select")
    SELECT = (By.TAG_NAME, "select")
    GO = (By.CLASS_NAME, "button")
    DELETE = (By.CLASS_NAME, "deletelink")
    SURE = (By.XPATH, '//*[@id="content"]/form/div/input[2]')
    ALL_IMAGE = (By.PARTIAL_LINK_TEXT, "Post object (23)")
    DATE = (By.CLASS_NAME, "vDateField")
    TIME = (By.CLASS_NAME, "vTimeField")
    SAVE = (By.CSS_SELECTOR, "[type='submit']")
