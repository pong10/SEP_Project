# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui',
# licensing of 'HomePage.ui' applies.
#
# Created: Sun May 26 14:21:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.Background = QtWidgets.QLabel(Form)
        self.Background.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.Background.setStyleSheet("QLabel{background: papayawhip;}")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.LOGO = QtWidgets.QLabel(Form)
        self.LOGO.setGeometry(QtCore.QRect(190, 70, 386, 58))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(30)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.LOGO.setFont(font)
        self.LOGO.setStyleSheet("QLabel{color:steelblue;}\n"
"")
        self.LOGO.setObjectName("LOGO")
        self.logo_pic = QtWidgets.QLabel(Form)
        self.logo_pic.setGeometry(QtCore.QRect(580, 80, 81, 51))
        self.logo_pic.setText("")
        self.logo_pic.setPixmap(QtGui.QPixmap("purepng.com-white-paper-planpaper-planeaeroplanepaper-gliderpaper-dartaircraftfolded-paperpaperboardclipart-1421526588176couen copy 2.png"))
        self.logo_pic.setObjectName("logo_pic")
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(300, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setStyleSheet("QLabel{color:dimgrey;}\n"
"")
        self.username.setObjectName("username")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setGeometry(QtCore.QRect(300, 180, 181, 31))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(300, 230, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(14)
        self.password.setFont(font)
        self.password.setStyleSheet("QLabel{color:dimgrey;}\n"
"")
        self.password.setObjectName("password")
        self.password_lineEdit = QtWidgets.QLineEdit(Form)
        self.password_lineEdit.setGeometry(QtCore.QRect(300, 250, 181, 31))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.SignIn = QtWidgets.QPushButton(Form)
        self.SignIn.setGeometry(QtCore.QRect(260, 310, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.SignIn.setFont(font)
        self.SignIn.setStyleSheet("")
        self.SignIn.setObjectName("SignIn")
        self.SignUp = QtWidgets.QPushButton(Form)
        self.SignUp.setGeometry(QtCore.QRect(420, 310, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        self.SignUp.setFont(font)
        self.SignUp.setObjectName("SignUp")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-40, 340, 841, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("paper_plane_PNG20 copy 2.png"))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.LOGO.setText(QtWidgets.QApplication.translate("Form", "Parcel Express", None, -1))
        self.username.setText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.password.setText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.SignIn.setText(QtWidgets.QApplication.translate("Form", "SignIn", None, -1))
        self.SignUp.setText(QtWidgets.QApplication.translate("Form", "SignUp", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

