# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from imgaug.augmenters.meta import *


class ChannelShuffleWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'ChannelShuffle'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add a value to all pixels in an image.'

    @staticmethod
    def __init_param():
        params = dict()

        params['p'] = FloatParam(
            name='p',
            value_range=(0, 1.),
            default=1
        )
        params['channels'] = ChoiceParam(
            name='channels',
            value_range={
                'Default': DefaultParam(),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='0,1,2,3',
                )
            },
            default='Default'
        )
        return params

    def to_aug(self):
        return ChannelShuffle(
            p=self.params['p'].get_value(),
            channels=self.params['channels'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.ChannelShuffle(\np={},\nchannels={}\n)'.format(
            self.params['p'].get_value(),
            self.params['channels'].get_value()
        )


class SequentialItem(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Sequential'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = True

    @staticmethod
    def __init_param():
        params = dict()
        params['random_order'] = EnumParam(
            name='random_order',
            value_range=('True', 'False'),
            default='False'
        )
        return params

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return Sequential(children=aug_children, random_order=self.params['random_order'].get_value())

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())
        if len(aug_children) == 0:
            return 'iaa.Sequential(\nrandom_order={},\nchildren=None\n)'.format(
                self.params['random_order'].get_value()
            )
        else:
            return 'iaa.Sequential(\nrandom_order={},\nchildren=[\n{}\n]\n)'.format(
                self.params['random_order'].get_value(),
                ",\n".join(aug_children)
            )


class OneOfItem(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'OneOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = True

    @staticmethod
    def __init_param():
        params = dict()
        return params

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return OneOf(children=aug_children)

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())
        if len(aug_children) == 0:
            return 'iaa.OneOf(\nchildren=None\n)'.format(
            )
        else:
            return 'iaa.OneOf(\nchildren=[\n{}\n]\n)'.format(
                ",\n".join(aug_children)
            )


class SomeOfItem(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'SomeOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = True

    @staticmethod
    def __init_param():
        params = dict()
        params['n'] = ChoiceParam(
            name='n',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 3),
                )
            },
            default='Default'
        )
        params['random_order'] = EnumParam(
            name='random_order',
            value_range=('True', 'False'),
            default='False'
        )
        return params

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return SomeOf(
            n=self.params['n'].get_value(),
            children=aug_children,
            random_order=self.params['random_order'].get_value())

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())
        if len(aug_children) == 0:
            return 'iaa.SomeOf(\nn={},\nrandom_order={},\nchildren=None\n)'.format(
                self.params['n'].get_value(),
                self.params['random_order'].get_value()
            )
        else:
            return 'iaa.SomeOf(\nn={},\nrandom_order={},\nchildren=[\n{}\n]\n)'.format(
                self.params['n'].get_value(),
                self.params['random_order'].get_value(),
                ",\n".join(aug_children)
            )


class SometimesItem(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Sometimes'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.child_names = ['then_list', 'else_list']
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = FloatParam(
            name='p',
            value_range=(0, 1),
            default=0.5
        )
        return params

    def to_aug(self):
        then_list = list()
        else_list = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'then_list':
                then_list = widget_child.to_aug()
            elif widget_child.name == 'else_list':
                else_list = widget_child.to_aug()

        return Sometimes(
            p=self.params['p'].get_value(),
            then_list=then_list,
            else_list=else_list
        )

    def to_code(self):
        then_list = list()
        else_list = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'then_list':
                then_list = widget_child.to_code()
            elif widget_child.name == 'else_list':
                else_list = widget_child.to_code()

        return 'iaa.Sometimes(\np={},\nthen_list={},\nelse_list={}\n)'.format(
            self.params['p'].get_value(),
            then_list,
            else_list
        )


class WithChannelsItem(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'WithChannels'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = True

    @staticmethod
    def __init_param():
        params = dict()
        params['channels'] = ChoiceParam(
            name='channels',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 3),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='0,1,2,3'
                )
            },
            default='Default'
        )
        return params

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return WithChannels(
            channels=self.params['channels'].get_value(),
            children=aug_children
        )

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())
        if len(aug_children) == 0:
            return 'iaa.WithChannels(\nchannels={},\nchildren=None\n)'.format(
                self.params['channels'].get_value(),
                self.params['random_order'].get_value()
            )
        else:
            return 'iaa.WithChannels(\nchannels={},\nchildren=[\n{}\n]\n)'.format(
                self.params['channels'].get_value(),
                ",\n".join(aug_children)
            )
