# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_register_form.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_clientRegistrationForm(object):
    def setupUi(self, clientRegistrationForm):
        if not clientRegistrationForm.objectName():
            clientRegistrationForm.setObjectName(u"clientRegistrationForm")
        clientRegistrationForm.resize(388, 507)
        clientRegistrationForm.setMinimumSize(QSize(0, 507))
        self.verticalLayout_2 = QVBoxLayout(clientRegistrationForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fullnameLabel = QLabel(clientRegistrationForm)
        self.fullnameLabel.setObjectName(u"fullnameLabel")

        self.horizontalLayout.addWidget(self.fullnameLabel)

        self.fullnameInput = QLineEdit(clientRegistrationForm)
        self.fullnameInput.setObjectName(u"fullnameInput")

        self.horizontalLayout.addWidget(self.fullnameInput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.contactsLabel = QLabel(clientRegistrationForm)
        self.contactsLabel.setObjectName(u"contactsLabel")

        self.horizontalLayout_3.addWidget(self.contactsLabel)

        self.contactsInput = QPlainTextEdit(clientRegistrationForm)
        self.contactsInput.setObjectName(u"contactsInput")

        self.horizontalLayout_3.addWidget(self.contactsInput)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.commentLabel = QLabel(clientRegistrationForm)
        self.commentLabel.setObjectName(u"commentLabel")

        self.horizontalLayout_2.addWidget(self.commentLabel)

        self.commentInput = QPlainTextEdit(clientRegistrationForm)
        self.commentInput.setObjectName(u"commentInput")

        self.horizontalLayout_2.addWidget(self.commentInput)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox = QDialogButtonBox(clientRegistrationForm)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(clientRegistrationForm)
        self.buttonBox.accepted.connect(clientRegistrationForm.accept)
        self.buttonBox.rejected.connect(clientRegistrationForm.reject)

        QMetaObject.connectSlotsByName(clientRegistrationForm)
    # setupUi

    def retranslateUi(self, clientRegistrationForm):
        clientRegistrationForm.setWindowTitle(QCoreApplication.translate("clientRegistrationForm", u"Dialog", None))
        self.fullnameLabel.setText(QCoreApplication.translate("clientRegistrationForm", u"Full name", None))
        self.contactsLabel.setText(QCoreApplication.translate("clientRegistrationForm", u"Contacts", None))
        self.commentLabel.setText(QCoreApplication.translate("clientRegistrationForm", u"Comment", None))
    # retranslateUi

