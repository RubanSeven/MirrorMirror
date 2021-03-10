# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ParamFrame(QFrame):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QFrame {
                border: none;
            }            
            """
        )


class ActionBarFrame(QFrame):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            background-color: rgb(83, 83, 83);
            border: none;
            font-size: 15px;
            color: rgb(214, 214, 214);
            """
        )


class SampleListFrame(QFrame):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QFrame {
                border: none;
                background-color: rgb(27, 27, 27);
            }            
            """
        )
