from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/")

    def destroy(self):
        self.wd.quit()


    def is_not_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False