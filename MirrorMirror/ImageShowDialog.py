# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ImageBox(QWidget):
    def __init__(self):
        super(ImageBox, self).__init__()
        self.img = None
        self.scaled_img = None
        self.point = QPoint(0, 0)
        self.start_pos = None
        self.end_pos = None
        self.left_click = False
        self.scale = 1.0

    def set_image(self, img: QPixmap):
        """
        open image file
        :param img: image
        :return:
        """
        self.img = img
        width_scale = self.size().width() / img.size().width()
        height_scale = self.size().height() / img.size().height()
        scale = min(width_scale, height_scale)
        size = QSize(int(round(img.size().width() * scale)), int(round(img.size().height() * scale)))
        self.point = QPoint((self.size().width() - size.width()) // 2, (self.size().height() - size.height()) // 2)
        self.scaled_img = self.img.scaled(size)

    def paintEvent(self, e):
        """
        receive paint events
        :param e: QPaintEvent
        :return:
        """
        if self.scaled_img:
            painter = QPainter()
            painter.begin(self)
            painter.scale(self.scale, self.scale)
            painter.drawPixmap(self.point, self.scaled_img)
            painter.end()

    def mouseMoveEvent(self, e):
        """
        mouse move events for the widget
        :param e: QMouseEvent
        :return:
        """
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()
            self.repaint()

    def mousePressEvent(self, e):
        """
        mouse press events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()

    def mouseReleaseEvent(self, e):
        """
        mouse release events for the widget
        :param e: QMouseEvent
        :return:
        """
        if e.button() == Qt.LeftButton:
            self.left_click = False

    def wheelEvent(self, e: QWheelEvent):
        """
        mouse wheel events for the widget
        :param e: QWheelEvent
        :return:
        """
        delta = e.angleDelta().y()
        if delta > 0:
            if self.scale < 4:
                self.scale *= 1.1
        elif delta < 0:
            if self.scale > 1:
                self.scale /= 1.1
                self.scale = max(self.scale, 1)
        self.adjustSize()
        self.repaint()


class TitleBar(QWidget):
    """主窗口无边框后使用的标题栏"""

    def __init__(self, *args, **kwargs):
        super(TitleBar, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)  # 支持使用QSS设置背景
        self._mouse_pos = None
        layout = QHBoxLayout(self)
        layout.setContentsMargins(QMargins(1, 1, 1, 1))
        layout.setSpacing(2)

        self.title_text = QLabel(self)
        self.title_text.setFixedHeight(26)
        self.title_text.setObjectName('TitleName')
        layout.addWidget(self.title_text, alignment=Qt.AlignLeft)  # 加入窗口文字

        layout.addStretch()

        self.close_button = QPushButton('r', self)
        layout.addWidget(self.close_button, alignment=Qt.AlignRight)
        font = QFont('webdings')  # 使用webding字体设置按钮的图标
        self.close_button.setFont(font)
        self.close_button.setFixedSize(26, 26)
        self.close_button.clicked.connect(self.window_close)

        # 设置objectName来设置样式
        self.setObjectName('titleBar')
        self.close_button.setObjectName('closeButton')
        self.setStyleSheet("""
        #titleBar{
            background-color: rgb(83,83,83);
        }
        #closeButton {
            border: none;
            color: rgb(168,168,168);
        }
        #closeButton:hover {
            background-color: rgb(71,71,71);
        }
        #TitleName {
            color: rgb(240, 240, 240);
        }
        """)

        self.setLayout(layout)

    def window_close(self):
        self.parent().close()

    def set_window_title(self, title):
        self.title_text.setText(title)


class CenterWidget(QStackedWidget):
    def __init__(self, *args, **kwargs):
        super(CenterWidget, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

    def clear(self):
        for i in range(self.count()):
            widget = self.widget(i)
            self.removeWidget(widget)
            if widget is not None:
                widget.deleteLater()
                del widget


class StatusBar(QStatusBar):
    def __init__(self, *args, **kwargs):
        super(StatusBar, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)


class ImageShowDialog(QDialog):
    MARGIN = 5

    def __init__(self, *args, **kwargs):
        super(ImageShowDialog, self).__init__(*args, **kwargs)
        self.resize(1024, 576)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.grabKeyboard()
        self._direction = None  # 此时鼠标的方向
        self._pressed = False  # 鼠标是否按下
        self._mouse_pos = None  # 记录鼠标位置
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(self.MARGIN, self.MARGIN, self.MARGIN, self.MARGIN))

        self.title = TitleBar(self)
        self.title.installEventFilter(self)  # 安装事件过滤,进入控件还原方向和鼠标状态
        layout.addWidget(self.title, alignment=Qt.AlignTop)

        self.center_widget = CenterWidget(self)
        self.center_widget.installEventFilter(self)
        layout.addWidget(self.center_widget)

        # self.status_bar = StatusBar(self)
        # self.status_bar.installEventFilter(self)
        # self.status_bar.hide()
        # layout.addWidget(self.status_bar, alignment=Qt.AlignBottom)

        self.setLayout(layout)

        self.images = list()
        self.cur_idx = 0

    # def paintEvent(self, event):
    #     m = 1
    #     path = QPainterPath()
    #     path.setFillRule(Qt.WindingFill)
    #     path.addRect(m, m, self.width() - m * 2, self.height() - m * 2)
    #     painter = QPainter(self)
    #     # painter.setRenderHint(QPainter.Antialiasing, True)
    #     painter.fillPath(path, QBrush(Qt.white))
    #
    #     color = QColor(100, 100, 100, 30)
    #     # for(int i=0; i<10; i++)
    #
    #     for i in range(m):
    #         path = QPainterPath()
    #         path.setFillRule(Qt.WindingFill)
    #         path.addRoundedRect(m - i, m - i, self.width() - (m - i) * 2, self.height() - (m - i) * 2, 1, 1)
    #         color.setAlphaF(90 - math.sqrt(i) * 30)
    #         painter.setPen(QPen(color, 1, Qt.SolidLine))
    #         painter.drawRoundedRect(QRect(m - i, m - i, self.width() - (m - i) * 2,
    #         self.height() - (m - i) * 2), 0, 0)

    def set_images(self, images, cur_idx):
        self.images = images
        self.cur_idx = min(len(self.images) - 1, max(0, cur_idx))
        img_box = ImageBox()

        center_size = QSize(self.size().width(), self.size().height() - self.title.height())
        img_box.setGeometry(QRect(0, 0, center_size.width(), center_size.height()))

        img_box.set_image(self.images[self.cur_idx])

        self.center_widget.clear()
        self.center_widget.addWidget(img_box)

    def eventFilter(self, obj, event):
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
            self._direction = None  # 去除方向
            self._pressed = None  # 去除按下标记
        return super(ImageShowDialog, self).eventFilter(obj, event)

    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Left:
            self.cur_idx -= 1
            if self.cur_idx < 0:
                self.cur_idx = len(self.images) - 1
        elif e.key() == Qt.Key_Right:
            self.cur_idx += 1
            if self.cur_idx >= len(self.images):
                self.cur_idx = 0
        img_box = ImageBox()

        center_size = QSize(self.size().width(), self.size().height() - self.title.height())
        img_box.setGeometry(QRect(0, 0, center_size.width(), center_size.height()))

        img_box.set_image(self.images[self.cur_idx])

        self.center_widget.clear()
        self.center_widget.addWidget(img_box)

    def setWindowTitle(self, title):
        super(ImageShowDialog, self).setWindowTitle(title)
        self.title.set_window_title(title)
