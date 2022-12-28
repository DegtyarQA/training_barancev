import pytest
from fixture.application import Application
from models.group import Group


@pytest.fixture
def app():
    fixture = Application()
    return fixture


def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.create_group(Group(name='fff', header='rrrr', footer='refdfd'))
    app.session.logout()
    app.destroy()

def test_add_empty_group(app):
    app.session.login(username='admin', password='secret')
    app.create_group(Group(name='', header='', footer=''))
    app.session.logout()
    app.destroy()

