# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ComboBox(QComboBox):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QComboBox {
                background-color: rgb(46, 46, 46);
                border:1px rgb(62, 62, 62);
                font-size: 15px;
                color: rgb(205, 205, 205);
                height: 30px;
            }            
            """
        )
