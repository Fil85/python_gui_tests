
def test_add_group(app):
    old_list = app.groups.get_group_list()
    group = app.groups.random_string()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)
