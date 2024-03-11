from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:

    def __init__(self, browser, config):
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
        self.project = ProjectHelper(self, config['web']['baseUrl'])
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

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
