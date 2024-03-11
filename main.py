# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import json
import sys
import os
import platform
from threading import Thread

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from PySide6 import QtSerialPort
import  re
import  time
from loguru import logger
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        SN_FILE_PATH = "data/sn.json"
        SN_FILE_BAK_PATH = "data/sn_bak.json"
        LOGS_FILE = "logs/logfile"
        SN_START = "580018020001"
        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serialport = QtSerialPort.QSerialPort()
        global widgets
        widgets = self.ui

        self.sn_path = SN_FILE_PATH
        self.sn_bak_path = SN_FILE_BAK_PATH
        self.logfile_path = LOGS_FILE
        self.sn_start_number = SN_START
        self.sn_length = 12
        self.sn = ""
        self.customer_version = False

        widgets.version.setText("v0.5.0")

        # mkdirs
        if not os.path.exists("data"):
            os.mkdir("data")
        if not os.path.exists("logs"):
            os.mkdir("logs")
        if not os.path.exists(self.sn_path):
            with open(self.sn_path, "w") as file:
                json_object = {"serial": "0"}
                # json_object["serial"] = str(sn_int + 1)
                json_object["serial"] = ('{0:0>' + str(self.sn_length) + '}').format(str(0))
                json.dump(json_object, file)
                file.close()

            with open(self.sn_bak_path, "w") as file:
                json_object = {"serial": "0"}
                json_object["serial"] = ('{0:0>' + str(self.sn_length) + '}').format(str(0))
                json.dump(json_object, file)
                file.close()
        #read the json file
        with open(self.sn_path, "r") as file:
            data = json.load(file)
            print("json data: ", data)
            widgets.lineEdit_sn.setText(data["serial"])

        ##########################SN not editable by customer##########################################
        oemRsaEncrypt = OemRsaEncrypt()
        public_key  = oemRsaEncrypt.publickeyEncryptData()
        private_key = oemRsaEncrypt.LocalPrivateKeyDecryptData()

        if public_key == False or private_key == False:
            self.customer_version = True

        if self.customer_version == True:
            widgets.lineEdit_sn.setText("")
            widgets.pushButton_writesn.setDisabled(True)
            widgets.pushButton_writesn.setStyleSheet("\
            QPushButton\
            {\
            background-color: #ffffff;\
            font: 11pt \"Microsoft YaHei UI\";\
            border-color:#367fa9\
            }")


        logger.add(self.logfile_path+"_{time}.log", format="[{time} {level}] {message}", rotation= "20 MB")
        #logger.add(self.logfile_path+"_{time}.log", rotation="20 MB")
        #logger.add(self.logfile_path + "_{time}.log", rotation='00:00')
        #logger.add(self.logfile_path + "_{time}.log", rotation='1 week')
        logger.info("=================== application run =================================")


        selrialPors = QtSerialPort.QSerialPortInfo().availablePorts()
        for serialPort in selrialPors:
            logger.info("serlial port name : {}", serialPort.portName())
            logger.info("serlial manufacture name : {}", serialPort.manufacturer())
            logger.info("serlial description : {}", serialPort.description())
            logger.info("serlial serial number : {}", serialPort.serialNumber())
            logger.info("serlial standradbaudrates : {}", serialPort.standardBaudRates())
            widgets.combox_serialPortNames.addItem(serialPort.portName())

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PyDracula - Modern GUI"
        description = "串口配置工具"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        #widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))
        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.recvTimer = QTimer(self)
        self.recvTimer.timeout.connect(self.serialport_readyRead)
        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        #widgets.btn_new.clicked.connect(self.buttonClick)
        #widgets.btn_save.clicked.connect(self.buttonClick)

        widgets.btn_openserialport.clicked.connect(self.buttonClick)

        widgets.pushButton_getsn.clicked.connect(self.buttonClick)
        widgets.pushButton_getdevinfo.clicked.connect(self.buttonClick)
        widgets.pushButton_getnetinfo.clicked.connect(self.buttonClick)
        widgets.pushButton_geticcid.clicked.connect(self.buttonClick)
        widgets.pushButton_opendebugmode.clicked.connect(self.buttonClick)

        widgets.pushButton_writeipport.clicked.connect(self.buttonClick)
        widgets.pushButton_writeuploadinterval.clicked.connect(self.buttonClick)
        widgets.pushButton_writesn.clicked.connect(self.buttonClick)

        widgets.pushButton_readipport.clicked.connect(self.buttonClick)
        widgets.pushButton_readipport_duplicate.clicked.connect(self.buttonClick)
        widgets.pushButton_readuploadinterval.clicked.connect(self.buttonClick)
        #widgets.pushButton_readsn.clicked.connect(self.buttonClick)

        widgets.pushButton_writeThreshold.clicked.connect(self.buttonClick)
        #widgets.pushButton_getcali.clicked.connect(self.buttonClick)
        widgets.pushButton_getthreshold.clicked.connect(self.buttonClick)

        widgets.pushButton_writeAdType.clicked.connect(self.buttonClick)
        widgets.pushButton_getAdType.clicked.connect(self.buttonClick)
        widgets.pushButton_readsn_duplicate.clicked.connect(self.buttonClick)
        self.getAdType_thread = None
        self.getCali_thread = None
        self.getUploadInterval_thread = None

        self.setSN_thread = None
        self.setadtype_thread = None
        self.setCali_thread = None
        self.setUploadInterval_thread = None
        self.WriteThreadshold_thread = None
        self.getthreshold_thread = None

        self.setIpPort_thread = None
        self.setdebugMode_thread = None

        self.readsn_thread = None
        self.getnetinfo_thread = None

        widgets.label_getsn.setText("")
        widgets.label_getdevinfo.setText("")
        widgets.label_getnetinfo.setText("")
        widgets.label_geticcid.setText("")
        widgets.label_getipport.setText("")
        widgets.label_getuploadinterval.setText("")
        widgets.label_getsn_2.setText("")
        #widgets.label_cali.setText("")
        widgets.label_threshold.setText("")
        widgets.label_getAdType.setText("")

        widgets.label_debug.setText("")
        widgets.pushButton_opendebugmode.setText("打开")

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        # widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        #widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        #widgets.stackedWidget.setCurrentWidget(widgets.home)
        #widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.stackedWidget.setCurrentWidget(widgets.widgets)
        widgets.btn_widgets.setStyleSheet(UIFunctions.selectMenu(widgets.btn_widgets.styleSheet()))

        widgets.lineEdit_sn.setEnabled(False)

        self.cali_flag = 0
        self.debug = 0
        self.debug_flag = 0

        self.interval_flag = 0
        self.adtype_flag   = 0
        self.netinfo_flag  = 0
        self.sninfo_flag   = 0
        self.buffer_string=""
        self.writethreshold_flag = 0

        # interval value
        self.uploadinterval_value = ""
        # ip
        self.ip_value = ""
        # port
        self.port_value = ""
        # cali
        self.cali_value = 0
        # adtype
        self.adtype_value = {}
        #threshold value
        self.threshold_channel = ""
        self.threshold_high = ""
        self.threshold_low = ""
    def parseString(self, orignString, startString, endString, offset):
        if (orignString.find(startString) != -1) and (orignString.find(endString) != -1):
            json_string = orignString[orignString.find(startString) + offset: orignString.find(endString) + 1]
            logger.debug("[parsing string json_string] ===>  {}", json_string)
            data = json.loads(json_string)
            return  data


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "pushButton_getdevinfo":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.serialport.write(QByteArray("devinfo\n"))

        if btnName == "pushButton_getsn":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.serialport.write(QByteArray("sninfo info\n"))

        if btnName == "pushButton_getnetinfo":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.serialport.write(QByteArray("netinfo info\n"))

        if btnName == "pushButton_geticcid":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.serialport.write(QByteArray("iccidinfo\n"))

        if btnName == "pushButton_opendebugmode":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.debug_flag = 0
            if self.debug == 0:
                self.serialport.write(QByteArray("dbg open\n"))
            else:
                self.serialport.write(QByteArray("dbg close\n"))

            widgets.pushButton_opendebugmode.setEnabled(False)
            if self.setdebugMode_thread is not None and self.setdebugMode_thread.is_alive():
                return
            self.setdebugMode_thread = Thread(target=self.setDebugMode_doing, args=())
            self.setdebugMode_thread.start()

        if btnName == "pushButton_writeipport":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            reg_string_pattern = "^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$"
            res_ip = re.match(reg_string_pattern, widgets.lineEdit_ip.text())

            reg_port_pattern = r"\d+"
            res_port = re.match(reg_port_pattern, widgets.lineEdit_port.text())

            ip_invalid = 0
            port_invalid = 0
            if res_ip is None:
                ip_invalid = 1
            if res_port is None:
                port_invalid = 1

            if ip_invalid:
                QMessageBox.about(self, "提示", "请输入正确的ip地址")
                return
            if port_invalid:
                QMessageBox.about(self, "提示", "请输入正确的端口号")
                return

            self.netinfo_flag = 0
            self.serialport.write(QByteArray("netinfo set" + " " + widgets.lineEdit_ip.text()+":"+
                                             widgets.lineEdit_port.text() + "\n"))

            widgets.pushButton_writeipport.setEnabled(False)
            if self.setIpPort_thread is not None and self.setIpPort_thread.is_alive():
                return
            self.setIpPort_thread = Thread(target=self.setIpPort_doing, args=())
            self.setIpPort_thread.start()

        if btnName == "pushButton_readipport":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.serialport.write(QByteArray("netinfo\n"))

        if btnName == "pushButton_readipport_duplicate":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            self.netinfo_flag = 0
            self.serialport.write(QByteArray("netinfo info\n"))

            widgets.pushButton_readipport_duplicate.setEnabled(False)
            if self.getnetinfo_thread is not None and self.getnetinfo_thread.is_alive():
                return
            self.getnetinfo_thread = Thread(target=self.getnetinfo_doing, args=())
            self.getnetinfo_thread.start()


        if btnName == "pushButton_writeuploadinterval":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            reg_uploadinterval_pattern = r"\d+"
            res_uploadinterval = re.match(reg_uploadinterval_pattern, widgets.lineEdit_uploadinterval.text())
            if res_uploadinterval is None:
                QMessageBox.about(self, "提示", "请输入正确的数据上报间隔")
                return

            self.interval_flag = 0
            self.serialport.write(QByteArray("interval value " + widgets.lineEdit_uploadinterval.text() + "\n"))
            widgets.pushButton_writeuploadinterval.setEnabled(False)
            if self.setUploadInterval_thread is not None and self.setUploadInterval_thread.is_alive():
                return
            self.setUploadInterval_thread = Thread(target=self.setUploadInterval_doing, args=())
            self.setUploadInterval_thread.start()

        if btnName == "pushButton_readuploadinterval":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            self.interval_flag = 0
            self.serialport.write(QByteArray("interval info\n"))

            widgets.pushButton_readuploadinterval.setEnabled(False)
            if self.getUploadInterval_thread is not None and self.getUploadInterval_thread.is_alive():
                return
            self.getUploadInterval_thread = Thread(target=self.getUploadInterval_doing, args=())
            self.getUploadInterval_thread.start()

        if btnName == "pushButton_writesn":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            file_not_found = 0

            if not os.path.exists(self.sn_path):
                # not exists
                file_not_found = 1

            if file_not_found:
                json_object = {"serial":"580018020001"}
                with open(self.sn_path, "w") as file:
                    json.dump(json_object, file)
                    file.close()

            data = ""
            #data = json.loads(json_string)
            with open(self.sn_path, "r") as fp:
                try:
                    data = json.load(fp)
                except:
                    print("load json file error")
                    json_object = {"serial": "580018020001"}
                    with open(self.sn_path, "w") as file:
                        json.dump(json_object, file)
                        file.close()

                #print("serial: ", data["serial"])
                widgets.lineEdit_sn.setText(data["serial"])

            self.sninfo_flag = 0
            self.serialport.write(QByteArray("sninfo set " + widgets.lineEdit_sn.text() + "\n"))

            widgets.pushButton_writesn.setEnabled(False)
            if self.setSN_thread is not None and self.setSN_thread.is_alive():
                return
            self.setSN_thread = Thread(target=self.setSN_doing, args=())
            self.setSN_thread.start()

        if btnName == "pushButton_readsn":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.serialport.write(QByteArray("sninfo info\n"))

        # if btnName == "pushButton_writecali":
        #     if self.serialport.isOpen() == False:
        #         QMessageBox.about(self, "提示", "串口未打开")
        #         return
        #
        #     self.cali_flag = 0
        #     self.serialport.write(QByteArray("cali value " + widgets.comboBox_cali.currentText() + "\n"))
        #     widgets.pushButton_writecali.setEnabled(False)
        #     if self.setCali_thread is not None and self.setCali_thread.is_alive():
        #         return
        #     self.setCali_thread = Thread(target=self.setCali_doing, args=())
        #     self.setCali_thread.start()


        if btnName == "pushButton_writeThreshold":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            pattern = r'\d\.\d\d:\d.\d\d'
            #print("text: ", widgets.lineEdit_threshold.text())
            value = re.findall(pattern, widgets.lineEdit_threshold.text())
            #print("value:", value)
            if len(value) == 0:
                QMessageBox.about(self, "提示", "阈值设置格式错误")
                return
            high_low = widgets.lineEdit_threshold.text().split(":")
            #logger.debug("high low: ", high_low)
            #logger.debug("set low:", high_low[0])
            logger.debug("[set channel] ===>  {}", widgets.comboBox_threshold_channel.currentIndex() + 1)
            logger.debug("[set low] ===>  {}", high_low[0])
            logger.debug("[set high] ===>  {}", high_low[1])

            if high_low[0] > high_low[1]:
                QMessageBox.about(self, "提示", "低阈值大于高阈值")
                return
            #logger.debug("set high:", high_low[1])
            #print("set low:", high_low[0])

            #print(" index: ", widgets.comboBox_threshold_channel.currentIndex())
            self.writethreshold_flag = 0
            self.serialport.write(QByteArray("threshold value " + str(widgets.comboBox_threshold_channel.currentIndex() + 1) + " " + high_low[0] + " " +  high_low[1] + "\n"))
            logger.debug("[command] ===>  {}", "threshold value " + str(widgets.comboBox_threshold_channel.currentIndex() + 1) + " " + high_low[0] + " " + high_low[1])
            widgets.pushButton_writeThreshold.setEnabled(False)
            if self.WriteThreadshold_thread is not None and self.WriteThreadshold_thread.is_alive():
                return
            self.WriteThreadshold_thread = Thread(target=self.WriteThreadshold_doing, args=())
            self.WriteThreadshold_thread.start()



        # if btnName == "pushButton_getcali":
        #     if self.serialport.isOpen() == False:
        #         QMessageBox.about(self, "提示", "串口未打开")
        #         return
        #
        #     self.cali_flag = 0
        #     self.serialport.write(QByteArray("cali info\n"))
        #
        #     widgets.pushButton_getcali.setEnabled(False)
        #     if self.getCali_thread is not None and self.getCali_thread.is_alive():
        #         return
        #     self.getCali_thread = Thread(target=self.getCali_doing, args=())
        #     self.getCali_thread.start()
        if btnName == "pushButton_getthreshold":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            self.writethreshold_flag = 0
            self.serialport.write(QByteArray("threshold info" + " " + str(widgets.comboBox_threshold_channel.currentIndex() + 1) + "\n"))
            logger.debug("[command] ===>  {}","threshold info" + " " + str(widgets.comboBox_threshold_channel.currentIndex() + 1))
            widgets.pushButton_getthreshold.setEnabled(False)
            if self.getthreshold_thread is not None and self.getthreshold_thread.is_alive():
                return
            self.getthreshold_thread = Thread(target=self.getthreshold_doing, args=())
            self.getthreshold_thread.start()

        if btnName == "pushButton_readsn_duplicate":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.sninfo_flag = 0
            self.serialport.write(QByteArray("sninfo info\n"))
            logger.debug("[command] ===>  {}", "sninfo info")
            widgets.pushButton_readsn_duplicate.setEnabled(False)
            if self.readsn_thread is not None and self.readsn_thread.is_alive():
                return
            self.readsn_thread = Thread(target=self.getsn_thread_doing, args=())
            self.readsn_thread.start()

        if btnName == "pushButton_writeAdType":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return

            channel = str(widgets.comboBox_adchannel.currentIndex() + 1)
            type = str(widgets.comboBox_adtype.currentIndex() + 1)

            self.adtype_flag = 0
            self.serialport.write(QByteArray("adtype set " + channel + " " +  type + "\n"))

            widgets.pushButton_writeAdType.setEnabled(False)
            if self.setadtype_thread is not None and self.setadtype_thread.is_alive():
                return
            self.setadtype_thread = Thread(target=self.setAdtype_doing, args=())
            self.setadtype_thread.start()

        if btnName == "pushButton_getAdType":
            if self.serialport.isOpen() == False:
                QMessageBox.about(self, "提示", "串口未打开")
                return
            self.adtype_flag = 0
            self.serialport.write(QByteArray("adtype info\n"))

            widgets.pushButton_getAdType.setEnabled(False)
            if self.getAdType_thread is not None and self.getAdType_thread.is_alive():
                return
            self.getAdType_thread = Thread(target=self.getAdType_doing, args=())
            self.getAdType_thread.start()
        # SHOW NEW PAGE
        #if btnName == "btn_new":
        #    widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
        #    UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
        #    btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        #if btnName == "btn_save":
        #    print("Save BTN clicked!")
        if btnName == "btn_openserialport":
            print("btn open serial port pressed.")
            if btn.text() == "打开串口":

                #self.serialport.setBaudRate(int(widgets.combox_serialBaudrate.currentText()))
                self.serialport.setBaudRate(QtSerialPort.QSerialPort.Baud115200)
                self.serialport.setDataBits(QtSerialPort.QSerialPort.Data8)
                self.serialport.setPortName(widgets.combox_serialPortNames.currentText())
                self.serialport.setParity(QtSerialPort.QSerialPort.NoParity)
                self.serialport.setStopBits(QtSerialPort.QSerialPort.OneStop)
                self.serialport.setFlowControl(QtSerialPort.QSerialPort.NoFlowControl)

                if not self.serialport.open(QIODevice.ReadWrite):
                    print(" open fail. ")
                    QMessageBox.about(self,"提示", "无法打开串口")
                    return
                btn.setText("关闭串口")

                widgets.combox_serialPortNames.setDisabled(True)
                widgets.combox_serialBaudrate.setDisabled(True)

                widgets.combox_serialPortNames.setStyleSheet("background-color: #ffffff;")
                widgets.combox_serialBaudrate.setStyleSheet("background-color: #ffffff;")

                self.serialport.timeout = 400
                self.recvTimer.start(20)

                time.sleep(0.1)
                self.serialport.write(QByteArray("dbg close\n"))


            elif btn.text() == "关闭串口":
                btn.setText("打开串口")
                widgets.combox_serialPortNames.setDisabled(False)
                widgets.combox_serialBaudrate.setDisabled(False)
                self.serialport.close()
                widgets.combox_serialPortNames.setStyleSheet("background-color: rgb(33, 37, 43);")
                widgets.combox_serialBaudrate.setStyleSheet("background-color: rgb(33, 37, 43);")
                #self.recvTimer.stop()

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
        logger.debug("[user action] button : {} is pressed ", btnName )

    def getAdType_doing(self):
        time.sleep(0.2)
        if self.adtype_flag:
            widgets.label_getAdType.setText("采集类型参数获取成功")
            widgets.label_getAdType.setStyleSheet("color:white;")
        else:
            widgets.label_getAdType.setText("采集类型参数获取失败")
            widgets.label_getAdType.setStyleSheet("color:red;")
        self.adtype_flag = 0
        widgets.pushButton_getAdType.setEnabled(True)

    # def getCali_doing(self):
    #     time.sleep(0.2)
    #     if self.cali_flag == 1:
    #         widgets.label_cali.setText("校准参数读取成功")
    #         widgets.label_cali.setStyleSheet("color:white;")
    #         if int(self.cali_value) == -2:
    #             widgets.comboBox_cali.setCurrentIndex(0)
    #         elif int(self.cali_value) == -1:
    #             widgets.comboBox_cali.setCurrentIndex(1)
    #         elif int(self.cali_value) == 0:
    #             widgets.comboBox_cali.setCurrentIndex(2)
    #         elif int(self.cali_value) == 1:
    #             widgets.comboBox_cali.setCurrentIndex(3)
    #         elif int(self.cali_value) == 2:
    #             widgets.comboBox_cali.setCurrentIndex(4)
    #     else:
    #         widgets.label_cali.setText("校准参数读取失败")
    #         widgets.label_cali.setStyleSheet("color:red;")
    #
    #     self.cali_flag = 0
    #     widgets.pushButton_getcali.setEnabled(True)

    def WriteThreadshold_doing(self):
        time.sleep(0.2)
        value = widgets.lineEdit_threshold.text().split(":")
        if self.writethreshold_flag == 1:
            widgets.label_threshold.setText(widgets.comboBox_threshold_channel.currentText() + " " + "低: " +
                                            value[0] + " " + " 高:" + value[1] + " 写入成功")
            widgets.label_threshold.setStyleSheet("color:white;")
        else:
            widgets.label_threshold.setText(widgets.comboBox_threshold_channel.currentText() + " " + "低 " +
                                            value[0] + " " + " 高:" + value[1] + " 写入失败")
            widgets.label_threshold.setStyleSheet("color:red;")
        self.writethreshold_flag = 0
        widgets.pushButton_writeThreshold.setEnabled(True)

    def getthreshold_doing(self):
        time.sleep(0.2)
        if self.writethreshold_flag == 1:
            widgets.label_threshold.setText("阈值参数读取成功")
            widgets.label_threshold.setStyleSheet("color:white;")

            widgets.lineEdit_threshold.setText(self.threshold_low + ":" + self.threshold_high)
           # widgets.lineEdit_uploadinterval.setText(self.uploadinterval_value)
        else:
            widgets.label_threshold.setText("阈值参数读取失败")
            widgets.label_threshold.setStyleSheet("color:red;")
        self.writethreshold_flag = 0
        widgets.pushButton_getthreshold.setEnabled(True)


    def getnetinfo_doing(self):
        time.sleep(0.2)
        if self.netinfo_flag == 1:
            widgets.label_getipport.setText("设备ip:"+self.ip_value + " 端口: " + self.port_value)
            widgets.label_getipport.setStyleSheet("color:white;")

            widgets.lineEdit_threshold.setText(self.threshold_low + ":" + self.threshold_high)
           # widgets.lineEdit_uploadinterval.setText(self.uploadinterval_value)
        else:
            widgets.label_getipport.setText("设备网络配置读取失败")
            widgets.label_getipport.setStyleSheet("color:red;")
        self.writethreshold_flag = 0
        widgets.pushButton_readipport_duplicate.setEnabled(True)

    def getUploadInterval_doing(self):
        time.sleep(0.2)
        if self.interval_flag == 1:
            widgets.label_getuploadinterval.setText("数据上报间隔参数读取成功")
            widgets.label_getuploadinterval.setStyleSheet("color:white;")

            widgets.lineEdit_uploadinterval.setText(self.uploadinterval_value)
        else:
            widgets.label_getuploadinterval.setText("数据上报间隔参数读取失败")
            widgets.label_getuploadinterval.setStyleSheet("color:red;")
        self.interval_flag = 0
        widgets.pushButton_readuploadinterval.setEnabled(True)

    def getsn_thread_doing(self):
        time.sleep(0.2)
        if self.sninfo_flag == 1:
            widgets.label_getsn_2.setText("设备SN:" + self.sn)
            widgets.label_getsn_2.setStyleSheet("color:white;")
        else:
            widgets.label_getsn_2.setText("读取SN失败")
            widgets.label_getsn_2.setStyleSheet("color:red;")
        self.sninfo_flag = 0
        widgets.pushButton_readsn_duplicate.setEnabled(True)


    def setUploadInterval_doing(self):
        time.sleep(0.2)
        if self.interval_flag == 1:
            widgets.label_getuploadinterval.setText("上报间隔: " + widgets.lineEdit_uploadinterval.text() + " 分钟, 写入成功")
            widgets.label_getuploadinterval.setStyleSheet("color:white;")
        else:
            widgets.label_getuploadinterval.setText("上报间隔: " + widgets.lineEdit_uploadinterval.text() + " 分钟, 写入失败")
            widgets.label_getuploadinterval.setStyleSheet("color:red;")
        self.interval_flag = 0
        widgets.pushButton_writeuploadinterval.setEnabled(True)

    def setSN_doing(self):
        time.sleep(0.2)
        if self.sninfo_flag:
            widgets.label_getsn_2.setText("SN: " + widgets.lineEdit_sn.text() + " 写入成功")
            widgets.label_getsn_2.setStyleSheet("color:white;")
        else:
            widgets.label_getsn_2.setText("SN: " + widgets.lineEdit_sn.text() + " 写入失败")
            widgets.label_getsn_2.setStyleSheet("color:red;")
            widgets.pushButton_writesn.setEnabled(True)
            return
        self.sninfo_flag = 0
        widgets.pushButton_writesn.setEnabled(True)
        sn_text = widgets.lineEdit_sn.text()

        try:
            sn_int = int(sn_text)
        except:
            logger.error("sn_text: {} translate error", sn_text)
            return

        with open(self.sn_path, "w") as file:
            json_object = {"serial": "11111111111111111111"}
            #json_object["serial"] = str(sn_int + 1)
            json_object["serial"] = ('{0:0>' + str(self.sn_length) + '}').format(str(sn_int + 1))
            json.dump(json_object, file)
            file.close()

        with open(self.sn_bak_path, "w") as file:
            json_object = {"serial": "11111111111111111111"}
            json_object["serial"] = ('{0:0>' + str(self.sn_length) + '}').format(str(sn_int + 1))
            json.dump(json_object, file)
            file.close()

    def setAdtype_doing(self):
        time.sleep(0.2)
        if self.adtype_flag:
            widgets.label_getAdType.setText("采集类型参数设置成功")
            widgets.label_getAdType.setStyleSheet("color:white;")
        else:
            widgets.label_getAdType.setText("采集类型参数设置失败")
            widgets.label_getAdType.setStyleSheet("color:red;")

        widgets.pushButton_writeAdType.setEnabled(True)
        self.adtype_flag = 0

    # def setCali_doing(self):
    #     time.sleep(0.2)
    #     if self.cali_flag == 1:
    #         widgets.label_cali.setText("校准参数写入成功")
    #         widgets.label_cali.setStyleSheet("color:white;")
    #     else:
    #         widgets.label_cali.setText("校准参数写入失败")
    #         widgets.label_cali.setStyleSheet("color:red;")
    #     widgets.pushButton_writecali.setEnabled(True)
    #     self.cali_flag = 0

    def setIpPort_doing(self):
        time.sleep(0.2)
        if self.netinfo_flag == 1:
            widgets.label_getipport.setText("IP: "+widgets.lineEdit_ip.text() +" Port: " + widgets.lineEdit_port.text() +
                                            " 写入成功")
            widgets.label_getipport.setStyleSheet("color:white;")
        else:
            widgets.label_getipport.setText("IP: "+widgets.lineEdit_ip.text() +" Port: " + widgets.lineEdit_port.text() +
                                            " 写入失败")
            widgets.label_getipport.setStyleSheet("color:red;")

        self.netinfo_flag = 0
        widgets.pushButton_writeipport.setEnabled(True)

    def setDebugMode_doing(self):
        time.sleep(0.2)
        if self.debug_flag == 1:
            if self.debug == 0:
                widgets.label_debug.setText("调试模式关闭成功")
                widgets.pushButton_opendebugmode.setText("打开")
            else:
                widgets.pushButton_opendebugmode.setText("关闭")
                widgets.label_debug.setText("调试模式打开成功")
        else:
            widgets.label_debug.setText("调试模式设置失败")
        self.debug_flag = 0
        widgets.pushButton_opendebugmode.setEnabled(True)

    def serialport_readyRead(self):
        isReadyForSerialData = 0
        isReadyForSerialData = self.serialport.isReadable()
        if isReadyForSerialData == True:
            try:
                buffer = self.serialport.readLine()
                if buffer.length() != 0:
                    if len(self.buffer_string) > 1024:
                        self.buffer_string=""

                    self.buffer_string += buffer.toStdString()
                    # print("buffer: ", buffer.toStdString())
                    logger.debug("serial buffer ===> {}", buffer.toStdString())
                    if (self.buffer_string.find("{") != -1) and (self.buffer_string.find("}") != -1):
                        stringTemp = self.buffer_string
                        #print(" xxx final string: ", self.buffer_string)
                        logger.debug("final string ===> {}", self.buffer_string)
                        if stringTemp.find("devinfo:") != -1:
                            json_string = ""
                            if (stringTemp.find("devinfo:{") != -1) and (stringTemp.find("}") != -1):
                                start_pos = stringTemp.find("devinfo:{")
                                end_pos = stringTemp.find("}", start_pos , -1)
                                test_string = stringTemp[stringTemp.find("devinfo:{") + 8: stringTemp.find("}") + 1]

                                json_string = stringTemp[stringTemp.find("devinfo:{") + 8: stringTemp.find("}") + 1]
                                #print("json_string: ", json_string)
                                data = json.loads(json_string)
                                logger.info("data model : {}", data["model"])
                                logger.info("data hw version : {}", data["hw_rev"])
                                logger.info("data sw version : {}", data["sw_rev"])

                                widgets.label_getdevinfo.setText("设备型号:" + data["model"] +
                                                                 " 硬件版本:" + data["hw_rev"] +
                                                                 " 软件版本:" + data["sw_rev"])
                        if stringTemp.find("sninfo:") != -1:
                            #widgets.label_getsn.setText(buffer.toStdString())
                            json_string = stringTemp[stringTemp.find("sninfo:{") + 7: stringTemp.find("}") + 1]

                            data = json.loads(json_string)
                            logger.info("data serial : {}", data["serial"])
                            if data["serial"] == "":
                                widgets.label_getsn.setText("获取设备SN为空")
                                self.buffer_string = ""
                                return
                            widgets.label_getsn.setText("设备SN:" + data["serial"])
                            self.sn = data["serial"]
                            self.sninfo_flag = 1

                        if stringTemp.find("iccidinfo:") != -1:
                            #widgets.label_geticcid.setText(buffer.toStdString())
                            json_string = stringTemp[stringTemp.find("iccidinfo:{") + 10: stringTemp.find("}") + 1]
                            data = json.loads(json_string)
                            #print("data iccid : ", data["iccid"])
                            logger.info("data iccid : {}", data["iccid"])
                            if data["iccid"] == "":
                                widgets.label_geticcid.setText("无法获取到iccid")
                                widgets.label_geticcid.setStyleSheet("color:red;")
                                self.buffer_string = ""
                                logger.error("无法获取到iccid,请留意sim卡是否未接好或欠费")
                                return
                            widgets.label_geticcid.setText("设备ICCID:" + data["iccid"])
                            widgets.label_geticcid.setStyleSheet("color:white;")

                        if stringTemp.find("netinfo:") != -1:
                            #.label_getnetinfo.setText(buffer.toStdString())
                            json_string = stringTemp[stringTemp.find("netinfo:{") + 8: stringTemp.find("}") + 1]
                            #print("json_string: ", json_string)
                            data = json.loads(json_string)
                            #print("data ip : ", data["ip"])
                            #print("data port : ", data["port"])

                            logger.info("netinfo ip : {}", data["ip"])
                            logger.info("netinfo port : {}", data["port"])

                            widgets.label_getnetinfo.setText("设备ip:" + data["ip"] + ", 端口: " + data["port"])
                            widgets.lineEdit_ip.setText(data["ip"])
                            widgets.lineEdit_port.setText(data["port"])
                            #print("json_string: ", json_string)

                            self.netinfo_flag = 1
                            self.ip_value = data["ip"]
                            self.port_value = data["port"]

                        if stringTemp.find("caliinfo:") != -1:
                            data = self.parseString(stringTemp, "caliinfo:{", "}", 9)
                            #print("data[cali]: ", data["cali"])
                            logger.info("cali info : {}", data["cali"])
                            self.cali_flag = 1
                            self.cali_value = data["cali"]

                        if stringTemp.find("dbg:") != -1:
                            data = self.parseString(stringTemp, "dbg:{", "}", 4)
                            #print("data[dbg]: ", data["dbg"])
                            logger.info("data debug : {}", data["dbg"])

                            if data["dbg"] == "0":
                                self.debug = 0
                            else:
                                self.debug = 1
                            self.debug_flag = 1

                        if stringTemp.find("interval:") != -1:
                            data = self.parseString(stringTemp, "interval:{", "}", 9)
                            #print("data[interval]: ", data["interval"])
                            logger.info("data upload interval : {}", data["interval"])
                            self.interval_flag = 1
                            self.uploadinterval_value=data["interval"]

                        if stringTemp.find("threshold:") != -1:
                            data = self.parseString(stringTemp, "threshold:{", "}", 10)
                            #print("data[interval]: ", data["interval"])
                            #logger.info("data threshold : {}", data["threshold"])
                            self.writethreshold_flag = 1
                            self.threshold_chann = data["passage"]
                            self.threshold_high = data["high"]
                            self.threshold_low = data["low"]

                        if stringTemp.find("adtype:") != -1:
                            data = self.parseString(stringTemp, "adtype:{", "}", 7)
                            #print("data[channel]: ", data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1) ])
                            logger.info("data channel{}  adtype: {}", widgets.comboBox_adchannel.currentIndex() + 1,
                                        data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1) ])
                            self.adtype_flag = 1
                            self.adtype_value["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] = \
                                data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)]

                            if widgets.comboBox_adchannel.currentIndex() == 0:
                                if data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "1":
                                    widgets.comboBox_adtype.setCurrentIndex(0)
                                elif data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "2":
                                    widgets.comboBox_adtype.setCurrentIndex(1)
                            elif widgets.comboBox_adchannel.currentIndex() == 1:
                                if data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "1":
                                    widgets.comboBox_adtype.setCurrentIndex(0)
                                elif data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "2":
                                    widgets.comboBox_adtype.setCurrentIndex(1)
                            elif widgets.comboBox_adchannel.currentIndex() == 2:
                                if data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "1":
                                    widgets.comboBox_adtype.setCurrentIndex(0)
                                elif data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "2":
                                    widgets.comboBox_adtype.setCurrentIndex(1)
                            elif widgets.comboBox_adchannel.currentIndex() == 3:
                                if data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "1":
                                    widgets.comboBox_adtype.setCurrentIndex(0)
                                elif data["channel:" + str(widgets.comboBox_adchannel.currentIndex() + 1)] == "2":
                                    widgets.comboBox_adtype.setCurrentIndex(1)
                        self.buffer_string = ""
            except:
                #print("[error] have execption")
                logger.error(" serial get data have exceptions ")
                self.buffer_string = ""
                pass
    def serialport_SendData(self):
        if self.serialport.isOpen():
            pass
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)
    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            #print('Mouse click: LEFT CLICK')
            pass
        if event.buttons() == Qt.RightButton:
            #print('Mouse click: RIGHT CLICK')
            pass

class OemRsaEncrypt():
    # the invoke method example
    # oemRsaEncrypt = OemRsaEncrypt()
    # #oemRsaEncrypt.generateRSA()
    # oemRsaEncrypt.publickeyEncryptData()
    # #oemRsaEncrypt.privatekeyDecryptData()
    # oemRsaEncrypt.LocalPrivateKeyDecryptData()
    def __init__(self):
        self.encrypted_data = ""
        self.encrypted_string = "$#..password##$"
    def generateRSA(self):
        # 生成一对新的RSA秘钥
        key = RSA.generate(2048)

        # 获取私钥，并保存到一个文件中
        private_key = key.exportKey()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)
        file_out.close()

        # 获取公钥，保存到一个文件中
        public_key = key.public_key().exportKey()
        file_out = open("public.pem", "wb")
        file_out.write(public_key)
        file_out.close()

    def readPrivateKey(self):
        file_in = open("private.pem", "rb")
        private_key = RSA.import_key(file_in.read())
        file_in.close()

    def publickeyEncryptData(self):
        public_key_string = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsK3mRYFEnHlKVPQp6sfM\niKsT/qC8M/rsNP43knp93hVYj3fqN2PpELkdRTdSihlM4HfFIvBmUsWv7PmSWik3\n0uxqyOL2E6740rNko0M98SBneMACupGYStzFUQjz9EuWDuRfzwzn28KB3OBiWpmV\nyXgMCZlJBRFdoMgkVrutl3fok8AqJinKQ4FOXJarGJkdf762bhw9r5T5NNhMbOUQ\nx34wKPxoyo5bKJeGXhy8zwIQdD/w9dh9pUioSB2iezEuakDVHwJU5ZK2vZ+YLnfC\nep3MwAm9FBvFxTDcr2/PSpIuowVxDWvA0OfKusi8Ra93jXSiTIIGsWo2ptYUJ8im\nCwIDAQAB\n-----END PUBLIC KEY-----"
        public_key = RSA.import_key(public_key_string)
        # 加载公钥
        # public_key = ""
        # try:
        #     file_in = open("public.pem", "rb")
        #     #print("public key: ",file_in.read())
        #     public_key = RSA.import_key(file_in.read())
        #     file_in.close()
        # except:
        #     print("the public file not found or file not right")
        #     return False

        try:
            # 创建PKCS1_OAEP对象
            ciper = PKCS1_OAEP.new(public_key)
            # 加密数据
            self.encrypted_data = ciper.encrypt(b"$#..password##$")
        except:
            print("encrypt error")
            return False
    def privatekeyDecryptData(self):
        file_in = open("private.pem", "rb")
        print("private key: ", file_in.read())
        private_key = RSA.import_key(file_in.read())
        file_in.close()
        # 创建PKCS1_OAEP对象
        ciper = PKCS1_OAEP.new(private_key)

        # 解密数据
        decrypted_data = ciper.decrypt(self.encrypted_data)

        print("decrypted_data: ", decrypted_data)

    def LocalPrivateKeyDecryptData(self):
        # private_key_string = "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAsK3mRYFEnHlKVPQp6sfMiKsT/qC8M/rsNP43knp93hVYj3fq\nN2PpELkdRTdSihlM4HfFIvBmUsWv7PmSWik30uxqyOL2E6740rNko0M98SBneMAC\nupGYStzFUQjz9EuWDuRfzwzn28KB3OBiWpmVyXgMCZlJBRFdoMgkVrutl3fok8Aq\nJinKQ4FOXJarGJkdf762bhw9r5T5NNhMbOUQx34wKPxoyo5bKJeGXhy8zwIQdD/w\n9dh9pUioSB2iezEuakDVHwJU5ZK2vZ+YLnfCep3MwAm9FBvFxTDcr2/PSpIuowVx\nDWvA0OfKusi8Ra93jXSiTIIGsWo2ptYUJ8imCwIDAQABAoIBABaFzKWOoZL66U1k\nJNXPq5S+jll23xcXRTZKNAZhxBrkCLqdVEfEXkkp9//DWivNpt20lvZpw/mIRvGE\nLTJ+L6YdSk2alTkUJJcjlFA1ubc75MThYVesSMg+VY8Lf6HkYtg6J7aK1CHRLWHd\nXtxi2NPqkEpG9qaFPLTK3ssJuMrmoVKGefy+Y9b9Usk6tCx/jR2ZE9/C/kVGOZDa\nflPTqkMpDMnOkafF8dfVYtpyNYLj8Ocemqw/rvRbY3f8KeupELgEXAffwhKikh9V\nEEvqoGGe7UGEITlhAOZFkN1RaduzI8QtoOTEeT0vFEFUgVM0cDHxfs2OqDKbzT6E\nDbW5+HUCgYEAwZgNExgXkg+fjeg+5oRQawjHItiAMXdUgl3aQnaBs/W78oL4npgh\nysX/5sGbaZLL0/5c/X3FM0EqLkHypWM91P14KxL1BZPBZQSzVlccBtm5j5QxWG4J\nB9kipMFFaAFt6SPnL7PnZZtJkAKqyPRyCYsUye3QJ1dS3CLxa2wPHi0CgYEA6aIA\nM2B8ruYXeXCLJHe74Kc4+6pbvoDEQtZwX+dngwkWxNDD1z1zwufRQXP+i7C67FBl\nR09+hEHxSOiYG7nNjk+Qa0jmA0y2GeFF3cO4FEyhqER0VtBCsDdzn+Mv7dESBmzb\n0iMZwIH0C20BS5dLkvuQ5VCKE2eilK38hb8msBcCgYBH9KMPcMn6ARKV5TfT6GQX\nlHiny/7B5A+mMQoZ4ABPikukVOfh0rvkqXl3JIkGUYivMAESOzgb1+G8tchhjqSB\n0QBkSjSGMSgVywx5UAFbzns5EaTRsHxszVkiEbAhez6GBFE+msisLG7INyWRccId\nJ/O/JkRTCxMCPX6sJcrstQKBgDefhTK2Lxko2L/l5oq5IvbaeTuZlJwnZhKPoVOD\n8WYGHPCgz2+IRu5JaM2PgzPY0LgAcAxpRbLRTFPSZJx9QQ43rSeNxI1WjyhcNNkW\nhtX2ZKp+GcCtdqMjoJiZa0jQdN0ov7EpADGP/v1VZ3CKxchpslaWNTlnfBKv1aY2\nG0zjAoGBAICiC+FKkQRWzcB6GKekz6Ewpol5rhIKg0JFU1FTdZzFrBMFf/HuUjdA\nRTbpf4t/4f+X8B8f6ckGU5LtpPNsNPOaRwOJadGFoeLcSXl3xzbtf/aXEFkdmtWh\ngfJ7rFeOnGkr2GqfnmTnmjorvHhgI6yIsVvWfG2JCVnSeedIcuEy\n-----END RSA PRIVATE KEY-----"
        # private_key = RSA.import_key(private_key_string)

        # 加载私钥
        private_key = ""
        try:
            file_in = open("private.pem", "rb")
            #print("public key: ",file_in.read())
            private_key = RSA.import_key(file_in.read())
            file_in.close()
        except:
            print("the private file not found or file not right")
            return False

    # 创建PKCS1_OAEP对象
        try:
            ciper = PKCS1_OAEP.new(private_key)
            # 解密数据
            decrypted_data = ciper.decrypt(self.encrypted_data)
            print("decrypted_data: ", decrypted_data)

            if decrypted_data.decode('utf-8') == self.encrypted_string:
                print("decrpyt ok.")
                return True
            else:
                print("decrpyt data not equal: ", decrypted_data)
                return False
        except:
            print("Incorrect decryption.")
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
