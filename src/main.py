from config import read_config
from plugins.tistory import TistoryBlog
from utils.selenium_util import create_browser

def main():
    """
    Main starting point
    """

    config_dict = read_config()
    print(config_dict)

    browser = create_browser()

    for blog_type in config_dict.get("blog", []):
        if blog_type == "tistory":
            blog = TistoryBlog(browser=browser)
            blog.login()

if __name__ == "__main__":
    main()
