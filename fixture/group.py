import random
import string


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def del_group(self, group):
        self.open_group_editor()
        groups_tree = self.group_editor.child_window(auto_id="uxAddressTreeView")
        groups_tree.get_item(["Contact groups", "%s" % group]).click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        delete_group = self.app.application.window(title="Delete group")
        delete_group.window(auto_id="uxOKAddressButton").click()
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    @staticmethod
    def random_string():
        maxlen = 10
        symbols = string.ascii_letters + string.digits
        return "group_" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
