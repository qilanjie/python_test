# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1970, 900)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_head = QLabel(self.frame)
        self.label_head.setObjectName(u"label_head")
        self.label_head.setGeometry(QRect(10, 50, 1251, 101))
        font = QFont()
        font.setPointSize(35)
        self.label_head.setFont(font)
        self.label_head.setAlignment(Qt.AlignCenter)
        self.btn_1 = QPushButton(self.frame)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(60, 230, 551, 261))
        font1 = QFont()
        font1.setPointSize(30)
        self.btn_1.setFont(font1)
        self.btn_1.setCheckable(False)
        self.btn_1.setChecked(False)
        self.btn_2 = QPushButton(self.frame)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(660, 230, 551, 261))
        self.btn_2.setFont(font1)
        self.btn_2.setLayoutDirection(Qt.RightToLeft)
        self.btn_2.setCheckable(False)
        self.btn_4 = QPushButton(self.frame)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setGeometry(QRect(660, 530, 551, 261))
        self.btn_4.setFont(font1)
        self.btn_4.setCheckable(False)
        self.btn_4.setChecked(False)
        self.btn_3 = QPushButton(self.frame)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(60, 530, 551, 261))
        self.btn_3.setFont(font1)
        self.btn_3.setCheckable(False)
        self.btn_3.setChecked(False)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_head.setText(QCoreApplication.translate("Widget", u"\u611f\u8c22\u4ee5\u4e0b\u6240\u6709\u7c89\u4e1d\u5bf9\u6211\u7684\u652f\u6301\uff0c\u611f\u8c22\uff01", None))
        self.btn_1.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u62bd\u53d6", None))
        self.btn_2.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u62bd\u53d6", None))
        self.btn_4.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u62bd\u53d6", None))
        self.btn_3.setText(QCoreApplication.translate("Widget", u"\u70b9\u51fb\u62bd\u53d6", None))
    # retranslateUi

