from PySide6.QtCore import Qt, QUrl, QDateTime, QDate, QJsonDocument, QPoint, QPropertyAnimation, QAbstractAnimation, QSequentialAnimationGroup, QTime, QEventLoop
import rc_pic
from ui_widget import Ui_Widget
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGraphicsOpacityEffect
from PySide6.QtGui import QFont, QPalette, QBrush, QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest

import sys


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        # 设置去掉窗口边框和半透明背景
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 设置全局文字字体颜色
        self.setStyleSheet("QLabel{color:#292929}")

        # 当前温度文字字体样式
        self.label_temp = QLabel(self)
        ft_temp = QFont("Arial", 50, 75)
        self.label_temp.setFont(ft_temp)

        # 当前天气文字字体样式
        self.label_curr_weather = QLabel(self)
        ft_weather = QFont("Arial", 20, 75)
        self.label_curr_weather.setFont(ft_weather)
        self.label_curr_weather.setStyleSheet("color:#ffffff")

        # 当前城市和日期文字的字体颜色
        self.ui.label_curr_city.setStyleSheet("color:#ffffff")
        self.ui.label_curr_date.setStyleSheet("color:#ffffff")

        # 当前温度和天气状况文字的初始位置
        self.label_temp.move(180, 80)
        self.label_curr_weather.move(220, 200)

        # 折叠按钮的样式
        self.btn_fold = QPushButton(self)
        self.btn_fold.setFixedSize(50, 50)
        self.btn_fold.setText("折叠")
        self.btn_fold.setStyleSheet("QPushButton{font:Arial;color:#ffffff;font-size:20px;background-color:rgba(0,0,0,0);border:none}"
                                    "QPushButton:hover{font-size:22px;}")
        self.btn_fold.clicked.connect(self.slot_up)
        self.btn_fold.move(380, 0)

        # 关闭按钮的样式
        btn_close = QPushButton(self)
        btn_close.setFixedSize(50, 50)
        btn_close.setText("关闭")
        btn_close.setStyleSheet("QPushButton{font:Arial;color:#ffffff;font-size:20px;background-color:rgba(0,0,0,0);border:none}"
                                "QPushButton:hover{font-size:22px;}")
        btn_close.move(440, 0)
        btn_close.clicked.connect(self.close)

        # 获取天气API
        str_url = "http://wthrcdn.etouch.cn/weather_mini?city=深圳"
        url = QUrl(str_url)
        self.manager = QNetworkAccessManager(self)
        self.request = QNetworkRequest(url)
        self.manager.finished.connect(self.doProcessfinished)
        self.manager.get(self.request)

        # 获取当前日期时间
        dt = QDateTime()
        date = QDate.currentDate()
        dt.setDate(date)
        currentDate = dt.toString("MM-dd ddd")
        self.ui.label_curr_date.setText(currentDate)

    def doProcessfinished(self, reply):
        arry = reply.readAll()
        doc = QJsonDocument.fromJson(arry)
        if doc.isNull():
            return

        obj = doc.object()
        if not obj.contains("data"):
            return

        val = obj.value("data")
        if not val.isObject():
            return

        jsonDate = val.toObject()
        curr_temp = jsonDate.value("wendu").toString()
        city = jsonDate.value("city").toString()

        fore = jsonDate.value("forecast")
        if fore.isArray():
            Jsonarry = fore.toArray()
            for i in range(4):
                weaobj = Jsonarry.at(i).toObject()

                high = weaobj.value("high").toString()[3:]
                low = weaobj.value("low").toString()[3:5]
                Week = weaobj.value("date").toString()[2:]
                weather = weaobj.value("type").toString()

                if i == 0:
                    self.label_temp.setText(curr_temp + "℃")
                    self.label_temp.adjustSize()
                    self.label_curr_weather.setText(weather)
                    self.label_curr_weather.adjustSize()
                    self.ui.label_curr_city.setText(city)
                    self.ui.label_curr_city.adjustSize()
                    self.set_weather_pic(weather)
                elif i == 1:
                    self.ui.label_future_day_1.setText(Week)
                    self.ui.label_future_weather_1.setText(weather)
                    self.ui.label_future_temp_1.setText(low + "/" + high)
                elif i == 2:
                    self.ui.label_future_day_2.setText(Week)
                    self.ui.label_future_weather_2.setText(weather)
                    self.ui.label_future_temp_2.setText(low + "/" + high)
                elif i == 3:
                    self.ui.label_future_day_3.setText(Week)
                    self.ui.label_future_weather_3.setText(weather)
                    self.ui.label_future_temp_3.setText(low + "/" + high)

    def set_weather_pic(self, weather):
        print(weather)
        path = ""
        if "雨" in weather:
            path = ":/res/pic/day-rain.png"
            self.label_temp.setStyleSheet("color:#ffffff")
        elif "晴" in weather:
            path = ":/res/pic/day-sun.png"
            self.label_temp.setStyleSheet("color:#ffffff")
        elif "雪" in weather:
            path = ":/res/pic/day-snow.png"
            self.label_temp.setStyleSheet("color:#ffffff")
        elif "多云" in weather:
            path = ":/res/pic/cloudy.png"
            self.label_temp.setStyleSheet("color:#ffffff")
        else:
            path = ":/res/pic/all.png"
            self.label_temp.setStyleSheet("color:#ffffff")

        # 设置背景图片
        self.ui.frame_pic.setAutoFillBackground(True)
        palette = self.ui.frame_pic.palette()
        palette.setBrush(QPalette.Window,
                         QBrush(QPixmap(path).scaled(
                             # 缩放背景图.
                             self.ui.frame_pic.size(),
                             Qt.IgnoreAspectRatio,
                             Qt.SmoothTransformation)))  # 使用平滑的缩放方式
        self.ui.frame_pic.setPalette(palette)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mousePress = True
        # 窗口移动距离
        self.movePoint = event.globalPos() - self.pos()

    def mouseReleaseEvent(self, event):
        self.mousePress = False

    def mouseMoveEvent(self, event):
        if self.mousePress:
            movePos = event.globalPos()  # 窗口初始位置
            self.move(movePos - self.movePoint)

    def slot_up(self):
        static_status = True
        if static_status:
            self.up()
        else:
            self.down()
        static_status = not static_status

    def up(self):
        self.btn_fold.setText("展开")

        # 上升
        animation_text_temp_left = QPropertyAnimation(self.label_temp, "pos")
        animation_text_temp_left.setStartValue(self.label_temp.pos())
        animation_text_temp_left.setEndValue(
            QPoint(self.ui.frame_pic.pos().x() + 70, self.label_temp.pos().y() - 80))
        animation_text_temp_left.setDirection(
            QAbstractAnimation.Direction.Forward)
        animation_text_temp_left.setDuration(500)

        animation_text_weather_left = QPropertyAnimation(
            self.label_curr_weather, "pos")
        animation_text_weather_left.setStartValue(
            self.label_curr_weather.pos())
        animation_text_weather_left.setEndValue(QPoint(
            self.ui.frame_pic.pos().x() + 70, self.label_curr_weather.pos().y() - 100))
        animation_text_weather_left.setDirection(
            QAbstractAnimation.Direction.Forward)
        animation_text_weather_left.setDuration(500)

        animation_future_up_1 = QPropertyAnimation(self.ui.frame_future, "pos")
        animation_future_up_1.setStartValue(
            QPoint(self.ui.frame_future.pos().x(), self.ui.frame_future.pos().y()))
        animation_future_up_1.setEndValue(QPoint(self.ui.frame_future.pos().x(
        ), self.ui.frame_future.pos().y() - self.ui.frame_future.height() - 400))
        animation_future_up_1.setDirection(
            QAbstractAnimation.Direction.Forward)
        animation_future_up_1.setDuration(300)

        animation_pic_up = QPropertyAnimation(self.ui.frame_pic, "pos")
        animation_pic_up.setStartValue(
            QPoint(self.ui.frame_pic.pos().x(), self.ui.frame_pic.pos().y()))
        animation_pic_up.setEndValue(
            QPoint(self.ui.frame_pic.pos().x(), self.ui.frame_pic.pos().y() - 400))
        animation_pic_up.setDirection(QAbstractAnimation.Direction.Forward)
        animation_pic_up.setDuration(300)

        # 设置动画组，按照顺序执行动画
        pPosGroup = QSequentialAnimationGroup(self)
        pPosGroup.addAnimation(animation_text_temp_left)
        pPosGroup.addAnimation(animation_text_weather_left)
        pPosGroup.addAnimation(animation_future_up_1)
        pPosGroup.addAnimation(animation_pic_up)
        pPosGroup.start(QAbstractAnimation.DeleteWhenStopped)

    def down(self):
        self.btn_fold.setText("折叠")

        # 下降
        # 背景图移动动画
        animation_pic_down = QPropertyAnimation(self.ui.frame_pic, b"pos")
        animation_pic_down.setDuration(300)
        animation_pic_down.setStartValue(
            QPoint(self.ui.frame_pic.pos().x(), self.ui.frame_pic.pos().y()))
        animation_pic_down.setEndValue(
            QPoint(self.ui.frame_pic.pos().x(), self.ui.frame_pic.pos().y() + 400))
        animation_pic_down.setDirection(QAbstractAnimation.Direction.Forward)

        # 未来天气背景框移动动画
        animation_future_down = QPropertyAnimation(
            self.ui.frame_future, b"pos")
        animation_future_down.setStartValue(
            QPoint(self.ui.frame_future.pos().x(), self.ui.frame_future.pos().y()))
        animation_future_down.setEndValue(QPoint(self.ui.frame_future.pos().x(
        ), self.ui.frame_future.pos().y() + self.ui.frame_future.height() + 400))
        animation_future_down.setDirection(
            QAbstractAnimation.Direction.Forward)
        # animation_future_up_1->setEasingCurve(QEasingCurve::OutBounce)  # 缓和曲线风格
        animation_future_down.setDuration(500)

        # opacity
        # 未来第一天天气文字渐变动画
        pButtonOpacity_1 = QGraphicsOpacityEffect(self)
        pButtonOpacity_1.setOpacity(0)
        self.ui.frame_weather_1.setGraphicsEffect(pButtonOpacity_1)
        pOpacityAnimation_1 = QPropertyAnimation(pButtonOpacity_1, b"opacity")
        pOpacityAnimation_1.setDuration(300)
        pOpacityAnimation_1.setStartValue(0)
        pOpacityAnimation_1.setEndValue(1)

        # 未来第二天天气文字渐变动画
        pButtonOpacity_2 = QGraphicsOpacityEffect(self)
        pButtonOpacity_2.setOpacity(0)
        self.ui.frame_weather_2.setGraphicsEffect(pButtonOpacity_2)
        pOpacityAnimation_2 = QPropertyAnimation(pButtonOpacity_2, b"opacity")
        pOpacityAnimation_2.setDuration(300)
        pOpacityAnimation_2.setStartValue(0)
        pOpacityAnimation_2.setEndValue(1)

        # 未来第三天天气文字渐变动画
        pButtonOpacity_3 = QGraphicsOpacityEffect(self)
        pButtonOpacity_3.setOpacity(0)
        self.ui.frame_weather_3.setGraphicsEffect(pButtonOpacity_3)
        pOpacityAnimation_3 = QPropertyAnimation(pButtonOpacity_3, b"opacity")
        pOpacityAnimation_3.setDuration(300)
        pOpacityAnimation_3.setStartValue(0)
        pOpacityAnimation_3.setEndValue(1)

        # 当前温度文字的移动动画
        animation_text_temp_right = QPropertyAnimation(self.label_temp, b"pos")
        animation_text_temp_right.setStartValue(self.label_temp.pos())
        animation_text_temp_right.setEndValue(QPoint(180, 80))
        animation_text_temp_right.setDirection(
            QAbstractAnimation.Direction.Forward)
        animation_text_temp_right.setDuration(500)
        # 创建当前天气状况文字移动动画
        animation_text_weather_right = QPropertyAnimation(
            self.label_curr_weather, b"pos")
        animation_text_weather_right.setStartValue(
            self.label_curr_weather.pos())
        animation_text_weather_right.setEndValue(QPoint(220, 200))
        animation_text_weather_right.setDirection(
            QAbstractAnimation.Direction.Forward)
        animation_text_weather_right.setDuration(500)

        # 设置动画组，按顺序执行动画
        pPosGroup = QSequentialAnimationGroup(self)
        pPosGroup.addAnimation(animation_pic_down)
        pPosGroup.addAnimation(animation_future_down)
        pPosGroup.addAnimation(pOpacityAnimation_1)
        pPosGroup.addAnimation(pOpacityAnimation_2)
        pPosGroup.addAnimation(pOpacityAnimation_3)
        pPosGroup.addAnimation(animation_text_temp_right)
        pPosGroup.addAnimation(animation_text_weather_right)
        pPosGroup.start(QAbstractAnimation.DeleteWhenStopped)

    def msleep(msec):

        end_time = QTime.currentTime().addMSecs(msec)
        while QTime.currentTime() < end_time:
            QApplication.processEvents(QEventLoop.AllEvents, 200)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Widget()

    window.setWindowTitle("登录界面")

    window.show()
    sys.exit(app.exec())
    # serial_close()
