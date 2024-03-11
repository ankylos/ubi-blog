from enum import Enum

class BlogTypes(Enum):
    TISTORY = "tistory"

class BlogManagerClass:
    def __init__(self):
        pass

    def login(self):
        """
        Login to the blog/media
        """
        pass

    def new_post(self, post_md: str) -> int:
        """
        Create new post in markdown format
        """
        pass

    def check_post_exists(self, post_title: str) -> bool:
        """
        Checks whether a post already exists
        """
        pass
