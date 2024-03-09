from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "chromedriver" or browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "geckodriver" or browser == "firefox" or browser == "ff":
            self.wd = webdriver.Firefox()
        elif browser == "iedriver" or browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(0.5)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self, base_url)
        self.base_url = base_url

    def is_valid(self):
        try:
            # noinspection PyStatementEffect
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)  # если мы не вошли или находимся не на хоум пейдж - идём по адресу


    def destroy(self):
        self.wd.quit()
