# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *


class ScrollArea(QScrollArea):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyleSheet(
            """
            QScrollBar:vertical {
                border: none;
                background: rgb(74, 74, 74);
                width: 6px;
                margin: 0px 0 0px 0;
            }
            QScrollBar::handle:vertical {
                background: rgb(105, 105, 105);
                border-radius: 3px;
                border: none;
            }
            QScrollBar::add-line:vertical {
                border: 0px solid grey;
                background: #32CC99;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                border: 0px solid grey;
                background: #32CC99;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
                width: 0px;
                height: 0px;
            }
            """
        )
