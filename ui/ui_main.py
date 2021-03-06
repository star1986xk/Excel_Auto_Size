# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 138)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{background-color: rgb(255, 255, 255);}\n"
"\n"
"QPushButton{\n"
"border-style:none;\n"
"text-align: left;\n"
"background-color:#20b1ff;\n"
"border:2px;\n"
"border-radius:2px;\n"
"padding:2px 4px;\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{color:lightskyblue}\n"
"QPushButton:pressed {\n"
"    /* 改变背景色 */\n"
"    /* background-color:rgb(180, 180, 180,120); */\n"
"    /* 改变边框风格 */\n"
"    /* border-style:inset; */\n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:6px;\n"
"    padding-top:4px;\n"
"}\n"
"#pushButton_run{\n"
"text-align: center;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border: 1px solid #20b1ff;\n"
"border-radius:2px;\n"
"background-color:#f0f0f0;\n"
"}\n"
"\n"
"#lineEdit_domain,#lineEdit_random{\n"
"background-color:#ffffff;\n"
"}\n"
"\n"
"QComboBox{\n"
"border: 1px solid #20b1ff;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol- position :  top  right ;\n"
"     width :  20px ;\n"
"     border-left-width :  1px ;\n"
"     border-left-color : darkgray;\n"
"     border-left-style :  solid ; \n"
"     border-top-right-radius:  3px ;\n"
"     border-bottom-right-radius:  3px ;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_excel = QtWidgets.QPushButton(self.widget)
        self.pushButton_excel.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_excel.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_excel.setFont(font)
        self.pushButton_excel.setObjectName("pushButton_excel")
        self.horizontalLayout.addWidget(self.pushButton_excel)
        self.lineEdit_excel = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_excel.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_excel.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_excel.setFont(font)
        self.lineEdit_excel.setText("")
        self.lineEdit_excel.setReadOnly(True)
        self.lineEdit_excel.setObjectName("lineEdit_excel")
        self.horizontalLayout.addWidget(self.lineEdit_excel)
        self.verticalLayout.addWidget(self.widget)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_run = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_run.setMinimumSize(QtCore.QSize(80, 25))
        self.pushButton_run.setMaximumSize(QtCore.QSize(80, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.horizontalLayout_4.addWidget(self.pushButton_run)
        self.verticalLayout.addWidget(self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动填size"))
        self.pushButton_excel.setText(_translate("MainWindow", "导入Excel"))
        self.pushButton_run.setText(_translate("MainWindow", "生成"))
import img_rc
