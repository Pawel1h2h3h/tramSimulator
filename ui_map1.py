# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Map.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTimeEdit, QVBoxLayout, QWidget)

class Ui_Map(object):
    def setupUi(self, Map):
        if not Map.objectName():
            Map.setObjectName(u"Map")
        Map.resize(829, 602)
        self.centralwidget = QWidget(Map)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Stop = QPushButton(self.widget)
        self.Stop.setObjectName(u"Stop")

        self.gridLayout.addWidget(self.Stop, 0, 1, 1, 1)

        self.showNetwork = QPushButton(self.widget)
        self.showNetwork.setObjectName(u"showNetwork")

        self.gridLayout.addWidget(self.showNetwork, 0, 3, 1, 1)

        self.Save = QPushButton(self.widget)
        self.Save.setObjectName(u"Save")

        self.gridLayout.addWidget(self.Save, 0, 4, 1, 1)

        self.timeEdit = QTimeEdit(self.widget)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout.addWidget(self.timeEdit, 0, 2, 1, 1)

        self.Start = QPushButton(self.widget)
        self.Start.setObjectName(u"Start")

        self.gridLayout.addWidget(self.Start, 0, 0, 1, 1)

        self.splitter.addWidget(self.widget)

        self.verticalLayout.addWidget(self.splitter)

        self.Map_2 = QGraphicsView(self.centralwidget)
        self.Map_2.setObjectName(u"Map_2")

        self.verticalLayout.addWidget(self.Map_2)

        Map.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Map)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 829, 24))
        Map.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Map)
        self.statusbar.setObjectName(u"statusbar")
        Map.setStatusBar(self.statusbar)

        self.retranslateUi(Map)

        QMetaObject.connectSlotsByName(Map)
    # setupUi

    def retranslateUi(self, Map):
        Map.setWindowTitle(QCoreApplication.translate("Map", u"MainWindow", None))
        self.Stop.setText(QCoreApplication.translate("Map", u"Stop", None))
        self.showNetwork.setText(QCoreApplication.translate("Map", u"Show", None))
        self.Save.setText(QCoreApplication.translate("Map", u"Save", None))
        self.Start.setText(QCoreApplication.translate("Map", u"Start", None))
    # retranslateUi

