# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kelmo\Desktop\OLD DESKTOP\-Python\CODE\elmocut\exe\ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 510))
        MainWindow.setToolTip("")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 365, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chkMinimized = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkMinimized.setFont(font)
        self.chkMinimized.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkMinimized.setObjectName("chkMinimized")
        self.gridLayout_3.addWidget(self.chkMinimized, 0, 1, 1, 1)
        self.chkRemember = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkRemember.setFont(font)
        self.chkRemember.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkRemember.setObjectName("chkRemember")
        self.gridLayout_3.addWidget(self.chkRemember, 1, 0, 1, 1)
        self.chkAutoupdate = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkAutoupdate.setFont(font)
        self.chkAutoupdate.setChecked(False)
        self.chkAutoupdate.setObjectName("chkAutoupdate")
        self.gridLayout_3.addWidget(self.chkAutoupdate, 1, 1, 1, 1)
        self.chkAutostart = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkAutostart.setFont(font)
        self.chkAutostart.setObjectName("chkAutostart")
        self.gridLayout_3.addWidget(self.chkAutostart, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 3, 0, 1, 4)
        self.btnUpdate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUpdate.sizePolicy().hasHeightForWidth())
        self.btnUpdate.setSizePolicy(sizePolicy)
        self.btnUpdate.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setObjectName("btnUpdate")
        self.gridLayout.addWidget(self.btnUpdate, 5, 0, 1, 4)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 361, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rdbLight = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdbLight.sizePolicy().hasHeightForWidth())
        self.rdbLight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbLight.setFont(font)
        self.rdbLight.setObjectName("rdbLight")
        self.horizontalLayout_2.addWidget(self.rdbLight)
        self.rdbDark = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rdbDark.sizePolicy().hasHeightForWidth())
        self.rdbDark.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rdbDark.setFont(font)
        self.rdbDark.setChecked(True)
        self.rdbDark.setObjectName("rdbDark")
        self.horizontalLayout_2.addWidget(self.rdbDark)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 4)
        self.btnDefaults = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDefaults.sizePolicy().hasHeightForWidth())
        self.btnDefaults.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnDefaults.setFont(font)
        self.btnDefaults.setObjectName("btnDefaults")
        self.gridLayout.addWidget(self.btnDefaults, 4, 0, 1, 2)
        self.btnApply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnApply.sizePolicy().hasHeightForWidth())
        self.btnApply.setSizePolicy(sizePolicy)
        self.btnApply.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnApply.setFont(font)
        self.btnApply.setObjectName("btnApply")
        self.gridLayout.addWidget(self.btnApply, 4, 2, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 78))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboInterface = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.comboInterface.sizePolicy().hasHeightForWidth())
        self.comboInterface.setSizePolicy(sizePolicy)
        self.comboInterface.setMinimumSize(QtCore.QSize(0, 9))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboInterface.setFont(font)
        self.comboInterface.setObjectName("comboInterface")
        self.horizontalLayout_3.addWidget(self.comboInterface)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 4)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 115))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinCount = QtWidgets.QSpinBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinCount.sizePolicy().hasHeightForWidth())
        self.spinCount.setSizePolicy(sizePolicy)
        self.spinCount.setMinimumSize(QtCore.QSize(55, 0))
        self.spinCount.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinCount.setFont(font)
        self.spinCount.setMinimum(25)
        self.spinCount.setMaximum(255)
        self.spinCount.setObjectName("spinCount")
        self.gridLayout_2.addWidget(self.spinCount, 0, 2, 1, 1)
        self.sliderCount = QtWidgets.QSlider(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderCount.sizePolicy().hasHeightForWidth())
        self.sliderCount.setSizePolicy(sizePolicy)
        self.sliderCount.setMinimumSize(QtCore.QSize(179, 0))
        self.sliderCount.setMinimum(25)
        self.sliderCount.setMaximum(255)
        self.sliderCount.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCount.setObjectName("sliderCount")
        self.gridLayout_2.addWidget(self.sliderCount, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(90, 0))
        self.label.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 70, 361, 31))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.spinThreads = QtWidgets.QSpinBox(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinThreads.sizePolicy().hasHeightForWidth())
        self.spinThreads.setSizePolicy(sizePolicy)
        self.spinThreads.setMinimumSize(QtCore.QSize(55, 0))
        self.spinThreads.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinThreads.setFont(font)
        self.spinThreads.setMinimum(5)
        self.spinThreads.setMaximum(255)
        self.spinThreads.setProperty("value", 5)
        self.spinThreads.setObjectName("spinThreads")
        self.gridLayout_4.addWidget(self.spinThreads, 0, 2, 1, 1)
        self.sliderThreads = QtWidgets.QSlider(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderThreads.sizePolicy().hasHeightForWidth())
        self.sliderThreads.setSizePolicy(sizePolicy)
        self.sliderThreads.setMinimumSize(QtCore.QSize(179, 0))
        self.sliderThreads.setMinimum(5)
        self.sliderThreads.setMaximum(255)
        self.sliderThreads.setProperty("value", 5)
        self.sliderThreads.setOrientation(QtCore.Qt.Horizontal)
        self.sliderThreads.setObjectName("sliderThreads")
        self.gridLayout_4.addWidget(self.sliderThreads, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setMinimumSize(QtCore.QSize(90, 0))
        self.label_2.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 4)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Misc."))
        self.chkMinimized.setText(_translate("MainWindow", "Minimize on exit"))
        self.chkRemember.setText(_translate("MainWindow", "Remember killed devices"))
        self.chkAutoupdate.setText(_translate("MainWindow", "Check updates on start"))
        self.chkAutostart.setText(_translate("MainWindow", "Start with Windows"))
        self.btnUpdate.setText(_translate("MainWindow", "Check for update"))
        self.groupBox.setTitle(_translate("MainWindow", "Theme"))
        self.rdbLight.setText(_translate("MainWindow", "Light"))
        self.rdbDark.setText(_translate("MainWindow", "Dark"))
        self.btnDefaults.setText(_translate("MainWindow", "Defaults"))
        self.btnApply.setText(_translate("MainWindow", "Apply"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Network Interface"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Performance"))
        self.label.setText(_translate("MainWindow", "Device Count"))
        self.label_2.setText(_translate("MainWindow", "Max Threads"))
