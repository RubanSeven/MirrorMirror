# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from PyQt5.QtWidgets import *
from imgaug.augmenters.size import *


class CenterCropToAspectRatioWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterCropToAspectRatio'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Crop images equally on all sides until they reach an aspect ratio.'

    @staticmethod
    def __init_param():
        params = dict()

        params['aspect_ratio'] = FloatParam(
            name='aspect_ratio',
            value_range=(0, 1e8),
            default=1
        )
        return params

    def to_aug(self):
        return CenterCropToAspectRatio(
            aspect_ratio=self.params['aspect_ratio'].get_value()
        )

    def to_code(self):
        return 'iaa.CenterCropToAspectRatio(\naspect_ratio={}\n)'.format(self.params['aspect_ratio'].get_value())


class CenterCropToFixedSizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterCropToFixedSize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Take a crop from the center of each image.'

    @staticmethod
    def __init_param():
        params = dict()

        params['width'] = ChoiceParam(
            name='width',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default',
        )
        params['height'] = ChoiceParam(
            name='height',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
        )
        return params

    def to_aug(self):
        return CenterCropToFixedSize(
            width=self.params['width'].get_value(),
            height=self.params['height'].get_value(),
        )

    def to_code(self):
        return 'iaa.CenterCropToFixedSize(\nwidth={},\nheight={}\n)'.format(
            self.params['width'].get_value(),
            self.params['height'].get_value(),
        )


class CenterCropToMultiplesOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterCropToMultiplesOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Crop images equally on all sides until H/W are multiples of given values.'

    @staticmethod
    def __init_param():
        params = dict()

        params['width_multiple'] = ChoiceParam(
            name='width_multiple',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        params['height_multiple '] = ChoiceParam(
            name='height_multiple ',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        return params

    def to_aug(self):
        return CenterCropToMultiplesOf(
            width_multiple=self.params['width_multiple'].get_value(),
            height_multiple=self.params['height_multiple '].get_value(),
        )

    def to_code(self):
        return 'iaa.CenterCropToMultiplesOf(\nwidth_multiple={},\nheight_multiple={}\n)'.format(
            self.params['width_multiple'].get_value(),
            self.params['height_multiple'].get_value(),
        )


class CenterCropToPowersOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterCropToPowersOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Crop images equally on all sides until H/W is a power of a base.'

    @staticmethod
    def __init_param():
        params = dict()

        params['width_base'] = ChoiceParam(
            name='width_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        params['height_base'] = ChoiceParam(
            name='height_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        return params

    def to_aug(self):
        return CenterCropToPowersOf(
            width_base=self.params['width_base'].get_value(),
            height_base=self.params['height_base'].get_value(),
        )

    def to_code(self):
        return 'iaa.CenterCropToPowersOf(\nwidth_base={},\nheight_base={}\n)'.format(
            self.params['width_base'].get_value(),
            self.params['height_base'].get_value(),
        )


class CenterCropToSquareWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterCropToSquare'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Crop images equally on all sides until their height/width are identical.'

    @staticmethod
    def __init_param():
        params = dict()

        return params

    def to_aug(self):
        return CenterCropToSquare()

    def to_code(self):
        return 'iaa.CenterCropToSquare()'


class CenterPadToAspectRatioWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterPadToAspectRatio'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Pad images equally on all sides until H/W matches an aspect ratio.'

    @staticmethod
    def __init_param():
        params = dict()

        params['aspect_ratio'] = IntParam(
            name='aspect_ratio',
            value_range=(0, 1e8),
            default=1
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
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
                        'center-center', 'center-bottom', 'right-top', 'right-center', 'right-bottom'
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
        return params

    def to_aug(self):
        return CenterPadToAspectRatio(
            aspect_ratio=self.params['aspect_ratio'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value()
        )

    def to_code(self):
        return 'iaa.CenterPadToAspectRatio(\naspect_ratio={},\npad_mode={},\npad_cval={}\n)'.format(
            self.params['aspect_ratio'].get_value(),
            self.params['pad_mode'].get_value(),
            self.params['pad_cval'].get_value(),
        )


class CenterPadToFixedSizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterPadToFixedSize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['width'] = ChoiceParam(
            name='width',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
        )
        params['height'] = ChoiceParam(
            name='height',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
                )
            },
            default='Int'
        )
        return params

    def to_aug(self):
        return CenterPadToFixedSize(
            width=self.params['width'].get_value(),
            height=self.params['height'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value()
        )

    def to_code(self):
        return 'iaa.CenterPadToFixedSize(\nwidth={},\nheight={},\npad_mode={},\npad_cval={}\n)'.format(
            self.params['width'].get_value(),
            self.params['height'].get_value(),
            self.params['pad_mode'].get_value(),
            self.params['pad_cval'].get_value(),
        )


class CenterPadToMultiplesOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterPadToMultiplesOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['width_multiple'] = ChoiceParam(
            name='width_multiple',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        params['height_multiple'] = ChoiceParam(
            name='height_multiple',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
                )
            },
            default='Int'
        )
        return params

    def to_aug(self):
        return CenterPadToMultiplesOf(
            width_multiple=self.params['width_multiple'].get_value(),
            height_multiple=self.params['height_multiple'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value()
        )

    def to_code(self):
        return 'iaa.CenterPadToMultiplesOf(\nwidth_multiple={},\nheight_multiple={},\npad_mode={},\npad_cval={}\n)'.format(
            self.params['width_multiple'].get_value(),
            self.params['height_multiple'].get_value(),
            self.params['pad_mode'].get_value(),
            self.params['pad_cval'].get_value(),
        )


class CenterPadToPowersOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterPadToPowersOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['width_base'] = ChoiceParam(
            name='width_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        params['height_base'] = ChoiceParam(
            name='height_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
                )
            },
            default='Int'
        )
        return params

    def to_aug(self):
        return CenterPadToPowersOf(
            width_base=self.params['width_base'].get_value(),
            height_base=self.params['height_base'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value()
        )

    def to_code(self):
        return 'iaa.CenterPadToPowersOf(\nwidth_base={},\nheight_base={},\npad_mode={},\npad_cval={}\n)'.format(
            self.params['width_base'].get_value(),
            self.params['height_base'].get_value(),
            self.params['pad_mode'].get_value(),
            self.params['pad_cval'].get_value(),
        )


class CenterPadToSquareWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CenterPadToSquare'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
                )
            },
            default='Int'
        )
        return params

    def to_aug(self):
        return CenterPadToSquare(
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value()
        )

    def to_code(self):
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        return 'iaa.CenterPadToSquare(\npad_mode={},\npad_cval={}\n)'.format(
            pad_mode,
            self.params['pad_cval'].get_value()
        )


class CropToAspectRatioWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CropToAspectRatio'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['aspect_ratio'] = FloatParam(
            name='aspect_ratio',
            value_range=(0, 1e8),
            default=1,
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
        return params

    def to_aug(self):
        return CropToAspectRatio(
            aspect_ratio=self.params['aspect_ratio'].get_value(),
            position=self.params['position'].get_value()
        )

    def to_code(self):
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.CropToAspectRatio(\naspect_ratio={},\nposition={}\n)'.format(
            self.params['aspect_ratio'].get_value(),
            position
        )


class CropToFixedSizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CropToFixedSize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['width'] = ChoiceParam(
            name='width',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
        )
        params['height'] = ChoiceParam(
            name='height',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
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
        return params

    def to_aug(self):
        return CropToFixedSize(
            width=self.params['width'].get_value(),
            height=self.params['height'].get_value(),
            position=self.params['position'].get_value()
        )

    def to_code(self):
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.CropToFixedSize(\nwidth={},\nheight={},\nposition={}\n)'.format(
            self.params['width'].get_value(),
            self.params['height'].get_value(),
            position
        )


class CropToMultiplesOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CropToMultiplesOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['width_multiple'] = ChoiceParam(
            name='width_multiple',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        params['height_multiple '] = ChoiceParam(
            name='height_multiple ',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
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
        return params

    def to_aug(self):
        return CropToMultiplesOf(
            width_multiple=self.params['width_multiple'].get_value(),
            height_multiple=self.params['height_multiple'].get_value(),
            position=self.params['position'].get_value()
        )

    def to_code(self):
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.CropToMultiplesOf(\nwidth_multiple={},\nheight_multiple={},\nposition={}\n)'.format(
            self.params['width_multiple'].get_value(),
            self.params['height_multiple'].get_value(),
            position
        )


class CropToPowersOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CropToPowersOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['width_base'] = ChoiceParam(
            name='width_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        params['height_base'] = ChoiceParam(
            name='height_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
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
        return params

    def to_aug(self):
        return CropToPowersOf(
            width_base=self.params['width_base'].get_value(),
            height_base=self.params['height_base'].get_value(),
            position=self.params['position'].get_value()
        )

    def to_code(self):
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.CropToPowersOf(\nwidth_base={},\nheight_base={},\nposition={}\n)'.format(
            self.params['width_base'].get_value(),
            self.params['height_base'].get_value(),
            position
        )


class CropToSquareWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'CropToSquare'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Crop images until their width and height are identical.'

    @staticmethod
    def __init_param():
        params = dict()

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
        return params

    def to_aug(self):
        return CropToSquare(
            position=self.params['position'].get_value()
        )

    def to_code(self):
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.CropToSquare(\nposition={}\n)'.format(
            position
        )


class KeepSizeByResizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'KeepSizeByResize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = True

    @staticmethod
    def __init_param():
        params = dict()

        params['interpolation'] = ChoiceParam(
            name='interpolation',
            value_range={
                'Multi Select': MultiSelectParam(
                    value_range=('nearest', 'linear', 'area', 'cubic'),
                    default=[3]
                ),
                'NO_RESIZE': DefaultParam(
                    name='NO_RESIZE',
                    default='NO_RESIZE'
                )
            },
            default='Multi Select'
        )
        params['interpolation_heatmaps'] = ChoiceParam(
            name='interpolation_heatmaps',
            value_range={
                'SAME_AS_IMAGES': DefaultParam(
                    name='SAME_AS_IMAGES',
                    default='SAME_AS_IMAGES'
                ),
                'NO_RESIZE': DefaultParam(
                    name='NO_RESIZE',
                    default='NO_RESIZE'
                ),
                'Multi Select': MultiSelectParam(
                    value_range=('nearest', 'linear', 'area', 'cubic'),
                    default=[3]
                )
            },
            default='SAME_AS_IMAGES'
        )
        params['interpolation_segmaps'] = ChoiceParam(
            name='interpolation_segmaps',
            value_range={
                'SAME_AS_IMAGES': DefaultParam(
                    name='SAME_AS_IMAGES',
                    default='SAME_AS_IMAGES'
                ),
                'NO_RESIZE': DefaultParam(
                    name='NO_RESIZE',
                    default='NO_RESIZE'
                ),
                'Multi Select': MultiSelectParam(
                    value_range=('nearest', 'linear', 'area', 'cubic'),
                    default=[0]
                )
            },
            default='Multi Select'
        )
        return params

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return KeepSizeByResize(
            children=aug_children,
            interpolation=self.params['interpolation'].get_value(),
            interpolation_heatmaps=self.params['interpolation_heatmaps'].get_value(),
            interpolation_segmaps=self.params['interpolation_segmaps'].get_value(),
        )

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())
        if len(aug_children) == 0:
            return 'iaa.Sequential(\nchildren=[],\ninterpolation={},\ninterpolation_heatmaps={},\n' \
                   'interpolation_segmaps={}\n)'.format(self.params['interpolation'].get_value(),
                                                        self.params['interpolation_heatmaps'].get_value(),
                                                        self.params['interpolation'].get_value(),
                                                        )
        else:
            return 'iaa.Sequential(\nchildren=[\n{}\n],\ninterpolation={},\ninterpolation_heatmaps={},\n' \
                   'interpolation_segmaps={}\n)'.format(",\n".join(aug_children),
                                                        self.params['interpolation'].get_value(),
                                                        self.params['interpolation_heatmaps'].get_value(),
                                                        self.params['interpolation_segmaps'].get_value(),
                                                        )


class PadWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Pad'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        params['px'] = ChoiceParam(
            name='px',
            default='px',
            value_range={
                'px': ChoiceParam(
                    value_range={
                        'Int': IntParam(
                            value_range=(0, 1e8),
                            default=0,
                        ),
                        'Int Range': IntRangeParam(
                            value_ranges=((0, 1e8), (0, 1e8)),
                            default=(0, 3),
                        ),
                        'Dict': DictParam(
                            children={
                                "top": ChoiceParam(
                                    value_range={
                                        'Int': IntParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Int Range': IntRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 3),
                                        )
                                    },
                                    default='Int'
                                ),
                                "right": ChoiceParam(
                                    value_range={
                                        'Int': IntParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Int Range': IntRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 3),
                                        )
                                    },
                                    default='Int'
                                ),
                                "bottom": ChoiceParam(
                                    value_range={
                                        'Int': IntParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Int Range': IntRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 3),
                                        )
                                    },
                                    default='Int'
                                ),
                                "left": ChoiceParam(
                                    value_range={
                                        'Int': IntParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Int Range': IntRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 3),
                                        )
                                    },
                                    default='Int'
                                ),
                            }
                        )
                    },
                    default='Int',
                ),
                'percent': ChoiceParam(
                    value_range={
                        'Float': FloatParam(
                            value_range=(0, 1e8),
                            default=0,
                        ),
                        'Float Range': FloatRangeParam(
                            value_ranges=((0, 1e8), (0, 1e8)),
                            default=(0, 0.5),
                        ),
                        'Dict': DictParam(
                            children={
                                "top": ChoiceParam(
                                    value_range={
                                        'Float': FloatParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Float Range': FloatRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 0.5),
                                        )
                                    },
                                    default='Float'
                                ),
                                "right": ChoiceParam(
                                    value_range={
                                        'Float': FloatParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Float Range': FloatRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 0.5),
                                        )
                                    },
                                    default='Float'
                                ),
                                "bottom": ChoiceParam(
                                    value_range={
                                        'Float': FloatParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Float Range': FloatRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 0.5),
                                        )
                                    },
                                    default='Float'
                                ),
                                "left": ChoiceParam(
                                    value_range={
                                        'Float': FloatParam(
                                            value_range=(0, 1e8),
                                            default=0,
                                        ),
                                        'Float Range': FloatRangeParam(
                                            value_ranges=((0, 1e8), (0, 1e8)),
                                            default=(0, 0.5),
                                        )
                                    },
                                    default='Float'
                                ),
                            }
                        )
                    },
                    default='Float'
                )
            }
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
                )
            },
            default='Int'
        )
        params['keep_size'] = EnumParam(
            name='keep_size',
            value_range=('True', 'False'),
            default='True'
        )
        params['sample_independently'] = EnumParam(
            name='sample_independently',
            value_range=('True', 'False'),
            default='True'
        )
        return params

    def to_aug(self):
        px = self.params['px'].get_value()
        if type(px) is dict:
            px = (px['top'], px['right'], px['bottom'], px['left'])
        if self.params['px'].value == 0:
            return Pad(
                px=px,
                pad_mode=self.params['pad_mode'].get_value(),
                pad_cval=self.params['pad_cval'].get_value(),
                keep_size=self.params['keep_size'].get_value(),
                sample_independently=self.params['sample_independently'].get_value(),
            )
        else:
            return Pad(
                percent=px,
                pad_mode=self.params['pad_mode'].get_value(),
                pad_cval=self.params['pad_cval'].get_value(),
                keep_size=self.params['keep_size'].get_value(),
                sample_independently=self.params['sample_independently'].get_value(),
            )

    def to_code(self):
        px = self.params['px'].get_value()
        if type(px) is dict:
            px = (px['top'], px['right'], px['bottom'], px['left'])
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        if self.params['px'].value == 0:
            return 'iaa.Pad(\npx={},\npad_mode={},\npad_cval={},\nkeep_size={},\nsample_independently={}\n)'.format(
                px,
                pad_mode,
                self.params['pad_cval'].get_value(),
                self.params['keep_size'].get_value(),
                self.params['sample_independently'].get_value()
            )
        else:
            return 'iaa.Pad(\npercent={},\npad_mode={},\npad_cval={},\nkeep_size={},\nsample_independently={}\n' \
                   ')'.format(px,
                              pad_mode,
                              self.params['pad_cval'].get_value(),
                              self.params['keep_size'].get_value(),
                              self.params['sample_independently'].get_value()
                              )


class PadToAspectRatioWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'PadToAspectRatio'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Pad images until their width/height matches an aspect ratio.'

    @staticmethod
    def __init_param():
        params = dict()

        params['aspect_ratio'] = IntParam(
            name='aspect_ratio',
            value_range=(0, 1e8),
            default=1
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
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
        return params

    def to_aug(self):
        return PadToAspectRatio(
            aspect_ratio=self.params['aspect_ratio'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value(),
            position=self.params['position'].get_value(),
        )

    def to_code(self):
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.PadToAspectRatio(\naspect_ratio={},\npad_mode={},\npad_cval={},\nposition={}\n)'.format(
            self.params['aspect_ratio'].get_value(),
            pad_mode,
            self.params['pad_cval'].get_value(),
            position
        )


class PadToFixedSizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'PadToFixedSize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Pad images to a predefined minimum width and/or height.'

    @staticmethod
    def __init_param():
        params = dict()

        params['width'] = ChoiceParam(
            name='width',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
        )
        params['height'] = ChoiceParam(
            name='height',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512
                ),
            },
            default='Default'
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
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
        return params

    def to_aug(self):
        return PadToFixedSize(
            width=self.params['width'].get_value(),
            height=self.params['height'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value(),
            position=self.params['position'].get_value(),
        )

    def to_code(self):
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.PadToFixedSize(\nwidth={},\nheight={},\npad_mode={},\npad_cval={},\nposition={}\n)'.format(
            self.params['width'].get_value(),
            self.params['height'].get_value(),
            pad_mode,
            self.params['pad_cval'].get_value(),
            position
        )


class PadToMultiplesOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'PadToMultiplesOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Pad images until their height/width is a multiple of a value.'

    @staticmethod
    def __init_param():
        params = dict()

        params['width_multiple'] = ChoiceParam(
            name='width_multiple',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        params['height_multiple'] = ChoiceParam(
            name='height_multiple',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=1
                ),
            },
            default='Default'
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
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
        return params

    def to_aug(self):
        return PadToMultiplesOf(
            width_multiple=self.params['width_multiple'].get_value(),
            height_multiple=self.params['height_multiple'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value(),
            position=self.params['position'].get_value(),
        )

    def to_code(self):
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.PadToMultiplesOf(\nwidth_multiple={},\nheight_multiple={},\npad_mode={},\npad_cval={},' \
               '\nposition={}\n)'.format(self.params['width_multiple'].get_value(),
                                         self.params['height_multiple'].get_value(),
                                         pad_mode,
                                         self.params['pad_cval'].get_value(),
                                         position
                                         )


class PadToPowersOfWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'PadToPowersOf'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Pad images until their height/width is a multiple of a value.'

    @staticmethod
    def __init_param():
        params = dict()

        params['width_base'] = ChoiceParam(
            name='width_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        params['height_base'] = ChoiceParam(
            name='height_base',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=2
                ),
            },
            default='Default'
        )
        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0],
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
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
        return params

    def to_aug(self):
        return PadToPowersOf(
            width_base=self.params['width_base'].get_value(),
            height_base=self.params['height_base'].get_value(),
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value(),
            position=self.params['position'].get_value(),
        )

    def to_code(self):
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.PadToPowersOf(\nwidth_base={},\nheight_base={},\npad_mode={},\npad_cval={},' \
               '\nposition={}\n)'.format(self.params['width_base'].get_value(),
                                         self.params['height_base'].get_value(),
                                         pad_mode,
                                         self.params['pad_cval'].get_value(),
                                         position
                                         )


class PadToSquareWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'PadToSquare'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Pad images until their height and width are identical.'

    @staticmethod
    def __init_param():
        params = dict()

        params['pad_mode'] = MultiSelectParam(
            name='pad_mode',
            value_range=("constant", "edge", "linear_ramp", "maximum", "mean", "median",
                         "minimum", "reflect", "symmetric", "wrap"),
            default=[0]
        )
        params['pad_cval'] = ChoiceParam(
            name='pad_cval',
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
                    default='0, 128'
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
        return params

    def to_aug(self):
        return PadToSquare(
            pad_mode=self.params['pad_mode'].get_value(),
            pad_cval=self.params['pad_cval'].get_value(),
        )

    def to_code(self):
        pad_mode = self.params['pad_mode'].get_value()
        if type(pad_mode) is str:
            pad_mode = '"' + pad_mode + '"'
        position = self.params['position'].get_value()
        if type(position) is str:
            position = '"' + position + '"'
        return 'iaa.PadToSquare(\npad_mode={},\npad_cval={},\nposition={}\n)'.format(
            pad_mode,
            self.params['pad_cval'].get_value(),
            position,
        )


class ResizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Resize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False

    @staticmethod
    def __init_param():
        params = dict()

        def create_size_value_range():
            return {
                'Enum': DefaultParam(
                    name='keep',
                    default='keep'
                ),
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=512,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(256, 512),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='256,512'
                ),
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.5, 2),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.5,1,2'
                )
            }

        params['size'] = ChoiceParam(
            name='size',
            value_range={
                'Enum': DefaultParam(
                    name='keep',
                    default='keep'
                ),
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=512,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(256, 512),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='256,512'
                ),
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.5, 2),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.5,1,2'
                ),
                'height-width': DictParam(children={
                    "height": ChoiceParam(value_range=create_size_value_range(), default='Enum'),
                    "width": ChoiceParam(value_range=create_size_value_range(), default='Enum')
                }),
                'shorter-longer': DictParam(children={
                    "shorter-side": ChoiceParam(value_range=create_size_value_range(), default='Enum'),
                    "longer-side": ChoiceParam(value_range=create_size_value_range(), default='Enum')
                })
            },
            default='Enum'
        )
        params['interpolation'] = MultiSelectParam(
            name='interpolation',
            value_range=('nearest', 'linear', 'area', 'cubic'),
            default=[3]
        )
        return params

    def to_aug(self):
        print(self.params['size'].get_value(),
              self.params['interpolation'].get_value())
        return Resize(
            size=self.params['size'].get_value(),
            interpolation=self.params['interpolation'].get_value(),
        )

    def to_code(self):
        size = self.params['size'].get_value()
        if type(size) is str:
            size = '"' + size + '"'
        return 'iaa.Resize(\nsize={},\ninterpolation="{}"\n)'.format(
            size,
            self.params['interpolation'].get_value(),
        )
