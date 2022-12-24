import unittest
from application import Application
from group import Group

def is_alert_present(wd):
    try:
        wd.swich_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = Application

    def test_add_group(self):
        self.app.login(username = 'admin', password = 'secret')
        self.app.create_group(Group(name='fff', header='rrrr', footer='refdfd'))
        self.app.logout()

    def test_add_group(self):
        self.app.login(username='admin', password='secret')
        self.app.create_group(Group(name='', header='', footer=''))
        self.app.logout()


if __name__ == '__main__':
    unittest.main()