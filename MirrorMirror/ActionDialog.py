# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
import os
import inspect
import numpy as np
from .theme import *
from . import augmenters
from imgaug.augmenters import Sequential
from .ImageShowDialog import ImageShowDialog
from .utils.layout import clear_layout, FlowLayout

cur_path = os.path.dirname(os.path.realpath(__file__))


def get_modules(base_module):
    modules = inspect.getmembers(base_module, inspect.ismodule)
    new_modules = list()
    for module in modules:
        if module[0] == 'param':
            continue
        classes = inspect.getmembers(module[1], inspect.isclass)
        classes = [c for c in classes if c[1].__module__ == base_module.__name__ + '.' + module[0] and
                   c[0] != 'SequentialItem' and c[0] != 'ChildItem']
        if len(classes) > 0:
            new_modules.append((module[0], module[1], classes))

    return new_modules


class ActionDialog(QDialog):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.resize(1024, 680)
        self.__class_dict = dict()
        self.__init_element()
        self.__action_item = None
        self.samples = list()
        self.tmp_samples = list()
        self.aug_sample_imgs = list()

    def set_samples(self, samples):
        self.samples = samples
        self.__init_sample_layout()

    def __init_element(self):
        self.__main_grid = QGridLayout()
        self.__main_grid.setSpacing(0)
        self.__main_grid.setContentsMargins(0, 0, 0, 0)
        self.__main_grid.setColumnStretch(0, 4)
        self.__main_grid.setColumnStretch(1, 8)
        self.__main_grid.setColumnStretch(2, 5)
        self.setLayout(self.__main_grid)

        self.__action_tree = self.__create_action_tree()
        self.__main_grid.addWidget(self.__action_tree, 0, 0)

        middle_frame = SampleListFrame()
        middle_layout = QVBoxLayout()
        middle_layout.setContentsMargins(0, 0, 0, 12)
        self.__sample_layout = FlowLayout()
        middle_layout.addLayout(self.__sample_layout)
        middle_layout.addStretch()

        bottom_bar_layout = QHBoxLayout()
        bottom_bar_layout.setAlignment(Qt.AlignCenter)
        data_refresh_btn = IconButton(os.path.join(cur_path, r'resources/img/datarefresh.png'), height=32)
        data_refresh_btn.clicked.connect(self.__init_sample_layout)
        bottom_bar_layout.addWidget(data_refresh_btn)
        refresh_btn = IconButton(os.path.join(cur_path, r'resources/img/refresh.png'), height=32)
        refresh_btn.clicked.connect(self.__refresh_sample_layout)
        bottom_bar_layout.addWidget(refresh_btn)
        middle_layout.addLayout(bottom_bar_layout)

        middle_frame.setLayout(middle_layout)
        self.__main_grid.addWidget(middle_frame, 0, 1)

        right_grid = QVBoxLayout()

        right_scroll = ScrollArea()
        right_scroll.setWidgetResizable(True)
        right_frame = QFrame()
        right_scroll.setWidget(right_frame)
        self.__param_layout = QVBoxLayout()
        right_frame.setLayout(self.__param_layout)
        right_grid.addWidget(right_scroll)

        button_grid = QHBoxLayout()
        button_grid.addStretch()
        cancel_btn = CancelButton('取消')
        cancel_btn.clicked.connect(self.close)
        button_grid.addWidget(cancel_btn, 0, Qt.AlignRight)
        button_grid.addSpacing(18)
        ok_btn = OKButton('添加')
        ok_btn.clicked.connect(self.accept)
        button_grid.addWidget(ok_btn, 0, Qt.AlignRight)
        button_grid.setContentsMargins(0, 20, 20, 20)
        right_grid.addLayout(button_grid)

        self.__main_grid.addLayout(right_grid, 0, 2)

    def __create_action_tree(self):
        action_tree = ParamTree()
        action_tree.setHeaderHidden(True)
        modules = get_modules(augmenters)
        for module in modules:
            module_item = QTreeWidgetItem()
            module_item.setText(0, module[0])
            action_tree.addTopLevelItem(module_item)
            for c in module[2]:
                class_item = c[1]()
                self.__class_dict[class_item.name] = c[1]
                module_item.addChild(class_item)

        action_tree.clicked.connect(self.__action_tree_clicked)

        return action_tree

    def __init_sample_layout(self):
        if len(self.samples) > 0:
            self.tmp_samples = list()
            for sample in np.random.choice(self.samples, 4):
                img = Image.open(sample)
                # Image.Image.resize(img, (256, 256))
                img = np.array(img)
                self.tmp_samples.append(img)
            # self.tmp_samples = np.array(self.tmp_samples)
            self.__refresh_sample_layout()

    def __sample_clicked(self, cur_img_idx):
        def sample_clicked_fun():
            image_show_dialog = ImageShowDialog()
            image_show_dialog.setWindowTitle('图片查看器')
            image_show_dialog.set_images(self.aug_sample_imgs, cur_img_idx)
            image_show_dialog.exec()
        return sample_clicked_fun

    def __refresh_sample_layout(self):
        if len(self.tmp_samples) > 0:
            self.aug_sample_imgs = list()
            clear_layout(self.__sample_layout)
            item = self.__action_tree.currentItem()
            if item is None:
                aug_imgs = self.tmp_samples
            else:
                try:
                    seq = Sequential(children=[item.to_aug()])
                    aug_imgs = seq(images=self.tmp_samples)
                except Exception as e:
                    print(e)
                    aug_imgs = self.tmp_samples
            for img_idx, img in enumerate(aug_imgs):
                img = Image.fromarray(img)
                img = img.toqpixmap()
                img = QPixmap(img)
                self.aug_sample_imgs.append(img)
                sample_img = SampleImage(img, side_thresh=230)
                sample_img.clicked.connect(self.__sample_clicked(img_idx))
                self.__sample_layout.addWidget(sample_img)

    def __action_tree_clicked(self, _q_model_index):
        item = self.__action_tree.currentItem()
        try:
            params = item.params
        except Exception as _e:
            print(_e)
            return 0
        clear_layout(self.__param_layout)
        self.__refresh_sample_layout()
        for param_name in params:
            param = params[param_name]
            param_layout = param.to_widget()
            param.set_value_changed_fun(self.__refresh_sample_layout)
            self.__param_layout.addWidget(param_layout)
        self.__param_layout.addStretch()
        self.__action_item = item

    def get_result(self):
        result = self.__class_dict[self.__action_item.name]()
        try:
            params = self.__action_item.params
        except Exception as _e:
            print(_e)
            return 0
        for param_name in params:
            result.params[param_name] = params[param_name]
        return result

# if __name__ == '__main__':
#
#     print(modules)
#     # modules = [(module[0], module[1], inspect.getmembers(module[1], inspect.isclass)) for module in modules]
#     # print(modules)
