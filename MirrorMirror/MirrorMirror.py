# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
import sys
from .MainWindow import MainWindow
from PyQt5.QtWidgets import *


class MirrorMirror(object):
    def __init__(self):
        pass

    @staticmethod
    def run():
        app = QApplication(sys.argv)
        form = MainWindow()
        form.show()
        sys.exit(app.exec_())
