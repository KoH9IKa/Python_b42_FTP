import random
import time
from model.project_model import Project


class ProjectHelper:

    def __init__(self, app, base_url):
        self.app = app
        self.contact_cache = None
        self.base_url = base_url

    def open_manage_projects(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            url = f'{self.base_url}/manage_proj_page.php'
            wd.get(url)
        else:
            pass

    def get_projects_list(self):
        wd = self.app.wd
        self.open_manage_projects()
        list = []
        count = len(wd.find_elements_by_xpath('//table[@class="width100"][2]//tbody//tr'))
        # print(count)
        try:
            for n in range(3, count + 1):
                id = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').get_attribute(
                    'href')
                id = str(id).split("=")[1]
                name = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').text
                status = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[2]').text
                enabled = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[3]').text
                view_status = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[4]').text
                description = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td[5]').text
                list.append(Project(id=id, name=name, status=status, enabled=enabled, view_status=view_status,
                                    description=description))
            return list
        except:
            return list

    def add_new_project(self, project):
        self.open_manage_projects()
        self.create_new_project_button()
        self.fill_project_form(project)
        self.add_project_button_in_form()
        self.open_manage_projects()

    def create_new_project_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="button-small"][@value="Create New Project"]').click()

    def add_project_button_in_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="button"][@value="Add Project"]').click()

    def confirm_delete_button(self):
        self.delete_project_button_in_form()

    def delete_project_button_in_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@class="button"][@value="Delete Project"]').click()

    def fill_project_form(self, project, status_loc=None, view_loc=None):
        wd = self.app.wd
        name_loc = '//*[@name="name"]'
        status_selector_loc = '//select[@name="status"]'
        inherit_glob_cat_loc = '//input[@type="checkbox"]'
        view_status_selector_loc = '//select[@name="view_state"]'
        description_loc = '//textarea[@name="description"]'
        self.input_check_with_xpath(project.name, name_loc)
        self.selector_check(project.status, status_selector_loc, status_loc)
        if project.inherit is None:
            wd.find_element_by_xpath(inherit_glob_cat_loc).click()
        self.selector_check(project.view_status, view_status_selector_loc, view_loc)
        self.input_check_with_xpath(project.description, description_loc)

    def input_check_with_xpath(self, param, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_xpath(locator).click()
            wd.find_element_by_xpath(locator).clear()
            wd.find_element_by_xpath(locator).send_keys(param)
        else:  # Можно убрать елсе блок. Оставил что бы смотреть за шагами
            wd.find_element_by_xpath(locator).click()

    def selector_check(self, param, selector, locator):
        wd = self.app.wd
        if param is not None:
            wd.find_element_by_xpath(selector).click()  # открываем селектор
            if locator is not None:
                wd.find_element_by_css_selector(locator).click()  # 2й раз жмём на селектор, что бы закрыть его
            else:
                wd.find_element_by_xpath(selector).click()
        else:  # два раза жмём на селектор, что бы открыть и закрыть его
            wd.find_element_by_xpath(selector).click()
            wd.find_element_by_xpath(selector).click()

    def delete_by_index(self, index):
        self.open_project_by_index(index)
        self.delete_project_button_in_form()
        self.confirm_delete_button()
        self.open_manage_projects()

    def open_project_by_index(self, index):
        wd = self.app.wd
        n = index + 3
        wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').click()

