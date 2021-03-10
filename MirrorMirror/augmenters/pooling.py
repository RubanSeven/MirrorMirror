# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from PyQt5.QtWidgets import *
from imgaug.augmenters.pooling import *


class AveragePoolingWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AveragePooling'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()

        params['kernel_size'] = ChoiceParam(
            name='kernel_size',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=3
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 5)
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='1,3,5'
                ),
                'Dict': DictParam(
                    children={
                        "height": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        ),
                        "width": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        )
                    }
                )
            },
            default='Int Range'
        )

        params['keep_size'] = EnumParam(
            name='keep_size',
            value_range=('True', 'False'),
            default='True'
        )
        return params

    def to_aug(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return AveragePooling(
            kernel_size=kernel_size,
            keep_size=self.params['keep_size'].get_value()
        )

    def to_code(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return 'iaa.AveragePooling(\nkernel_size={},\nkeep_size={}\n)'.format(
            kernel_size,
            self.params['keep_size'].get_value()
        )


class MaxPoolingWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MaxPooling'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()

        params['kernel_size'] = ChoiceParam(
            name='kernel_size',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=3
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 5)
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='1,3,5'
                ),
                'Dict': DictParam(
                    children={
                        "height": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        ),
                        "width": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        )
                    }
                )
            },
            default='Int Range'
        )
        params['keep_size'] = EnumParam(
            name='keep_size',
            value_range=('True', 'False'),
            default='True'
        )
        return params

    def to_aug(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return MaxPooling(
            kernel_size=kernel_size,
            keep_size=self.params['keep_size'].get_value()
        )

    def to_code(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return 'iaa.MaxPooling(\nkernel_size={},\nkeep_size={}\n)'.format(
            kernel_size,
            self.params['keep_size'].get_value()
        )


class MedianPoolingWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MedianPooling'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()

        params['kernel_size'] = ChoiceParam(
            name='kernel_size',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=3
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 5)
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='1,3,5'
                ),
                'Dict': DictParam(
                    children={
                        "height": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        ),
                        "width": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        )
                    }
                )
            },
            default='Int Range'
        )
        params['keep_size'] = EnumParam(
            name='keep_size',
            value_range=('True', 'False'),
            default='True'
        )
        return params

    def to_aug(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return MedianPooling(
            kernel_size=kernel_size,
            keep_size=self.params['keep_size'].get_value()
        )

    def to_code(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return 'iaa.MedianPooling(\nkernel_size={},\nkeep_size={}\n)'.format(
            kernel_size,
            self.params['keep_size'].get_value()
        )


class MinPoolingWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MinPooling'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()

        params['kernel_size'] = ChoiceParam(
            name='kernel_size',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=3
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 5)
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='1,3,5'
                ),
                'Dict': DictParam(
                    children={
                        "height": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        ),
                        "width": ChoiceParam(
                            value_range={
                                'Int Range': IntRangeParam(
                                    value_ranges=((1, 1e8), (1, 1e8)),
                                    default=(1, 5)
                                ),
                                'Int List': IntListParam(
                                    value_range=(1, 1e8),
                                    default='1,3,5'
                                )
                            },
                            default='Int List'
                        )
                    }
                )
            },
            default='Int Range'
        )
        params['keep_size'] = EnumParam(
            name='keep_size',
            value_range=('True', 'False'),
            default='True'
        )
        return params

    def to_aug(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return MinPooling(
            kernel_size=kernel_size,
            keep_size=self.params['keep_size'].get_value()
        )

    def to_code(self):
        kernel_size = self.params['kernel_size'].get_value()
        if type(kernel_size) is dict:
            kernel_size = (kernel_size['height'], kernel_size['width'])
        return 'iaa.MinPooling(\nkernel_size={},\nkeep_size={}\n)'.format(
            kernel_size,
            self.params['keep_size'].get_value()
        )
