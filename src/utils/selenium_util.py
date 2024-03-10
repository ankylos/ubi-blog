from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options 

def create_browser(headless=False):
    opts = Options()
    if headless is True:
        opts.set_headless()

    browser = Firefox(options=opts)

    return browser
