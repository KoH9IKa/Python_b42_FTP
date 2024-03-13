import time
from random import randrange
from datetime import datetime
from model.project_model import Project

proj_name_raw = datetime.now()


def test_get_projects_for_user(app, data_creds):
    user = data_creds
    projects = app.soap.get_projects_for_user(username=user.username, password=user.password)
    # projects = app.soap.get_projects_unstructured_data_for_user(username=user.username, password=user.password)
    print(projects)


def test_add_new_project_soap(app, data_creds):
    user = data_creds
    app.session.login(username=user.username, password=user.password)
    app.project.open_manage_projects()
    old_list = app.soap.get_projects_for_user(username=user.username, password=user.password)
    proj_name = ("project " + str(proj_name_raw))[:-7]
    app.project.add_new_project(Project(name=proj_name))
    time.sleep(0)
    old_list.append(Project(name=proj_name))
    new_list = app.soap.get_projects_for_user(username=user.username, password=user.password)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    app.session.logout()


def test_delete_project_soap(app, data_creds):
    user = data_creds
    app.session.login(username=user.username, password=user.password)
    old_list = app.soap.get_projects_for_user(username=user.username, password=user.password)
    app.project.open_manage_projects()
    index = randrange(len(old_list))
    app.project.delete_by_index(index)
    old_list.remove(old_list[index])
    new_list = app.soap.get_projects_for_user(username=user.username, password=user.password)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
    app.session.logout()
