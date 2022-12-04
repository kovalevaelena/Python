# задание к уроку 4(кеширование и хеширование)

from model.group import Group


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
 #      app.group.create(Group(name="test"))
#    app.group.modify_first_group(Group(header="New header"))
 #   new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#       app.group.create(Group(name="test"))
#    app.group.modify_first_group(Group(header="New footer"))
#   new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)