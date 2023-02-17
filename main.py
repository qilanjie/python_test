# 安装：pip3 install pyserial   //python3
import sys

import serial
import serial.tools.list_ports
import time
import threading
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QApplication
from sp_ui import Ui_Form


from qt_material import apply_stylesheet
com_rx_buf = ''  # 接收缓冲区
com_tx_buf = ''  # 发送缓冲区
COMM = serial.Serial()  # 定义串口对象
port_list: list  # 可用串口列表
port_select: list  # 选择好的串口
ui: Ui_Form

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


# 打开串口
def serial_open(n=0):
    global COMM
    serial_port = set_com_port(n)
    COMM = serial.Serial(serial_port, 115200, timeout=0)
    if COMM.isOpen():
        print(serial_port, "open success")
        return 0
    else:
        print("open failed")
        return 255


# 关闭串口
def serial_close():
    global COMM
    COMM.close()
    print(COMM.name + "closed.")


def set_com_rx_buf(my_buf=''):
    global com_rx_buf
    com_rx_buf = my_buf


def set_com_tx_buf(my_buf=''):
    global com_tx_buf
    com_tx_buf = my_buf


def get_com_rx_buf():
    global com_rx_buf
    return com_rx_buf


def get_com_tx_buf():
    global com_tx_buf
    return com_tx_buf


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

        except IOError:
            pass
    pass


# def serial_encode(addr=0, command=0, param1=0, param0=0):
#     my_buf = [addr, command, param1, param0, 0, 0, 0, 0]
#     print(my_buf)
#     return my_buf


def serial_send_command(addr=0, command=0, param1=0, param0=0, data3=0, data2=0, data1=0, data0=0):
    my_buf = [addr, command, param1, param0, data3, data2, data1, data0]
    COMM.write(my_buf)
    pass


def serial_init():
    my_buf = "AT+CG\r\n"
    COMM.write(my_buf)
    time.sleep(0.05)
    my_buf = COMM.read_all()
    if my_buf != "OK\r\n":
        return 254  # 进入调试模式失败

    my_buf = "AT+CAN_MODE=0\r\n"
    COMM.write(my_buf)
    time.sleep(0.05)
    my_buf = COMM.read_all()
    if my_buf != "OK\r\n":
        return 253  # 进入正常模式失败，模块处于1状态，即环回模式中

    my_buf = "AT+CAN_BAUD=500000\r\n"
    COMM.write(my_buf)
    time.sleep(0.05)
    my_buf = COMM.read_all()
    if my_buf != "OK\r\n":
        return 253  # 波特率设置失败

    my_buf = "AT+FRAMEFORMAT=1,0,\r\n"
    COMM.write(my_buf)
    time.sleep(0.05)
    my_buf = COMM.read_all()
    if my_buf != "OK\r\n":
        return 253  # 波特率设置失败

    my_buf = "AT+ET\r\n"  # 进入透传模式
    COMM.write(my_buf)
    time.sleep(0.05)
    my_buf = COMM.read_all()
    if my_buf != "OK\r\n":
        return 255  # 不是CAN模块


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        global ui
        ui = Ui_Form()
        ui.setupUi(self)
        textEditSignal.update_text.connect(ui.textEdit.setPlainText)


if __name__ == '__main__':
    port_list = get_com_list()
    length = port_list.__len__()
    device = port_list[0].device
    print(length, device)
    serial_open(0)
    thread1 = threading.Thread(target=thread_com_receive)
    thread1.start()
    COMM.timeout = 1
    COMM.write_timeout = 1
    COMM.inter_byte_timeout = 0.5
    buf = [33, 2, 0x55, 1, 4]
    COMM.write(buf)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(150, 150, 640, 480)
    window.setWindowTitle("串口通信")
    apply_stylesheet(app, theme='light_blue_500.xml')
    window.show()
    sys.exit(app.exec())
    # serial_close()
