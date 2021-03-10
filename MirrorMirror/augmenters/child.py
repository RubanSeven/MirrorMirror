# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *


class ChildItem(QTreeWidgetItem):
    def __init__(self, name, *__args):
        super().__init__(*__args)
        self.name = name
        self.setText(0, name)
        self.params = {}
        self.has_child = True

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return aug_children

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())

        if len(aug_children) == 0:
            return 'None'
        elif len(aug_children) == 1:
            return aug_children
        else:
            return "[\n" + ",\n".join(aug_children) + "\n]"
