# задание к уроку 4
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test",lastname="Test", mobile="333-33-33"))
    app.contact.del_first_contact()

