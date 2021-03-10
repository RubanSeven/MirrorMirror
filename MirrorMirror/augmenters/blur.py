# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from imgaug.augmenters.blur import *
from PyQt5.QtWidgets import *


class AverageBlurWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AverageBlur'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Blur an image by computing simple means over neighbourhoods.'

    @staticmethod
    def __init_param():
        params = dict()
        params['k'] = ChoiceParam(
            name='k',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 7),
                ),
                'Dict': DictParam(
                    children={
                        "height": IntRangeParam(
                            value_ranges=((1, 1e8), (1, 1e8)),
                            default=(1, 7),
                        ),
                        "width": IntRangeParam(
                            value_ranges=((1, 1e8), (1, 1e8)),
                            default=(1, 7),
                        )
                    }
                )
            },
            default='Int Range'
        )
        return params

    def to_aug(self):
        k = self.params['k'].get_value()
        if type(k) is dict:
            k = (k['height'], k['width'])
        return AverageBlur(k=k)

    def to_code(self):
        k = self.params['k'].get_value()
        if type(k) is dict:
            k = (k['height'], k['width'])
        return 'iaa.AverageBlur(\nk={}\n)'.format(
            k,
        )


class BilateralBlurWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'BilateralBlur'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Blur/Denoise an image using a bilateral filter.'

    @staticmethod
    def __init_param():
        params = dict()
        params['d'] = ChoiceParam(
            name='d',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 9),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='1,3,9'
                )
            },
            default='Int Range'
        )
        params['sigma_color'] = ChoiceParam(
            name='sigma_color',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(10, 250),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='10,100,200'
                )
            },
            default='Int Range'
        )
        params['sigma_space'] = ChoiceParam(
            name='sigma_space',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(10, 250),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='10,100,200'
                )
            },
            default='Int Range'
        )
        return params

    def to_aug(self):
        return BilateralBlur(
            d=self.params['d'].get_value(),
            sigma_color=self.params['sigma_color'].get_value(),
            sigma_space=self.params['sigma_space'].get_value(),
        )

    def to_code(self):
        return 'iaa.BilateralBlur(\nd={},\nsigma_color={},\nsigma_space={}\n)'.format(
            self.params['d'].get_value(),
            self.params['sigma_color'].get_value(),
            self.params['sigma_space'].get_value(),
        )


class GaussianBlurWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'GaussianBlur'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Augmenter to blur images using gaussian kernels.'

    @staticmethod
    def __init_param():
        params = dict()
        params['sigma'] = ChoiceParam(
            name='sigma',
            value_range={
                'Float': FloatParam(
                    value_range=(1, 3),
                    default=1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((1, 3), (1, 3)),
                    default=(0.0, 3.0),
                ),
                'Float List': FloatListParam(
                    value_range=(1, 3),
                    default='0.0,1.0,2.0,3.0'
                )
            },
            default='Float Range'
        )
        return params

    def to_aug(self):
        return GaussianBlur(
            sigma=self.params['sigma'].get_value()
        )

    def to_code(self):
        return 'iaa.GaussianBlur(\nsigma={}\n)'.format(
            self.params['sigma'].get_value()
        )


class MeanShiftBlurWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MeanShiftBlur'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Apply a pyramidic mean shift filter to each image.'

    @staticmethod
    def __init_param():
        params = dict()
        params['spatial_radius'] = ChoiceParam(
            name='spatial_radius',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=5.0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(5.0, 40.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='5.0,20.0,40.0'
                )
            },
            default='Float Range'
        )
        params['color_radius'] = ChoiceParam(
            name='color_radius',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=5.0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(5.0, 40.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='5.0,20.0,40.0'
                )
            },
            default='Float Range'
        )
        return params

    def to_aug(self):
        return MeanShiftBlur(
            spatial_radius=self.params['spatial_radius'].get_value(),
            color_radius=self.params['color_radius'].get_value()
        )

    def to_code(self):
        return 'iaa.MeanShiftBlur(\nspatial_radius={},\ncolor_radius={}\n)'.format(
            self.params['spatial_radius'].get_value(),
            self.params['color_radius'].get_value()
        )


class MedianBlurWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MedianBlur'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Blur an image by computing simple means over neighbourhoods.'

    @staticmethod
    def __init_param():
        params = dict()
        params['k'] = ChoiceParam(
            name='k',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 7),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='1,3,5'
                )
            },
            default='Int Range'
        )
        return params

    def to_aug(self):
        return MedianBlur(k=self.params['k'].get_value())

    def to_code(self):
        return 'iaa.MedianBlur(\nk={}\n)'.format(
            self.params['k'].get_value(),
        )


class MotionBlurWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MotionBlur'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Blur images in a way that fakes camera or object movements.'

    @staticmethod
    def __init_param():
        params = dict()
        params['k'] = ChoiceParam(
            name='k',
            value_range={
                'Int': IntParam(
                    value_range=(3, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((3, 1e8), (3, 1e8)),
                    default=(3, 7),
                ),
                'Int List': IntListParam(
                    value_range=(3, 1e8),
                    default='3,5,7'
                )
            },
            default='Int Range'
        )
        params['angle'] = ChoiceParam(
            name='angle',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 360),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 360), (0, 360)),
                    default=(0, 360),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 360),
                    default='0,90,180,270'
                )
            },
            default='Float Range'
        )
        params['direction'] = ChoiceParam(
            name='direction',
            value_range={
                'Float': FloatParam(
                    value_range=(-1, 1),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((-1, 1), (-1, 1)),
                    default=(-1, 1),
                ),
                'Float List': FloatListParam(
                    value_range=(-1, 1),
                    default='-0.5,0,0.5'
                )
            },
            default='Float Range'
        )
        params['order'] = MultiSelectParam(
            name='order',
            value_range=(0, 1),
            default=[1]
        )
        return params

    def to_aug(self):
        return MotionBlur(
            k=self.params['k'].get_value(),
            angle=self.params['angle'].get_value(),
            direction=self.params['direction'].get_value(),
            order=self.params['order'].get_value()
        )

    def to_code(self):
        return 'iaa.MotionBlur(\nk={},\nangle={},\ndirection={},\norder={}\n)'.format(
            self.params['k'].get_value(),
            self.params['angle'].get_value(),
            self.params['direction'].get_value(),
            self.params['order'].get_value(),
        )
