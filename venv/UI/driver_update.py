# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driver_update.ui',
# licensing of 'driver_update.ui' applies.
#
# Created: Thu May 30 13:10:37 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_Driver_Update(object):
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
        self.bg.setStyleSheet("QLabel{background:peachpuff;}\n"
"")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 60, 491, 91))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:slategrey;}\n"
"")
        self.label.setObjectName("label")
        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(640, 60, 71, 81))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("purepng.com-white-paper-planpaper-planeaeroplanepaper-gliderpaper-dartaircraftfolded-paperpaperboardclipart-1421526588176couen copy 2.png"))
        self.pic.setObjectName("pic")
        self.current_location = QtWidgets.QLabel(Form)
        self.current_location.setGeometry(QtCore.QRect(70, 170, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(22)
        self.current_location.setFont(font)
        self.current_location.setStyleSheet("QLabel{color:peru;}\n"
"")
        self.current_location.setObjectName("current_location")
        self.destination = QtWidgets.QLabel(Form)
        self.destination.setGeometry(QtCore.QRect(70, 270, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(22)
        self.destination.setFont(font)
        self.destination.setStyleSheet("QLabel{color:peru;}\n"
"")
        self.destination.setObjectName("destination")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(380, 175, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.destination_input = QtWidgets.QLabel(Form)
        self.destination_input.setGeometry(QtCore.QRect(280, 280, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.destination_input.setFont(font)
        self.destination_input.setText("")
        self.destination_input.setObjectName("destination_input")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(270, 370, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.commandLinkButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shipping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 390, 241, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../kisspng-van-car-truck-delivery-cartoon-yellow-express-truck-5a7f5b77cdcad6.9479006315182959278429 copy 2.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(620, 440, 91, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("red-location-icon-map-png-4 copy 2.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "Have a nice and safe ride!", None, -1))
        self.current_location.setText(QtWidgets.QApplication.translate("Form", "Current Location:", None, -1))
        self.destination.setText(QtWidgets.QApplication.translate("Form", "Destination:", None, -1))
        self.commandLinkButton.setText(QtWidgets.QApplication.translate("Form", "Parcels delivered!", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Driver_Update()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

