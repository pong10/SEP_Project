# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_enter_tracking.ui',
# licensing of 'user_enter_tracking.ui' applies.
#
# Created: Fri May 31 12:44:44 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_tracking_user(object):
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
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.background.setStyleSheet("QLabel{background:lightblue;}\n"
"")
        self.background.setText("")
        self.background.setObjectName("background")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(170, 80, 471, 101))
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
        self.logo.setGeometry(QtCore.QRect(670, 440, 131, 101))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("location-512 copy 2.png"))
        self.logo.setObjectName("logo")
        self.TrackingNo_lineEdit = QtWidgets.QLineEdit(Form)
        self.TrackingNo_lineEdit.setGeometry(QtCore.QRect(220, 190, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(50)
        font.setBold(False)
        self.TrackingNo_lineEdit.setFont(font)
        self.TrackingNo_lineEdit.setStyleSheet("QLineEdit {border: 2px solid gray}\n"
"QLineEdit { border-radius: 30px; }")
        self.TrackingNo_lineEdit.setObjectName("TrackingNo_lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 320, 141, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("food_delivery_man.png.pagespeed.ce.fgGExqcaLE copy 20.17.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(620, 90, 61, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("pin-png-25-300x300 copy 2.png"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 260, 631, 331))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("1334375.png"))
        self.label_2.setObjectName("label_2")
        self.history = QtWidgets.QPushButton(Form)
        self.history.setGeometry(QtCore.QRect(40, 540, 101, 41))
        self.history.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.history.setObjectName("history")
        self.receive = QtWidgets.QPushButton(Form)
        self.receive.setGeometry(QtCore.QRect(150, 540, 101, 41))
        self.receive.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.receive.setObjectName("receive")
        self.track = QtWidgets.QPushButton(Form)
        self.track.setGeometry(QtCore.QRect(600, 250, 91, 41))
        self.track.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 20px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.track.setObjectName("track")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.Title.setText(QtWidgets.QApplication.translate("Form", "Let\'s start tracking your parcel!", None, -1))
        self.history.setText(QtWidgets.QApplication.translate("Form", "History", None, -1))
        self.receive.setText(QtWidgets.QApplication.translate("Form", "Receive Parcel", None, -1))
        self.track.setText(QtWidgets.QApplication.translate("Form", "Track", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_tracking_user()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

