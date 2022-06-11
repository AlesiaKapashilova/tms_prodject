from selenium.webdriver.common.by import By


class Posts_Page_Locators:

    CHECKBOXES = (By.CLASS_NAME, "action-select")
    SELECT = (By.TAG_NAME, "select")
    GO = (By.CLASS_NAME, "button")
    SURE = (By.CSS_SELECTOR, "[type='submit']")
    NO_SURE = (By.CLASS_NAME, 'button cancel-link')
    ALL_IMAGE = (By.PARTIAL_LINK_TEXT, "Post object")
    DATE = (By.CLASS_NAME, "vDateField")
    TIME = (By.CLASS_NAME, "vTimeField")
    SAVE = (By.CSS_SELECTOR, "[type='submit']")
