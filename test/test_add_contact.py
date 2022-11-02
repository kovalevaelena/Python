# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Test", lastname="Test", mobile="333-33-33"))
        app.session.logout()













