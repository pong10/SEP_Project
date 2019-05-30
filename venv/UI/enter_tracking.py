# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_tracking.ui',
# licensing of 'enter_tracking.ui' applies.
#
# Created: Sun May 26 14:28:45 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(801, 600)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.background.setStyleSheet("QLabel{background:lightblue;}\n"
"")
        self.background.setText("")
        self.background.setObjectName("background")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(160, 100, 471, 101))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setStyleSheet("QLabel{color:dimgrey;}\n"
"")
        self.Title.setObjectName("Title")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(670, 410, 131, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("location-512 copy 2.png"))
        self.logo.setObjectName("logo")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 190, 381, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 320, 141, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("food_delivery_man.png.pagespeed.ce.fgGExqcaLE copy 20.17.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(610, 110, 61, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pin-png-25-300x300 copy 2.png"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 210, 631, 381))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("1334375.png"))
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(590, 260, 91, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("food_delivery_man.png.pagespeed.ce.fgGExqcaLE copy 20.17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.Title.setText(QtWidgets.QApplication.translate("Form", "Let\'s start tracking your parcel!", None, -1))
        self.commandLinkButton.setText(QtWidgets.QApplication.translate("Form", "Track!", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

