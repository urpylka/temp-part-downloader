# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ruleswindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RulesWindow(object):
    def setupUi(self, RulesWindow):
        RulesWindow.setObjectName("RulesWindow")
        RulesWindow.resize(800, 450)
        RulesWindow.setMinimumSize(QtCore.QSize(800, 450))
        self.centralwidget = QtWidgets.QWidget(RulesWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(50000, 50000))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setAutoRepeat(False)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_18.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_18.addWidget(self.checkBox_2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_18.addWidget(self.checkBox_5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_18.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_18.addWidget(self.checkBox_4)
        self.horizontalLayout_9.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_10.addWidget(self.checkBox_6)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(6, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setEnabled(False)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_14.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_14.addWidget(self.radioButton_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_14)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_9.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_11.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_11.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setEnabled(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.horizontalLayout_9.addWidget(self.groupBox_6)
        self.verticalLayout_16.addLayout(self.horizontalLayout_9)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout_10.addWidget(self.checkBox_8)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_7)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_10.addWidget(self.checkBox_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setEnabled(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox_4.setEnabled(False)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_10.addWidget(self.spinBox_4)
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        self.label_10.setEnabled(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox_5.setEnabled(False)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_10.addWidget(self.spinBox_5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.verticalLayout_16.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayout_12.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_10.setObjectName("checkBox_10")
        self.horizontalLayout_12.addWidget(self.checkBox_10)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_12.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.verticalLayout_16.addWidget(self.groupBox_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_7.addWidget(self.plainTextEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setEnabled(False)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_7.addWidget(self.plainTextEdit_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_6.addWidget(self.spinBox_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_6.addWidget(self.comboBox_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_7.addWidget(self.spinBox_2)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addWidget(self.groupBox)
        spacerItem3 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_8.addWidget(self.spinBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_8.addWidget(self.comboBox_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_17.addWidget(self.label_11)
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_6.setObjectName("spinBox_6")
        self.verticalLayout_17.addWidget(self.spinBox_6)
        self.verticalLayout_4.addWidget(self.groupBox_9)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_15.addWidget(self.lineEdit_4)
        self.verticalLayout_4.addWidget(self.groupBox_10)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setObjectName("groupBox_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_11)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_13.addWidget(self.comboBox_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_13.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addWidget(self.groupBox_11)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem8 = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        RulesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RulesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        RulesWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RulesWindow)
        self.statusbar.setObjectName("statusbar")
        RulesWindow.setStatusBar(self.statusbar)
        self.label_9.setBuddy(self.label_9)
        self.label_10.setBuddy(self.label_10)

        self.retranslateUi(RulesWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RulesWindow)

    def retranslateUi(self, RulesWindow):
        _translate = QtCore.QCoreApplication.translate
        RulesWindow.setWindowTitle(_translate("RulesWindow", "Rules"))
        self.groupBox_4.setTitle(_translate("RulesWindow", "Comparison"))
        self.checkBox.setText(_translate("RulesWindow", "Name"))
        self.checkBox_2.setText(_translate("RulesWindow", "Size"))
        self.checkBox_5.setText(_translate("RulesWindow", "Hashsum (for works needs download files)"))
        self.checkBox_3.setText(_translate("RulesWindow", "Time created"))
        self.checkBox_4.setText(_translate("RulesWindow", "Time modified"))
        self.groupBox_5.setTitle(_translate("RulesWindow", "Links"))
        self.checkBox_6.setText(_translate("RulesWindow", "Include symbolic links:"))
        self.radioButton.setText(_translate("RulesWindow", "Follow"))
        self.radioButton_2.setText(_translate("RulesWindow", "Direct"))
        self.groupBox_6.setTitle(_translate("RulesWindow", "Time shift"))
        self.label_7.setText(_translate("RulesWindow", "Ignore time shift [hh:mm]"))
        self.label_8.setText(_translate("RulesWindow", "Example: 1, 2, 4:30"))
        self.groupBox_7.setTitle(_translate("RulesWindow", "Errors"))
        self.checkBox_8.setText(_translate("RulesWindow", "Ignore errors"))
        self.checkBox_7.setText(_translate("RulesWindow", "Automatic retry"))
        self.label_9.setText(_translate("RulesWindow", "Retry count"))
        self.label_10.setText(_translate("RulesWindow", "Delay (in seconds)"))
        self.groupBox_8.setTitle(_translate("RulesWindow", "Logging"))
        self.checkBox_9.setText(_translate("RulesWindow", "Console"))
        self.checkBox_10.setText(_translate("RulesWindow", "File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RulesWindow", "Comparison"))
        self.groupBox_2.setTitle(_translate("RulesWindow", "By name"))
        self.label.setText(_translate("RulesWindow", "Include:"))
        self.label_2.setText(_translate("RulesWindow", "Exclude:"))
        self.label_3.setText(_translate("RulesWindow", "exclude list is priority then include"))
        self.groupBox.setTitle(_translate("RulesWindow", "By size"))
        self.label_6.setText(_translate("RulesWindow", "Min"))
        self.label_5.setText(_translate("RulesWindow", "Max"))
        self.groupBox_3.setTitle(_translate("RulesWindow", "By time"))
        self.label_4.setText(_translate("RulesWindow", "Time span"))
        self.pushButton_3.setText(_translate("RulesWindow", "Reset all filters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RulesWindow", "Filter"))
        self.groupBox_9.setTitle(_translate("RulesWindow", "Parallel"))
        self.label_11.setText(_translate("RulesWindow", "Parallel file operations"))
        self.groupBox_10.setTitle(_translate("RulesWindow", "Database"))
        self.groupBox_11.setTitle(_translate("RulesWindow", "Logging"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("RulesWindow", "Synchronization"))
        self.pushButton.setText(_translate("RulesWindow", "Save"))
        self.pushButton_2.setText(_translate("RulesWindow", "Cancel"))

