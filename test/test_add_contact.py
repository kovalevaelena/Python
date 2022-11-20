# -*- coding: utf-8 -*-
# задание к уроку 3_2
from model.contact import Contact


def test_add_contact(app):
         app.contact.open_new_contact_page()
         app.contact.create(Contact(firstname="Test", lastname="Test", mobile="333-33-33"))













