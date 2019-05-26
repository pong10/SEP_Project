# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui',
# licensing of 'SignUp.ui' applies.
#
# Created: Sun May 26 17:56:14 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 600)
        self.bg = QtWidgets.QLabel(Form)
        self.bg.setGeometry(QtCore.QRect(-10, 0, 811, 601))
        self.bg.setStyleSheet("QLabel{background: papayawhip;}")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(230, 40, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(28)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel{color:lightslategrey;}\n"
"")
        self.text.setObjectName("text")
        self.Mr = QtWidgets.QCheckBox(Form)
        self.Mr.setGeometry(QtCore.QRect(80, 160, 41, 20))
        self.Mr.setObjectName("Mr")
        self.buttonGroup = QtWidgets.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Mr)
        self.Ms = QtWidgets.QCheckBox(Form)
        self.Ms.setGeometry(QtCore.QRect(120, 160, 51, 20))
        self.Ms.setObjectName("Ms")
        self.buttonGroup.addButton(self.Ms)
        self.Mrs = QtWidgets.QCheckBox(Form)
        self.Mrs.setGeometry(QtCore.QRect(160, 160, 51, 20))
        self.Mrs.setObjectName("Mrs")
        self.buttonGroup.addButton(self.Mrs)
        self.driver_button = QtWidgets.QRadioButton(Form)
        self.driver_button.setGeometry(QtCore.QRect(350, 440, 100, 20))
        self.driver_button.setObjectName("driver_button")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.driver_button)
        self.admin_button = QtWidgets.QRadioButton(Form)
        self.admin_button.setGeometry(QtCore.QRect(350, 400, 100, 20))
        self.admin_button.setObjectName("admin_button")
        self.buttonGroup_2.addButton(self.admin_button)
        self.user_button = QtWidgets.QRadioButton(Form)
        self.user_button.setGeometry(QtCore.QRect(350, 480, 100, 20))
        self.user_button.setObjectName("user_button")
        self.buttonGroup_2.addButton(self.user_button)
        self.done = QtWidgets.QCommandLinkButton(Form)
        self.done.setGeometry(QtCore.QRect(650, 540, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.done.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("shipping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.done.setIcon(icon)
        self.done.setObjectName("done")
        self.admin_pic = QtWidgets.QLabel(Form)
        self.admin_pic.setGeometry(QtCore.QRect(420, 390, 51, 41))
        self.admin_pic.setText("")
        self.admin_pic.setPixmap(QtGui.QPixmap("Admin-staff-women-1-33jyeega3zzf8zdve4wxz4 copy 2.png"))
        self.admin_pic.setObjectName("admin_pic")
        self.driver_pic = QtWidgets.QLabel(Form)
        self.driver_pic.setGeometry(QtCore.QRect(440, 430, 31, 41))
        self.driver_pic.setText("")
        self.driver_pic.setPixmap(QtGui.QPixmap("delivery-man-driver-pngrepo-com copy 3.png"))
        self.driver_pic.setObjectName("driver_pic")
        self.user_pic = QtWidgets.QLabel(Form)
        self.user_pic.setGeometry(QtCore.QRect(420, 470, 61, 41))
        self.user_pic.setText("")
        self.user_pic.setPixmap(QtGui.QPixmap("users copy 2.png"))
        self.user_pic.setObjectName("user_pic")
        self.firstname_2 = QtWidgets.QLineEdit(Form)
        self.firstname_2.setGeometry(QtCore.QRect(230, 160, 141, 31))
        self.firstname_2.setStyleSheet("QPlainTextEdit{color:grey;}\n"
"")
        self.firstname_2.setInputMask("")
        self.firstname_2.setText("")
        self.firstname_2.setObjectName("firstname_2")
        self.firstname_3 = QtWidgets.QLineEdit(Form)
        self.firstname_3.setGeometry(QtCore.QRect(410, 160, 141, 31))
        self.firstname_3.setStyleSheet("QPlainTextEdit{color:grey;}\n"
"")
        self.firstname_3.setInputMask("")
        self.firstname_3.setText("")
        self.firstname_3.setObjectName("firstname_3")
        self.firstname_4 = QtWidgets.QLineEdit(Form)
        self.firstname_4.setGeometry(QtCore.QRect(230, 230, 191, 31))
        self.firstname_4.setStyleSheet("QPlainTextEdit{color:grey;}\n"
"")
        self.firstname_4.setInputMask("")
        self.firstname_4.setText("")
        self.firstname_4.setObjectName("firstname_4")
        self.firstname_5 = QtWidgets.QLineEdit(Form)
        self.firstname_5.setGeometry(QtCore.QRect(230, 300, 141, 31))
        self.firstname_5.setStyleSheet("QPlainTextEdit{color:grey;}\n"
"")
        self.firstname_5.setInputMask("")
        self.firstname_5.setText("")
        self.firstname_5.setObjectName("firstname_5")
        self.firstname_6 = QtWidgets.QLineEdit(Form)
        self.firstname_6.setGeometry(QtCore.QRect(410, 300, 141, 31))
        self.firstname_6.setStyleSheet("QPlainTextEdit{color:grey;}\n"
"")
        self.firstname_6.setInputMask("")
        self.firstname_6.setText("")
        self.firstname_6.setObjectName("firstname_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "Let\'s Sign Up!", None, -1))
        self.Mr.setText(QtWidgets.QApplication.translate("Form", "Mr.", None, -1))
        self.Ms.setText(QtWidgets.QApplication.translate("Form", "Ms.", None, -1))
        self.Mrs.setText(QtWidgets.QApplication.translate("Form", "Mrs.", None, -1))
        self.driver_button.setText(QtWidgets.QApplication.translate("Form", "Driver", None, -1))
        self.admin_button.setText(QtWidgets.QApplication.translate("Form", "Admin", None, -1))
        self.user_button.setText(QtWidgets.QApplication.translate("Form", "User", None, -1))
        self.done.setText(QtWidgets.QApplication.translate("Form", "DONE", None, -1))
        self.firstname_2.setPlaceholderText(QtWidgets.QApplication.translate("Form", "firstname", None, -1))
        self.firstname_3.setPlaceholderText(QtWidgets.QApplication.translate("Form", "lastname", None, -1))
        self.firstname_4.setPlaceholderText(QtWidgets.QApplication.translate("Form", "id number/ passport number ", None, -1))
        self.firstname_5.setPlaceholderText(QtWidgets.QApplication.translate("Form", "phone number", None, -1))
        self.firstname_6.setPlaceholderText(QtWidgets.QApplication.translate("Form", "email", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

