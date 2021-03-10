# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ActionTab(QTabWidget):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setAutoFillBackground(True)
        self.setStyleSheet(
            """
            QTabWidget::pane {
                background-color: rgb(83, 83, 83);
                border-left: 1px solid #383838;
                border-top: 1px solid #383838;
                font-size: 15px;
                color: rgb(214, 214, 214);
            }
            QHeaderView::section {
                background-color: #535353;
            }
            QTabBar::tab {
                color: rgb(214, 214, 214);
                background-color: rgb(66, 66, 66);
            }
            QTabBar::tab:hover {
                background-color: rgb(79, 79, 79);
            }
            QTabBar::tab:selected {
                background-color: rgb(83, 83, 83);
            }
            """
        )
