# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *


class ParamSpinBox(QSpinBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QSpinBox {
                background-color: rgb(46, 46, 46);
                border:1px rgb(62, 62, 62);
                font-size: 15px;
                color: rgb(205, 205, 205);
                height: 30px;
            }
            
            QSpinBox::up-button, QSpinBox::down-button {
                width:0px;
            }
            """
        )


class ParamDoubleSpinBox(QDoubleSpinBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QDoubleSpinBox {
                background-color: rgb(46, 46, 46);
                border:1px rgb(62, 62, 62);
                font-size: 15px;
                color: rgb(205, 205, 205);
                height: 30px;
            }
            
            QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
                width:0px;
            }
            """
        )
