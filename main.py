from PySide.QtCore import *
from PySide.QtGui import *
import title_bar, main_window_UIs
import os
BASE_DIR = os.getcwd()


class MainDialog(QMainWindow, main_window_UIs.Ui_MainDialog):
    def __init__(self):
        super(MainDialog, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._title = title_bar.TitleBar(self, 'Main Window', 28)
        self.title_ly.addWidget(self._title)
        self.resized = False
        self.last_pos = None
        self.__init()

    def __init(self):

        ico = os.path.join(BASE_DIR, 'res', 'app.png')
        if os.path.exists(ico):
            self.setWindowIcon(QIcon(ico))

        self.menubar = QMenuBar()
        self.menubar.setMaximumHeight(25)
        self.menu_ly.addWidget(self.menubar)

        users_menu = QMenu('File', self)
        users_menu.addAction(QAction('Some Action...', self, ))
        users_menu.addSeparator()
        users_menu.addAction(QAction('Exit', self, triggered=self.close))
        self.menubar.addMenu(users_menu)

        info_menu = QMenu('Help', self)
        info_menu.addAction(QAction('Manual...', self))
        self.menubar.addMenu(info_menu)
        self.__update_style()
        self.__add_shortcuts()

    def __update_style(self, widget=None):
        widget = widget or self
        style = os.path.join(BASE_DIR, 'res', 'style.css')
        if os.path.exists(style):
            widget.setStyleSheet(open(style).read())

    def __add_shortcuts(self):
        self.sc1 = QShortcut(self)
        self.sc1.setKey('F5')
        # self.sc1.activated.connect(self.__update_data)

        # sq = QKeySequence(Qt.CTRL + Qt.Key_P)
        # self.sc2 = QShortcut(sq, self)
        # self.sc2.activated.connect(self.show_html)

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.resized = True
            self.last_pos = event.globalPos()
        else:
            super(MainDialog, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.last_pos = None
        self.resized = False
        super(MainDialog, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.resized:
            new_pos = event.globalPos()
            dist = self.last_pos - new_pos
            sz = QSize(-dist.x(), -dist.y())
            self.resize(sz + self.size())
            self.last_pos = new_pos
        else:
            super(MainDialog, self).mouseMoveEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    w = MainDialog()
    w.show()
    app.exec_()

