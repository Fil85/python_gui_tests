import random


def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) <= 1:
        app.groups.add_new_group("my_group")
        old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.del_group(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)