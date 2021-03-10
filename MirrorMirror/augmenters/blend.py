# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from imgaug.augmenters.blend import *


class BlendAlphaWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'BlendAlpha'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.child_names = ['foreground', 'background']
        self.has_child = False
        self.describe = 'Alpha-blend two image sources using an alpha/opacity value.'

    @staticmethod
    def __init_param():
        params = dict()
        params['factor'] = ChoiceParam(
            name='factor',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.0, 1.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.0, 0.5, 1.0'
                )
            },
            default='Float Range'
        )
        params['per_channel'] = ChoiceParam(
            name='per_channel',
            value_range={
                'Enum': EnumParam(
                    value_range=('True', 'False'),
                    default='False',
                ),
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.5,
                )
            },
            default='Enum'
        )
        return params

    def to_aug(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_aug()
            elif widget_child.name == 'background':
                background = widget_child.to_aug()

        return BlendAlpha(factor=self.params['factor'].get_value(),
                          foreground=foreground,
                          background=background,
                          per_channel=self.params['per_channel'].get_value()
                          )

    def to_code(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_code()
            elif widget_child.name == 'background':
                background = widget_child.to_code()

        return 'iaa.BlendAlpha(\nfactor={},\nforeground={},\nbackground={},\nper_channel={}\n)'.format(
            self.params['factor'].get_value(),
            foreground,
            background,
            self.params['per_channel'].get_value()
        )


class BlendAlphaCheckerboardWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'BlendAlphaCheckerboard'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.child_names = ['foreground', 'background']
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()
        params['nb_rows'] = ChoiceParam(
            name='nb_rows',
            value_range={
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(1, 4),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='1,2,3,4'
                )
            },
            default='Int'
        )
        params['nb_cols'] = ChoiceParam(
            name='nb_cols',
            value_range={
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(1, 4),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='1,2,3,4'
                )
            },
            default='Int Range'
        )
        return params

    def to_aug(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_aug()
            elif widget_child.name == 'background':
                background = widget_child.to_aug()

        return BlendAlphaCheckerboard(
            nb_rows=self.params['nb_rows'].get_value(),
            nb_cols=self.params['nb_cols'].get_value(),
            foreground=foreground,
            background=background
        )

    def to_code(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_code()
            elif widget_child.name == 'background':
                background = widget_child.to_code()

        return 'iaa.BlendAlphaCheckerboard(\nnb_rows={},\nnb_cols={},\nforeground={},\nbackground={}\n)'.format(
            self.params['nb_rows={},\n'].get_value(),
            self.params['nb_cols={},\n'].get_value(),
            foreground,
            background
        )


class BlendAlphaElementwiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'BlendAlphaElementwise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.child_names = ['foreground', 'background']
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()
        params['factor'] = ChoiceParam(
            name='factor',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.0, 1.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.0, 0.5, 1.0'
                )
            },
            default='Float Range'
        )

        params['per_channel'] = ChoiceParam(
            name='per_channel',
            value_range={
                'Enum': EnumParam(
                    value_range=('True', 'False'),
                    default='False',
                ),
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.5,
                )
            },
            default='Enum'
        )
        return params

    def to_aug(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_aug()
            elif widget_child.name == 'background':
                background = widget_child.to_aug()

        return BlendAlphaElementwise(
            factor=self.params['factor'].get_value(),
            foreground=foreground,
            background=background,
            per_channel=self.params['per_channel'].get_value()
        )

    def to_code(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_code()
            elif widget_child.name == 'background':
                background = widget_child.to_code()

        return 'iaa.BlendAlphaElementwise(\nfactor={},\nforeground={},\nbackground={},\nper_channel={}\n)'.format(
            self.params['factor'].get_value(),
            foreground,
            background,
            self.params['per_channel'].get_value()
        )


class BlendAlphaFrequencyNoiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'BlendAlphaFrequencyNoise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.child_names = ['foreground', 'background']
        self.has_child = False
        self.describe = ''

    @staticmethod
    def __init_param():
        params = dict()
        params['exponent'] = ChoiceParam(
            name='exponent',
            value_range={
                'Float': FloatParam(
                    value_range=(-4, 4),
                    default=-2,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((-4, 4), (-4, 4)),
                    default=(-4, 4),
                ),
                'Float List': FloatListParam(
                    value_range=(-4, 4),
                    default='-4,-2,2,4'
                )
            },
            default='Float Range'
        )

        params['per_channel'] = ChoiceParam(
            name='per_channel',
            value_range={
                'Enum': EnumParam(
                    value_range=('True', 'False'),
                    default='False',
                ),
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.5,
                )
            },
            default='Enum'
        )
        params['size_px_max'] = ChoiceParam(
            name='size_px_max',
            value_range={
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=4,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(4, 16),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='4,8,12,16'
                )
            },
            default='Int Range'
        )
        params['upscale_method'] = ChoiceParam(
            name='upscale_method',
            value_range={
                'Default': DefaultParam(),
                'Multi Select': MultiSelectParam(
                    value_range=('nearest', 'linear', 'area', 'cubic'),
                    default=[2]
                ),
            },
            default='Default'
        )
        params['iterations'] = ChoiceParam(
            name='iterations',
            value_range={
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(1, 3),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='1,2,3'
                )
            },
            default='Int Range'
        )
        params['aggregation_method'] = MultiSelectParam(
            name='aggregation_method',
            value_range=('min', 'max', 'avg'),
            default=[0, 1]
        )
        params['sigmoid'] = ChoiceParam(
            name='sigmoid',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.5,
                ),
                'Enum': EnumParam(
                    value_range=('True', 'False'),
                    default='False',
                )
            },
            default='Float'
        )
        params['sigmoid_thresh'] = ChoiceParam(
            name='sigmoid_thresh',
            value_range={
                'Default': DefaultParam(),
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 5),
                )
            },
            default='Default'
        )
        return params

    def to_aug(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_aug()
            elif widget_child.name == 'background':
                background = widget_child.to_aug()

        return BlendAlphaFrequencyNoise(
            exponent=self.params['exponent'].get_value(),
            foreground=foreground,
            background=background,
            per_channel=self.params['per_channel'].get_value(),
            size_px_max=self.params['size_px_max'].get_value(),
            upscale_method=self.params['upscale_method'].get_value(),
            iterations=self.params['iterations'].get_value(),
            aggregation_method=self.params['aggregation_method'].get_value(),
            sigmoid=self.params['sigmoid'].get_value(),
            sigmoid_thresh=self.params['sigmoid_thresh'].get_value(),
        )

    def to_code(self):
        foreground = list()
        background = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            if widget_child.name == 'foreground':
                foreground = widget_child.to_code()
            elif widget_child.name == 'background':
                background = widget_child.to_code()

        return 'iaa.BlendAlphaFrequencyNoise(\nexponent={},\nforeground={},\nbackground={},\nper_channel={},\n' \
               'size_px_max={},\nupscale_method={},\niterations={},\naggregation_method={},\nsigmoid={},\n' \
               'sigmoid_thresh={}\n)'.format(self.params['exponent'].get_value(),
                                             foreground,
                                             background,
                                             self.params['per_channel'].get_value(),
                                             self.params['size_px_max'].get_value(),
                                             self.params['upscale_method'].get_value(),
                                             self.params['iterations'].get_value(),
                                             self.params['aggregation_method'].get_value(),
                                             self.params['sigmoid'].get_value(),
                                             self.params['sigmoid_thresh'].get_value(),
                                             )
