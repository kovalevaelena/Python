# задание к уроку 4.1
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test",lastname="Test", mobile="333-33-33"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1]=[]
    assert old_contacts == new_contacts