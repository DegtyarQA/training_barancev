from models.group import Group


def test_modify_group_name(app):
    app.session.login(username = "admin", password = "secret")
    app.group.modify_first_group(Group(name="Valery Degtyar"))
    app.session.logout()

#def test_modify_group_header(app):
 #   app.session.login(username="admin", password="secret")
  #  app.group.modify_first_group(Group("header" = Aleksandrovich))
   # app.session.logout()