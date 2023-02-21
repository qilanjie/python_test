# 安装：pip3 install pyserial   //python3
import sys

import serial
import serial.tools.list_ports
import threading
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from ui_sp_ui import Ui_Form


from qt_material import apply_stylesheet
com_rx_buf = ''  # 接收缓冲区
com_tx_buf = ''  # 发送缓冲区
COMM = serial.Serial()  # 定义串口对象
port_list: list  # 可用串口列表
port_select: list  # 选择好的串口
ui: Ui_Form
is_com_open: bool

# 无串口返回0，
# 返回可用的串口列表


class TextEditSignal(QObject):
    update_text = Signal(str)


textEditSignal = TextEditSignal()


def update_text_edit(data):
    text = data.decode('utf-8') + "\r"
    textEditSignal.update_text.emit(text)


def get_com_list():
    global port_list
    # a = serial.tools.list_ports.comports()
    # print(a)
    # port_list = list(serial.tools.list_ports.comports())
    port_list = serial.tools.list_ports.comports()
    return port_list


def set_com_port(n=0):
    global port_list
    global port_select
    port_select = port_list[n]
    return port_select.device


def thread_com_receive():
    rx_buf = []
    global ui

    while True:
        try:

            # rx_buf.extend(COMM.read_all())  # 转化为整型数字
            # a = rx_buf.__len__()
            # time.sleep(0.01)
            # rx_buf.extend(COMM.read_all())  # 转化为整型数字
            # b = rx_buf.__len__()
            # if a == b and a != 0:
            #     print("串口收到消息:", rx_buf.__len__())
            #     rx_buf.clear()
            # 等待空闲中断触发
            # COMM.reset_input_buffer()
            # COMM.read_until(b'\r\n')

            # 读取数据
            data = COMM.read_until(b'\r\n\r\n').strip()
            # print(data.decode('utf-8'))
            # rx_buf.extend(data.decode('utf-8'))
            update_text_edit(data)

            # ui.textEdit.setPlainText(data.decode('utf-8')+"\r")
            if not is_com_open:
                break
                print("接收线程退出了")
        except IOError:
            pass
    pass


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        global ui
        ui = Ui_Form()
        ui.setupUi(self)
        textEditSignal.update_text.connect(ui.textEdit.setPlainText)
        port_list = get_com_list()
        for number in port_list:     # 循环获取列表中单个元素
            # 单个元素为类 serial.tools.list_ports.ListPortInfo 获取类中的 device 属性，添加在列表中
            ui.comboBox.addItem(number.device)  # 将串口设备添加到列表中
        ui.pushButton.clicked.connect(self.pBtn_Serial_Open_Slot)
    # 打开串口槽函数

    @Slot()
    def pBtn_Serial_Open_Slot(self):
        global COMM, is_com_open
        print(ui.pushButton.text())
        if (ui.pushButton.text() == "打开串口"):
            choice_serial_port_number = ui.comboBox.currentText()

            try:
                COMM = serial.Serial(choice_serial_port_number, 115200, timeout=0
                                     )
                if COMM.is_open:
                    is_com_open = True
                    print("串口已经打开", COMM.name)
                    ui.pushButton.setText("关闭串口")
                    thread1 = threading.Thread(target=thread_com_receive)
                    thread1.start()

                    COMM.timeout = 1
                    COMM.write_timeout = 1
                    COMM.inter_byte_timeout = 0.5
                    buf = [33, 2, 0x55, 1, 4]
                    COMM.write(buf)
            except Exception as error:
                if "拒绝访问" in str(error):
                    QMessageBox.information(
                        self, "Error", "串口拒绝访问", QMessageBox.Yes, QMessageBox.Yes)
                else:
                    QMessageBox.information(
                        self, "Error", "打开失败", QMessageBox.Yes, QMessageBox.Yes)

                print(error)
        else:
            COMM.close()
            print(COMM.name + "closed.")
            is_com_open = False
            ui.pushButton.setText("打开串口")


if __name__ == '__main__':
    port_list = get_com_list()
    length = port_list.__len__()
    device = port_list[1].device
    print(length, device)
    # serial_open(1)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(150, 150, 640, 480)
    window.setWindowTitle("串口通信")
    apply_stylesheet(app, theme='light_blue_500.xml')

    window.show()
    sys.exit(app.exec())
    # serial_close()
