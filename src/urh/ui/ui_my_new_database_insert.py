# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'bd_insert.ui'
# #
# # Created by: PyQt5 UI code generator 5.10.1
# #
# # WARNING! All changes made in this file will be lost!
#
# from PyQt5 import QtCore, QtGui, QtWidgets
#
# class Ui_MainWindow1(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1081, 596)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setMaximumSize(QtCore.QSize(1081, 561))
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
#         self.gridLayout_2.setObjectName("gridLayout_2")
#         self.gridLayout = QtWidgets.QGridLayout()
#         self.gridLayout.setObjectName("gridLayout")
#         self.line_8 = QtWidgets.QFrame(self.centralwidget)
#         self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_8.setObjectName("line_8")
#         self.gridLayout.addWidget(self.line_8, 14, 1, 1, 3)
#         self.line_5 = QtWidgets.QFrame(self.centralwidget)
#         self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_5.setObjectName("line_5")
#         self.gridLayout.addWidget(self.line_5, 8, 1, 1, 3)
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setObjectName("pushButton")
#         self.gridLayout.addWidget(self.pushButton, 15, 5, 1, 1)
#         self.lineEdit_pulse = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_pulse.setObjectName("lineEdit_pulse")
#         self.gridLayout.addWidget(self.lineEdit_pulse, 5, 2, 1, 2)
#         self.lineEdit_period = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_period.setObjectName("lineEdit_period")
#         self.gridLayout.addWidget(self.lineEdit_period, 7, 2, 1, 2)
#         self.label_7 = QtWidgets.QLabel(self.centralwidget)
#         self.label_7.setObjectName("label_7")
#         self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
#         self.lineEdit_modulation = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_modulation.setObjectName("lineEdit_modulation")
#         self.gridLayout.addWidget(self.lineEdit_modulation, 9, 2, 1, 2)
#         self.lineEdit_bandwidth = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_bandwidth.setObjectName("lineEdit_bandwidth")
#         self.gridLayout.addWidget(self.lineEdit_bandwidth, 11, 2, 1, 2)
#         self.lineEdit_freq = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_freq.setObjectName("lineEdit_freq")
#         self.gridLayout.addWidget(self.lineEdit_freq, 3, 2, 1, 2)
#         self.lineEdit_comment = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_comment.setObjectName("lineEdit_comment")
#         self.gridLayout.addWidget(self.lineEdit_comment, 13, 2, 1, 2)
#         self.lineEdit_new_name = QtWidgets.QLineEdit(self.centralwidget)
#         self.lineEdit_new_name.setObjectName("lineEdit_new_name")
#         self.gridLayout.addWidget(self.lineEdit_new_name, 1, 2, 1, 2)
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setObjectName("label_2")
#         self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setObjectName("label_4")
#         self.gridLayout.addWidget(self.label_4, 9, 1, 1, 1)
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setObjectName("label_3")
#         self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setObjectName("label")
#         self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
#         self.label_8 = QtWidgets.QLabel(self.centralwidget)
#         self.label_8.setMaximumSize(QtCore.QSize(1061, 293))
#         self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.label_8.setFrameShape(QtWidgets.QFrame.Box)
#         self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.label_8.setObjectName("label_8")
#         self.gridLayout.addWidget(self.label_8, 16, 0, 1, 6)
#         self.label_9 = QtWidgets.QLabel(self.centralwidget)
#         self.label_9.setMaximumSize(QtCore.QSize(262, 262))
#         self.label_9.setObjectName("label_9")
#         self.label_9.setFrameShape(QtWidgets.QFrame.Box)
#         self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.gridLayout.addWidget(self.label_9, 1, 5, 13, 1)
#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setObjectName("label_6")
#         self.gridLayout.addWidget(self.label_6, 11, 1, 1, 1)
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setObjectName("label_5")
#         self.gridLayout.addWidget(self.label_5, 13, 1, 1, 1)
#         self.line_7 = QtWidgets.QFrame(self.centralwidget)
#         self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_7.setObjectName("line_7")
#         self.gridLayout.addWidget(self.line_7, 12, 1, 1, 3)
#         self.line = QtWidgets.QFrame(self.centralwidget)
#         self.line.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line.setObjectName("line")
#         self.gridLayout.addWidget(self.line, 2, 1, 1, 3)
#         self.line_4 = QtWidgets.QFrame(self.centralwidget)
#         self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_4.setObjectName("line_4")
#         self.gridLayout.addWidget(self.line_4, 6, 1, 1, 3)
#         self.line_3 = QtWidgets.QFrame(self.centralwidget)
#         self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_3.setObjectName("line_3")
#         self.gridLayout.addWidget(self.line_3, 4, 1, 1, 3)
#         self.line_2 = QtWidgets.QFrame(self.centralwidget)
#         self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_2.setObjectName("line_2")
#         self.gridLayout.addWidget(self.line_2, 0, 1, 1, 3)
#         self.line_9 = QtWidgets.QFrame(self.centralwidget)
#         self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
#         self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_9.setObjectName("line_9")
#         self.gridLayout.addWidget(self.line_9, 0, 0, 15, 1)
#         self.line_6 = QtWidgets.QFrame(self.centralwidget)
#         self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_6.setObjectName("line_6")
#         self.gridLayout.addWidget(self.line_6, 10, 1, 1, 3)
#         self.line_10 = QtWidgets.QFrame(self.centralwidget)
#         self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
#         self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line_10.setObjectName("line_10")
#         self.gridLayout.addWidget(self.line_10, 0, 4, 15, 1)
#         self.btn_insert = QtWidgets.QPushButton(self.centralwidget)
#         self.btn_insert.setObjectName("btn_insert")
#         self.btn_insert.setStyleSheet("background-color: green")
#         self.gridLayout.addWidget(self.btn_insert, 15, 2, 1, 3)
#         self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_5.setObjectName("pushButton_5")
#         self.gridLayout.addWidget(self.pushButton_5, 15, 0, 1, 2)
#         self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
#         # MainWindow.setCentralWidget(self.centralwidget)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Створення еталонного сигналу"))
#         self.pushButton.setText(_translate("MainWindow", "Завантажити вигляд станції"))
#         self.label_7.setText(_translate("MainWindow", "Назва станції"))
#         self.label_2.setText(_translate("MainWindow", "Тривалість імпульсу, мкс"))
#         self.label_4.setText(_translate("MainWindow", "Модуляція"))
#         self.label_3.setText(_translate("MainWindow", "Період слідування, мкс"))
#         self.label.setText(_translate("MainWindow", "Частота, МГц"))
#         self.label_8.setText(_translate("MainWindow", "TextLabel"))
#         self.label_9.setText(_translate("MainWindow", "Станція зображення"))
#         self.label_6.setText(_translate("MainWindow", "Ширина спектру, МГц"))
#         self.label_5.setText(_translate("MainWindow", "Комментар"))
#         self.btn_insert.setText(_translate("MainWindow", "Додати до еталонного переліку"))
#         self.pushButton_5.setText(_translate("MainWindow", "Завантажити вигляд сигналу"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bd_insert.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 596)
        MainWindow.setMinimumSize(QtCore.QSize(1081, 596))
        MainWindow.setMaximumSize(QtCore.QSize(1081, 596))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1081, 561))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 14, 1, 1, 3)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 8, 1, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 15, 5, 1, 1)
        self.lineEdit_pulse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pulse.setObjectName("lineEdit_pulse")
        self.gridLayout.addWidget(self.lineEdit_pulse, 5, 2, 1, 2)
        self.lineEdit_period = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_period.setObjectName("lineEdit_period")
        self.gridLayout.addWidget(self.lineEdit_period, 7, 2, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.lineEdit_modulation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_modulation.setObjectName("lineEdit_modulation")
        self.gridLayout.addWidget(self.lineEdit_modulation, 9, 2, 1, 2)
        self.lineEdit_bandwidth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bandwidth.setObjectName("lineEdit_bandwidth")
        self.gridLayout.addWidget(self.lineEdit_bandwidth, 11, 2, 1, 2)
        self.lineEdit_freq = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_freq.setObjectName("lineEdit_freq")
        self.gridLayout.addWidget(self.lineEdit_freq, 3, 2, 1, 2)
        self.lineEdit_comment = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_comment.setObjectName("lineEdit_comment")
        self.gridLayout.addWidget(self.lineEdit_comment, 13, 2, 1, 2)
        self.lineEdit_new_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new_name.setObjectName("lineEdit_new_name")

        self.gridLayout.addWidget(self.lineEdit_new_name, 1, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMaximumSize(QtCore.QSize(262, 264))
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setObjectName("label_9")
        self.label_9.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.label_9, 1, 5, 13, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 12, 1, 1, 3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 1, 1, 3)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 6, 1, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 4, 1, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 1, 1, 3)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 0, 0, 15, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 10, 1, 1, 3)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 0, 4, 15, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 15, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(1061, 293))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 16, 0, 1, 6)
        self.btn_insert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_insert.setObjectName("btn_insert")
        self.btn_insert.setStyleSheet("background-color: green")
        self.gridLayout.addWidget(self.btn_insert, 15, 2, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Створення еталонного запису"))
        self.pushButton.setText(_translate("MainWindow", "Завантажити вигляд станції"))
        self.label_7.setText(_translate("MainWindow", "Назва станції"))
        self.label_2.setText(_translate("MainWindow", "Тривалість імпульсу, мкс"))
        self.label_4.setText(_translate("MainWindow", "Модуляція"))
        self.label_3.setText(_translate("MainWindow", "Період слідування, мкс"))
        self.label.setText(_translate("MainWindow", "Частота, МГц"))
        self.label_9.setText(_translate("MainWindow", "Зображення станції "))
        self.label_6.setText(_translate("MainWindow", "Ширина спектру, МГц"))
        self.label_5.setText(_translate("MainWindow", "Комментар"))
        self.pushButton_5.setText(_translate("MainWindow", "Завантажити вигляд сигналу"))
        self.label_8.setText(_translate("MainWindow", "Зображення сигналу"))
        self.btn_insert.setText(_translate("MainWindow", "Додати до еталонного переліку"))
