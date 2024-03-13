import time
from random import randrange
from datetime import datetime
from model.project_model import Project

proj_name_raw = datetime.now()


def test_add_new_project(app, data_creds):
    user = data_creds
    app.session.login(username=user.username, password=user.password)
    old_list = app.project.get_projects_list()
    proj_name = ("project " + str(proj_name_raw))[:-7]
    app.project.add_new_project(Project(name=proj_name))
    time.sleep(0)
    old_list.append(Project(name=proj_name))
    new_list = app.project.get_projects_list()
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    app.session.logout()


def test_delete_project(app, data_creds):
    user = data_creds
    app.session.login(username=user.username, password=user.password)
    old_list = app.project.get_projects_list()
    index = randrange(len(old_list))
    app.project.delete_by_index(index)
    old_list.remove(old_list[index])
    new_list = app.project.get_projects_list()
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    app.session.logout()