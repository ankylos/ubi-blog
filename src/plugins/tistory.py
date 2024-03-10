import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.selenium_util import create_browser

class TistoryBlog:
    LOGIN_URL = "https://www.tistory.com/auth/login#"

    def __init__(self, browser: WebDriver, username: str, password: str):
        self.username = username
        self.password = password
        self.browser = browser

    def login(self):
        self.browser.get(self.LOGIN_URL)
        self.browser.execute_script("kakaoAuth();")

        time.sleep(5)
        # Enter username
        el_username = self.browser.find_element(by=By.ID, value="loginId--1")
        el_username.send_keys(self.username)

        # Enter password
        el_password = self.browser.find_element(by=By.ID, value="password--2")
        el_password.send_keys(self.password)

        # Login form
        el_form = self.browser.find_element(by=By.CSS_SELECTOR, value="form")
        el_form.submit()
