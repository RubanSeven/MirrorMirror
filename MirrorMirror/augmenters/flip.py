# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from imgaug.augmenters.flip import *


class FliplrWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Fliplr'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Flip/mirror input images horizontally.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = FloatParam(
            name='p',
            value_range=(0., 1.),
            default=1.
        )
        return params

    def to_aug(self):
        return Fliplr(p=self.params['p'].get_value())

    def to_code(self):
        return 'iaa.Fliplr(\np={}\n)'.format(
            self.params['p'].get_value(),
        )


class FlipudWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Flipud'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Flip/mirror input images vertically.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = FloatParam(
            name='p',
            value_range=(0., 1.),
            default=1.
        )
        return params

    def to_aug(self):
        return Flipud(p=self.params['p'].get_value())

    def to_code(self):
        return 'iaa.Flipud(\np={}\n)'.format(
            self.params['p'].get_value(),
        )
