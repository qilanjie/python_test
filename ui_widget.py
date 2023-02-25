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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(542, 891)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        self.gridLayout_9 = QGridLayout(Widget)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_8 = QSpacerItem(13, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_background = QFrame(Widget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setFrameShape(QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_background)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.frame_pic = QFrame(self.frame_background)
        self.frame_pic.setObjectName(u"frame_pic")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pic.sizePolicy().hasHeightForWidth())
        self.frame_pic.setSizePolicy(sizePolicy1)
        self.frame_pic.setMinimumSize(QSize(450, 600))
        self.frame_pic.setMaximumSize(QSize(450, 600))
        self.frame_pic.setStyleSheet(u"#frame_pic{\n"
"	border-radius:0px;\n"
"}")
        self.frame_pic.setFrameShape(QFrame.StyledPanel)
        self.frame_pic.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_pic)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_date = QFrame(self.frame_pic)
        self.frame_date.setObjectName(u"frame_date")
        self.frame_date.setMinimumSize(QSize(0, 20))
        self.frame_date.setStyleSheet(u"#frame_date{\n"
"	background-color:rgba(0,0,0,150);\n"
"	border-bottom-left-radius:0px;  \n"
"	border-bottom-right-radius:0px;\n"
"}")
        self.frame_date.setFrameShape(QFrame.StyledPanel)
        self.frame_date.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_date)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_curr_city = QLabel(self.frame_date)
        self.label_curr_city.setObjectName(u"label_curr_city")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label_curr_city.setFont(font)

        self.horizontalLayout.addWidget(self.label_curr_city)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_curr_date = QLabel(self.frame_date)
        self.label_curr_date.setObjectName(u"label_curr_date")
        self.label_curr_date.setFont(font)

        self.horizontalLayout.addWidget(self.label_curr_date)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_date, 1, 0, 1, 1)

        self.frame = QFrame(self.frame_pic)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 550))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,50);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_pic, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_background)

        self.frame_2 = QFrame(Widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_future = QFrame(self.frame_2)
        self.frame_future.setObjectName(u"frame_future")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_future.sizePolicy().hasHeightForWidth())
        self.frame_future.setSizePolicy(sizePolicy4)
        self.frame_future.setMinimumSize(QSize(450, 220))
        self.frame_future.setMaximumSize(QSize(450, 220))
        self.frame_future.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_future.setFrameShape(QFrame.StyledPanel)
        self.frame_future.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_future)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_weather_2 = QFrame(self.frame_future)
        self.frame_weather_2.setObjectName(u"frame_weather_2")
        self.frame_weather_2.setFrameShape(QFrame.StyledPanel)
        self.frame_weather_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_weather_2)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_future_day_2 = QLabel(self.frame_weather_2)
        self.label_future_day_2.setObjectName(u"label_future_day_2")
        self.label_future_day_2.setFont(font)
        self.label_future_day_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_future_day_2)

        self.horizontalSpacer_13 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.label_future_weather_2 = QLabel(self.frame_weather_2)
        self.label_future_weather_2.setObjectName(u"label_future_weather_2")
        self.label_future_weather_2.setFont(font)
        self.label_future_weather_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_future_weather_2)

        self.horizontalSpacer_14 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.label_future_temp_2 = QLabel(self.frame_weather_2)
        self.label_future_temp_2.setObjectName(u"label_future_temp_2")
        self.label_future_temp_2.setFont(font)
        self.label_future_temp_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_future_temp_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_weather_2, 3, 0, 1, 1)

        self.frame_weather_3 = QFrame(self.frame_future)
        self.frame_weather_3.setObjectName(u"frame_weather_3")
        self.frame_weather_3.setFrameShape(QFrame.StyledPanel)
        self.frame_weather_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_weather_3)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_future_day_3 = QLabel(self.frame_weather_3)
        self.label_future_day_3.setObjectName(u"label_future_day_3")
        self.label_future_day_3.setFont(font)
        self.label_future_day_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_future_day_3)

        self.horizontalSpacer_17 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_17)

        self.label_future_weather_3 = QLabel(self.frame_weather_3)
        self.label_future_weather_3.setObjectName(u"label_future_weather_3")
        self.label_future_weather_3.setFont(font)
        self.label_future_weather_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_future_weather_3)

        self.horizontalSpacer_18 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)

        self.label_future_temp_3 = QLabel(self.frame_weather_3)
        self.label_future_temp_3.setObjectName(u"label_future_temp_3")
        self.label_future_temp_3.setFont(font)
        self.label_future_temp_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_future_temp_3)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_weather_3, 5, 0, 1, 1)

        self.frame_weather_1 = QFrame(self.frame_future)
        self.frame_weather_1.setObjectName(u"frame_weather_1")
        self.frame_weather_1.setFrameShape(QFrame.StyledPanel)
        self.frame_weather_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_weather_1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_future_day_1 = QLabel(self.frame_weather_1)
        self.label_future_day_1.setObjectName(u"label_future_day_1")
        self.label_future_day_1.setFont(font)
        self.label_future_day_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_future_day_1)

        self.horizontalSpacer_9 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.label_future_weather_1 = QLabel(self.frame_weather_1)
        self.label_future_weather_1.setObjectName(u"label_future_weather_1")
        self.label_future_weather_1.setFont(font)
        self.label_future_weather_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_future_weather_1)

        self.horizontalSpacer_10 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)

        self.label_future_temp_1 = QLabel(self.frame_weather_1)
        self.label_future_temp_1.setObjectName(u"label_future_temp_1")
        self.label_future_temp_1.setFont(font)
        self.label_future_temp_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_future_temp_1)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_weather_1, 1, 0, 1, 1)

        self.line_2 = QFrame(self.frame_future)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_2, 4, 0, 1, 1)

        self.line_3 = QFrame(self.frame_future)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_3, 6, 0, 1, 1)

        self.line_4 = QFrame(self.frame_future)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_4, 0, 0, 1, 1)

        self.line = QFrame(self.frame_future)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_future)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_2, 7, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_future)

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_11 = QSpacerItem(13, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)


        self.gridLayout_9.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_curr_city.setText(QCoreApplication.translate("Widget", u"null", None))
        self.label_curr_date.setText(QCoreApplication.translate("Widget", u"null", None))
        self.label_future_day_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_weather_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_temp_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_day_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_weather_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_temp_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_day_1.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_weather_1.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_future_temp_1.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u672c\u754c\u9762\u7531bilibili up\u4e3b <\u8001\u5b9e\u7684\u5f90\u7801\u519c> \u8bbe\u8ba1", None))
    # retranslateUi

