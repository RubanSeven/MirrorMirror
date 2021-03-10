# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from ..theme import *
from ..utils.layout import clear_layout

INDENT = 24


class ParamBase(object):
    def __init__(self):
        self.name = ''
        self.type = ''
        self.value_range = None
        self.describe = ''
        self.value = None
        self.value_changed = None

    def get_value(self):
        return self.value

    def set_value_changed_fun(self, value_changed):
        self.value_changed = value_changed


class IntParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'int'
        self.name = name
        if type(value_range) is not tuple or len(value_range) != 2:
            assert 'value_range is not tuple or length != 2'
        if type(value_range[0]) is not int or type(value_range[0]) is not int:
            assert 'value_range is not int tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.spin_box = None

    def to_widget(self):
        # 水平方向
        self.spin_box = ParamSpinBox()
        # 设置最小值
        self.spin_box.setMinimum(self.value_range[0])
        # 设置最大值
        self.spin_box.setMaximum(self.value_range[1])
        if self.value is None:
            self.value = int(round((self.value_range[0] + self.value_range[1]) / 2.))
        self.spin_box.setValue(self.value)
        self.spin_box.valueChanged.connect(self.box_value_changed)

        if self.name is not None:
            frame = ParamFrame()
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addWidget(self.spin_box)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
            return frame
        else:
            return self.spin_box

    def box_value_changed(self):
        self.value = self.spin_box.value()
        if self.value_changed is not None:
            self.value_changed()


class FloatParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'float'
        self.name = name
        if type(value_range) is not tuple or len(value_range) != 2:
            assert 'value_range is not tuple or length != 2'
        if type(value_range[0]) is not float or type(value_range[0]) is not float:
            assert 'value_range is not float tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.spin_box = None

    def to_widget(self):
        # 水平方向
        self.spin_box = ParamDoubleSpinBox()
        # 设置最小值
        self.spin_box.setMinimum(self.value_range[0])
        # 设置最大值
        self.spin_box.setMaximum(self.value_range[1])
        if self.value is None:
            self.value = int(round((self.value_range[0] + self.value_range[1]) / 2.))
        self.spin_box.setValue(self.value)
        self.spin_box.valueChanged.connect(self.box_value_changed)

        if self.name is not None:
            frame = ParamFrame()
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addWidget(self.spin_box)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
            return frame
        else:
            return self.spin_box

    def box_value_changed(self):
        self.value = self.spin_box.value()
        if self.value_changed is not None:
            self.value_changed()


class IntRangeParam(ParamBase):
    def __init__(self, value_ranges, default, describe='', name=None):
        super().__init__()
        self.type = 'IntRange'
        self.name = name
        if type(value_ranges) is not tuple or len(value_ranges) != 2:
            assert 'value_ranges except ((a, b), (c,d))'
        for value_range in value_ranges:
            if type(value_range) is not tuple or len(value_range) != 2:
                assert 'value_ranges except ((a, b), (c,d))'
        self.value_ranges = value_ranges
        self.value = default
        self.describe = describe
        self.__min_spin_box = None
        self.__max_spin_box = None

    def to_widget(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        # if self.name is not None:
        #     layout.addSpacing(INDENT)

        if self.value is None:
            self.value = (int(round((self.value_ranges[0][0] + self.value_ranges[0][1]) / 2.)),
                          int(round((self.value_ranges[1][0] + self.value_ranges[1][1]) / 2.)))
        # 水平方向
        self.__min_spin_box = ParamSpinBox()
        # 设置最小值
        self.__min_spin_box.setMinimum(self.value_ranges[0][0])
        # 设置最大值
        self.__min_spin_box.setMaximum(self.value_ranges[0][1])
        self.__min_spin_box.setValue(self.value[0])
        self.__min_spin_box.valueChanged.connect(self.min_box_value_changed)
        layout.addWidget(self.__min_spin_box)

        txt_label = QLabel('至')
        txt_label.setMaximumWidth(24)
        layout.addWidget(txt_label)

        # 水平方向
        self.__max_spin_box = ParamSpinBox()
        # 设置最小值
        self.__max_spin_box.setMinimum(self.value_ranges[1][0])
        # 设置最大值
        self.__max_spin_box.setMaximum(self.value_ranges[1][1])
        self.__max_spin_box.setValue(self.value[1])
        self.__max_spin_box.valueChanged.connect(self.max_box_value_changed)
        layout.addWidget(self.__max_spin_box)

        frame = ParamFrame()
        if self.name is not None:
            frame_layout = QVBoxLayout()
            label = LabelText(self.name)
            frame_layout.addWidget(label)
            frame_layout.addLayout(layout)
            frame.setLayout(layout)
        else:
            frame.setLayout(layout)
        return frame

    def min_box_value_changed(self):
        if self.__min_spin_box.value() >= self.value[1]:
            self.__min_spin_box.setValue(self.value[0])
        self.value = (self.__min_spin_box.value(), self.__max_spin_box.value())
        if self.value_changed is not None:
            self.value_changed()

    def max_box_value_changed(self):
        if self.__max_spin_box.value() <= self.value[0]:
            self.__max_spin_box.setValue(self.value[1])
        self.value = (self.__min_spin_box.value(), self.__max_spin_box.value())
        if self.value_changed is not None:
            self.value_changed()


class FloatRangeParam(ParamBase):
    def __init__(self, value_ranges, default, describe='', name=None):
        super().__init__()
        self.type = 'FloatRange'
        self.name = name
        if type(value_ranges) is not tuple or len(value_ranges) != 2:
            assert 'value_ranges except ((a, b), (c,d))'
        for value_range in value_ranges:
            if type(value_range) is not tuple or len(value_range) != 2:
                assert 'value_ranges except ((a, b), (c,d))'
        self.value_ranges = value_ranges
        self.value = default
        self.describe = describe
        self.__min_spin_box = None
        self.__max_spin_box = None

    def to_widget(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        # if self.name is not None:
        #     layout.addSpacing(INDENT)

        if self.value is None:
            self.value = (int(round((self.value_ranges[0][0] + self.value_ranges[0][1]) / 2.)),
                          int(round((self.value_ranges[1][0] + self.value_ranges[1][1]) / 2.)))
        # 水平方向
        self.__min_spin_box = ParamDoubleSpinBox()
        # 设置最小值
        self.__min_spin_box.setMinimum(self.value_ranges[0][0])
        # 设置最大值
        self.__min_spin_box.setMaximum(self.value_ranges[0][1])
        self.__min_spin_box.setValue(self.value[0])
        self.__min_spin_box.valueChanged.connect(self.min_box_value_changed)
        layout.addWidget(self.__min_spin_box)

        txt_label = QLabel('至')
        txt_label.setMaximumWidth(24)
        layout.addWidget(txt_label)

        # 水平方向
        self.__max_spin_box = ParamDoubleSpinBox()
        # 设置最小值
        self.__max_spin_box.setMinimum(self.value_ranges[1][0])
        # 设置最大值
        self.__max_spin_box.setMaximum(self.value_ranges[1][1])
        self.__max_spin_box.setValue(self.value[1])
        self.__max_spin_box.valueChanged.connect(self.max_box_value_changed)
        layout.addWidget(self.__max_spin_box)

        frame = ParamFrame()
        if self.name is not None:
            frame_layout = QVBoxLayout()
            label = LabelText(self.name)
            frame_layout.addWidget(label)
            frame_layout.addLayout(layout)
            frame.setLayout(frame_layout)
        else:
            frame.setLayout(layout)
        return frame

    def min_box_value_changed(self):
        if self.__min_spin_box.value() >= self.value[1]:
            self.__min_spin_box.setValue(self.value[0])
        self.value = (self.__min_spin_box.value(), self.__max_spin_box.value())
        if self.value_changed is not None:
            self.value_changed()

    def max_box_value_changed(self):
        if self.__max_spin_box.value() <= self.value[0]:
            self.__max_spin_box.setValue(self.value[1])
        self.value = (self.__min_spin_box.value(), self.__max_spin_box.value())
        if self.value_changed is not None:
            self.value_changed()


class IntListParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'IntList'
        self.name = name
        if type(value_range) is not tuple:
            assert 'value_range is not tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.__value_edit = None

    def to_widget(self):
        # 水平方向
        self.__value_edit = ParamLineEdit()
        if self.value is None or not self.__check_form(self.value):
            self.value = ''
        # value_idx = self.value_range.index(self.value)
        # self.__combo_box.setCurrentIndex(self.value_range.index(self.value))
        self.__value_edit.setText(self.value)
        self.__value_edit.textChanged.connect(self.text_changed)

        if self.name is not None:
            frame = ParamFrame()
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addWidget(self.__value_edit)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
            return frame
        else:
            return self.__value_edit

    @staticmethod
    def __check_form(txt: str):
        try:
            for i in txt.split(','):
                try:
                    int(i)
                except:
                    return False
        except:
            return False
        return True

    def text_changed(self):
        if self.__check_form(self.__value_edit.text()):
            self.value = self.__value_edit.text()
            if self.value_changed is not None:
                self.value_changed()

    def get_value(self):
        return [int(i) for i in self.value.split(',')]


class FloatListParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'FloatList'
        self.name = name
        if type(value_range) is not tuple:
            assert 'value_range is not tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.__value_edit = None

    def to_widget(self):
        # 水平方向
        self.__value_edit = ParamLineEdit()
        if self.value is None or not self.__check_form(self.value):
            self.value = ''
        # value_idx = self.value_range.index(self.value)
        # self.__combo_box.setCurrentIndex(self.value_range.index(self.value))
        self.__value_edit.setText(self.value)
        self.__value_edit.textChanged.connect(self.text_changed)

        if self.name is not None:
            frame = ParamFrame()
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            content_layout.setContentsMargins(0, 0, 0, 0)
            # content_layout.addSpacing(INDENT)
            content_layout.addWidget(self.__value_edit)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
            return frame
        else:
            return self.__value_edit

    @staticmethod
    def __check_form(txt: str):
        try:
            for i in txt.split(','):
                try:
                    float(i)
                except:
                    return False
        except:
            return False
        return True

    def text_changed(self):
        if self.__check_form(self.__value_edit.text()):
            self.value = self.__value_edit.text()
            if self.value_changed is not None:
                self.value_changed()

    def get_value(self):
        return [float(i) for i in self.value.split(',')]


class EnumListParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'EnumFloatList'
        self.name = name
        if type(value_range) is not tuple:
            assert 'value_range is not tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.__value_edit = None

    def to_widget(self):
        # 水平方向
        self.__value_edit = QLineEdit()
        if self.value is None or not self.__check_form(self.value):
            self.value = ''
        # value_idx = self.value_range.index(self.value)
        # self.__combo_box.setCurrentIndex(self.value_range.index(self.value))
        self.__value_edit.setText(self.value)
        self.__value_edit.textChanged.connect(self.text_changed)

        if self.name is not None:
            frame = ParamFrame()
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addWidget(self.__value_edit)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
            return frame
        else:
            return self.__value_edit

    def __check_form(self, txt: str):
        try:
            for i in txt.split(','):
                if i not in self.value_range:
                    return False
        except:
            return False
        return True

    def text_changed(self):
        if self.__check_form(self.__value_edit.text()):
            self.value = self.__value_edit.text()
            if self.value_changed is not None:
                self.value_changed()

    def get_value(self):
        return self.value.split(',')


class EnumParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'Enum'
        self.name = name
        if type(value_range) is not tuple:
            assert 'value_range is not tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.__combo_box = None

    def to_widget(self):
        # 水平方向
        self.__combo_box = ComboBox()
        if self.value is None:
            self.value = self.value_range[0]
        for v in self.value_range:
            self.__combo_box.addItem(v)
        # value_idx = self.value_range.index(self.value)
        # self.__combo_box.setCurrentIndex(self.value_range.index(self.value))
        self.__combo_box.setCurrentText(self.value)
        self.__combo_box.currentIndexChanged.connect(self.selection_change)

        if self.name is not None:
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addWidget(self.__combo_box)
            layout.addLayout(content_layout)

            frame = ParamFrame()
            frame.setLayout(layout)
            return frame
        else:
            return self.__combo_box

    def selection_change(self, i):
        self.value = self.__combo_box.currentText()
        if self.value_changed is not None:
            self.value_changed()

    def get_value(self):
        if type(self.value) is str:
            if self.value == 'True':
                return True
            if self.value == 'False':
                return False
        return self.value


class DictParam(ParamBase):
    def __init__(self, children, describe='', name=None):
        super().__init__()
        self.type = 'Dict'
        self.name = name
        self.children = children
        self.describe = describe
        self.__param_group = None

    def to_widget(self):
        self.__param_group = QVBoxLayout()
        self.__param_group.setDirection(QBoxLayout.TopToBottom)
        for child_name in self.children:
            child_layout = QVBoxLayout()
            label = LabelText(child_name)
            child_layout.addWidget(label)
            child_item = self.children[child_name]
            item_widget = child_item.to_widget()
            child_layout.addWidget(item_widget)
            self.__param_group.addLayout(child_layout)
        # self.__param_group.addStretch()

        frame = ParamFrame()
        if self.name is not None:
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)
            self.__param_group.addSpacing(4)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addLayout(self.__param_group)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
        else:
            frame.setLayout(self.__param_group)
        return frame

    def set_value_changed_fun(self, value_changed):
        for child_name in self.children:
            child_item = self.children[child_name]
            child_item.set_value_changed_fun(value_changed)

    def get_value(self):
        result = dict()
        for child_name in self.children:
            child_item = self.children[child_name]
            result[child_name] = child_item.get_value()
        return result


class ChoiceParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'Choice'
        self.name = name
        if type(value_range) is not dict:
            assert 'value_range is not dict'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.__combo_box = None
        self.__items = list()
        self.__content_layout = None

    def to_widget(self):
        if self.value is None or self.value not in self.value_range:
            self.value = list(self.value_range.keys())[0]

        self.__combo_box = ComboBox()
        self.__items = list()
        for k in self.value_range:
            self.__combo_box.addItem(k)
            self.__items.append(self.value_range[k])
        self.__combo_box.setCurrentText(self.value)
        self.__combo_box.currentIndexChanged.connect(self.selection_change)
        # self.__radio_group = QButtonGroup()
        # item_layout = QVBoxLayout()
        # item_layout.setDirection(QBoxLayout.TopToBottom)
        # for choice_id, choice_item in enumerate(self.value_range):
        #     radio_layout = QHBoxLayout()
        #     radio_layout.setDirection(QBoxLayout.LeftToRight)
        #     item_widget = choice_item.to_widget()
        #     rb = QRadioButton(item_widget)
        #     if choice_id == self.value:
        #         rb.click()
        #     self.__radio_group.addButton(rb, choice_id)
        #     radio_layout.addWidget(rb)
        #     radio_layout.addWidget(item_widget)
        #     radio_layout.addStretch()
        #     item_layout.addLayout(radio_layout)
        # item_layout.addStretch()
        # for v in self.value_range:
        #     self.__combo_box.addItem(v)
        # value_idx = self.value_range.index(self.value)
        # self.__combo_box.setCurrentIndex(self.value_range.index(self.value))
        # self.__combo_box.setCurrentText(self.value)
        # self.__radio_group.buttonClicked.connect(self.selection_change)

        frame = ParamFrame()

        self.__content_layout = QVBoxLayout()
        self.__content_layout.setContentsMargins(0, 0, 0, 0)
        self.__content_layout.addWidget(self.__combo_box)
        item = self.value_range[self.value]
        if type(item) is not DefaultParam:
            self.__content_layout.addWidget(item.to_widget())

        if self.name is not None:
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)
            layout.addLayout(self.__content_layout)

            frame.setLayout(layout)
        else:
            frame.setLayout(self.__content_layout)
        return frame

    # def selection_change(self):
    #     self.value = self.__radio_group.checkedId()
    #     if self.value_changed is not None:
    #         self.value_changed()

    def selection_change(self):
        self.value = self.__combo_box.currentText()

        while self.__content_layout.count() > 1:
            item = self.__content_layout.takeAt(1)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                clear_layout(item.layout())

        item = self.value_range[self.value]
        if type(item) is not DefaultParam:
            self.__content_layout.addWidget(item.to_widget())

        if self.value_changed is not None:
            self.value_changed()

    def set_value_changed_fun(self, value_changed):
        self.value_changed = value_changed
        for k in self.value_range:
            self.value_range[k].set_value_changed_fun(value_changed)

    def get_value(self):
        return self.value_range[self.value].get_value()


class MultiSelectParam(ParamBase):
    def __init__(self, value_range, default, describe='', name=None):
        super().__init__()
        self.type = 'MultiSelect'
        self.name = name
        if type(value_range) is not tuple:
            assert 'value_range is not tuple'
        self.value_range = value_range
        self.describe = describe
        self.value = default
        self.cb_list = list()
        # self.__check_group = None

    def to_widget(self):
        if self.value is None or len(self.value) == 0:
            self.value = [0]

        self.cb_list = list()
        item_layout = QVBoxLayout()
        item_layout.setDirection(QBoxLayout.TopToBottom)
        for select_id, select_value in enumerate(self.value_range):
            cb = QCheckBox(str(select_value))
            if select_id in self.value:
                cb.setChecked(True)
            cb.stateChanged.connect(self.selection_change)
            self.cb_list.append(cb)
            # self.__check_group.addButton(cb, select_id)
            item_layout.addWidget(cb)
        # item_layout.addStretch()
        # for v in self.value_range:
        #     self.__combo_box.addItem(v)
        # value_idx = self.value_range.index(self.value)
        # self.__combo_box.setCurrentIndex(self.value_range.index(self.value))
        # self.__combo_box.setCurrentText(self.value)
        # self.__check_group.buttonClicked.connect(self.selection_change)
        frame = ParamFrame()
        if self.name is not None:
            layout = QVBoxLayout()
            label = LabelText(self.name)
            layout.addWidget(label)

            content_layout = QHBoxLayout()
            # content_layout.addSpacing(INDENT)
            content_layout.addLayout(item_layout)
            layout.addLayout(content_layout)

            frame.setLayout(layout)
        else:
            frame.setLayout(item_layout)
        return frame

    def is_empty(self):
        for tmp_cb in self.cb_list:
            if tmp_cb.isChecked():
                return False
        return True

    def selection_change(self):
        if self.is_empty():
            self.cb_list[self.value[0]].setChecked(True)
        else:
            self.value = [cb_id for cb_id, tmp_cb in enumerate(self.cb_list) if tmp_cb.isChecked()]
            if self.value_changed is not None:
                self.value_changed()

    def set_value_changed_fun(self, value_changed):
        self.value_changed = value_changed

    def get_value(self):
        if len(self.value) > 1:
            result = [self.value_range[v] for v in self.value]
            return result
        else:
            return self.value_range[self.value[0]]


class DefaultParam(ParamBase):
    def __init__(self, describe='', default=None, name='default'):
        super().__init__()
        self.type = 'None'
        self.value = default
        self.name = name
        self.describe = describe

    def to_widget(self):
        return LabelText(self.name)

    def set_value_changed_fun(self, value_changed):
        pass

    def get_value(self):
        return self.value
