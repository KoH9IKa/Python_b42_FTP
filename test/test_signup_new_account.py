import string
import random


def random_username(prefix, maxlen):
    return prefix + "".join([random.choice(string.ascii_letters) for i in range(random.randrange(maxlen))])


def test_sign_up_new_account(app):
    username = random_username('user_', 10)
    email = username + "@localhost"
    password = 'test'
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, password, email)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()


def test_sign_up_new_account_soap(app):
    username = random_username('user_', 10)
    email = username + "@localhost"
    password = 'test'
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, password, email)
    assert app.soap.can_login(username, password)
