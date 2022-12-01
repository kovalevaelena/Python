# -*- coding: utf-8 -*-
# задание к уроку 4
from model.contact import Contact


def test_add_contact(app):
         app.contact.open_new_contact_page()
         old_contacts = app.contact.get_contact_list()
         app.contact.create(Contact(firstname="Test", lastname="Test", mobile="333-33-33"))
         new_contacts = app.contact.get_contact_list()
         assert len(old_contacts)+1 == len(new_contacts)












