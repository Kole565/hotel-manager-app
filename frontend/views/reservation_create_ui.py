# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservation_create_form.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateTimeEdit, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_reservationCreateForm(object):
    def setupUi(self, reservationCreateForm):
        if not reservationCreateForm.objectName():
            reservationCreateForm.setObjectName(u"reservationCreateForm")
        reservationCreateForm.resize(299, 507)
        reservationCreateForm.setMinimumSize(QSize(0, 507))
        self.verticalLayout_2 = QVBoxLayout(reservationCreateForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(reservationCreateForm)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit = QLineEdit(reservationCreateForm)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(reservationCreateForm)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(reservationCreateForm)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_2 = QLineEdit(reservationCreateForm)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(reservationCreateForm)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(reservationCreateForm)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.dateTimeEdit = QDateTimeEdit(reservationCreateForm)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout_4.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(reservationCreateForm)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.dateTimeEdit_2 = QDateTimeEdit(reservationCreateForm)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.horizontalLayout_5.addWidget(self.dateTimeEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(reservationCreateForm)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.label_6 = QLabel(reservationCreateForm)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(reservationCreateForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(reservationCreateForm)
        self.buttonBox.accepted.connect(reservationCreateForm.accept)
        self.buttonBox.rejected.connect(reservationCreateForm.reject)

        QMetaObject.connectSlotsByName(reservationCreateForm)
    # setupUi

    def retranslateUi(self, reservationCreateForm):
        reservationCreateForm.setWindowTitle(QCoreApplication.translate("reservationCreateForm", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("reservationCreateForm", u"Client", None))
        self.pushButton.setText(QCoreApplication.translate("reservationCreateForm", u"Create", None))
        self.label_5.setText(QCoreApplication.translate("reservationCreateForm", u"Room", None))
        self.pushButton_2.setText(QCoreApplication.translate("reservationCreateForm", u"Check", None))
        self.label_2.setText(QCoreApplication.translate("reservationCreateForm", u"Date in", None))
        self.label_4.setText(QCoreApplication.translate("reservationCreateForm", u"Date out", None))
        self.label.setText(QCoreApplication.translate("reservationCreateForm", u"Total", None))
        self.label_6.setText(QCoreApplication.translate("reservationCreateForm", u"Sum", None))
    # retranslateUi

