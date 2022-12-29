from models.group import Group

def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Vasya'))
    app.group.del_first_group()
    app.session.logout()
