# Form implementation generated from reading ui file 'ui/active_schedule.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SpecialDate(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(500, 50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(500, 50))
        Frame.setStyleSheet("border-radius: 10;\n"
"background-color: rgba(0,127,255, 60);")
        self.title_label = QtWidgets.QLabel(Frame)
        self.title_label.setGeometry(QtCore.QRect(150, 10, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Regular")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: white;\n"
"background-color: rgb(255,160,0, 0);\n"
"")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setWordWrap(True)
        self.title_label.setObjectName("title_label")
        self.date_label = QtWidgets.QLabel(Frame)
        self.date_label.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet("color: white;\n"
"background-color: rgb(255,160,0, 0);\n"
"")
        self.date_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_label.setWordWrap(True)
        self.date_label.setObjectName("date_label")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.title_label.setText(_translate("Frame", "День программисата"))
        self.date_label.setText(_translate("Frame", "23.02.2023"))