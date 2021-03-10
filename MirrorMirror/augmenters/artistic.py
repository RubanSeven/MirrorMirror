# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from imgaug.augmenters.artistic import *


class CartoonWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Cartoon'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Convert the style of images to a more cartoonish one.'

    @staticmethod
    def __init_param():
        params = dict()
        params['blur_ksize'] = ChoiceParam(
            name='blur_ksize',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(1, 5),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='1, 3, 5'
                )
            },
            default='Int Range'
        )
        params['segmentation_size'] = ChoiceParam(
            name='segmentation_size',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.8, 1.2),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.8, 1.0, 1.2'
                )
            },
            default='Float Range'
        )
        params['saturation'] = ChoiceParam(
            name='saturation',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(1.5, 2.5),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='1.5, 2.0, 2.5'
                )
            },
            default='Float Range'
        )
        params['edge_prevalence'] = ChoiceParam(
            name='edge_prevalence',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.9, 1.1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.8, 1.0, 1.2'
                )
            },
            default='Float Range'
        )
        params['from_colorspace'] = (EnumParam(name='from_colorspace',
                                               value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                               default='RGB',
                                               describe='The source colorspace (of the input images).'))
        return params

    def to_aug(self):
        return Cartoon(blur_ksize=self.params['blur_ksize'].value,
                       segmentation_size=self.params['segmentation_size'].value,
                       saturation=self.params['saturation'].value,
                       edge_prevalence=self.params['edge_prevalence'].value,
                       from_colorspace=self.params['from_colorspace'].value)

    def to_code(self):
        return 'iaa.Cartoon(\nblur_ksize={},\nsegmentation_size={},\nsaturation={},\nedge_prevalence={},' \
               '\nfrom_colorspace="{}",\n)'.format(self.params['blur_ksize'].value,
                                                   self.params['segmentation_size'].value,
                                                   self.params['saturation'].value,
                                                   self.params['edge_prevalence'].value,
                                                   self.params['from_colorspace'].value
                                                   )
