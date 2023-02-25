from math import sin, cos, pi
import sys
from PySide6.QtGui import QPainter, QColor, QPainterPath, QFont, QRadialGradient, QBrush, QConicalGradient, QKeyEvent
from PySide6.QtCore import QPointF, QRectF, Qt, QTimer, QRect
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from ui_mainwindow import Ui_MainWindow
import rc_pic


class MainWindow(QMainWindow):
    degRotate = 0
    direction = 0

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1280, 800)
        self.setStyleSheet(
            "#MainWindow{background-image:url(:/res/pic/background.png)}")
        self.myTimer = QTimer(self)
        self.myTimer.timeout.connect(self.slot_speed_changed)

    def slot_speed_changed(self):
        if self.direction == 1:
            self.degRotate = self.degRotate+1
            if self.degRotate > 240:
                self.degRotate = 240
        elif self.direction == 0:
            self.degRotate = self.degRotate-1
            if self.degRotate < 0:
                self.degRotate = 0
                self.myTimer.stop()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width()
        height = self.height() - 100  # 移动仪表盘的高度
        radius = (height if width > height else width) / 2.0  # 仪表盘的中心位置
        # 移动画笔到中下方
        painter.translate(width/2, height*0.6)
        # 启用反锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setPen(Qt.NoPen)
        # 设置画刷颜色
        painter.setBrush(QColor(138, 43, 226))
        self.drawSmallScale(painter, radius - 60)  # 刻度线
        self.draw_digital(painter, radius - 90)  # 刻度数字
        self.drawCircle(painter, radius - 35)  # 渐变发光外扇形
        self.drawCircle_arc(painter, radius - 40)  # 动态扇形环
        self.drawPointer(painter, radius - 130)  # 指针
        self.drawCircle_line(painter, radius - 35)  # 最外细圆线
        self.draw_circle_bom_big(painter, radius - 150)  # 中间大圆
        self.draw_circle_bom_shine(painter, radius - 230)  # 渐变发光内圈
        self.drawCircle_bom_small(painter, radius - 200)  # 中间小圆
        self.drawUnit(painter, radius - 390)  # 单位
        self.drawNum(painter, radius - 300)  # 时速

    def draw_point(self, painter, radius):
        # 组装点的路径图
        pointPath = QPainterPath()
        pointPath.moveTo(-2, -2)
        pointPath.lineTo(2, -2)
        pointPath.lineTo(2, 2)
        pointPath.lineTo(0, 4)
        pointPath.lineTo(-2, 2)

        # 绘制13个小点
        for i in range(13):
            point = QPointF(0, 0)
            painter.save()
            painter.setBrush(QColor(250, 252, 78))

            # 计算并移动绘图对象中心点
            point.setX(radius * cos(((210 - i * 20) * pi) / 180))
            point.setY(radius * sin(((210 - i * 20) * pi) / 180))

            # 计算并移动绘图对象的中心点
            painter.translate(point.x(), -point.y())

            # 计算并选择绘图对象坐标
            painter.rotate(-120 + i * 20)

            # 绘制路径
            painter.drawPath(pointPath)
            painter.restore()

    def draw_digital(self, painter, radius):
        painter.setPen(QColor(255, 255, 255))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        painter.setFont(font)
        for i in range(13):
            point = QPointF(0, 0)
            painter.save()
            point.setX(radius*cos(((210-i*20)*pi)/180))
            point.setY(radius*sin(((210-i*20)*pi)/180))
            painter.translate(point.x(), -point.y())
            painter.rotate(-120+i*20)
            painter.drawText(-25, 0, 50, 20, Qt.AlignCenter, str(i*20))
            painter.restore()
        painter.setPen(Qt.NoPen)

    def draw_circle_bom(self, painter, radius):
        painter.save()
        out_ring = QPainterPath()
        out_ring.moveTo(0, 0)
        out_ring.arcTo(-radius, -radius, 2*radius, 2*radius, -30, 240)
        out_ring.closeSubpath()
        painter.setBrush(QColor(14, 15, 33))
        painter.drawPath(out_ring)
        painter.restore()

    def draw_circle_bom_shine(self, painter, radius):
        painter.save()
        radial_gradient = QRadialGradient(0, 0, radius, 0, 0)
        radial_gradient.setColorAt(0.5, QColor(10, 68, 185, 150))
        radial_gradient.setColorAt(1.0, QColor(0, 0, 0, 0))
        painter.setBrush(QBrush(radial_gradient))
        painter.drawRect(QRectF(-radius, -radius, 2*radius, 2*radius))
        painter.restore()

    def draw_circle_bom_big(self, painter, radius):
        painter.save()
        in_ring = QPainterPath()
        in_ring.moveTo(0, 0)
        in_ring.addEllipse(-radius+50, -radius+50, 2 *
                           (radius-50), 2*(radius-50))
        painter.setBrush(QColor(10, 20, 30))
        painter.drawPath(in_ring)
        painter.restore()

    def drawCircle_bom_small(self, painter: QPainter, radius: int):
        # 保存绘图对象
        painter.save()
        # 计算大小圆路径
        inRing = QPainterPath()
        inRing.moveTo(0, 0)
        inRing.addEllipse(-radius + 50, -radius + 50, 2 *
                          (radius - 50), 2 * (radius - 50))
        # 设置画刷
        painter.setBrush(QColor(10, 20, 30))
        painter.drawPath(inRing)

        painter.restore()

    def drawCircle_arc(self, painter: QPainter, radius: int):
        rect = QRect(-radius, -radius, 2 * radius, 2 * radius)
        Conical = QConicalGradient(0, 0, -70)

        Conical.setColorAt(0.1, QColor(255, 88, 127, 200))  # 红色
        Conical.setColorAt(0.5, QColor(53, 179, 251, 150))  # 蓝色
        painter.setBrush(Conical)
        painter.drawPie(rect, 210 * 16, -(self.degRotate) * 16)

    def drawCircle(self, painter: QPainter, radius: int):
        # 保存绘图对象
        painter.save()
        # 计算大小圆路径
        outRing = QPainterPath()
        inRing = QPainterPath()
        outRing.moveTo(0, 0)
        inRing.moveTo(0, 0)
        outRing.arcTo(-radius, -radius, 2 * radius, 2 * radius, -30, 240)
        inRing.addEllipse(-radius + 50, -radius + 50, 2 *
                          (radius - 50), 2 * (radius - 50))
        outRing.closeSubpath()
        # 设置渐变色
        radialGradient = QRadialGradient(0, 0, radius, 0, 0)
        radialGradient.setColorAt(1, QColor(0, 82, 199))
        radialGradient.setColorAt(0.92, QColor(Qt.transparent))
        # 设置画刷
        painter.setBrush(radialGradient)
        # 大圆减小圆
        painter.drawPath(outRing.subtracted(inRing))
        painter.restore()

    def drawCircle_line(self, painter, radius):
        # 保存绘图对象
        painter.save()

        # 计算大小圆路径
        outRing = QPainterPath()
        inRing = QPainterPath()
        outRing.moveTo(0, 0)
        inRing.moveTo(0, 0)
        outRing.arcTo(-radius, -radius, 2 * radius, 2 * radius, -30, 240)
        inRing.addEllipse(-radius + 2, -radius + 2, 2 *
                          (radius - 2), 2 * (radius - 2))
        outRing.closeSubpath()

        # 设置画刷
        painter.setBrush(QColor(5, 228, 255))

        # 大圆减小圆
        painter.drawPath(outRing.subtracted(inRing))
        painter.restore()

    def drawSmallScale(self, painter, radius):
        # 组装点的路径图
        pointPath_small = QPainterPath()
        pointPath_small.moveTo(-2, -2)
        pointPath_small.lineTo(2, -2)
        pointPath_small.lineTo(2, 8)
        pointPath_small.lineTo(-2, 8)

        pointPath_big = QPainterPath()
        pointPath_big.moveTo(-2, -2)
        pointPath_big.lineTo(2, -2)
        pointPath_big.lineTo(2, 20)
        pointPath_big.lineTo(-2, 20)

        # 绘制121个小点
        for i in range(0, 121, 2):
            point = QPointF(0, 0)
            painter.save()
            point.setX(radius * cos((210 - i * 2) * pi / 180))
            point.setY(radius * sin((210 - i * 2) * pi / 180))
            painter.translate(point.x(), -point.y())
            painter.rotate(-120 + i * 2)

            if i < 80:
                painter.setBrush(QColor(255, 255, 255))
            if i >= 80:
                painter.setBrush(QColor(235, 70, 70))

            if i % 5 == 0:
                painter.drawPath(pointPath_big)
            else:
                painter.drawPath(pointPath_small)

            painter.restore()
     # 绘制文字

    def drawUnit(self, painter, radius):
        painter.save()
        painter.setPen(QColor(255, 255, 255))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(-50, -radius, 100, 20, Qt.AlignCenter, "km/h")
        painter.drawText(-60, -radius + 130, 120, 40, Qt.AlignCenter, "当前车速")

        painter.setPen(QColor(255, 255, 255, 50))
        painter.drawText(-120, -radius + 280, 250, 40,
                         Qt.AlignCenter, "-请按space键加速-")
        painter.restore()

    # 绘制实时时速数字
    def drawNum(self, painter, radius):
        painter.save()
        painter.setPen(QColor(255, 255, 255))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(45)
        painter.setFont(font)
        painter.drawText(-75, -radius - 20, 150, 100,
                         Qt.AlignCenter, str(self.degRotate))
        painter.restore()

    # 绘制指针
    def drawPointer(self, painter, radius):
        # 组装点的路径图
        pointPath = QPainterPath()
        pointPath.moveTo(10, 0)
        pointPath.lineTo(1, -radius)
        pointPath.lineTo(-1, -radius)
        pointPath.lineTo(-10, 0)
        pointPath.arcTo(-10, 0, 20, 20, 180, 180)
        inRing = QPainterPath()
        inRing.addEllipse(-5, -5, 10, 10)
        painter.save()

        # 计算并选择绘图对象坐标
        painter.rotate(self.degRotate - 120)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawPath(pointPath.subtracted(inRing))
        painter.restore()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Space:
            if self.direction == 0:
                self.myTimer.start(1)
                self.direction = 1

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Space:
            self.direction = 0


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()

    window.setWindowTitle("登录界面")

    window.show()
    sys.exit(app.exec())
    # serial_close()
