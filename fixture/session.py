import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        try:
            if len(wd.find_elements_by_xpath("//input[@type='submit']")) > 0:
                # login
                wd.find_element_by_xpath("//input[@name='username']").click()
                wd.find_element_by_xpath('//input[@name="username"]').send_keys(username)
                wd.find_element_by_xpath("//input[@name='password']").click()
                wd.find_element_by_xpath('//input[@name="password"]').send_keys(password)
                wd.find_element_by_xpath("//input[@type='submit']").click()
        except:
            if self.is_logged_in_as(username):
                pass


    def logout(self):
        wd = self.app.wd
        time.sleep(0.2)  # этот нужен, что бы предыдущая страница успела прогрузиться
        wd.find_element_by_link_text("Logout").click()
        time.sleep(0.2)  # а этот что бы разлогин успел произойти перед следующим тестом

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username) -> bool:
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath('//*[@class="login-info-left"]//span').text

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
        else:
            pass

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
