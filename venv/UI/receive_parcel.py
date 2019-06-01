# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receive_parcel.ui',
# licensing of 'receive_parcel.ui' applies.
#
# Created: Sat Jun  1 19:48:12 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_Receive_Parcel(object):
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
        self.bg.setStyleSheet("QLabel{background: linen;}")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(220, 60, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(30)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel{color:gray;}\n"
"")
        self.text.setObjectName("text")
        self.enter_trackingid = QtWidgets.QLineEdit(Form)
        self.enter_trackingid.setGeometry(QtCore.QRect(260, 200, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.enter_trackingid.setFont(font)
        self.enter_trackingid.setTabletTracking(False)
        self.enter_trackingid.setStyleSheet("QLineEdit { border: 1px solid gray}\n"
"QLineEdit { border-radius: 20px;}")
        self.enter_trackingid.setText("")
        self.enter_trackingid.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_trackingid.setObjectName("enter_trackingid")
        self.enter_sender = QtWidgets.QLineEdit(Form)
        self.enter_sender.setGeometry(QtCore.QRect(260, 310, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.enter_sender.setFont(font)
        self.enter_sender.setStyleSheet("QLineEdit { border: 1px solid gray}\n"
"QLineEdit { border-radius: 20px;}")
        self.enter_sender.setText("")
        self.enter_sender.setAlignment(QtCore.Qt.AlignCenter)
        self.enter_sender.setObjectName("enter_sender")
        self.openLocker_button = QtWidgets.QPushButton(Form)
        self.openLocker_button.setGeometry(QtCore.QRect(480, 430, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.openLocker_button.setFont(font)
        self.openLocker_button.setStyleSheet("QPushButton { \n"
"border: 2px solid gray;\n"
"border-radius: 20px;\n"
"padding :0 8px;\n"
"background: white;\n"
"}\n"
"QPushButton:hover:enabled{color:gold}\n"
"QPushButton:enabled{color:black}")
        self.openLocker_button.setObjectName("openLocker_button")
        self.pic2 = QtWidgets.QLabel(Form)
        self.pic2.setGeometry(QtCore.QRect(10, 400, 241, 201))
        self.pic2.setText("")
        self.pic2.setPixmap(QtGui.QPixmap("1c669cd2aa6168788050badee0f3e174 copy 4.png"))
        self.pic2.setObjectName("pic2")
        self.pic1 = QtWidgets.QLabel(Form)
        self.pic1.setGeometry(QtCore.QRect(550, 40, 161, 91))
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap("christmas-gift copy 2.png"))
        self.pic1.setObjectName("pic1")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(170, 430, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton { \n"
"border: 2px solid gray;\n"
"border-radius: 20px;\n"
"padding :0 8px;\n"
"background: white;\n"
"}\n"
"QPushButton:hover:enabled{color:gold}\n"
"QPushButton:enabled{color:black}")
        self.back.setObjectName("back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "Receive Parcel ", None, -1))
        self.enter_trackingid.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Tracking id", None, -1))
        self.enter_sender.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Sender\'s name", None, -1))
        self.openLocker_button.setText(QtWidgets.QApplication.translate("Form", "Open locker!", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("Form", "Back", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Receive_Parcel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

