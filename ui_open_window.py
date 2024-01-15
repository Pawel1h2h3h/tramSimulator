# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpenWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QListView, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_OpenWidow(object):
    def setupUi(self, OpenWidow):
        if not OpenWidow.objectName():
            OpenWidow.setObjectName(u"OpenWidow")
        OpenWidow.resize(800, 600)
        self.centralwidget = QWidget(OpenWidow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FolderView = QListView(self.centralwidget)
        self.FolderView.setObjectName(u"FolderView")

        self.verticalLayout.addWidget(self.FolderView)

        OpenWidow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(OpenWidow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        OpenWidow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(OpenWidow)
        self.statusbar.setObjectName(u"statusbar")
        OpenWidow.setStatusBar(self.statusbar)

        self.retranslateUi(OpenWidow)

        QMetaObject.connectSlotsByName(OpenWidow)
    # setupUi

    def retranslateUi(self, OpenWidow):
        OpenWidow.setWindowTitle(QCoreApplication.translate("OpenWidow", u"MainWindow", None))
    # retranslateUi

