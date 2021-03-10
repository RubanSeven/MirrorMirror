# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *


class CodeTextEdit(QTextEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QTextEdit {
                background-color: rgb(83, 83, 83);
                border:0px;
                font-size: 15px;
                color: rgb(214, 214, 214);
            }            
            """
        )


class ParamLineEdit(QLineEdit):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QLineEdit {
                background-color: rgb(46, 46, 46);
                border:1px rgb(62, 62, 62);
                font-size: 15px;
                color: rgb(205, 205, 205);
                height: 30px;
            }            
            """
        )


class LabelText(QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QLabel {
                border: none;
                font-size: 13px;
                color: rgb(153, 153, 153);
            }            
            """
        )
