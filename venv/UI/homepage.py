# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui',
# licensing of 'HomePage.ui' applies.
#
# Created: Tue May 28 18:17:57 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication, QMessageBox
from SignUp_user import Ui_Form2
from SignIn import *
from signUp import *
from AdminSignIn import Ui_Form_admin1
from AdminSignIn_2 import Ui_Form_admin2
from admin_enter_tracking import Ui_Form_tracking_admin
from user_enter_tracking import Ui_Form_tracking_user
from Create_TrackingNumber import Ui_Form_Create_TrackingNumber
from SignUp_admin import Ui_Form_SignUp_Admin

class Ui_Form1(object):
    
    def callUserPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_tracking_user()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
    def callAdminCreateAdmin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_SignUp_Admin()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.selectpage)
    def callAdminCreateTrackingPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Create_TrackingNumber()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.selectpage)
    def callAdminTrackingPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_tracking_admin()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.selectpage)
    def selectpage(self):
        if self.AdminName == "pnmoiannnygcoeu362":
            self.callMAdminPage()
        else:
            self.callNAdminPage()
    def callNAdminPage(self):
        self.callAdminPage()
    def callMAdminPage(self):
        self.callAdminPage("MasterAdmin")
    def selectAdminPage(self):
        a = self.ui.buttonGroup_2.checkedButton()
        b = a.text()
        if b == None:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Error")
            self.msg.setText("Please select an action")
            #self.msg.setInformativeText("Informative text here!")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
        else:
            if b == "Start tracking":
                self.callAdminTrackingPage()
            elif b == "Add new admin / driver":
                self.callAdminCreateAdmin()
            else:
                self.callAdminCreateTrackingPage()
    def callAdminPage(self,admin='--'):
        if admin == "MasterAdmin":
            self.ui = Ui_Form_admin1()
        else:
            self.ui = Ui_Form_admin2()
        self.window = QtWidgets.QWidget()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.AdminName.setText(self.AdminName)
        self.ui.confirm.clicked.connect(self.selectAdminPage)
    def callUserSignUp(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form2()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.done_2.clicked.connect(self.callback)
        self.ui.done.clicked.connect(self.StoreNClose)
    def StoreNClose(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        firstname = self.ui.firstname.text()
        lastname = self.ui.lastname.text()
        province = self.ui.province.text()
        phoneNumber = self.ui.phoneNo.text()
        email = self.ui.email.text()
        #phoneNumber=int(phoneNumber)
        print(type(username))
        print(type(password))
        print(type(firstname))
        print('firstname', firstname)
        print(type(lastname))
        print(type(province))
        print(type(phoneNumber))
        print(type(email))
        if len(username) > 15 or len(username) < 6 or len(password) > 15 or len(password) < 6:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Warning")
            self.msg.setText("Please enter the username or password between 8-16 characters long")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
        else:
            #print(username,password,firstname,lastname,province,phoneNo,email)
            t = SignUp(username,password)
            verify = t.UserExist()
            t.insertDatabase(firstname,lastname,phoneNumber,email,province)
            #t.mycursor.execute("(insert into User (UserId,PhoneNumber,Email,Firstname,Province) Values(%d,%s,%s,%s,%s))"%(int(UserID),str(phoneNo),str(email),str(firstname),str(province)))
            #print(verify)
            if verify is True:
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setWindowTitle("Error")
                self.msg.setText("This username already exist")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.show()
            else:
                t.signUp()
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QMessageBox.Information)
                self.msg.setWindowTitle("Thankyou")
                self.msg.setText("Thankyou for signing up with Parcel Express. Enjoy our services.")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.show()
                self.window.close()
                self.form.show()
        
    def callback(self):
        self.form.show()
        self.window.close()

    def identifyUser(self,a,b):
        user = SignIn(a,b)
        return user.signIn()
    def callNextPage(self):
        a = self.username_lineEdit.text()
        b = self.password_lineEdit.text()
        self.AdminName = a
        if (a == "pnmoiannnygcoeu362" and b == "qwerty"):
            self.callAdminPage("MasterAdmin")
        elif(len(a) > 15 or len(a) < 6 or len(b) > 15 or len(b) < 6):
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Error")
            self.msg.setText("Please enter the username or password between 8-16 characters long")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
        else:
            t = self.identifyUser(a,b)
            #not done
            if t is True:
                if(a[0:3] == "Ad_"):
                    self.callAdminPage()
                elif(a[0:3] == "Dr_"):
                    print("Driver")
                else:
                    pass
                    self.callUserPage()
            else:
                self.msg = QtWidgets.QMessageBox()
                self.msg.setIcon(QMessageBox.Warning)
                self.msg.setWindowTitle("User not Exist")
                self.msg.setText("Please check your username or password")
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.show()
                
        
    def setupUi(self, Form):
        self.form = Form
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setWindowIcon(QtGui.QIcon("860139 copy 2.png"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setMinimumSize(QtCore.QSize(800, 600))
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
        self.password_lineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
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
        self.SignUp.clicked.connect(self.callUserSignUp)
        self.SignIn.clicked.connect(self.callNextPage)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Parcel Express", None, -1))
        self.LOGO.setText(QtWidgets.QApplication.translate("Form", "Parcel Express", None, -1))
        self.username.setText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.password.setText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.SignIn.setText(QtWidgets.QApplication.translate("Form", "SignIn", None, -1))
        self.SignUp.setText(QtWidgets.QApplication.translate("Form", "SignUp", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

