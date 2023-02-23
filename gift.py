
import sys
from PySide6.QtCore import QFile, QIODeviceBase, QTextStream, QTimer
from PySide6.QtWidgets import QWidget, QApplication, QLineEdit
from ui_widget import Ui_Widget
from qt_material import apply_stylesheet
import rc_pic
import rc_qss


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        ui = Ui_Widget()
        ui.setupUi(self)
        self.setStyleSheet(
            "#frame{background-image:url(:/new/prefix1/res/pic/background.jpg)}")
        self.mytime = QTimer(self)
        self.mytime.timeout.connect(self.slot_timeout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(150, 150, 640, 480)
    window.setWindowTitle("登录界面")

    window.show()
    sys.exit(app.exec())
    # serial_close()
