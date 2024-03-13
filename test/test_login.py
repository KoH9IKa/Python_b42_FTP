import time


def test_login(app, data_creds):
    user = data_creds
    app.session.login(username=user.username, password=user.password)
    assert app.session.is_logged_in_as(user.username)
    app.session.logout()
