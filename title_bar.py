from PySide.QtCore import *
from PySide.QtGui import *
import os
BASE_DIR = os.getcwd()
icons = os.path.join(BASE_DIR, 'res')


class TitleBar(QFrame):
    click_action = Signal(str)
    move_signal = Signal(QPoint)
    btn_size = 20

    def __init__(self, parent, title=None, height=28, min_button=True, max_button=True, close_btn=True,
                 min_action=None, max_action=None, close_action=None, restore_action=None, subtitle=''):
        super(TitleBar, self).__init__(parent)
        self.setObjectName('maintitle')
        self.par = parent
        self.ly = QHBoxLayout(self)
        self.ly.setSpacing(3)
        self.ly.setContentsMargins(3, 3, 3, 3)
        self.title = QLabel('<b style="font-size:16px;">%s</b>&nbsp;&nbsp;&nbsp;%s'% (title or parent.windowTitle(), subtitle))
        self.title.setObjectName('titlelabel')
        # self.title.setStyleSheet('color: black;')
        self.ly.addWidget(self.title)
        spacerItem = QSpacerItem(510, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.ly.addItem(spacerItem)
        self.minimize_btn = QPushButton()
        # self.minimize_btn.setIcon(QIcon(':/images/min.png'))
        self.minimize_btn.setIcon(QIcon(os.path.join(icons, 'min.png')))
        self.minimize_btn.setMinimumSize(QSize(self.btn_size, self.btn_size))
        self.minimize_btn.setMaximumSize(QSize(self.btn_size, self.btn_size))
        self.ly.addWidget(self.minimize_btn)
        if not min_button:
            self.minimize_btn.hide()
        self.maximize_btn = QPushButton()
        # self.maximize_btn.setIcon(QIcon(':/images/max.png'))
        self.maximize_btn.setIcon(QIcon(os.path.join(icons, 'max.png')))
        self.maximize_btn.setMinimumSize(QSize(self.btn_size, self.btn_size))
        self.maximize_btn.setMaximumSize(QSize(self.btn_size, self.btn_size))
        self.ly.addWidget(self.maximize_btn)
        if not max_button:
            self.maximize_btn.hide()
        self.restore_btn = QPushButton()
        # self.restore_btn.setIcon(QIcon(':/images/restore.png'))
        self.restore_btn.setIcon(QIcon(os.path.join(icons, 'restore.png')))
        self.restore_btn.setMinimumSize(QSize(self.btn_size, self.btn_size))
        self.restore_btn.setMaximumSize(QSize(self.btn_size, self.btn_size))
        self.ly.addWidget(self.restore_btn)
        self.close_btn = QPushButton()
        # self.close_btn.setIcon(QIcon(':/images/close.png'))
        self.close_btn.setIcon(QIcon(os.path.join(icons, 'close.png')))
        self.close_btn.setMinimumSize(QSize(self.btn_size, self.btn_size))
        self.close_btn.setMaximumSize(QSize(self.btn_size, self.btn_size))
        self.ly.addWidget(self.close_btn)
        if not close_btn:
            self.close_btn.hide()

        self.setMaximumHeight(height)
        if parent.isMaximized():
            self.maximize_btn.hide()
        else:
            self.restore_btn.hide()

        if close_action:
            self.close_btn.clicked.connect(close_action)
        else:
            self.close_btn.clicked.connect(lambda: self.click('close'))
        if max_action:
            self.maximize_btn.clicked.connect(max_action)
        else:
            self.maximize_btn.clicked.connect(lambda: self.click('max'))
        if min_action:
            self.minimize_btn.clicked.connect(min_action)
        else:
            self.minimize_btn.clicked.connect(lambda: self.click('min'))
        if restore_action:
            self.restore_btn.clicked.connect(restore_action)
        else:
            self.restore_btn.clicked.connect(lambda: self.click('restore'))
        self.last_pos = None

    def hide_buttons(self):
        self.close_btn.hide()
        self.maximize_btn.hide()
        self.minimize_btn.hide()
        self.restore_btn.hide()

    def click(self, action):
        if action == 'max':
            self.maximize_btn.hide()
            self.restore_btn.show()
        elif action == 'restore':
            self.maximize_btn.show()
            self.restore_btn.hide()
        self.click_action.emit(action)
        self.titlebar_action(action)

    def mousePressEvent(self, event):
        self.last_pos = event.globalPos()
        super(TitleBar, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # print self.last_pos
        super(TitleBar, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        new_pos = event.globalPos()
        dist = self.last_pos - new_pos
        # self.move_signal.emit(dist)
        self.move_parent(dist)
        self.last_pos = new_pos
        super(TitleBar, self).mouseMoveEvent(event)

    def move_parent(self, dist):
        if self.par.isMaximized():
            return
        self.par.move(self.par.pos() - dist)

    def mouseDoubleClickEvent(self, event):
        if self.par.isMaximized():
            self.click('restore')
        else:
            self.click('max')
        super(TitleBar, self).mouseDoubleClickEvent(event)

    def titlebar_action(self, action):
        """
        Title bar actions
        """
        if action == 'max':
            self.par.setWindowState(Qt.WindowMaximized)
        elif action == 'min':
            self.par.setWindowState(Qt.WindowMinimized)
        elif action == 'close':
            self.par.close()
        elif action == 'restore':
            self.par.setWindowState(Qt.WindowNoState)
        self.par.setFocus()