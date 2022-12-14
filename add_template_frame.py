# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_template_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewTemlate(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(120, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(120, 150))
        Frame.setStyleSheet("border-radius: 15;\n"
"background-color: rgba(150,150,150, 230);")
        self.text_label = QtWidgets.QLabel(Frame)
        self.text_label.setGeometry(QtCore.QRect(0, 0, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.text_label.setFont(font)
        self.text_label.setStyleSheet("color: white;\n"
"background-color: rgb(255,160,0, 0);\n"
"")
        self.text_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_label.setWordWrap(True)
        self.text_label.setObjectName("text_label")
        self.new_template_button = QtWidgets.QPushButton(Frame)
        self.new_template_button.setGeometry(QtCore.QRect(30, 80, 61, 61))
        self.new_template_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_template_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../icons/main_window/templte/add_template.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_template_button.setIcon(icon)
        self.new_template_button.setIconSize(QtCore.QSize(50, 50))
        self.new_template_button.setObjectName("new_template_button")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.text_label.setText(_translate("Frame", "????????????????"))
