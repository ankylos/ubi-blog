from selenium.webdriver.remote.webdriver import WebDriver
from utils.selenium_util import create_browser

class TistoryBlog:
    LOGIN_URL = "https://www.tistory.com/auth/login#"

    def __init__(self, browser: WebDriver):
        self.browser = browser

    def login(self):
        self.browser.get(self.LOGIN_URL)
        self.browser.execute_script("kakaoAuth();")
