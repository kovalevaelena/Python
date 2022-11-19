# -*- coding: utf-8 -*-
# задание к уроку 3.1
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test4", header="test4", footer="test4"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))




