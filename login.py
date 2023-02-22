
import sys
from PySide6.QtCore import QFile, QIODeviceBase, QTextStream
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
        ui.label_user_name.setScaledContents(True)
        ui.label_pwd.setScaledContents(True)
        ui.lineE_pwd.setEchoMode(QLineEdit.EchoMode.Password)
        ui.btn_1.clicked.connect(self.set_style)
        ui.btn_2.clicked.connect(self.set_style)
        ui.btn_3.clicked.connect(self.set_style)
        ui.btn_4.clicked.connect(self.set_style)

    def set_style(self):
        sender = self.sender()
        if sender.objectName() == "btn_1":
            filePath = ':/res/qss/style-1.qss'
        if sender.objectName() == "btn_2":
            filePath = ':/res/qss/style-2.qss'
        if sender.objectName() == "btn_3":
            filePath = ':/res/qss/style-3.qss'
        if sender.objectName() == "btn_4":
            filePath = ':/res/qss/style-4.qss'
        print(filePath)
        file = QFile(filePath)
        file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        filetext = QTextStream(file)
        stylesheet = filetext.readAll()
        self.setStyleSheet(stylesheet)
        file.close()


class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(filePath):
        file = QFile(filePath)
        file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        filetext = QTextStream(file)
        stylesheet = filetext.readAll()

        file.close()
        return stylesheet


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(150, 150, 640, 480)
    window.setWindowTitle("登录界面")

    style_file = ':/res/qss/style-1.qss'
    style_sheet = QSSLoader.read_qss_file(style_file)
    window.setStyleSheet(style_sheet)
    window.show()
    sys.exit(app.exec())
    # serial_close()
