# задание к уроку 4(рандом)

from model.contact import Contact
from random import randrange


def test_change_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", lastname="Test", mobile="333-33-33"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="firstname changed", lastname="lastname changed", mobile="mobilexxx zzzchanged")
    contact.id = old_contacts[index].id
    app.contact.change_contact(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)