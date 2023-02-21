
import sys
from PySide6.QtWidgets import QWidget, QApplication
from ui_widget import Ui_Widget
from qt_material import apply_stylesheet
import rc_pic
import rc_qss


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        ui = Ui_Widget()
        ui.setupUi(self)

# 封装修改样式工具
# 定义一个专门用来操作qss样式的类


class QSSTool():
    # 静态方法
    @staticmethod
    def setQssToObj(file_path, obj):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            obj.setStyleSheet(content)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(150, 150, 640, 480)
    window.setWindowTitle("登录界面")

    QSSTool.setQssToObj("res/qss/style-4.qss", app)

    window.show()
    sys.exit(app.exec())
    # serial_close()
