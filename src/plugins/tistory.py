import os
import time

import markdown
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from interfaces import BlogManagerClass
from utils.selenium_util import send_keys_delayed

class TistoryBlog(BlogManagerClass):
    ROOT_URL = "https://www.tistory.com"
    LOGIN_URL = "https://www.tistory.com/auth/login#"
    NEW_POST_ENDPOINT = "manage/newpost/?type=post&returnURL=%2Fmanage%2Fposts%2F"

    def __init__(self, browser: WebDriver, blog_url: str, username: str, password: str):
        self.browser = browser
        self.blog_url = blog_url
        self.username = username
        self.password = password

    def login(self):
        self.browser.get(self.LOGIN_URL)
        time.sleep(2)

        self.browser.execute_script("kakaoAuth();")

        # Enter username
        el_username = self.browser.find_element(by=By.ID, value="loginId--1")
        # ActionChains(self.browser).click(el_username).perform()
        send_keys_delayed(el_username, self.username)

        # Enter password
        el_password = self.browser.find_element(by=By.ID, value="password--2")
        send_keys_delayed(el_password, self.password)

        # Login form
        el_login_btn = self.browser.find_element(by=By.CSS_SELECTOR, value="#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit")
        el_login_btn.click()

    def new_post(self, post_md: str):
        new_post_url = os.path.join(self.blog_url, self.NEW_POST_ENDPOINT)
        self.browser.get(new_post_url)
        time.sleep(5)

        # Change to markdown editor mode
        editor_mode_el = self.browser.find_element(by=By.ID, value="editor-mode-layer-btn-open")
        editor_mode_el.click()

        markdown_mode_el = self.browser.find_element(by=By.ID, value="editor-mode-markdown")
        markdown_mode_el.click()

        self.browser.switch_to().alert().accept()

        html = markdown.markdown(post_md)

        return 1

    def check_post_exists(self, post_title: str):
        return True
