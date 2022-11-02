# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.open_contact_page()
        app.contact.create(Contact(firstname="Test", lastname="Test", mobile="333-33-33"))
        app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.create(Contact(firstname="", lastname="", mobile=""))
    app.session.logout()












