# Form implementation generated from reading ui file 'ui/get_name_templ.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Naming(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 163)
        Dialog.setStyleSheet("background-color:     #333333")
        self.name_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.name_lineEdit.setGeometry(QtCore.QRect(30, 60, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.name_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.name_lineEdit.setText("")
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.finish_naming_button = QtWidgets.QPushButton(Dialog)
        self.finish_naming_button.setGeometry(QtCore.QRect(130, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.finish_naming_button.setFont(font)
        self.finish_naming_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.finish_naming_button.setStyleSheet("color: white;\n"
"background-color: #0080ff;\n"
"border-radius: 8;\n"
"")
        self.finish_naming_button.setObjectName("finish_naming_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Template name:"))
        self.finish_naming_button.setText(_translate("Dialog", "Ok"))
