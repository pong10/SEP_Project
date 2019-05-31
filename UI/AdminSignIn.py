# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminSignIn.ui',
# licensing of 'AdminSignIn.ui' applies.
#
# Created: Thu May 30 18:46:50 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_admin1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setWindowIcon(QtGui.QIcon("860139 copy 2.png"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setBaseSize(QtCore.QSize(800, 600))
        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.bg.setStyleSheet("QLabel{background: wheat;}")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(130, 90, 400, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel{color:lightslategrey;}\n"
"")
        self.text.setObjectName("text")
        self.AdminName = QtWidgets.QLabel(Form)
        self.AdminName.setGeometry(QtCore.QRect(540, 90, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(True)
        self.AdminName.setFont(font)
        self.AdminName.setStyleSheet("QLabel{color:black;}\n"
"")
        self.AdminName.setObjectName("AdminName")
        self.text2 = QtWidgets.QLabel(Form)
        self.text2.setGeometry(QtCore.QRect(220, 170, 421, 51))
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
        self.radioButton.setGeometry(QtCore.QRect(320, 280, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 330, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup_2.addButton(self.radioButton_2)
        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(320, 390, 181, 201))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("860139 copy 2.png"))
        self.pic.setObjectName("pic")
        self.confirm = QtWidgets.QCommandLinkButton(Form)
        self.confirm.setGeometry(QtCore.QRect(640, 540, 141, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shipping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm.setIcon(icon)
        self.confirm.setObjectName("confirm")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(320, 240, 301, 20))
        self.buttonGroup_2.addButton(self.radioButton_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "Welcome Back Admin: ", None, -1))
        self.AdminName.setText(QtWidgets.QApplication.translate("Form", "AdminName", None, -1))
        self.text2.setText(QtWidgets.QApplication.translate("Form", "Please select your action", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Form", "Create Tracking Number", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Form", "Start tracking", None, -1))
        self.confirm.setText(QtWidgets.QApplication.translate("Form", "CONFIRM", None, -1))
        self.radioButton_3.setText(QtWidgets.QApplication.translate("Form", "Add new admin / driver", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_admin1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

