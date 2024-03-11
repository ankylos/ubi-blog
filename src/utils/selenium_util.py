import time
import random

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options 

def create_browser(headless=False):
    opts = Options()
    if headless is True:
        opts.set_headless()

    browser = Firefox(options=opts)

    return browser

def send_keys_delayed(element, text):
   for char in text:
      element.send_keys(char)
      time.sleep(random.uniform(0.03,0.2))
