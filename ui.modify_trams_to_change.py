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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSplitter,
    QStackedWidget, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

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
        self.addLine = QPushButton(self.centralwidget)
        self.addLine.setObjectName(u"addLine")

        self.gridLayout.addWidget(self.addLine, 0, 1, 1, 1)

        self.StartSimulation = QPushButton(self.centralwidget)
        self.StartSimulation.setObjectName(u"StartSimulation")

        self.gridLayout.addWidget(self.StartSimulation, 0, 0, 1, 1)

        self.addTram = QPushButton(self.centralwidget)
        self.addTram.setObjectName(u"addTram")

        self.gridLayout.addWidget(self.addTram, 0, 3, 1, 1)

        self.addStop = QPushButton(self.centralwidget)
        self.addStop.setObjectName(u"addStop")

        self.gridLayout.addWidget(self.addStop, 0, 2, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.ModifyNetworkTree = QTreeWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem(self.ModifyNetworkTree)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.ModifyNetworkTree.setObjectName(u"ModifyNetworkTree")
        self.ModifyNetworkTree.setAnimated(False)
        self.ModifyNetworkTree.setColumnCount(1)
        self.splitter.addWidget(self.ModifyNetworkTree)
        self.ModifyWidget = QStackedWidget(self.splitter)
        self.ModifyWidget.setObjectName(u"ModifyWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.ModifyWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.ModifyWidget.addWidget(self.page_2)
        self.splitter.addWidget(self.ModifyWidget)

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
        self.addLine.setText(QCoreApplication.translate("ModifyNetwork", u"add line", None))
        self.StartSimulation.setText(QCoreApplication.translate("ModifyNetwork", u"open map", None))
        self.addTram.setText(QCoreApplication.translate("ModifyNetwork", u"add tram", None))
        self.addStop.setText(QCoreApplication.translate("ModifyNetwork", u"add stop", None))
        ___qtreewidgetitem = self.ModifyNetworkTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ModifyNetwork", u"Tram Network", None));

        __sortingEnabled = self.ModifyNetworkTree.isSortingEnabled()
        self.ModifyNetworkTree.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.ModifyNetworkTree.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("ModifyNetwork", u"Line 1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("ModifyNetwork", u"Trams", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("ModifyNetwork", u"Tram 1", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("ModifyNetwork", u"Stops", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("ModifyNetwork", u"Stop 1", None));
        self.ModifyNetworkTree.setSortingEnabled(__sortingEnabled)

    # retranslateUi

