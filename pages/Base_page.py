from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage:
    url = "http://localhost:8000/"

    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}")

    def open_main_page(self):
        return self.browser.get(self.url)

    def open(self, url):
        return self.browser.get(url)

    def refresh(self):
        return self.browser.refresh()

    def current_url(self):
        return self.browser.current_url
