# -*- coding: utf-8 -*-
# задание к уроку 4(кеширование и хеширование)
from model.contact import Contact


def test_add_contact(app):
         old_contacts = app.contact.get_contact_list()
         contact = Contact(firstname="Test", lastname="Test", mobile="333-33-33")
         app.contact.open_new_contact_page()
         app.contact.create(contact)
         assert len(old_contacts) + 1 == app.contact.count()
         new_contacts = app.contact.get_contact_list()
         old_contacts.append(contact)
         assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








