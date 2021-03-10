# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from PyQt5.QtWidgets import *
from imgaug.augmenters.pillike import *


class AffineWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Affine'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Apply PIL-like affine transformations to images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['scale'] = ChoiceParam(
            name='scale',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 3),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.5,0.8,1,2,3'
                ),
                'Dict': DictParam(
                    children={
                        "x": ChoiceParam(
                            value_range={
                                'Float': FloatParam(
                                    value_range=(0.0001, 1e8),
                                    default=1.,
                                ),
                                'Float Range': FloatRangeParam(
                                    value_ranges=((0.0001, 1e8), (0.0001, 1e8)),
                                    default=(0, 3),
                                ),
                                'Float List': FloatListParam(
                                    value_range=(0.0001, 1e8),
                                    default='0.5,0.8,1,2,3'
                                )
                            },
                            default='Float'
                        ),
                        "y": ChoiceParam(
                            value_range={
                                'Float': FloatParam(
                                    value_range=(0.0001, 1e8),
                                    default=1.,
                                ),
                                'Float Range': FloatRangeParam(
                                    value_ranges=((0.0001, 1e8), (0.0001, 1e8)),
                                    default=(0, 3),
                                ),
                                'Float List': FloatListParam(
                                    value_range=(0.0001, 1e8),
                                    default='0.5,0.8,1,2,3'
                                )
                            },
                            default='Float'
                        )
                    }
                )
            },
            default='Float'
        )
        params['translate'] = ChoiceParam(
            name='translate',
            default='translate_percent',
            value_range={
                'translate_percent': ChoiceParam(
                    value_range={
                        'Float': FloatParam(
                            value_range=(0, 1),
                            default=0,
                        ),
                        'Float Range': FloatRangeParam(
                            value_ranges=((0, 1), (0, 1)),
                            default=(0, 0.1),
                        ),
                        'Float List': FloatListParam(
                            value_range=(0, 1),
                            default='0,0.1,0.2'
                        ),
                        'Dict': DictParam(
                            children={
                                "x": ChoiceParam(
                                    value_range={
                                        'Float': FloatParam(
                                            value_range=(0, 1),
                                            default=0,
                                        ),
                                        'Float Range': FloatRangeParam(
                                            value_ranges=((0, 1), (0, 1)),
                                            default=(0, 0.1),
                                        ),
                                        'Float List': FloatListParam(
                                            value_range=(0, 1),
                                            default='0,0.1,0.2'
                                        )
                                    },
                                    default='Float'
                                ),
                                "y": ChoiceParam(
                                    value_range={
                                        'Float': FloatParam(
                                            value_range=(0, 1),
                                            default=0,
                                        ),
                                        'Float Range': FloatRangeParam(
                                            value_ranges=((0, 1), (0, 1)),
                                            default=(0, 0.1),
                                        ),
                                        'Float List': FloatListParam(
                                            value_range=(0, 1),
                                            default='0,0.1,0.2'
                                        )
                                    },
                                    default='Float'
                                )
                            }
                        )
                    },
                    default=0
                ),
                'translate_px': ChoiceParam(
                    value_range={
                        'Int': IntParam(
                            value_range=(0, 1e8),
                            default=0,
                        ),
                        'Int Range': IntRangeParam(
                            value_ranges=((0, 1e8), (0, 1e8)),
                            default=(0, 3),
                        ),
                        'Int List': IntListParam(
                            value_range=(0, 1e8),
                            default='0,1,2,3'
                        ),
                        'Dict': DictParam(
                            children={
                                "x": ChoiceParam(
                                    value_range={
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
                                    default='Int'
                                ),
                                "y": ChoiceParam(
                                    value_range={
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
                                    default='Int'
                                )
                            }
                        )
                    },
                    default='Int'
                )
            }
        )
        return params

    def to_aug(self):
        if self.params['translate'].value == 0:
            return Affine(
                scale=self.params['scale'].get_value(),
                translate_percent=self.params['translate'].get_value()
            )
        else:
            return Affine(
                scale=self.params['scale'].get_value(),
                translate_px=self.params['translate'].get_value()
            )

    def to_code(self):
        if self.params['translate'].value == 0:
            return 'iaa.Affine(\nscale={},\ntranslate_percent={}\n)'.format(
                self.params['scale'].get_value(),
                self.params['translate'].get_value()
            )
        else:
            return 'iaa.Affine(\nscale={},\ntranslate_px={}\n)'.format(
                self.params['scale'].get_value(),
                self.params['translate'].get_value()
            )
