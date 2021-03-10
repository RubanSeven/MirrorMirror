# -*- coding:utf-8 -*-
"""
@author: RubanSeven
@project: MirrorMirror
"""
import os
import codecs
import autopep8
from .utils.layout import *
from .augmenters.meta import *
from .augmenters.child import *
from .ActionDialog import ActionDialog
from .FrameLessWindow import FrameLessWindow
from .ImageShowDialog import ImageShowDialog

cur_path = os.path.dirname(os.path.realpath(__file__))


class ActionTree(QTreeWidget):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setContextMenuPolicy(Qt.CustomContextMenu)  # 打开右键菜单的策略
        self.customContextMenuRequested.connect(self.menu_fun)  # 绑定事件
        self.__pop_menu = None
        self.refresh_sample_fun = None
        self.clear_param_layout_fun = None
        # self.setHeaderLabel('序列')
        self.setHeaderHidden(True)
        self.samples = list()

    def set_samples(self, samples):
        self.samples = samples

    # 定义treewidget中item右键界面
    def menu_fun(self, pos):
        item = self.currentItem()
        item1 = self.itemAt(pos)

        if item is not None and item1 is not None:
            self.__pop_menu = QMenu()
            if item.has_child:
                self.__pop_menu.addAction(QAction(u'添加', self))
            if item.parent() is not None:
                self.__pop_menu.addAction(QAction(u'删除', self))
                # self.__pop_menu.addAction(QAction(u'上移', self))
                # self.__pop_menu.addAction(QAction(u'下移', self))
            self.__pop_menu.triggered[QAction].connect(self.process_trigger)
            self.__pop_menu.exec_(QCursor.pos())

    def process_trigger(self, q):
        # 判断是项目节点还是任务节点
        command = q.text()
        item = self.currentItem()
        if command == "添加":
            self.__pop_menu.close()
            if item.has_child:
                action_dialog = ActionDialog(self,
                                             Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
                action_dialog.set_samples(self.samples)
                action_dialog.setWindowTitle('增强方法')
                if action_dialog.exec():
                    child_item = action_dialog.get_result()
                    try:
                        for child_name in child_item.child_names:
                            child_item.addChild(ChildItem(child_name, child_item))
                    except:
                        pass
                    item.addChild(child_item)
                    if self.refresh_sample_fun is not None:
                        self.refresh_sample_fun()
        elif command == "删除":
            self.__pop_menu.close()
            try:
                if item.isSelected() and self.clear_param_layout_fun is not None:
                    self.clear_param_layout_fun()
                item.parent().removeChild(item)
                if self.refresh_sample_fun is not None:
                    self.refresh_sample_fun()
            except:
                pass
        pass


class MainWindow(FrameLessWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(300, 300, 500, 400)
        self.__init_elements()
        self.__init_title_menu_bar()
        # icon = QIcon(QPixmap(r'./resources/img/icon.png'))
        self.setWindowIcon(QIcon(QPixmap(os.path.join(cur_path, r'resources/img/icon.png'))))
        # self.setWindowTitle('MirrorMirror')
        self.showMaximized()
        self.samples = list()
        self.tmp_samples = list()
        self.sample_imgs = list()
        self.aug_sample_imgs = list()

    def __init_elements(self):
        frame = QFrame()
        frame.setStyleSheet(
            "background-color: rgb(66, 66, 66);"
        )
        self.set_center_widget(frame)

        main_grid = QGridLayout()
        main_grid.setSpacing(0)
        main_grid.setContentsMargins(0, 0, 0, 0)
        main_grid.setColumnStretch(1, 5)
        main_grid.setColumnStretch(2, 1)
        frame.setLayout(main_grid)

        # 左侧工具栏
        left_bar_frame = QFrame()
        left_bar_frame.setStyleSheet(
            """
            background-color: rgb(83, 83, 83);
            border-top: 1px solid #383838;
            border-right: 1px solid #383838;
            """
        )
        left_bar_frame.setMaximumWidth(36)
        left_bar_frame.setMinimumWidth(36)
        left_bar_frame.setContentsMargins(0, 0, 0, 0)
        self.left_bar = QVBoxLayout()
        self.left_bar.setContentsMargins(2, 5, 0, 0)
        left_bar_frame.setLayout(self.left_bar)
        main_grid.addWidget(left_bar_frame, 0, 0)
        self.__init_left_bar()

        sample_frame = QFrame()
        sample_frame.setStyleSheet(
            "background-color: rgb(40, 40, 40);"
        )
        self.__sample_layout = FlowLayout()
        sample_frame.setLayout(self.__sample_layout)
        main_grid.addWidget(sample_frame, 0, 1)

        action_tab = ActionTab()

        action_frame = ActionBarFrame()
        action_frame.setContentsMargins(0, 0, 0, 0)
        action_grid = QGridLayout()
        action_grid.setContentsMargins(0, 0, 0, 0)
        action_frame.setLayout(action_grid)
        action_grid.setRowStretch(0, 1)
        action_grid.setRowStretch(1, 1)

        param_scroll = QScrollArea()
        param_scroll.setWidgetResizable(True)
        param_frame = QFrame()
        self.__param_layout = QVBoxLayout()
        param_frame.setLayout(self.__param_layout)
        param_scroll.setWidget(param_frame)
        action_grid.addWidget(param_scroll, 0, 0)
        param_scroll.setStyleSheet(
            """
            border-bottom: 1px solid #383838;
            """
        )

        self.__action_tree = ActionTree()
        self.__action_tree.setContentsMargins(0, 0, 0, 0)
        self.sequential = SequentialItem(self.__action_tree)
        self.__action_tree.addTopLevelItem(self.sequential)
        self.__action_tree.expandAll()
        self.__action_tree.clicked.connect(self.__action_tree_clicked)
        self.__action_tree.refresh_sample_fun = self.__refresh_sample_layout
        self.__action_tree.clear_param_layout_fun = self.__clear_param_layout
        action_grid.addWidget(self.__action_tree, 1, 0)

        action_tab.addTab(action_frame, "配置")

        self.__code_text_edit = CodeTextEdit()
        action_tab.addTab(self.__code_text_edit, "代码")
        self.refresh_code()

        main_grid.addWidget(action_tab, 0, 2)

    def __init_left_bar(self):
        data_refresh_btn = IconButton(os.path.join(cur_path, r'resources/img/datarefresh.png'))
        data_refresh_btn.clicked.connect(self.__init_sample_layout)
        self.left_bar.addWidget(data_refresh_btn)

        refresh_btn = IconButton(os.path.join(cur_path, r'resources/img/refresh.png'))
        refresh_btn.clicked.connect(self.__refresh_sample_layout)
        self.left_bar.addWidget(refresh_btn)

        self.left_bar.addStretch()

    def __init_title_menu_bar(self):
        title_menu_bar = self.get_title_menu_bar()
        file_menu = title_menu_bar.addMenu('文件')

        open_action = QAction('导入数据', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        export_action = QAction('导出代码', self)
        export_action.triggered.connect(self.export_code)
        file_menu.addAction(export_action)

        # 设置objectName来设置样式
        title_menu_bar.setObjectName('TitleMenuBar')
        file_menu.setObjectName('FileMenu')
        title_menu_bar.setStyleSheet("""
                    #TitleMenuBar{
                        border: none;
                        background-color: rgba(0,0,0,0);
                        color: rgb(240,240,240);
                    }
                     #FileMenu:hover {
                        background-color: rgb(71,71,71);
                    }
                """)

    def open_file(self):
        self.samples = list()
        sample_root = QFileDialog.getExistingDirectory(self, "选取文件夹", r"D:\data\bd_imgs\书籍封面")
        if os.path.exists(sample_root):
            sample_names = os.listdir(sample_root)
            for sample_name in sample_names:
                sample_path = os.path.join(sample_root, sample_name)
                self.samples.append(sample_path)

            self.__init_sample_layout()
            self.__action_tree.set_samples(samples=self.samples)

    def export_code(self):
        action_code = "from imgaug import augmenters as iaa\n\n"
        action_code += 'seq=' + self.sequential.to_code()
        action_code = autopep8.fix_code(action_code)
        save_code_path = QFileDialog.getSaveFileName(self, "保存为", r'D:\\', '*.py')[0]
        if save_code_path != '':
            with codecs.open(save_code_path, 'wb', encoding='utf-8') as save_file:
                save_file.write(action_code)

    def __init_sample_layout(self):
        self.tmp_samples = list()
        self.sample_imgs = list()
        for sample in np.random.choice(self.samples, 20):
            img = Image.open(sample)
            # Image.Image.resize(img, (256, 256))
            img = np.array(img)
            self.tmp_samples.append(img)
            self.sample_imgs.append(img)
        # self.tmp_samples = np.array(self.tmp_samples)
        self.__refresh_sample_layout()

    def refresh_code(self):
        action_code = "from imgaug import augmenters as iaa\n\n"
        action_code += 'seq=' + self.sequential.to_code()
        action_code = autopep8.fix_code(action_code)
        self.__code_text_edit.clear()
        self.__code_text_edit.append(action_code)

    def __sample_clicked(self, cur_img_idx):
        def sample_clicked_fun():
            image_show_dialog = ImageShowDialog()
            image_show_dialog.setWindowTitle('图片查看器')
            image_show_dialog.set_images(self.aug_sample_imgs, cur_img_idx)
            image_show_dialog.exec()

        return sample_clicked_fun

    def __refresh_sample_layout(self):
        self.aug_sample_imgs = list()
        clear_layout(self.__sample_layout)
        seq = self.sequential.to_aug()
        self.refresh_code()
        aug_imgs = seq(images=self.tmp_samples)
        for img_idx, img in enumerate(aug_imgs):
            img = Image.fromarray(img)
            img = img.toqpixmap()
            img = QPixmap(img)
            self.aug_sample_imgs.append(img)
            sample_img = SampleImage(img)
            sample_img.clicked.connect(self.__sample_clicked(img_idx))
            self.__sample_layout.addWidget(sample_img)
        # cpu_count = multiprocessing.cpu_count()
        # print('cpu:', cpu_count)
        # if cpu_count <= 1:
        #     aug_imgs = seq(images=self.tmp_samples)
        #     for img in aug_imgs:
        #         self.__sample_layout.addWidget(SampleImage(img))
        # else:
        #     if len(self.tmp_samples) < cpu_count:
        #         batch_size = 1
        #         cpu_count = len(self.tmp_samples)
        #     elif len(self.tmp_samples) % cpu_count == 0:
        #         batch_size = len(self.tmp_samples) // cpu_count
        #     else:
        #         batch_size = len(self.tmp_samples) // (cpu_count - 1)
        #     batches = [ia.Batch(images=self.tmp_samples[batch_size * i: batch_size * (i + 1)]) for i in
        #                range(cpu_count)]
        #     aug_batches = list(seq.augment_batches(batches, background=True))
        #     for aug_batch in aug_batches:
        #         for img in aug_batch.images_aug:
        #             self.__sample_layout.addWidget(SampleImage(img))

    def __clear_param_layout(self):
        clear_layout(self.__param_layout)

    def __action_tree_clicked(self, _q_model_index):
        clear_layout(self.__param_layout)
        item = self.__action_tree.currentItem()
        try:
            params = item.params
        except Exception as _e:
            print(_e)
            return 0
        for param_name in params:
            param = params[param_name]
            param.set_value_changed_fun(self.__refresh_sample_layout)
            param_layout = param.to_widget()
            self.__param_layout.addWidget(param_layout)
        self.__param_layout.addStretch()
        self.__action_item = item
