# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModifyTramNetwork.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSplitter, QStatusBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ModifyNetwork(object):
    def setupUi(self, ModifyNetwork):
        if not ModifyNetwork.objectName():
            ModifyNetwork.setObjectName(u"ModifyNetwork")
        ModifyNetwork.resize(794, 600)
        self.centralwidget = QWidget(ModifyNetwork)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.addTram = QPushButton(self.centralwidget)
        self.addTram.setObjectName(u"addTram")

        self.gridLayout.addWidget(self.addTram, 0, 3, 1, 1)

        self.addStop = QPushButton(self.centralwidget)
        self.addStop.setObjectName(u"addStop")

        self.gridLayout.addWidget(self.addStop, 0, 2, 1, 1)

        self.addLine = QPushButton(self.centralwidget)
        self.addLine.setObjectName(u"addLine")

        self.gridLayout.addWidget(self.addLine, 0, 1, 1, 1)

        self.StartSimulation = QPushButton(self.centralwidget)
        self.StartSimulation.setObjectName(u"StartSimulation")

        self.gridLayout.addWidget(self.StartSimulation, 0, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.ModifyNetworkTree = QTreeWidget(self.splitter)
        self.ModifyNetworkTree.setObjectName(u"ModifyNetworkTree")
        self.ModifyNetworkTree.setAnimated(False)
        self.ModifyNetworkTree.setColumnCount(1)
        self.splitter.addWidget(self.ModifyNetworkTree)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 110, 60, 16))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 330, 60, 16))
        self.TextLabel = QLabel(self.frame)
        self.TextLabel.setObjectName(u"TextLabel")
        self.TextLabel.setGeometry(QRect(20, 60, 171, 20))
        self.TextLabel2 = QLabel(self.frame)
        self.TextLabel2.setObjectName(u"TextLabel2")
        self.TextLabel2.setGeometry(QRect(20, 290, 181, 20))
        self.SliderTime = QSlider(self.frame)
        self.SliderTime.setObjectName(u"SliderTime")
        self.SliderTime.setGeometry(QRect(20, 160, 160, 22))
        self.SliderTime.setOrientation(Qt.Horizontal)
        self.SliderNumber = QSlider(self.frame)
        self.SliderNumber.setObjectName(u"SliderNumber")
        self.SliderNumber.setGeometry(QRect(20, 380, 160, 22))
        self.SliderNumber.setOrientation(Qt.Horizontal)
        self.splitter.addWidget(self.frame)

        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout)

        ModifyNetwork.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ModifyNetwork)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 37))
        ModifyNetwork.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ModifyNetwork)
        self.statusbar.setObjectName(u"statusbar")
        ModifyNetwork.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyNetwork)

        QMetaObject.connectSlotsByName(ModifyNetwork)
    # setupUi

    def retranslateUi(self, ModifyNetwork):
        ModifyNetwork.setWindowTitle(QCoreApplication.translate("ModifyNetwork", u"MainWindow", None))
        self.addTram.setText(QCoreApplication.translate("ModifyNetwork", u"add tram", None))
        self.addStop.setText(QCoreApplication.translate("ModifyNetwork", u"add stop", None))
        self.addLine.setText(QCoreApplication.translate("ModifyNetwork", u"add line", None))
        self.StartSimulation.setText(QCoreApplication.translate("ModifyNetwork", u"open map", None))
        ___qtreewidgetitem = self.ModifyNetworkTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ModifyNetwork", u"Tram Network", None));
        self.label.setText(QCoreApplication.translate("ModifyNetwork", u"1", None))
        self.label_2.setText(QCoreApplication.translate("ModifyNetwork", u"1", None))
        self.TextLabel.setText(QCoreApplication.translate("ModifyNetwork", u"Travel time between stops", None))
        self.TextLabel2.setText(QCoreApplication.translate("ModifyNetwork", u"Trams number in single line", None))
    # retranslateUi

