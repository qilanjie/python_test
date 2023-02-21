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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1600, 900)
        Widget.setMinimumSize(QSize(800, 450))
        self.gridLayout_6 = QGridLayout(Widget)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_background = QFrame(Widget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setFrameShape(QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_background)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.btn_1 = QPushButton(self.frame_background)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setMinimumSize(QSize(100, 30))
        self.btn_1.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(10)
        self.btn_1.setFont(font)

        self.horizontalLayout_12.addWidget(self.btn_1)

        self.horizontalSpacer_23 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_23)

        self.btn_2 = QPushButton(self.frame_background)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setMinimumSize(QSize(100, 30))
        self.btn_2.setMaximumSize(QSize(100, 30))
        self.btn_2.setFont(font)

        self.horizontalLayout_12.addWidget(self.btn_2)

        self.horizontalSpacer_24 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_24)

        self.btn_3 = QPushButton(self.frame_background)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setMinimumSize(QSize(100, 30))
        self.btn_3.setMaximumSize(QSize(100, 30))
        self.btn_3.setFont(font)

        self.horizontalLayout_12.addWidget(self.btn_3)

        self.horizontalSpacer_25 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_25)

        self.btn_4 = QPushButton(self.frame_background)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setMinimumSize(QSize(100, 30))
        self.btn_4.setMaximumSize(QSize(100, 30))
        self.btn_4.setFont(font)

        self.horizontalLayout_12.addWidget(self.btn_4)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.frame = QFrame(self.frame_background)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_login = QFrame(self.frame)
        self.frame_login.setObjectName(u"frame_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_login.sizePolicy().hasHeightForWidth())
        self.frame_login.setSizePolicy(sizePolicy1)
        self.frame_login.setMinimumSize(QSize(500, 600))
        self.frame_login.setMaximumSize(QSize(500, 600))
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_login)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_login = QLabel(self.frame_login)
        self.label_login.setObjectName(u"label_login")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(22)
        self.label_login.setFont(font1)

        self.horizontalLayout.addWidget(self.label_login)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_20 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_20)

        self.frame_user_name = QFrame(self.frame_login)
        self.frame_user_name.setObjectName(u"frame_user_name")
        self.frame_user_name.setFrameShape(QFrame.StyledPanel)
        self.frame_user_name.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_user_name)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_21 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_21)

        self.label_user_name = QLabel(self.frame_user_name)
        self.label_user_name.setObjectName(u"label_user_name")
        sizePolicy.setHeightForWidth(self.label_user_name.sizePolicy().hasHeightForWidth())
        self.label_user_name.setSizePolicy(sizePolicy)
        self.label_user_name.setMinimumSize(QSize(30, 30))
        self.label_user_name.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_11.addWidget(self.label_user_name)

        self.lineE_user_name = QLineEdit(self.frame_user_name)
        self.lineE_user_name.setObjectName(u"lineE_user_name")

        self.horizontalLayout_11.addWidget(self.lineE_user_name)


        self.gridLayout_4.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_user_name)

        self.horizontalSpacer_22 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_22)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.frame_pwd = QFrame(self.frame_login)
        self.frame_pwd.setObjectName(u"frame_pwd")
        self.frame_pwd.setFrameShape(QFrame.StyledPanel)
        self.frame_pwd.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_pwd)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_pwd = QLabel(self.frame_pwd)
        self.label_pwd.setObjectName(u"label_pwd")
        sizePolicy.setHeightForWidth(self.label_pwd.sizePolicy().hasHeightForWidth())
        self.label_pwd.setSizePolicy(sizePolicy)
        self.label_pwd.setMinimumSize(QSize(30, 30))
        self.label_pwd.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.label_pwd)

        self.lineE_pwd = QLineEdit(self.frame_pwd)
        self.lineE_pwd.setObjectName(u"lineE_pwd")

        self.horizontalLayout_3.addWidget(self.lineE_pwd)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_pwd)

        self.horizontalSpacer_19 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_19)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_11 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)

        self.btn_forget = QPushButton(self.frame_login)
        self.btn_forget.setObjectName(u"btn_forget")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setUnderline(True)
        self.btn_forget.setFont(font2)

        self.horizontalLayout_5.addWidget(self.btn_forget)

        self.horizontalSpacer_12 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.btn_login = QPushButton(self.frame_login)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setMinimumSize(QSize(320, 50))
        self.btn_login.setMaximumSize(QSize(320, 50))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        self.btn_login.setFont(font3)

        self.horizontalLayout_6.addWidget(self.btn_login)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_10 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.btn_wx = QPushButton(self.frame_login)
        self.btn_wx.setObjectName(u"btn_wx")
        sizePolicy.setHeightForWidth(self.btn_wx.sizePolicy().hasHeightForWidth())
        self.btn_wx.setSizePolicy(sizePolicy)
        self.btn_wx.setMinimumSize(QSize(50, 50))
        self.btn_wx.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.btn_wx)

        self.horizontalSpacer_7 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.btn_qq = QPushButton(self.frame_login)
        self.btn_qq.setObjectName(u"btn_qq")
        sizePolicy.setHeightForWidth(self.btn_qq.sizePolicy().hasHeightForWidth())
        self.btn_qq.setSizePolicy(sizePolicy)
        self.btn_qq.setMinimumSize(QSize(50, 50))
        self.btn_qq.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.btn_qq)

        self.horizontalSpacer_8 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.btn_wb = QPushButton(self.frame_login)
        self.btn_wb.setObjectName(u"btn_wb")
        sizePolicy.setHeightForWidth(self.btn_wb.sizePolicy().hasHeightForWidth())
        self.btn_wb.setSizePolicy(sizePolicy)
        self.btn_wb.setMinimumSize(QSize(50, 50))
        self.btn_wb.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.btn_wb)

        self.horizontalSpacer_9 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_8 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.label = QLabel(self.frame_login)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.frame_login)

        self.frame_pic = QFrame(self.frame)
        self.frame_pic.setObjectName(u"frame_pic")
        sizePolicy1.setHeightForWidth(self.frame_pic.sizePolicy().hasHeightForWidth())
        self.frame_pic.setSizePolicy(sizePolicy1)
        self.frame_pic.setMinimumSize(QSize(500, 600))
        self.frame_pic.setFrameShape(QFrame.StyledPanel)
        self.frame_pic.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_pic)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_10 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_background, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btn_1.setText(QCoreApplication.translate("Widget", u"\u7c89\u7ea2", None))
        self.btn_2.setText(QCoreApplication.translate("Widget", u"\u9ec4\u8272", None))
        self.btn_3.setText(QCoreApplication.translate("Widget", u"\u6d45\u7d2b", None))
        self.btn_4.setText(QCoreApplication.translate("Widget", u"\u9752\u7eff", None))
        self.label_login.setText(QCoreApplication.translate("Widget", u"LOGIN", None))
        self.label_user_name.setText("")
        self.label_pwd.setText("")
        self.btn_forget.setText(QCoreApplication.translate("Widget", u"Forget Password?", None))
        self.btn_login.setText(QCoreApplication.translate("Widget", u"LOGIN", None))
        self.btn_wx.setText("")
        self.btn_qq.setText("")
        self.btn_wb.setText("")
        self.label.setText(QCoreApplication.translate("Widget", u"\u672c\u754c\u9762\u4e3abilibili up\u4e3b <\u8001\u5b9e\u7684\u5f90\u7801\u519c> \u8bbe\u8ba1", None))
    # retranslateUi

