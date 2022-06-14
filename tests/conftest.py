import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from configs.common_parsing import username, password, new_username, \
    new_password
from pages.Database_page import DataBasePage
from pages.Group_page import GroupsPage
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.User_add_page import User_add_page
from pages.User_page_logout import User_Page_Logout
from pages.Post_page import PostsPage



@pytest.fixture(scope='class')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(
        executable_path="tests/chromedriver",
        options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    yield login_page
    browser.quit()


@pytest.fixture(scope="class")
def main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    yield main_page
    browser.quit()


@pytest.fixture()
def groups_page(browser):
    login_page = LoginPage(browser)
    login_page.login(username, password)
    groups_page = GroupsPage(browser)
    groups_page.open_groups_page()
    yield groups_page


@pytest.fixture()
def add_user_page(browser):
    add_user_page = User_add_page(browser)
    add_user_page.open_add_user_page()
    yield add_user_page


@pytest.fixture()
def log_in_new_user(browser):
    user_page = User_Page_Logout(browser)
    user_page.click_logout_field()
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.login(new_username, new_password)
    admin_page = WelcomePage(browser)
    admin_page.open_admin_page()
    yield admin_page
    browser.quit()


@pytest.fixture(scope="class")
def posts_page(browser):
    posts_page = PostsPage(browser)
    posts_page.open_posts_page()
    yield posts_page
    browser.quit()
