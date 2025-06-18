# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTableView, QWidget)

class Ui_TableViewer(object):
    def setupUi(self, TableViewer):
        if not TableViewer.objectName():
            TableViewer.setObjectName(u"TableViewer")
        TableViewer.resize(800, 600)
        self.centralwidget = QWidget(TableViewer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputElements = QGroupBox(self.centralwidget)
        self.inputElements.setObjectName(u"inputElements")

        self.gridLayout.addWidget(self.inputElements, 0, 0, 1, 1)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)

        self.crudButtons = QGroupBox(self.centralwidget)
        self.crudButtons.setObjectName(u"crudButtons")

        self.gridLayout.addWidget(self.crudButtons, 1, 1, 1, 1)

        TableViewer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TableViewer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        TableViewer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TableViewer)
        self.statusbar.setObjectName(u"statusbar")
        TableViewer.setStatusBar(self.statusbar)

        self.retranslateUi(TableViewer)

        QMetaObject.connectSlotsByName(TableViewer)
    # setupUi

    def retranslateUi(self, TableViewer):
        TableViewer.setWindowTitle(QCoreApplication.translate("TableViewer", u"MainWindow", None))
        self.inputElements.setTitle(QCoreApplication.translate("TableViewer", u"GroupBox", None))
        self.crudButtons.setTitle(QCoreApplication.translate("TableViewer", u"GroupBox", None))
    # retranslateUi

