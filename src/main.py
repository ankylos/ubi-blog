import os

from dotenv import load_dotenv
load_dotenv()

from config import read_config
from plugins.tistory import TistoryBlog
from utils.selenium_util import create_browser
from interfaces import BlogTypes

def main():
    """
    Main starting point
    """

    config_dict = read_config()
    print(config_dict)

    browser = create_browser()
    browser.implicitly_wait(20)

    for blog_type, blog_info in config_dict["blogs"].items():
        if blog_type == BlogTypes.TISTORY.value:
            blog = TistoryBlog(
                browser=browser,
                blog_url=blog_info["blog_url"],
                username=os.getenv("TISTORY_USERNAME", ""),
                password=os.getenv("TISTORY_PASSWORD", "")
            )
            print("logging in")
            blog.login()

            print("Creating new post")
            blog.new_post("hello")

if __name__ == "__main__":
    main()
