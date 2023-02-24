
import sys

from PySide6.QtCore import QFile, QIODeviceBase, QTextStream, QTimer, QTime, QIODeviceBase, Qt, QPropertyAnimation, QPoint, QAbstractAnimation, QCoreApplication, QEventLoop
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QGraphicsOpacityEffect
from ui_widget import Ui_Widget
import rc_pic
import rc_txt
import random


class MaskLabel(QLabel):
    def __init__(self, pos_x, fans_name,  parent=None):
        super().__init__(parent)

        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setStyleSheet("color:white;font-size:20px")
        parent.animation_fans = QPropertyAnimation(self, b'pos')
        parent.animation_fans.setStartValue(QPoint(pos_x, 900))
        # 起始位置
        parent.animation_fans.setEndValue(QPoint(pos_x, -50))
        # 结束位置
        parent.animation_fans.setDirection(
            QAbstractAnimation.Direction.Forward)
        parent.animation_fans.setDuration(15000)
        # 时长15妙
        parent.animation_fans.start(
            QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)
        # 动画结束后自动关闭，释放内存
        self.setText("粉丝名称的长度设置初始化")
        self.adjustSize()
        self.setFixedHeight(50)
        self.setText(fans_name)
        parent.pGra = QGraphicsOpacityEffect(parent)
        parent.pGra.setOpacity(0)
        parent.setGraphicsEffect(parent.pGra)
        parent.animation_opa = QPropertyAnimation(parent.pGra, b"opacity")
        parent.animation_opa.setDuration(2000)
        parent.animation_opa.setStartValue(0)
        parent.animation_opa.setEndValue(1)
        parent.animation_opa.start(
            QAbstractAnimation.DeletionPolicy.DeleteWhenStopped)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setStyleSheet(
            "#frame{background-image:url(:/new/prefix1/res/pic/background.jpg)}")
        self.mytime = QTimer(self)
        self.mytime.timeout.connect(self.slot_timeout)
        nameFile = QFile(":/new/prefix1/res/txt/fans_name.txt")

        if nameFile.open(QIODeviceBase.OpenModeFlag.ReadOnly) == False:
            return
        toText = QTextStream(nameFile)

        self.name_items = []

        while not toText.atEnd():
            name = toText.readLine()
            self.name_items.append(name.replace("\n", ""))
        nameFile.close()
        self.btn_items = [self.ui.btn_1, self.ui.btn_2,
                          self.ui.btn_3, self.ui.btn_4]
        for btn in self.btn_items:
            btn.clicked.connect(self.slot_btn_click)
            btn.setStyleSheet("QPushButton{color:rgb(75,152,204);background-color:rgb(255,255,255);border-radius:20px}"
                              "QPushButton::hover{color:rgb(53,135,202)}")
            btn.hide()
        self.mytime.start(10000)
        self.ui.label_head.setStyleSheet("color:rgba(255,255,255,100)")
        self.ui.label_head.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    def slot_timeout(self):
        self.mytime.stop()
        k = 0
        self.label_items = []
        arr_pox_x = [20, 220, 420, 620, 820, 1020, 120, 320, 520, 720, 920]
        for i in range(self.name_items.__len__()):

            pos_x = arr_pox_x[k]
            k = k+1

            # self.label_items.append(MaskLabel(pos_x, self.name_items[i], self))

            # self.label_items[i].show()
            MaskLabel(pos_x, self.name_items[i], self).show()
            if k == 6:
                self.msleep(1500)
            elif k == 11:
                k = 0
                self.msleep(1500)

        self.msleep(15000)
        for btn in self.btn_items:
            btn.show()
        self.ui.label_head.setText("幸运粉丝")
        self.ui.label_head.setStyleSheet("color:rgba(255,255,255,255)")

    def msleep(self, msec):
        dieTime = QTime.currentTime().addMSecs(msec)
        while QTime.currentTime() < dieTime:
            QCoreApplication.processEvents(
                QEventLoop.ProcessEventsFlag.AllEvents, 200)

    def slot_btn_click(self):
        btn = self.sender()
        randtime = QTime.currentTime()

        random.seed(randtime.msec()+randtime.second()*1000)
        num = random.randrange(0, self.name_items.__len__())
        btn.setText(self.name_items[num])
        btn.setDisabled(True)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(150, 150, 640, 480)
    window.setWindowTitle("登录界面")

    window.show()
    sys.exit(app.exec())
    # serial_close()
