# задание к уроку 4
import random

from model.contact import Contact
from random import randrange


def test_change_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test", lastname="Test", mobile="333-33-33"))
    old_contacts = app.contact.get_contact_list()
    if len(old_contacts) == 1 or len(old_contacts) == 2:
        contact = Contact(firstname="firstname changed", lastname="lastname changed", mobile="mobile changed")
        contact.id = old_contacts[0].id
        app.contact.change_first_contact()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        old_contacts[0] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    else:
      index = randrange(2, len(old_contacts))
      contact = Contact(firstname="firstname changed", lastname="lastname changed", mobile="mobile changed")
      contact.id = old_contacts[index].id
      app.contact.change_contact_by_index(index)
      new_contacts = app.contact.get_contact_list()
      assert len(old_contacts) == len(new_contacts)
      old_contacts[index] = contact
      assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)