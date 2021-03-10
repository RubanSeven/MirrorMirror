# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from .param import *
from PyQt5.QtWidgets import *
from imgaug.augmenters.segmentation import *


class KMeansColorQuantizationWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'RegularGridVoronoi'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Quantize colors using k-Means clustering.'

    @staticmethod
    def __init_param():
        params = dict()

        params['n_rows'] = ChoiceParam(
            name='n_rows',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=10,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(10, 30),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='10,20,30'
                )
            },
            default='Int Range'
        )
        params['n_cols'] = ChoiceParam(
            name='n_cols',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=10,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(10, 30),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='10,20,30'
                )
            },
            default='Int Range'
        )
        params['p_drop_points'] = ChoiceParam(
            name='p_drop_points',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.5,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.0, 0.5),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.0,0.2,0.5'
                )
            },
            default='Float Range'
        )
        params['p_replace'] = ChoiceParam(
            name='p_replace',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.5,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.5, 1.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.5,0.7,1.0'
                )
            },
            default='Float Range'
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
        return RegularGridVoronoi(
            n_rows=self.params['n_rows'].get_value(),
            n_cols=self.params['n_cols'].get_value(),
            p_drop_points=self.params['p_drop_points'].get_value(),
            p_replace=self.params['p_replace'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.RegularGridVoronoi(\nn_colors={},\nn_cols={},\np_drop_points={},\np_replace={},\nmax_size={},\n' \
               'interpolation="{}"\n)'.format(self.params['n_rows'].get_value(),
                                              self.params['n_cols'].get_value(),
                                              self.params['p_drop_points'].get_value(),
                                              self.params['p_replace'].get_value(),
                                              self.params['max_size'].get_value(),
                                              self.params['interpolation'].get_value()
                                              )


class RelativeRegularGridVoronoiWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'RelativeRegularGridVoronoi'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Sample Voronoi cells from image-dependent grids and color-average them.'

    @staticmethod
    def __init_param():
        params = dict()

        params['n_rows_frac'] = ChoiceParam(
            name='n_rows_frac',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.05,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.05, 0.15),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.05,0.1,0.15'
                )
            },
            default='Float Range'
        )
        params['n_cols_frac'] = ChoiceParam(
            name='n_cols_frac',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.05,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.05, 0.15),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.05,0.1,0.15'
                )
            },
            default='Float Range'
        )
        params['p_drop_points'] = ChoiceParam(
            name='p_drop_points',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.5,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.0, 0.5),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.0,0.2,0.5'
                )
            },
            default='Float Range'
        )
        params['p_replace'] = ChoiceParam(
            name='p_replace',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.5,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.5, 1.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.5,0.7,1.0'
                )
            },
            default='Float Range'
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
        return RelativeRegularGridVoronoi(
            n_rows_frac=self.params['n_rows_frac'].get_value(),
            n_cols_frac=self.params['n_cols_frac'].get_value(),
            p_drop_points=self.params['p_drop_points'].get_value(),
            p_replace=self.params['p_replace'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.RelativeRegularGridVoronoi(\nn_rows_frac={},\nn_cols_frac={},\np_drop_points={},\np_replace={},\n' \
               'max_size={},\ninterpolation="{}"\n)'.format(self.params['n_rows_frac'].get_value(),
                                                            self.params['n_cols_frac'].get_value(),
                                                            self.params['p_drop_points'].get_value(),
                                                            self.params['p_replace'].get_value(),
                                                            self.params['max_size'].get_value(),
                                                            self.params['interpolation'].get_value()
                                                            )


class SuperpixelsWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'Superpixels'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Transform images parially/completely to their superpixel representation.'

    @staticmethod
    def __init_param():
        params = dict()

        params['p_replace'] = ChoiceParam(
            name='p_replace',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.5,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.5, 1.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.5,0.7,1.0'
                )
            },
            default='Float Range'
        )
        params['n_segments'] = ChoiceParam(
            name='n_segments',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=50,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(50, 120),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='50,80,120'
                )
            },
            default='Int Range'
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
        return Superpixels(
            p_replace=self.params['p_replace'].get_value(),
            n_segments=self.params['n_segments'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.Superpixels(\np_replace={},\nn_segments={},\nmax_size={},\ninterpolation="{}"\n)'.format(
            self.params['p_replace'].get_value(),
            self.params['n_segments'].get_value(),
            self.params['max_size'].get_value(),
            self.params['interpolation'].get_value()
        )


class UniformVoronoiWidget(QTreeWidgetItem):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.name = 'UniformVoronoi'
        self.setText(0, self.name)
        self.params = self.__init_param()
        self.has_child = False
        self.describe = 'Transform images parially/completely to their superpixel representation.'

    @staticmethod
    def __init_param():
        params = dict()

        params['n_points'] = ChoiceParam(
            name='n_points',
            value_range={
                'Int': IntParam(
                    value_range=(1, 1e8),
                    default=50,
                ),
                'Int Range': IntRangeParam(
                    value_ranges=((1, 1e8), (1, 1e8)),
                    default=(50, 500),
                ),
                'Int List': IntListParam(
                    value_range=(1, 1e8),
                    default='50,200,500'
                )
            },
            default='Int Range'
        )
        params['p_replace'] = ChoiceParam(
            name='p_replace',
            value_range={
                'Float': FloatParam(
                    value_range=(0, 1),
                    default=0.5,
                ),
                'Float Range': FloatRangeParam(
                    value_ranges=((0, 1), (0, 1)),
                    default=(0.5, 1.0),
                ),
                'Float List': FloatListParam(
                    value_range=(0, 1),
                    default='0.5,0.7,1.0'
                )
            },
            default='Float Range'
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
        return UniformVoronoi(
            n_points=self.params['n_points'].get_value(),
            p_replace=self.params['p_replace'].get_value(),
            max_size=self.params['max_size'].get_value(),
            interpolation=self.params['interpolation'].get_value()
        )

    def to_code(self):
        return 'iaa.UniformVoronoi(\nn_points={},\np_replace={},\nmax_size={},\ninterpolation="{}"\n)'.format(
            self.params['n_points'].get_value(),
            self.params['p_replace'].get_value(),
            self.params['max_size'].get_value(),
            self.params['interpolation'].get_value()
        )
