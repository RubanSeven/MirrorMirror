# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from imgaug.augmenters.color import *


class WithColorspaceWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'WithColorspace'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = True
        self.describe = 'This augumenter takes a source colorspace A and a target colorspace B as well as children C.' \
                        ' It changes images from A to B, then applies the child augmenters C and finally changes the ' \
                        'colorspace back from B to A. See also ChangeColorspace() for more.'

    @staticmethod
    def __init_param():
        params = dict()
        params['to_colorspace'] = EnumParam(
            name='to_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='HSV',
            describe='The target colorspace'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB',
            describe='The source colorspace (of the input images).'
        )
        return params

    def to_aug(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_aug())

        return WithColorspace(
            to_colorspace=self.params['to_colorspace'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value(),
            children=aug_children
        )

    def to_code(self):
        aug_children = list()
        for child_idx in range(self.childCount()):
            widget_child = self.child(child_idx)
            aug_children.append(widget_child.to_code())
        if len(aug_children) == 0:
            return 'iaa.WithColorspace(\nto_colorspace="{}",\nfrom_colorspace="{}",\nchildren=[]\n)'.format(
                self.params['to_colorspace'].get_value(),
                self.params['from_colorspace'].get_value(),
            )
        else:
            return 'iaa.WithColorspace(\nto_colorspace="{}",\nfrom_colorspace="{}",\nchildren=[\n{}\n]\n)'.format(
                self.params['to_colorspace'].get_value(),
                self.params['from_colorspace'].get_value(),
                ",\n".join(aug_children)
            )


class MultiplyAndAddToBrightnessWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MultiplyAndAddToBrightness'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply and add to the brightness channels of input images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.7, 1.3),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.7,1.0,1.3'
                )
            },
            default='Float Range'
        )
        params['add'] = ChoiceParam(
            name='add',
            value_range={
                'Int': IntParam(
                    value_range=(-255, 255),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((-255, 255), (-255, 255)),
                    default=(-30, 30),
                ),
                'Int List': IntListParam(
                    value_range=(-255, 255),
                    default='-30,0,30'
                )
            },
            default='Int Range'
        )
        params['to_colorspace'] = (MultiSelectParam(name='to_colorspace',
                                                    value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab',
                                                                 'Luv', 'YUV'),
                                                    default=[2, 3, 4, 5, 6, 7],
                                                    describe='The target colorspace'))
        params['from_colorspace'] = (EnumParam(name='from_colorspace',
                                               value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                               default='RGB',
                                               describe='The source colorspace (of the input images).'))
        params['random_order'] = EnumParam(
            name='random_order',
            value_range=('True', 'False'),
            default='False',
            describe='.'
        )
        return params

    def to_aug(self):
        return MultiplyAndAddToBrightness(
            mul=self.params['mul'].get_value(),
            add=self.params['add'].get_value(),
            to_colorspace=self.params['to_colorspace'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value(),
            random_order=self.params['random_order'].get_value()
        )

    def to_code(self):
        return 'iaa.MultiplyAndAddToBrightness(\nmul={},\nadd={},\nto_colorspace="{}",\nfrom_colorspace="{}",\n' \
               'random_order={}\n)'.format(self.params['mul'].get_value(),
                                           self.params['add'].get_value(),
                                           self.params['to_colorspace'].get_value(),
                                           self.params['from_colorspace'].get_value(),
                                           self.params['random_order'].get_value(),
                                           )


class AddToBrightnessWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AddToBrightness'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add to the brightness channels of input images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['add'] = ChoiceParam(
            name='add',
            value_range={
                'Int': IntParam(
                    value_range=(-255, 255),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((-255, 255), (-255, 255)),
                    default=(-30, 30),
                ),
                'Int List': IntListParam(
                    value_range=(-255, 255),
                    default='-30,0,30'
                )
            },
            default='Int Range'
        )
        params['to_colorspace'] = (MultiSelectParam(name='to_colorspace',
                                                    value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab',
                                                                 'Luv', 'YUV'),
                                                    default=[2, 3, 4, 5, 6, 7],
                                                    describe='The target colorspace'))
        params['from_colorspace'] = (EnumParam(name='from_colorspace',
                                               value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                               default='RGB',
                                               describe='The source colorspace (of the input images).'))
        return params

    def to_aug(self):
        return AddToBrightness(
            add=self.params['add'].get_value(),
            to_colorspace=self.params['to_colorspace'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.AddToBrightness(\nadd={},\nto_colorspace="{}",\nfrom_colorspace="{}"\n)'.format(
            self.params['add'].get_value(),
            self.params['to_colorspace'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class MultiplyBrightnessWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MultiplyBrightness'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply the brightness channels of input images.'

    @staticmethod
    def __init_param():
        params = dict()
        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1e8),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1e8), (0, 1e8)),
                    default=(0.7, 1.3),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1e8),
                    default='0.7,1.0,1.3'
                )
            },
            default='Float Range'
        )
        params['to_colorspace'] = (MultiSelectParam(name='to_colorspace',
                                                    value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab',
                                                                 'Luv', 'YUV'),
                                                    default=[2, 3, 4, 5, 6, 7],
                                                    describe='The target colorspace'))
        params['from_colorspace'] = (EnumParam(name='from_colorspace',
                                               value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                               default='RGB',
                                               describe='The source colorspace (of the input images).'))
        return params

    def to_aug(self):
        return MultiplyBrightness(
            mul=self.params['mul'].get_value(),
            to_colorspace=self.params['to_colorspace'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.MultiplyBrightness(\nmul={},\nto_colorspace="{}",\nfrom_colorspace="{}"\n)'.format(
            self.params['mul'].get_value(),
            self.params['to_colorspace'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class MultiplyHueWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MultiplyHue'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply the hue of images by random values.'

    @staticmethod
    def __init_param():
        params = dict()

        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'Float': FloatParam(
                    value_range=(-10, 10),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((-10, 10), (-10, 10)),
                    default=(-3.0, 3.0),
                ),
                'Float List': FloatListParam(
                    value_range=(-10, 10),
                    default='-3.0,3.0'
                )
            },
            default='Float Range'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        return params

    def to_aug(self):
        return MultiplyHue(
            mul=self.params['mul'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.MultiplyHue(\nmul={},\nfrom_colorspace="{}"\n)'.format(
            self.params['mul'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class AddToHueWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AddToHue'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add random values to the hue of images.'

    @staticmethod
    def __init_param():
        params = dict()

        params['value'] = ChoiceParam(
            name='value',
            value_range={
                'Int': IntParam(
                    value_range=(-255, 255),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((-255, 255), (-255, 255)),
                    default=(-255, 255),
                ),
                'Int List': IntListParam(
                    value_range=(-255, 255),
                    default='-128,0,128'
                )
            },
            default='Int Range'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB',
            describe='The source colorspace (of the input images).'
        )
        return params

    def to_aug(self):
        return AddToHue(
            value=self.params['value'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.AddToHue(\nvalue={},\nfrom_colorspace="{}"\n)'.format(
            self.params['value'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class AddToHueAndSaturationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AddToHueAndSaturation'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Increases or decreases hue and saturation by random values.'

    @staticmethod
    def __init_param():
        params = dict()

        params['value'] = ChoiceParam(
            name='value',
            value_range={
                'value': ChoiceParam(
                    value_range={
                        'Int': IntParam(
                            value_range=(-255, 255),
                            default=0,
                        ),
                        'Int Range': IntRangeParam(
                            value_ranges=((-255, 255), (-255, 255)),
                            default=(-255, 255),
                        ),
                        'Int List': IntListParam(
                            value_range=(-255, 255),
                            default='-128,0,128'
                        )
                    },
                    default='Int Range'
                ),
                'value_hue': ChoiceParam(
                    value_range={
                        'Int': IntParam(
                            value_range=(-255, 255),
                            default=0,
                        ),
                        'Int Range': IntRangeParam(
                            value_ranges=((-255, 255), (-255, 255)),
                            default=(-255, 255),
                        ),
                        'Int List': IntListParam(
                            value_range=(-255, 255),
                            default='-128,0,128'
                        )
                    },
                    default='Int Range'
                ),
                'value_saturation': ChoiceParam(
                    value_range={
                        'Int': IntParam(
                            value_range=(-255, 255),
                            default=1.,
                        ),
                        'Int Range': IntRangeParam(
                            value_ranges=((-255, 255), (-255, 255)),
                            default=(-255, 255),
                        ),
                        'Int List': IntListParam(
                            value_range=(-255, 255),
                            default='-128,0,128'
                        )
                    },
                    default='Int Range'
                )
            },
            default='value'
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
        params['from_colorspace'] = EnumParam(name='from_colorspace',
                                              value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                              default='RGB',
                                              describe='The source colorspace (of the input images).')
        return params

    def to_aug(self):
        if self.params['value'].value == 0:
            return AddToHueAndSaturation(
                value=self.params['value'].get_value(),
                per_channel=self.params['per_channel'].get_value(),
                from_colorspace=self.params['from_colorspace'].get_value()
            )
        elif self.params['value'].value == 1:
            return AddToHueAndSaturation(
                value_hue=self.params['value'].get_value(),
                per_channel=self.params['per_channel'].get_value(),
                from_colorspace=self.params['from_colorspace'].get_value()
            )
        else:
            return AddToHueAndSaturation(
                value_saturation=self.params['value'].get_value(),
                per_channel=self.params['per_channel'].get_value(),
                from_colorspace=self.params['from_colorspace'].get_value()
            )

    def to_code(self):
        if self.params['value'].value == 0:
            return 'iaa.AddToHueAndSaturation(\nvalue={},\nper_channel={},\nfrom_colorspace="{}"\n)'.format(
                self.params['value'].get_value(),
                self.params['per_channel'].get_value(),
                self.params['from_colorspace'].get_value()
            )
        elif self.params['value'].value == 1:
            return 'iaa.AddToHueAndSaturation(\nvalue_hue={},\nper_channel={},\nfrom_colorspace="{}"\n)'.format(
                self.params['value'].get_value(),
                self.params['per_channel'].get_value(),
                self.params['from_colorspace'].get_value()
            )
        else:
            return 'iaa.AddToHueAndSaturation(\nvalue_saturation={},\nper_channel={},\nfrom_colorspace="{}"\n)'.format(
                self.params['value'].get_value(),
                self.params['per_channel'].get_value(),
                self.params['from_colorspace'].get_value()
            )


class AddToSaturationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'AddToSaturation'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Add random values to the saturation of images.'

    @staticmethod
    def __init_param():
        params = dict()

        params['value'] = ChoiceParam(
            name='value',
            value_range={
                'Int': IntParam(
                    value_range=(-255, 255),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((-255, 255), (-255, 255)),
                    default=(-75, 75),
                ),
                'Int List': IntListParam(
                    value_range=(-255, 255),
                    default='-75,0,75'
                )
            },
            default='Int Range'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB',
            describe='The source colorspace (of the input images).'
        )
        return params

    def to_aug(self):
        return AddToSaturation(
            value=self.params['value'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.AddToSaturation(\nvalue={},\nfrom_colorspace="{}"\n)'.format(
            self.params['value'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class ChangeColorTemperatureWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'ChangeColorTemperature'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Change the temperature to a provided Kelvin value.'

    @staticmethod
    def __init_param():
        params = dict()

        params['kelvin'] = ChoiceParam(
            name='kelvin',
            value_range={
                'Int': IntParam(
                    value_range=(1000, 40000),
                    default=1000,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1000, 40000), (1000, 40000)),
                    default=(1000, 11000),
                ),
                'Int List': IntListParam(
                    value_range=(1000, 40000),
                    default='1000,11000'
                )
            },
            default='Int Range'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        return params

    def to_aug(self):
        return ChangeColorTemperature(
            kelvin=self.params['kelvin'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.ChangeColorTemperature(\nkelvin={},\nfrom_colorspace="{}"\n)'.format(
            self.params['kelvin'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class ChangeColorspaceWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'ChangeColorspace'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Augmenter to change the colorspace of images.'

    @staticmethod
    def __init_param():
        params = dict()

        params['to_colorspace'] = ChoiceParam(
            name='to_colorspace',
            value_range={
                'Enum': EnumParam(
                    value_range=('RGB', 'BGR', 'GRAY', 'CIE', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv'),
                    default='RGB'
                ),
                'Enum List': EnumListParam(
                    value_range=('RGB', 'BGR', 'GRAY', 'CIE', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv'),
                    default='BGR,GRAY'
                )
            },
            default='Enum'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        params['alpha'] = ChoiceParam(
            name='alpha',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=1.0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0, 1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.0,0.5,1.0'
                )
            },
            default='Float Range'
        )
        return params

    def to_aug(self):
        return ChangeColorspace(
            to_colorspace=self.params['to_colorspace'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value(),
            alpha=self.params['alpha'].get_value()
        )

    def to_code(self):
        return 'iaa.ChangeColorspace(\nto_colorspace="{}",\nfrom_colorspace="{}",\nalpha={}\n)'.format(
            self.params['to_colorspace'].get_value(),
            self.params['from_colorspace'].get_value(),
            self.params['alpha'].get_value()
        )


class GrayscaleWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Grayscale'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Augmenter to convert images to their grayscale versions.'

    @staticmethod
    def __init_param():
        params = dict()

        params['alpha'] = ChoiceParam(
            name='alpha',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=1.0,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0, 1),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.0,0.5,1.0'
                )
            },
            default='Float Range'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB',
            describe='The source colorspace (of the input images).'
        )

        return params

    def to_aug(self):
        return Grayscale(
            alpha=self.params['alpha'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.Grayscale(\nalpha={},\nfrom_colorspace="{}"\n)'.format(
            self.params['alpha'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class KMeansColorQuantizationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'KMeansColorQuantization'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Quantize colors using k-Means clustering.'

    @staticmethod
    def __init_param():
        params = dict()

        params['n_colors'] = ChoiceParam(
            name='n_colors',
            value_range={
                'Int': IntParam(
                    value_range=(2, 256),
                    default=16,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((2, 256), (2, 256)),
                    default=(2, 16),
                ),
                'Int List': IntListParam(
                    value_range=(2, 256),
                    default='2,8,16'
                )
            },
            default='Int Range'
        )
        params['to_colorspace'] = ChoiceParam(
            name='to_colorspace',
            value_range={
                'Default': DefaultParam(),
                'Enum': EnumParam(value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                  default='RGB',
                                  describe='The colorspace in which to perform the quantization.'),
                'Enum List': EnumListParam(value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                           default='RGB,Lab',
                                           describe='The colorspace in which to perform the quantization.')
            },
            default='Enum List'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB',
            describe='The source colorspace (of the input images).'
        )
        params['max_size'] = ChoiceParam(
            name='max_size',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=128,
                )
            },
            default='Int'
        )
        params['interpolation'] = EnumParam(
            name='interpolation',
            value_range=('nearest', 'linear', 'area', 'cubic'),
            default='linear'
        )
        return params

    def to_aug(self):
        return KMeansColorQuantization(
            n_colors=self.params['n_colors'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value(),
            to_colorspace=self.params['to_colorspace'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.KMeansColorQuantization(\nn_colors={},\nfrom_colorspace="{}",\nto_colorspace="{}",\nmax_size={},\n' \
               'interpolation="{}"\n)'.format(self.params['n_colors'].get_value(),
                                              self.params['from_colorspace'].get_value(),
                                              self.params['to_colorspace'].get_value(),
                                              self.params['max_size'].get_value(),
                                              self.params['interpolation'].get_value()
                                              )


class MultiplyHueAndSaturationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MultiplyHueAndSaturation'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply the hue of images by random values.'

    @staticmethod
    def __init_param():
        params = dict()

        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'mul': ChoiceParam(
                    value_range={
                        'Float': FloatParam(
                            value_range=(-10, 10),
                            default=1.,
                        ),
                        'Float Range': FloatRangeParam(
                            value_ranges=((-10, 10), (-10, 10)),
                            default=(-3.0, 3.0),
                        ),
                        'Float List': FloatListParam(
                            value_range=(-10, 10),
                            default='-3.0,3.0'
                        )
                    },
                    default='Float Range'
                ),
                'mul_hue': ChoiceParam(
                    value_range={
                        'Float': FloatParam(
                            value_range=(-10, 10),
                            default=1.,
                        ),
                        'Float Range': FloatRangeParam(
                            value_ranges=((-10, 10), (-10, 10)),
                            default=(-3.0, 3.0),
                        ),
                        'Float List': FloatListParam(
                            value_range=(-10, 10),
                            default='-3.0,3.0'
                        )
                    },
                    default='Float Range'
                ),
                'mul_saturation': ChoiceParam(
                    value_range={
                        'Float': FloatParam(
                            value_range=(0, 10),
                            default=1.,
                        ),
                        'Float Range': FloatRangeParam(
                            value_ranges=((0, 10), (0, 10)),
                            default=(0.0, 3.0),
                        ),
                        'Float List': FloatListParam(
                            value_range=(0, 10),
                            default='1.0,3.0'
                        )
                    },
                    default='Float Range'
                )
            },
            default='mul'
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
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        return params

    def to_aug(self):
        if self.params['mul'].value == 0:
            return MultiplyHueAndSaturation(
                mul=self.params['mul'].get_value(),
                per_channel=self.params['per_channel'].get_value(),
                from_colorspace=self.params['from_colorspace'].get_value()
            )
        elif self.params['mul'].value == 1:
            return MultiplyHueAndSaturation(
                mul_hue=self.params['mul'].get_value(),
                per_channel=self.params['per_channel'].get_value(),
                from_colorspace=self.params['from_colorspace'].get_value()
            )
        else:
            return MultiplyHueAndSaturation(
                mul_saturation=self.params['mul'].get_value(),
                per_channel=self.params['per_channel'].get_value(),
                from_colorspace=self.params['from_colorspace'].get_value()
            )

    def to_code(self):
        if self.params['mul'].value == 0:
            return 'iaa.MultiplyHueAndSaturation(\nmul={},\nper_channel={},\nfrom_colorspace="{}"\n)'.format(
                self.params['mul'].get_value(),
                self.params['per_channel'].get_value(),
                self.params['from_colorspace'].get_value()
            )
        elif self.params['mul'].value == 1:
            return 'iaa.MultiplyHueAndSaturation(\nmul_hue={},\nper_channel={},\nfrom_colorspace="{}"\n)'.format(
                self.params['mul'].get_value(),
                self.params['per_channel'].get_value(),
                self.params['from_colorspace'].get_value()
            )
        else:
            return 'iaa.MultiplyHueAndSaturation(\nmul_saturation={},\nper_channel={},\nfrom_colorspace="{}"\n)'.format(
                self.params['mul'].get_value(),
                self.params['per_channel'].get_value(),
                self.params['from_colorspace'].get_value()
            )


class MultiplySaturationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'MultiplySaturation'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Multiply the saturation of images by random values.'

    @staticmethod
    def __init_param():
        params = dict()

        params['mul'] = ChoiceParam(
            name='mul',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 10),
                    default=1.,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 10), (0, 10)),
                    default=(0.0, 3.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 10),
                    default='1.0,3.0'
                )
            },
            default='Float Range'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        return params

    def to_aug(self):
        return MultiplySaturation(
            mul=self.params['mul'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.MultiplySaturation(\nmul={},\nfrom_colorspace="{}"\n)'.format(
            self.params['mul'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class PosterizeWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Posterize'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Quantize images by setting 8-B bits of each component to zero.'

    @staticmethod
    def __init_param():
        params = dict()

        params['nb_bits'] = ChoiceParam(
            name='nb_bits',
            value_range={
                'Int': IntParam(
                    value_range=(0, 16),
                    default=0,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((0, 16), (0, 16)),
                    default=(1, 8),
                ),
                'Int List': IntListParam(
                    value_range=(0, 16),
                    default='1,2,3,4,5,6,7,8'
                )
            },
            default='Int Range'
        )
        params['to_colorspace'] = ChoiceParam(
            name='to_colorspace',
            value_range={
                'Default': DefaultParam(),
                'Enum List': EnumListParam(
                    value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                    default='RGB'
                )
            },
            default='Default'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        params['max_size'] = ChoiceParam(
            name='max_size',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512,
                )
            },
            default='Default'
        )
        params['interpolation'] = EnumParam(
            name='interpolation',
            value_range=('nearest', 'linear', 'area', 'cubic'),
            default='linear'
        )
        return params

    def to_aug(self):
        return Posterize(
            nb_bits=self.params['nb_bits'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value(),
            to_colorspace=self.params['to_colorspace'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.Posterize(\nnb_bits={},\nfrom_colorspace="{}",\nto_colorspace="{}",\nmax_size={},\n' \
               'interpolation="{}"\n)'.format(self.params['nb_bits'].get_value(),
                                              self.params['from_colorspace'].get_value(),
                                              self.params['to_colorspace'].get_value(),
                                              self.params['max_size'].get_value(),
                                              self.params['interpolation'].get_value()
                                              )


class RemoveSaturationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'RemoveSaturation'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Decrease the saturation of images by varying degrees.'

    @staticmethod
    def __init_param():
        params = dict()

        params['mul'] = ChoiceParam(
            name='mul',
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
                    default='0.1,0.5,1.0'
                )
            },
            default='Float'
        )
        params['from_colorspace'] = EnumParam(
            name='from_colorspace',
            value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
            default='RGB'
        )
        return params

    def to_aug(self):
        return RemoveSaturation(
            mul=self.params['mul'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value()
        )

    def to_code(self):
        return 'iaa.RemoveSaturation(\nmul={},\nfrom_colorspace="{}"\n)'.format(
            self.params['mul'].get_value(),
            self.params['from_colorspace'].get_value()
        )


class UniformColorQuantizationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'UniformColorQuantization'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Quantize colors into N bins with regular distance.'

    @staticmethod
    def __init_param():
        params = dict()

        params['n_colors'] = ChoiceParam(
            name='n_colors',
            value_range={
                'Int': IntParam(
                    value_range=(2, 256),
                    default=16,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((2, 256), (2, 256)),
                    default=(2, 16),
                ),
                'Int List': IntListParam(
                    value_range=(2, 256),
                    default='2,8,16'
                )
            },
            default='Int Range'
        )
        params['to_colorspace'] = ChoiceParam(
            name='to_colorspace',
            value_range={
                'Default': DefaultParam(),
                'Enum': EnumParam(
                    value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                    default='RGB'
                ),
                'Enum List': EnumListParam(
                    value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                    default='RGB,Lab'
                )
            },
            default='Default'
        )
        params['from_colorspace'] = EnumParam(name='from_colorspace',
                                              value_range=('RGB', 'BGR', 'YCrCb', 'HSV', 'HLS', 'Lab', 'Luv', 'YUV'),
                                              default='RGB',
                                              describe='The source colorspace (of the input images).')
        params['max_size'] = ChoiceParam(
            name='max_size',
            value_range={
                'Default': DefaultParam(),
                'Int': IntParam(
                    value_range=(0, 1e8),
                    default=512,
                )
            },
            default='Default'
        )
        params['interpolation'] = EnumParam(
            name='interpolation',
            value_range=('nearest', 'linear', 'area', 'cubic'),
            default='linear'
        )
        return params

    def to_aug(self):
        return UniformColorQuantization(
            n_colors=self.params['n_colors'].get_value(),
            from_colorspace=self.params['from_colorspace'].get_value(),
            to_colorspace=self.params['to_colorspace'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.UniformColorQuantization(\nn_colors={},\nfrom_colorspace="{}",\nto_colorspace="{}",\nmax_size={},\n' \
               'interpolation="{}"\n)'.format(self.params['n_colors'].get_value(),
                                              self.params['from_colorspace'].get_value(),
                                              self.params['to_colorspace'].get_value(),
                                              self.params['max_size'].get_value(),
                                              self.params['interpolation'].get_value()
                                              )
