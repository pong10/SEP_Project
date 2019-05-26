# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminSignIn.ui',
# licensing of 'AdminSignIn.ui' applies.
#
# Created: Sun May 26 17:46:47 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.bg.setStyleSheet("QLabel{background: wheat;}")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(50, 80, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(26)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel{color:lightslategrey;}\n"
"")
        self.text.setObjectName("text")
        self.AdminName = QtWidgets.QLabel(Form)
        self.AdminName.setGeometry(QtCore.QRect(560, 80, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(13)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.AdminName.setFont(font)
        self.AdminName.setStyleSheet("QLabel{color:lightgrey;}\n"
"")
        self.AdminName.setObjectName("AdminName")
        self.text2 = QtWidgets.QLabel(Form)
        self.text2.setGeometry(QtCore.QRect(200, 160, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(19)
        font.setWeight(75)
        font.setBold(True)
        self.text2.setFont(font)
        self.text2.setStyleSheet("QLabel{color:dimgrey;}\n"
"")
        self.text2.setObjectName("text2")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(260, 250, 311, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 290, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(320, 360, 181, 201))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("860139 copy 2.png"))
        self.pic.setObjectName("pic")
        self.confirm = QtWidgets.QCommandLinkButton(Form)
        self.confirm.setGeometry(QtCore.QRect(660, 540, 121, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shipping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm.setIcon(icon)
        self.confirm.setObjectName("confirm")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "Welcome Back Admin ", None, -1))
        self.AdminName.setText(QtWidgets.QApplication.translate("Form", "AdminName", None, -1))
        self.text2.setText(QtWidgets.QApplication.translate("Form", "Please select your action", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Form", "Create Tracking Number", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Form", "Start tracking", None, -1))
        self.confirm.setText(QtWidgets.QApplication.translate("Form", "CONFIRM", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

