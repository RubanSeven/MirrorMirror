# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class IconButton(QPushButton):
    def __init__(self, img_path, side_thresh=14., width=32, height=26, *__args):
        super().__init__(*__args)
        img = Image.open(img_path)
        img = img.toqpixmap()
        img = QPixmap(img)
        pix_size = img.size()
        max_side = max(pix_size.width(), pix_size.height())
        if max_side > side_thresh:
            pix_size.setWidth(int(round(pix_size.width() * side_thresh / max_side)))
            pix_size.setHeight(int(round(pix_size.height() * side_thresh / max_side)))
        self.setContentsMargins(0, 0, 0, 0)
        icon = QIcon(img)
        self.setIcon(icon)
        self.setFixedSize(pix_size)
        self.setIconSize(pix_size)
        self.setMaximumWidth(width)
        self.setMinimumWidth(width)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setObjectName('icon_btn')
        self.setStyleSheet(
            """
            #icon_btn {
                border: None;
            }
            #icon_btn:hover {
                background-color: rgb(69, 69, 69);
            }
            """
        )


class OKButton(QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setObjectName('OKButton')
        self.setMaximumWidth(64)
        self.setMinimumWidth(64)
        self.setStyleSheet(
            """
            #OKButton {
                width: 64px;
                height: 32px;
                border: 0px;
                border-radius: 16px;
                background-color: rgb(20, 115, 230);
            }
            #OKButton:hover {
                background-color: rgb(15, 100, 210);
            }
            #OKButton:pressed {
                background-color: rgb(70, 160, 245);
            }
            """
        )


class CancelButton(QPushButton):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setObjectName('CancelButton')
        self.setMaximumWidth(64)
        self.setMinimumWidth(64)
        self.setStyleSheet(
            """
            #CancelButton {
                width: 64px;
                height: 28px;
                border: 2px solid #CDCDCD;
                border-radius: 16px;
                background-color: #00000000;
            }
            #CancelButton:hover {
                color: rgb(46, 46, 46);
                background-color: rgb(205, 205, 205);
            }
            #CancelButton:pressed {
                border: 2px solid rgb(70, 160, 245);
                background-color: rgb(70, 160, 245);
            }
            """
        )


class SampleImage(QPushButton):
    def __init__(self, img, side_thresh=240., *__args):
        super().__init__(*__args)
        pix_size = img.size()
        max_side = max(pix_size.width(), pix_size.height())
        if max_side > side_thresh:
            pix_size.setWidth(int(round(pix_size.width() * side_thresh / max_side)))
            pix_size.setHeight(int(round(pix_size.height() * side_thresh / max_side)))
        icon = QIcon(img)
        self.setIcon(icon)
        self.setFixedSize(pix_size)
        self.setIconSize(pix_size)
