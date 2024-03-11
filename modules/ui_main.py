# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainVSMAES.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1377, 869)
        MainWindow.setMinimumSize(QSize(240, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_bak.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/guide.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setMaximumSize(QSize(16777215, 120))
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.row_1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.row_1)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";")
        self.groupBox.setTitle(u"\u4e32\u53e3\u914d\u7f6e")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(120, 16777215))
        self.label_12.setMargin(18)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.combox_serialPortNames = QComboBox(self.groupBox)
        self.combox_serialPortNames.setObjectName(u"combox_serialPortNames")
        self.combox_serialPortNames.setMaximumSize(QSize(160, 16777215))
        self.combox_serialPortNames.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.combox_serialPortNames)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(150, 16777215))
        self.label_13.setMargin(50)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.combox_serialBaudrate = QComboBox(self.groupBox)
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.addItem("")
        self.combox_serialBaudrate.setObjectName(u"combox_serialBaudrate")
        self.combox_serialBaudrate.setMaximumSize(QSize(160, 16777215))
        self.combox_serialBaudrate.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_6.addWidget(self.combox_serialBaudrate)

        self.btn_openserialport = QPushButton(self.groupBox)
        self.btn_openserialport.setObjectName(u"btn_openserialport")
        self.btn_openserialport.setMinimumSize(QSize(0, 30))
        self.btn_openserialport.setMaximumSize(QSize(150, 16777215))
        self.btn_openserialport.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.btn_openserialport)

        self.horizontalSpacer = QSpacerItem(188, 76, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_7.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.groupBox_2 = QGroupBox(self.row_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_10 = QWidget(self.groupBox_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_getsn = QPushButton(self.widget_10)
        self.pushButton_getsn.setObjectName(u"pushButton_getsn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_getsn.sizePolicy().hasHeightForWidth())
        self.pushButton_getsn.setSizePolicy(sizePolicy5)
        self.pushButton_getsn.setMinimumSize(QSize(400, 40))
        self.pushButton_getsn.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton_getsn)

        self.label_getsn = QLabel(self.widget_10)
        self.label_getsn.setObjectName(u"label_getsn")
        self.label_getsn.setStyleSheet(u"")
        self.label_getsn.setMargin(2)

        self.horizontalLayout_9.addWidget(self.label_getsn)


        self.verticalLayout_4.addWidget(self.widget_10)

        self.widget_7 = QWidget(self.groupBox_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(10, 10))
        self.widget_7.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_geticcid = QPushButton(self.widget_7)
        self.pushButton_geticcid.setObjectName(u"pushButton_geticcid")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_geticcid.sizePolicy().hasHeightForWidth())
        self.pushButton_geticcid.setSizePolicy(sizePolicy6)
        self.pushButton_geticcid.setMinimumSize(QSize(400, 40))
        self.pushButton_geticcid.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.pushButton_geticcid)

        self.label_geticcid = QLabel(self.widget_7)
        self.label_geticcid.setObjectName(u"label_geticcid")
        self.label_geticcid.setStyleSheet(u"")
        self.label_geticcid.setMargin(2)
        self.label_geticcid.setIndent(-1)

        self.horizontalLayout_14.addWidget(self.label_geticcid)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.groupBox_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_getdevinfo = QPushButton(self.widget_9)
        self.pushButton_getdevinfo.setObjectName(u"pushButton_getdevinfo")
        sizePolicy6.setHeightForWidth(self.pushButton_getdevinfo.sizePolicy().hasHeightForWidth())
        self.pushButton_getdevinfo.setSizePolicy(sizePolicy6)
        self.pushButton_getdevinfo.setMinimumSize(QSize(400, 40))
        self.pushButton_getdevinfo.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_getdevinfo)

        self.label_getdevinfo = QLabel(self.widget_9)
        self.label_getdevinfo.setObjectName(u"label_getdevinfo")
        self.label_getdevinfo.setStyleSheet(u"")
        self.label_getdevinfo.setMargin(2)

        self.horizontalLayout_11.addWidget(self.label_getdevinfo)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.groupBox_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pushButton_getnetinfo = QPushButton(self.widget_8)
        self.pushButton_getnetinfo.setObjectName(u"pushButton_getnetinfo")
        sizePolicy6.setHeightForWidth(self.pushButton_getnetinfo.sizePolicy().hasHeightForWidth())
        self.pushButton_getnetinfo.setSizePolicy(sizePolicy6)
        self.pushButton_getnetinfo.setMinimumSize(QSize(400, 40))
        self.pushButton_getnetinfo.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.horizontalLayout_13.addWidget(self.pushButton_getnetinfo)

        self.label_getnetinfo = QLabel(self.widget_8)
        self.label_getnetinfo.setObjectName(u"label_getnetinfo")
        self.label_getnetinfo.setStyleSheet(u"")
        self.label_getnetinfo.setMargin(2)

        self.horizontalLayout_13.addWidget(self.label_getnetinfo)


        self.verticalLayout_4.addWidget(self.widget_8)


        self.verticalLayout_19.addWidget(self.groupBox_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.row_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei UI"])
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setItalic(False)
        self.groupBox_3.setFont(font5)
        self.groupBox_3.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_2 = QWidget(self.groupBox_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)
        self.verticalLayout_23 = QVBoxLayout(self.widget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_23.addWidget(self.label_4)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_23.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_23.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_23.addWidget(self.label_5)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_23.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.verticalLayout_23.addWidget(self.label_9)


        self.horizontalLayout_8.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.groupBox_3)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy8)
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox_adtype = QComboBox(self.widget_3)
        self.comboBox_adtype.addItem("")
        self.comboBox_adtype.addItem("")
        self.comboBox_adtype.setObjectName(u"comboBox_adtype")
        self.comboBox_adtype.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.gridLayout_4.addWidget(self.comboBox_adtype, 6, 3, 1, 1)

        self.comboBox_threshold_channel = QComboBox(self.widget_3)
        self.comboBox_threshold_channel.addItem("")
        self.comboBox_threshold_channel.addItem("")
        self.comboBox_threshold_channel.addItem("")
        self.comboBox_threshold_channel.addItem("")
        self.comboBox_threshold_channel.setObjectName(u"comboBox_threshold_channel")
        self.comboBox_threshold_channel.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.gridLayout_4.addWidget(self.comboBox_threshold_channel, 5, 0, 1, 1)

        self.lineEdit_ip = QLineEdit(self.widget_3)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")
        self.lineEdit_ip.setMinimumSize(QSize(120, 30))
        self.lineEdit_ip.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_ip, 1, 0, 1, 2)

        self.lineEdit_sn = QLineEdit(self.widget_3)
        self.lineEdit_sn.setObjectName(u"lineEdit_sn")
        self.lineEdit_sn.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_sn, 3, 0, 1, 4)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.gridLayout_4.addWidget(self.label_7, 2, 3, 1, 1)

        self.pushButton_opendebugmode = QPushButton(self.widget_3)
        self.pushButton_opendebugmode.setObjectName(u"pushButton_opendebugmode")
        sizePolicy.setHeightForWidth(self.pushButton_opendebugmode.sizePolicy().hasHeightForWidth())
        self.pushButton_opendebugmode.setSizePolicy(sizePolicy)
        self.pushButton_opendebugmode.setMinimumSize(QSize(0, 30))
        self.pushButton_opendebugmode.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")
        self.pushButton_opendebugmode.setFlat(False)

        self.gridLayout_4.addWidget(self.pushButton_opendebugmode, 0, 0, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 0))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")
        self.label_6.setMargin(10)

        self.gridLayout_4.addWidget(self.label_6, 1, 2, 1, 1)

        self.comboBox_adchannel = QComboBox(self.widget_3)
        self.comboBox_adchannel.addItem("")
        self.comboBox_adchannel.addItem("")
        self.comboBox_adchannel.addItem("")
        self.comboBox_adchannel.addItem("")
        self.comboBox_adchannel.setObjectName(u"comboBox_adchannel")
        self.comboBox_adchannel.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.gridLayout_4.addWidget(self.comboBox_adchannel, 6, 0, 1, 1)

        self.lineEdit_port = QLineEdit(self.widget_3)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setEnabled(True)
        self.lineEdit_port.setMinimumSize(QSize(0, 30))
        self.lineEdit_port.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_port, 1, 3, 1, 1)

        self.lineEdit_uploadinterval = QLineEdit(self.widget_3)
        self.lineEdit_uploadinterval.setObjectName(u"lineEdit_uploadinterval")
        self.lineEdit_uploadinterval.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.lineEdit_uploadinterval, 2, 0, 1, 3)

        self.lineEdit_threshold = QLineEdit(self.widget_3)
        self.lineEdit_threshold.setObjectName(u"lineEdit_threshold")

        self.gridLayout_4.addWidget(self.lineEdit_threshold, 5, 3, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.gridLayout_4.addWidget(self.label_10, 5, 1, 1, 2)


        self.horizontalLayout_8.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.groupBox_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy7.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy7)
        self.widget_4.setMinimumSize(QSize(150, 0))
        self.verticalLayout_24 = QVBoxLayout(self.widget_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setStyleSheet(u"background:transparent;border:none;")
        self.pushButton_6.setFlat(True)

        self.verticalLayout_24.addWidget(self.pushButton_6)

        self.pushButton_writeipport = QPushButton(self.widget_4)
        self.pushButton_writeipport.setObjectName(u"pushButton_writeipport")
        self.pushButton_writeipport.setMinimumSize(QSize(0, 30))
        self.pushButton_writeipport.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.pushButton_writeipport)

        self.pushButton_writeuploadinterval = QPushButton(self.widget_4)
        self.pushButton_writeuploadinterval.setObjectName(u"pushButton_writeuploadinterval")
        self.pushButton_writeuploadinterval.setMinimumSize(QSize(0, 30))
        self.pushButton_writeuploadinterval.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.pushButton_writeuploadinterval)

        self.pushButton_writesn = QPushButton(self.widget_4)
        self.pushButton_writesn.setObjectName(u"pushButton_writesn")
        self.pushButton_writesn.setMinimumSize(QSize(0, 30))
        self.pushButton_writesn.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.pushButton_writesn)

        self.pushButton_writeThreshold = QPushButton(self.widget_4)
        self.pushButton_writeThreshold.setObjectName(u"pushButton_writeThreshold")
        self.pushButton_writeThreshold.setMinimumSize(QSize(0, 30))
        self.pushButton_writeThreshold.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.pushButton_writeThreshold)

        self.pushButton_writeAdType = QPushButton(self.widget_4)
        self.pushButton_writeAdType.setObjectName(u"pushButton_writeAdType")
        self.pushButton_writeAdType.setMinimumSize(QSize(0, 30))
        self.pushButton_writeAdType.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_24.addWidget(self.pushButton_writeAdType)


        self.horizontalLayout_8.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.groupBox_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy7.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy7)
        self.widget_5.setMinimumSize(QSize(150, 0))
        self.verticalLayout_25 = QVBoxLayout(self.widget_5)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_readipport = QPushButton(self.widget_5)
        self.pushButton_readipport.setObjectName(u"pushButton_readipport")
        self.pushButton_readipport.setMinimumSize(QSize(0, 30))
        self.pushButton_readipport.setStyleSheet(u"background:transparent;border:none;\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_readipport)

        self.pushButton_readipport_duplicate = QPushButton(self.widget_5)
        self.pushButton_readipport_duplicate.setObjectName(u"pushButton_readipport_duplicate")
        self.pushButton_readipport_duplicate.setMinimumSize(QSize(0, 30))
        self.pushButton_readipport_duplicate.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_readipport_duplicate)

        self.pushButton_readuploadinterval = QPushButton(self.widget_5)
        self.pushButton_readuploadinterval.setObjectName(u"pushButton_readuploadinterval")
        self.pushButton_readuploadinterval.setMinimumSize(QSize(0, 30))
        self.pushButton_readuploadinterval.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_readuploadinterval)

        self.pushButton_readsn_duplicate = QPushButton(self.widget_5)
        self.pushButton_readsn_duplicate.setObjectName(u"pushButton_readsn_duplicate")
        self.pushButton_readsn_duplicate.setMinimumSize(QSize(0, 30))
        self.pushButton_readsn_duplicate.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")
        self.pushButton_readsn_duplicate.setFlat(True)

        self.verticalLayout_25.addWidget(self.pushButton_readsn_duplicate)

        self.pushButton_getthreshold = QPushButton(self.widget_5)
        self.pushButton_getthreshold.setObjectName(u"pushButton_getthreshold")
        self.pushButton_getthreshold.setMinimumSize(QSize(0, 30))
        self.pushButton_getthreshold.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_getthreshold)

        self.pushButton_getAdType = QPushButton(self.widget_5)
        self.pushButton_getAdType.setObjectName(u"pushButton_getAdType")
        self.pushButton_getAdType.setMinimumSize(QSize(0, 30))
        self.pushButton_getAdType.setStyleSheet(u"QPushButton\n"
"{\n"
"  background-color:#3c8dbc;\n"
"	font: 11pt \"Microsoft YaHei UI\";\n"
"  border-color:#367fa9\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: #00a65a;\n"
"  border-width: 1px;\n"
"  border-radius: 3px;\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_getAdType)


        self.horizontalLayout_8.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.groupBox_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_26 = QVBoxLayout(self.widget_6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_debug = QLabel(self.widget_6)
        self.label_debug.setObjectName(u"label_debug")

        self.verticalLayout_26.addWidget(self.label_debug)

        self.label_getipport = QLabel(self.widget_6)
        self.label_getipport.setObjectName(u"label_getipport")
        self.label_getipport.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.label_getipport)

        self.label_getuploadinterval = QLabel(self.widget_6)
        self.label_getuploadinterval.setObjectName(u"label_getuploadinterval")
        self.label_getuploadinterval.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.label_getuploadinterval)

        self.label_getsn_2 = QLabel(self.widget_6)
        self.label_getsn_2.setObjectName(u"label_getsn_2")
        self.label_getsn_2.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.label_getsn_2)

        self.label_threshold = QLabel(self.widget_6)
        self.label_threshold.setObjectName(u"label_threshold")

        self.verticalLayout_26.addWidget(self.label_threshold)

        self.label_getAdType = QLabel(self.widget_6)
        self.label_getAdType.setObjectName(u"label_getAdType")

        self.verticalLayout_26.addWidget(self.label_getAdType)


        self.horizontalLayout_8.addWidget(self.widget_6)


        self.horizontalLayout_12.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 30))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.combox_serialBaudrate.setCurrentIndex(7)
        self.comboBox_threshold_channel.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u914d\u7f6e\u5de5\u5177", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4e32\u53e3:</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.combox_serialBaudrate.setItemText(0, QCoreApplication.translate("MainWindow", u"1200", None))
        self.combox_serialBaudrate.setItemText(1, QCoreApplication.translate("MainWindow", u"2400", None))
        self.combox_serialBaudrate.setItemText(2, QCoreApplication.translate("MainWindow", u"4800", None))
        self.combox_serialBaudrate.setItemText(3, QCoreApplication.translate("MainWindow", u"9600", None))
        self.combox_serialBaudrate.setItemText(4, QCoreApplication.translate("MainWindow", u"19200", None))
        self.combox_serialBaudrate.setItemText(5, QCoreApplication.translate("MainWindow", u"38400", None))
        self.combox_serialBaudrate.setItemText(6, QCoreApplication.translate("MainWindow", u"57600", None))
        self.combox_serialBaudrate.setItemText(7, QCoreApplication.translate("MainWindow", u"115200", None))
        self.combox_serialBaudrate.setItemText(8, QCoreApplication.translate("MainWindow", u"460800", None))
        self.combox_serialBaudrate.setItemText(9, QCoreApplication.translate("MainWindow", u"921600", None))
        self.combox_serialBaudrate.setItemText(10, QCoreApplication.translate("MainWindow", u"230400", None))

        self.btn_openserialport.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u4e32\u53e3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u67e5\u8be2", None))
        self.pushButton_getsn.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8bbe\u5907SN", None))
        self.label_getsn.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_geticcid.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5361\u53f7ICCID", None))
        self.label_geticcid.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_getdevinfo.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8bbe\u5907\u4fe1\u606f", None))
        self.label_getdevinfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_getnetinfo.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u7f51\u7edc\u914d\u7f6e", None))
        self.label_getnetinfo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u914d\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8c03\u8bd5\u6a21\u5f0f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4e0a\u62a5\u95f4\u9694", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SN", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u7c7b\u578b", None))
        self.comboBox_adtype.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6db2\u4f4d\u4f20\u611f\u5668", None))
        self.comboBox_adtype.setItemText(1, QCoreApplication.translate("MainWindow", u"\u538b\u529b\u4f20\u611f\u5668", None))

        self.comboBox_threshold_channel.setItemText(0, QCoreApplication.translate("MainWindow", u"\u901a\u90531", None))
        self.comboBox_threshold_channel.setItemText(1, QCoreApplication.translate("MainWindow", u"\u901a\u90532", None))
        self.comboBox_threshold_channel.setItemText(2, QCoreApplication.translate("MainWindow", u"\u901a\u90533", None))
        self.comboBox_threshold_channel.setItemText(3, QCoreApplication.translate("MainWindow", u"\u901a\u90534", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949f", None))
        self.pushButton_opendebugmode.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3:", None))
        self.comboBox_adchannel.setItemText(0, QCoreApplication.translate("MainWindow", u"\u901a\u90531", None))
        self.comboBox_adchannel.setItemText(1, QCoreApplication.translate("MainWindow", u"\u901a\u90532", None))
        self.comboBox_adchannel.setItemText(2, QCoreApplication.translate("MainWindow", u"\u901a\u90533", None))
        self.comboBox_adchannel.setItemText(3, QCoreApplication.translate("MainWindow", u"\u901a\u90534", None))

#if QT_CONFIG(tooltip)
        self.lineEdit_threshold.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_threshold.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_threshold.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.00:4.00", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4f4e: \u9ad8", None))
        self.pushButton_6.setText("")
        self.pushButton_writeipport.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.pushButton_writeuploadinterval.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.pushButton_writesn.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.pushButton_writeThreshold.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.pushButton_writeAdType.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.pushButton_readipport.setText("")
        self.pushButton_readipport_duplicate.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.pushButton_readuploadinterval.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.pushButton_readsn_duplicate.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.pushButton_getthreshold.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.pushButton_getAdType.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.label_debug.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_getipport.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_getuploadinterval.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_getsn_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_threshold.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_getAdType.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>authored by: wit_yuan</p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"0.4.0", None))
    # retranslateUi

