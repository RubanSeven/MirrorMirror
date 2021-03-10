# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from PyQt5.QtWidgets import *
from imgaug.augmenters.arithmetic import *


class AddWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Add'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add a value to all pixels in an image.'

    @staticmethod
    def __init_param():
        params = dict()
        params['value'] = ChoiceParam(
            name='value',
            value_range={
                'Int': IntParam(
                    value_range=(-1e8, 1e8),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((-1e8, 1e8), (-1e8, 1e8)),
                    default=(-20, 20),
                ),
                'Int List': IntListParam(
                    value_range=(-1e8, 1e8),
                    default='-20,-10,0,10,20'
                )
            },
            default='Int Range'
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
        return Add(
            value=self.params['value'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.Add(\nvalue={},\nper_channel={}\n)'.format(
            self.params['value'].get_value(),
            self.params['per_channel'].get_value()
        )


class AddElementwiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AddElementwise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add to the pixels of images values that are pixelwise randomly sampled.'

    @staticmethod
    def __init_param():
        params = dict()
        params['value'] = ChoiceParam(
            name='value',
            value_range={
                'Int': IntParam(
                    value_range=(-1e8, 1e8),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((-1e8, 1e8), (-1e8, 1e8)),
                    default=(-20, 20),
                ),
                'Int List': IntListParam(
                    value_range=(-1e8, 1e8),
                    default='-20,-10,0,10,20'
                )
            },
            default='Int Range'
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
        return AddElementwise(
            value=self.params['value'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.AddElementwise(\nvalue={},\nper_channel={}\n)'.format(
            self.params['value'].get_value(),
            self.params['per_channel'].get_value()
        )


class AdditiveGaussianNoiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AdditiveGaussianNoise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add noise sampled from gaussian distributions elementwise to images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['loc'] = ChoiceParam(
            name='loc',
            value_range={
                'Float': FloatParam(
                    value_range=(-1e8, 1e8),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((-1e8, 1e8), (-1e8, 1e8)),
                    default=(-1, 1),
                ),
                'Float List': FloatListParam(
                    value_range=(-1e8, 1e8),
                    default='-2,-1,0,1,2'
                )
            },
            default='Float',
            describe='Standard deviation of the normal distribution that generates the noise.'
                     ' Must be >=0. If 0 then loc will simply be added to all pixels.'
        )

        params['scale'] = ChoiceParam(
            name='scale',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 15),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0,1,2,3'
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
        return AdditiveGaussianNoise(
            loc=self.params['loc'].get_value(),
            scale=self.params['scale'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.AdditiveGaussianNoise(\nloc={},\nscale={},\nper_channel={}\n)'.format(
            self.params['loc'].get_value(),
            self.params['scale'].get_value(),
            self.params['per_channel'].get_value()
        )


class AdditiveLaplaceNoiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AdditiveLaplaceNoise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add noise sampled from gaussian distributions elementwise to images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['loc'] = ChoiceParam(
            name='loc',
            value_range={
                'Float': FloatParam(
                    value_range=(-1e8, 1e8),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((-1e8, 1e8), (-1e8, 1e8)),
                    default=(-1, 1),
                ),
                'Float List': FloatListParam(
                    value_range=(-1e8, 1e8),
                    default='-2,-1,0,1,2'
                )
            },
            default='Float'
        )

        params['scale'] = ChoiceParam(
            name='scale',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 15),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0,1,2,3'
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
        return AdditiveLaplaceNoise(
            loc=self.params['loc'].get_value(),
            scale=self.params['scale'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.AdditiveLaplaceNoise(\nloc={},\nscale={},\nper_channel={}\n)'.format(
            self.params['loc'].get_value(),
            self.params['scale'].get_value(),
            self.params['per_channel'].get_value()
        )


class AdditivePoissonNoiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AdditivePoissonNoise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add noise sampled from gaussian distributions elementwise to images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['lam'] = ChoiceParam(
            name='lam',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.0, 15.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0,1,2'
                )
            },
            default='Float'
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
        return AdditivePoissonNoise(
            lam=self.params['lam'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.AdditivePoissonNoise(\nlam={},\nper_channel={}\n)'.format(
            self.params['lam'].get_value(),
            self.params['per_channel'].get_value()
        )


class CoarseDropoutWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CoarseDropout'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add noise sampled from gaussian distributions elementwise to images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0.02, 0.1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.01,0.02,0.05'
                )
            },
            default='Float Range'
        )

        params['size'] = ChoiceParam(
            name='size',
            default='size_percent',
            value_range={
                'size_percent': ChoiceParam(
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
                'size_px': ChoiceParam(
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
                        )
                    },
                    default='Int'
                )
            }
        )

        params['min_size'] = IntParam(
            name='min_size',
            value_range=(1, 1e8),
            default=3,
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
        if self.params['size'].value == 0:
            return CoarseDropout(
                p=self.params['p'].get_value(),
                size_percent=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )
        else:
            return CoarseDropout(
                p=self.params['p'].get_value(),
                size_px=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )

    def to_code(self):
        if self.params['size'].value == 0:
            return 'iaa.CoarseDropout(\np={},\nsize_percent={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )
        else:
            return 'iaa.CoarseDropout(\np={},\nsize_px={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )


class CoarsePepperWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CoarsePepper'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace rectangular areas in images with black-ish pixel noise.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0.02, 0.1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.01,0.02,0.05'
                )
            },
            default='Float Range'
        )

        params['size'] = ChoiceParam(
            name='size',
            default=0,
            value_range={
                'size_percent': ChoiceParam(
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
                'size_px': ChoiceParam(
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
                        )
                    },
                    default='Int'
                )
            }
        )

        params['min_size'] = IntParam(
            name='min_size',
            value_range=(1, 1e8),
            default=3,
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
        if self.params['size'].value == 0:
            return CoarsePepper(
                p=self.params['p'].get_value(),
                size_percent=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )
        else:
            return CoarsePepper(
                p=self.params['p'].get_value(),
                size_px=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )

    def to_code(self):
        if self.params['size'].value == 0:
            return 'iaa.CoarsePepper(\np={},\nsize_percent={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )
        else:
            return 'iaa.CoarsePepper(\np={},\nsize_px={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )


class CoarseSaltWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CoarseSalt'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace rectangular areas in images with black-ish pixel noise.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0.02, 0.1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.01,0.02,0.05'
                )
            },
            default='Float'
        )

        params['size'] = ChoiceParam(
            name='size',
            default='size_percent',
            value_range={
                'size_percent': ChoiceParam(
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
                'size_px': ChoiceParam(
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
                        )
                    },
                    default='Int'
                )
            }
        )

        params['min_size'] = IntParam(
            name='min_size',
            value_range=(1, 1e8),
            default=3,
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
        if self.params['size'].value == 0:
            return CoarseSalt(
                p=self.params['p'].get_value(),
                size_percent=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )
        else:
            return CoarseSalt(
                p=self.params['p'].get_value(),
                size_px=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )

    def to_code(self):
        if self.params['size'].value == 0:
            return 'iaa.CoarseSalt(\np={},\nsize_percent={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )
        else:
            return 'iaa.CoarseSalt(\np={},\nsize_px={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )


class CoarseSaltAndPepperWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CoarseSaltAndPepper'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace rectangular areas in images with white/black-ish pixel noise.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0.02, 0.1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.01,0.02,0.05'
                )
            },
            default='Float Range'
        )

        params['size'] = ChoiceParam(
            name='size',
            default='size_percent',
            value_range={
                'size_percent': ChoiceParam(
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
                'size_px': ChoiceParam(
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
                        )
                    },
                    default='Int'
                )
            }
        )

        params['min_size'] = IntParam(
            name='min_size',
            value_range=(1, 1e8),
            default=3,
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
        if self.params['size'].value == 0:
            return CoarseSaltAndPepper(
                p=self.params['p'].get_value(),
                size_percent=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )
        else:
            return CoarseSaltAndPepper(
                p=self.params['p'].get_value(),
                size_px=self.params['size'].get_value(),
                min_size=self.params['min_size'].get_value(),
                per_channel=self.params['per_channel'].get_value() == 'True'
            )

    def to_code(self):
        if self.params['size'].value == 0:
            return 'iaa.CoarseSaltAndPepper(\np={},\nsize_percent={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )
        else:
            return 'iaa.CoarseSaltAndPepper(\np={},\nsize_px={},\nmin_size={},\nper_channel={}\n)'.format(
                self.params['p'].get_value(),
                self.params['size'].get_value(),
                self.params['min_size'].get_value(),
                self.params['per_channel'].get_value()
            )


class CutoutWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Cutout'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Fill one or more rectangular areas in an image using a fill mode.'

    @staticmethod
    def __init_param():
        params = dict()
        params['nb_iterations'] = ChoiceParam(
            name='nb_iterations',
            value_range={
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0, 10),
                ),
                'Int List': IntListParam(
                    value_range=(0, 1e8),
                    default='0,1,2,3'
                )
            },
            default='Int'
        )
        params['position'] = ChoiceParam(
            name='position',
            value_range={
                'Enum': EnumParam(
                    value_range=(
                        'uniform', 'normal', 'center', 'left-top', 'left-center', 'left-bottom', 'center-top',
                        'center-center',
                        'center-bottom', 'right-top', 'right-center', 'right-bottom'
                    ),
                    default='uniform'
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0, 1)
                )
            },
            default='Enum'
        )
        params['size'] = ChoiceParam(
            name='size',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.2,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.5),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
                )
            },
            default='Float'
        )
        params['squared'] = ChoiceParam(
            name='squared',
            value_range={
                'Enum': EnumParam(
                    value_range=('True', 'False'),
                    default='True',
                ),
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.5,
                )
            },
            default='Enum'
        )
        params['fill_mode'] = MultiSelectParam(
            name='fill_mode',
            value_range=('constant', 'gaussian'),
            default=[0],
        )
        params['cval'] = ChoiceParam(
            name='cval',
            value_range={
                'Int': IntParam(
                    value_range=(0, 255),
                    default=128,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 255), (0, 255)),
                    default=(0, 255),
                ),
                'Int List': IntListParam(
                    value_range=(0, 255),
                    default='0, 128'
                )
            },
            default='Int'
        )
        params['fill_per_channel'] = ChoiceParam(
            name='fill_per_channel',
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
            default=0,
            describe='.'
        )

        return params

    def to_aug(self):
        # print(self.params['fill_mode'].get_value())
        return Cutout(
            nb_iterations=self.params['nb_iterations'].get_value(),
            position=self.params['position'].get_value(),
            size=self.params['size'].get_value(),
            squared=self.params['squared'].get_value(),
            fill_mode=self.params['fill_mode'].get_value(),
            cval=self.params['cval'].get_value(),
            fill_per_channel=self.params['fill_per_channel'].get_value()
        )

    def to_code(self):
        return 'iaa.Cutout(\nnb_iterations={},\nposition="{}",\nsize={},\nsquared={},\nfill_mode="{}",\n' \
               'cval={},\nfill_per_channel={}\n)'.format(self.params['nb_iterations'].get_value(),
                                                         self.params['position'].get_value(),
                                                         self.params['size'].get_value(),
                                                         self.params['squared'].get_value(),
                                                         self.params['fill_mode'].get_value(),
                                                         self.params['cval'].get_value(),
                                                         self.params['fill_per_channel'].get_value()
                                                         )


class DropoutWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Dropout'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Set a fraction of pixels in images to zero.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.2,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.05),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
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
        # print(self.params['fill_mode'].get_value())
        return Dropout(
            p=self.params['p'].get_value(),
            per_channel=self.params['per_channel'].get_value()
        )

    def to_code(self):
        return 'iaa.Dropout(\np={},\nper_channel={}\n)'.format(
            self.params['p'].get_value(),
            self.params['per_channel'].get_value(),
        )


class Dropout2dWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Dropout2d'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Set a fraction of pixels in images to zero.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.5),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
                )
            },
            default='Float'
        )
        params['nb_keep_channels'] = IntParam(
            name='nb_keep_channels',
            value_range=(0, 1e8),
            default=1,
            describe='.'
        )
        return params

    def to_aug(self):
        return Dropout2d(
            p=self.params['p'].get_value(),
            nb_keep_channels=self.params['nb_keep_channels'].get_value()
        )

    def to_code(self):
        return 'iaa.Dropout2d(\np={},\nnb_keep_channels={}\n)'.format(
            self.params['p'].get_value(),
            self.params['nb_keep_channels'].get_value(),
        )


class ImpulseNoiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'ImpulseNoise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add impulse noise to images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.03),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
                )
            },
            default='Float Range'
        )
        return params

    def to_aug(self):
        return ImpulseNoise(
            p=self.params['p'].get_value()
        )

    def to_code(self):
        return 'iaa.ImpulseNoise(\np={},\n)'.format(
            self.params['p'].get_value(),
        )


class InvertWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Invert'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Invert all values in images, e.g. turn 5 into 255-5=250.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = FloatParam(
            name='p',
            value_range=(0, 1.),
            default=1.
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
        params['min_value'] = ChoiceParam(
            name='min_value',
            value_range={
                'Default': DefaultParam(),
                'Float': FloatParam(
                    value_range=(0, 255),
                    default=0,
                )
            },
            default='Default'
        )
        params['max_value'] = ChoiceParam(
            name='max_value',
            value_range={
                'default': DefaultParam(),
                'Float': FloatParam(
                    value_range=(0, 255),
                    default=255,
                )
            },
            default='default'
        )

        params['threshold'] = ChoiceParam(
            name='threshold',
            value_range={
                'default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 255),
                    default=128,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 255), (0, 255)),
                    default=(0, 255),
                ),
                'Int List': IntListParam(
                    value_range=(0, 255),
                    default='0,50,100,150'
                )
            },
            default='default'
        )
        params['invert_above_threshold'] = ChoiceParam(
            name='invert_above_threshold',
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
            default='Float'
        )
        return params

    def to_aug(self):
        return Invert(
            p=self.params['p'].get_value(),
            per_channel=self.params['per_channel'].get_value(),
            min_value=self.params['min_value'].get_value(),
            max_value=self.params['max_value'].get_value(),
            threshold=self.params['threshold'].get_value(),
            invert_above_threshold=self.params['invert_above_threshold'].get_value()
        )

    def to_code(self):
        return 'iaa.Invert(\np={},\nper_channel={},\nmin_value={},\nmax_value={},\nthreshold={},\n' \
               'invert_above_threshold={}\n)'.format(self.params['p'].get_value(),
                                                     self.params['per_channel'].get_value(),
                                                     self.params['min_value'].get_value(),
                                                     self.params['max_value'].get_value(),
                                                     self.params['threshold'].get_value(),
                                                     self.params['invert_above_threshold'].get_value(),
                                                     )


class JpegCompressionWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'JpegCompression'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Degrade the quality of images by JPEG-compressing them.'

    @staticmethod
    def __init_param():
        params = dict()
        params['compression'] = ChoiceParam(
            name='compression',
            value_range={
                'Int': IntParam(
                    value_range=(0, 100),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 100), (0, 100)),
                    default=(0, 100),
                ),
                'Int List': IntListParam(
                    value_range=(0, 100),
                    default='0, 30, 60, 100'
                )
            },
            default='Int Range'
        )
        return params

    def to_aug(self):
        return JpegCompression(
            compression=self.params['compression'].get_value()
        )

    def to_code(self):
        return 'iaa.JpegCompression(\ncompression={}\n)'.format(
            self.params['compression'].get_value(),
        )


class MultiplyWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Multiply'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply all pixels in an image with a random value sampled once per image.'

    @staticmethod
    def __init_param():
        params = dict()
        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.0,
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
        return Multiply(
            mul=self.params['mul'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.Multiply(\nmul={},\nper_channel={}\n)'.format(
            self.params['mul'].get_value(),
            self.params['per_channel'].get_value()
        )


class MultiplyElementwiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MultiplyElementwise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply image pixels with values that are pixelwise randomly sampled.'

    @staticmethod
    def __init_param():
        params = dict()
        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.0,
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
        return MultiplyElementwise(
            mul=self.params['mul'].get_value(),
            per_channel=self.params['per_channel'].get_value() == 'True'
        )

    def to_code(self):
        return 'iaa.MultiplyElementwise(\nmul={},\nper_channel={}\n)'.format(
            self.params['mul'].get_value(),
            self.params['per_channel'].get_value()
        )


class PepperWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Pepper'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace pixels in images with pepper noise, i.e. black-ish pixels.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.05),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
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
        return Pepper(
            p=self.params['p'].get_value(),
            per_channel=self.params['per_channel'].get_value()
        )

    def to_code(self):
        return 'iaa.Pepper(\np={},\nper_channel={}\n)'.format(
            self.params['p'].get_value(),
            self.params['per_channel'].get_value(),
        )


class ReplaceElementwiseWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'ReplaceElementwise'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace pixels in an image with new values.'

    @staticmethod
    def __init_param():
        params = dict()
        params['mask'] = ChoiceParam(
            name='mask',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.05,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
                )
            },
            default='Float'
        )
        params['replacement'] = ChoiceParam(
            name='replacement',
            value_range={
                'Int': IntParam(
                    value_range=(0, 255),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 255), (0, 255)),
                    default=(0, 255),
                ),
                'Int List': IntListParam(
                    value_range=(0, 255),
                    default='0, 128, 255'
                )
            },
            default='Int Range'
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
        return ReplaceElementwise(
            mask=self.params['mask'].get_value(),
            replacement=self.params['replacement'].get_value(),
            per_channel=self.params['per_channel'].get_value()
        )

    def to_code(self):
        return 'iaa.ReplaceElementwise(\nmask={},\nreplacement={},\nper_channel={}\n)'.format(
            self.params['mask'].get_value(),
            self.params['replacement'].get_value(),
            self.params['per_channel'].get_value(),
        )


class SaltWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Salt'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace pixels in images with salt noise, i.e. white-ish pixels.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.03),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
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
        return Salt(
            p=self.params['p'].get_value(),
            per_channel=self.params['per_channel'].get_value()
        )

    def to_code(self):
        return 'iaa.Salt(\np={},\nper_channel={}\n)'.format(
            self.params['p'].get_value(),
            self.params['per_channel'].get_value(),
        )


class SaltAndPepperWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'SaltAndPepper'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Replace pixels in images with salt/pepper noise (white/black-ish colors).'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.03),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
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
        return SaltAndPepper(
            p=self.params['p'].get_value(),
            per_channel=self.params['per_channel'].get_value()
        )

    def to_code(self):
        return 'iaa.SaltAndPepper(\np={},\nper_channel={}\n)'.format(
            self.params['p'].get_value(),
            self.params['per_channel'].get_value(),
        )


class SolarizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Solarize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Invert all pixel values above a threshold.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = FloatParam(
            name='p',
            value_range=(0, 1.),
            default=1.
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
        params['min_value'] = ChoiceParam(
            name='min_value',
            value_range={
                'Default': DefaultParam(),
                'Float': FloatParam(
                    value_range=(0, 255),
                    default=0,
                )
            },
            default='Default'
        )
        params['max_value'] = ChoiceParam(
            name='max_value',
            value_range={
                'Default': DefaultParam(),
                'Float': FloatParam(
                    value_range=(0, 255),
                    default=255,
                )
            },
            default='Default'
        )
        params['threshold'] = ChoiceParam(
            name='threshold',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 255),
                    default=128,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 255), (0, 255)),
                    default=(64, 192),
                ),
                'Int List': IntListParam(
                    value_range=(0, 255),
                    default='0,50,100,150'
                )
            },
            default='Int'
        )
        params['invert_above_threshold'] = ChoiceParam(
            name='invert_above_threshold',
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
            default='Float'
        )
        return params

    def to_aug(self):
        return Solarize(
            p=self.params['p'].get_value(),
            per_channel=self.params['per_channel'].get_value(),
            min_value=self.params['min_value'].get_value(),
            max_value=self.params['max_value'].get_value(),
            threshold=self.params['threshold'].get_value(),
            invert_above_threshold=self.params['invert_above_threshold'].get_value()
        )

    def to_code(self):
        return 'iaa.Solarize(\np={},\nper_channel={},\nmin_value={},\nmax_value={},\nthreshold={},\n' \
               'invert_above_threshold={}\n)'.format(self.params['p'].get_value(),
                                                     self.params['per_channel'].get_value(),
                                                     self.params['min_value'].get_value(),
                                                     self.params['max_value'].get_value(),
                                                     self.params['threshold'].get_value(),
                                                     self.params['invert_above_threshold'].get_value(),
                                                     )


class TotalDropoutWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'TotalDropout'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Drop all channels of a defined fraction of all images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['p'] = ChoiceParam(
            name='p',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1.),
                    default=0.2,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1.), (0, 1.)),
                    default=(0, 0.05),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1.),
                    default='0,0.1,0.2,0.3'
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
        # print(self.params['fill_mode'].get_value())
        return TotalDropout(
            p=self.params['p'].get_value()
        )

    def to_code(self):
        return 'iaa.TotalDropout(\np={}\n)'.format(
            self.params['p'].get_value()
        )
