# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create_TrackingNumber.ui',
# licensing of 'Create_TrackingNumber.ui' applies.
#
# Created: Fri May 31 13:06:08 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form_Create_TrackingNumber(object):
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
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setMaximumSize(QtCore.QSize(800, 600))
        self.background.setBaseSize(QtCore.QSize(800, 600))
        self.background.setStyleSheet("QLabel{background:lightblue;}\n"
"\n"
"")
        self.background.setText("")
        self.background.setObjectName("background")
        self.ParcelExpress = QtWidgets.QLabel(Form)
        self.ParcelExpress.setGeometry(QtCore.QRect(250, 10, 351, 101))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(26)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.ParcelExpress.setFont(font)
        self.ParcelExpress.setStyleSheet("QLabel{color:chocolate;}\n"
"")
        self.ParcelExpress.setObjectName("ParcelExpress")
        self.Information = QtWidgets.QLabel(Form)
        self.Information.setGeometry(QtCore.QRect(320, 90, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Information.setFont(font)
        self.Information.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Information.setObjectName("Information")
        self.Sender = QtWidgets.QLabel(Form)
        self.Sender.setGeometry(QtCore.QRect(150, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Sender.setFont(font)
        self.Sender.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Sender.setObjectName("Sender")
        self.Receiver = QtWidgets.QLabel(Form)
        self.Receiver.setGeometry(QtCore.QRect(550, 170, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Receiver.setFont(font)
        self.Receiver.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Receiver.setObjectName("Receiver")
        self.Sender_firstname = QtWidgets.QLineEdit(Form)
        self.Sender_firstname.setGeometry(QtCore.QRect(40, 210, 141, 21))
        self.Sender_firstname.setInputMask("")
        self.Sender_firstname.setObjectName("Sender_firstname")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(570, 30, 71, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("purepng.com-white-paper-planpaper-planeaeroplanepaper-gliderpaper-dartaircraftfolded-paperpaperboardclipart-1421526588176couen copy 2.png"))
        self.label.setObjectName("label")
        self.Sender_lastname = QtWidgets.QLineEdit(Form)
        self.Sender_lastname.setGeometry(QtCore.QRect(210, 210, 141, 21))
        self.Sender_lastname.setObjectName("Sender_lastname")
        self.Receiver_lastname = QtWidgets.QLineEdit(Form)
        self.Receiver_lastname.setGeometry(QtCore.QRect(620, 210, 141, 21))
        self.Receiver_lastname.setObjectName("Receiver_lastname")
        self.Receiver_firstname = QtWidgets.QLineEdit(Form)
        self.Receiver_firstname.setGeometry(QtCore.QRect(450, 210, 141, 21))
        self.Receiver_firstname.setObjectName("Receiver_firstname")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 119, 801, 41))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(390, 140, 20, 411))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.Sender_2 = QtWidgets.QLabel(Form)
        self.Sender_2.setGeometry(QtCore.QRect(140, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Sender_2.setFont(font)
        self.Sender_2.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Sender_2.setObjectName("Sender_2")
        self.Sender_3 = QtWidgets.QLabel(Form)
        self.Sender_3.setGeometry(QtCore.QRect(550, 260, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Sender_3.setFont(font)
        self.Sender_3.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Sender_3.setObjectName("Sender_3")
        self.Sender_address = QtWidgets.QTextEdit(Form)
        self.Sender_address.setGeometry(QtCore.QRect(30, 310, 321, 91))
        self.Sender_address.setObjectName("Sender_address")
        self.Receiver_address = QtWidgets.QTextEdit(Form)
        self.Receiver_address.setGeometry(QtCore.QRect(440, 310, 321, 91))
        self.Receiver_address.setObjectName("Receiver_address")
        self.Sender_province = QtWidgets.QLineEdit(Form)
        self.Sender_province.setGeometry(QtCore.QRect(30, 430, 141, 21))
        self.Sender_province.setInputMask("")
        self.Sender_province.setObjectName("Sender_province")
        self.Sender_postcode = QtWidgets.QLineEdit(Form)
        self.Sender_postcode.setGeometry(QtCore.QRect(210, 430, 141, 21))
        self.Sender_postcode.setInputMask("")
        self.Sender_postcode.setObjectName("Sender_postcode")
        self.Receiver_province = QtWidgets.QLineEdit(Form)
        self.Receiver_province.setGeometry(QtCore.QRect(440, 430, 141, 21))
        self.Receiver_province.setInputMask("")
        self.Receiver_province.setObjectName("Receiver_province")
        self.Receiver_postcode = QtWidgets.QLineEdit(Form)
        self.Receiver_postcode.setGeometry(QtCore.QRect(610, 430, 141, 21))
        self.Receiver_postcode.setInputMask("")
        self.Receiver_postcode.setObjectName("Receiver_postcode")
        self.Sender_4 = QtWidgets.QLabel(Form)
        self.Sender_4.setGeometry(QtCore.QRect(140, 460, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Sender_4.setFont(font)
        self.Sender_4.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Sender_4.setObjectName("Sender_4")
        self.Sender_5 = QtWidgets.QLabel(Form)
        self.Sender_5.setGeometry(QtCore.QRect(550, 460, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(15)
        font.setWeight(75)
        font.setBold(True)
        self.Sender_5.setFont(font)
        self.Sender_5.setStyleSheet("QLabel{color:sienna;}\n"
"")
        self.Sender_5.setObjectName("Sender_5")
        self.Sender_telno = QtWidgets.QLineEdit(Form)
        self.Sender_telno.setGeometry(QtCore.QRect(100, 510, 171, 21))
        self.Sender_telno.setInputMask("")
        self.Sender_telno.setObjectName("Sender_telno")
        self.Receiver_telno = QtWidgets.QLineEdit(Form)
        self.Receiver_telno.setGeometry(QtCore.QRect(520, 510, 171, 21))
        self.Receiver_telno.setInputMask("")
        self.Receiver_telno.setObjectName("Receiver_telno")
        self.Create = QtWidgets.QPushButton(Form)
        self.Create.setGeometry(QtCore.QRect(670, 560, 93, 28))
        self.Create.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.Create.setObjectName("Create")
        self.back = QtWidgets.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(40, 560, 93, 28))
        self.back.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.back.setObjectName("Back")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(-10, 540, 811, 31))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.ParcelExpress.setText(QtWidgets.QApplication.translate("Form", "Parcel Express", None, -1))
        self.Information.setText(QtWidgets.QApplication.translate("Form", "Information", None, -1))
        self.Sender.setText(QtWidgets.QApplication.translate("Form", "Sender", None, -1))
        self.Receiver.setText(QtWidgets.QApplication.translate("Form", "Receiver", None, -1))
        self.Sender_firstname.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Firstname", None, -1))
        self.Sender_lastname.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Lastname", None, -1))
        self.Receiver_lastname.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Lastname", None, -1))
        self.Receiver_firstname.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Firstname", None, -1))
        self.Sender_2.setText(QtWidgets.QApplication.translate("Form", "Address", None, -1))
        self.Sender_3.setText(QtWidgets.QApplication.translate("Form", "Address", None, -1))
        self.Sender_province.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Province", None, -1))
        self.Sender_postcode.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Postcode", None, -1))
        self.Receiver_province.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Province", None, -1))
        self.Receiver_postcode.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Postcode", None, -1))
        self.Sender_4.setText(QtWidgets.QApplication.translate("Form", "Contact", None, -1))
        self.Sender_5.setText(QtWidgets.QApplication.translate("Form", "Contact", None, -1))
        self.Sender_telno.setPlaceholderText(QtWidgets.QApplication.translate("Form", "                Tel.no", None, -1))
        self.Receiver_telno.setPlaceholderText(QtWidgets.QApplication.translate("Form", "               Tel.no", None, -1))
        self.Create.setText(QtWidgets.QApplication.translate("Form", "CREATE", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("Form", "BACK", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Create_TrackingNumber()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

