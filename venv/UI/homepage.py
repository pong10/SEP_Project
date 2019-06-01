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
from signUp import SignUp
from AdminSignIn import Ui_Form_admin1
from AdminSignIn_2 import Ui_Form_admin2
from admin_enter_tracking import Ui_Form_tracking_admin
from user_enter_tracking import Ui_Form_tracking_user
from Create_TrackingNumber import Ui_Form_Create_TrackingNumber
from SignUp_admin import Ui_Form_SignUp_Admin
from Confirm import Ui_Form_Confirm
from Number_Generater import generate
from Number_Generater import generate2
from Admin import Admin
import CreateTracking as ct
from Tracking import Tracking
from showTrackingInfo import Ui_Form_showTrackingInfo
from showHistory import *
from tracking_history import Ui_Form_Tracking_history
from driver_task import Ui_Form_Driver
from Parcel import *
from driver_update import Ui_Form_Driver_Update
from Driver import *
from receive_parcel import Ui_Form_Receive_Parcel
from Locker import Locker

class Ui_Form1(object):
    def callConfirm(self):
        self.sfirstname = self.ui.Sender_firstname.text()
        self.slastname = self.ui.Sender_lastname.text()
        self.saddress = self.ui.Sender_address.toPlainText()
        self.sprovince = self.ui.Sender_province.text()
        self.spostcode = self.ui.Sender_postcode.text()
        self.stelno = self.ui.Sender_telno.text()
        self.rfirstname = self.ui.Receiver_firstname.text()
        self.rlastname = self.ui.Receiver_lastname.text()
        self.raddress = self.ui.Receiver_address.toPlainText()
        self.rprovince = self.ui.Receiver_province.text()
        self.rpostcode = self.ui.Receiver_postcode.text()
        self.rtelno = self.ui.Receiver_telno.text()
        
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Confirm()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()

        self.tracking_no = generate()
        self.ui.showtrackingnumber.setText(self.tracking_no)
        self.ui.showsname.setText(self.sfirstname + " " + self.slastname)
        self.ui.showsAdd.setText(self.saddress + " " + self.sprovince + " " + self.spostcode)
        self.ui.showsendercon.setText(self.stelno)

        self.ui.showrname.setText(self.rfirstname + " " + self.rlastname)
        self.ui.showradd.setText(self.raddress + " " + self.rprovince + " " + self.rpostcode)
        self.ui.showrcon.setText(self.rtelno)

        self.ui.confirm.clicked.connect(self.confirmshipment)
        self.ui.back.clicked.connect(self.callAdminCreateTrackingPage)
    def confirmshipment(self):
        a = "Parcel is in the source branch"
        
        ct.createTrackingNumber(self.tracking_no,self.sfirstname,self.slastname,self.saddress,self.sprovince,self.spostcode,self.stelno,self.rfirstname,self.rlastname,self.raddress,self.rprovince,self.rpostcode,self.rtelno,a)

        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Thankyou")
        self.msg.setText("Thankyou for Using our Service. Your Tracking No is : %s"%(self.tracking_no))
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()
        self.selectpage()
    def callUserPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_tracking_user()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.track.clicked.connect(self.showTrackInfo)
        self.ui.history.clicked.connect(self.callHistory)
        self.ui.receive.clicked.connect(self.callReceive)
        
    def callReceive(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Receive_Parcel()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.callUserPage)
        self.ui.openLocker_button.clicked.connect(self.openlocker)
    def openlocker(self):
        a = self.ui.enter_trackingid.text()
        b = self.ui.enter_sender.text()
        c = Locker(a,b)
        d = c.open()
        if d == False:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Error")
            self.msg.setText("Please re-enter your Information")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
        else:
            zz = generate2()
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle("Parcel Receive")
            self.msg.setText("Parcel receive. Your PIN to open locker is: "+str(zz))
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
            self.callUserPage()
    def callHistory(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Tracking_history()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.user = self.AdminName
        print(self.AdminName)
        self.ui.table()
        self.ui.back_button.clicked.connect(self.callUserPage)
        
    def callAdminCreateAdmin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_SignUp_Admin()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.selectpage)
        self.ui.done.clicked.connect(self.saveAdmin)
    def saveAdmin(self):
        username = self.ui.lineEdit_6.text()
        password = self.ui.lineEdit_7.text()
        firstname = self.ui.lineEdit.text()
        lastname = self.ui.lineEdit_2.text()
        province = self.ui.lineEdit_3.text()
        phoneno = self.ui.lineEdit_4.text()
        email = self.ui.lineEdit_5.text()
        role = self.ui.buttonGroup_2.checkedButton()
        
        if len(username) > 15 or len(username) < 6 or len(password) > 15 or len(password) < 6:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Warning")
            self.msg.setText("Please enter the username or password between 8-16 characters long")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
        else:
            if role.text() == "Admin":
                username = "Ad_"+username
            else:
                username = "Dr_"+username
            t = SignUp(username,password,firstname,lastname,phoneno,email,province)
            verify = t.UserExist()
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
                self.selectpage()
    def callAdminCreateTrackingPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Create_TrackingNumber()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.selectpage)
        self.ui.Create.clicked.connect(self.callConfirm)
    def callAdminTrackingPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_tracking_admin()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.back.clicked.connect(self.selectpage)
        self.ui.track.clicked.connect(self.showTrackInfo)

    def showTrackInfo(self):
        trackno = self.ui.TrackingNo_lineEdit.text()
        a = Tracking(trackno)
        a.track()
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_showTrackingInfo()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()

        self.ui.showtrackingnumber.setText(a.getTrackingNumber())
        self.ui.show_sender.setText(a.getSender())
        self.ui.show_receiveraddress.setText(a.getReceiver_address()+" "+a.getReceiver_province()+" "+a.getReceiver_postcode())
        self.ui.progressBar.setValue(a.trackPercent(a.getState()))
        
        self.ui.commandLinkButton.clicked.connect(self.selectpage2)
    def selectpage2(self):
        if self.AdminName[0:3] == "Ad_":
            self.callAdminTrackingPage()
        elif self.AdminName == "pnmoiannnygcoeu362":
            self.callAdminTrackingPage()
        else:
            self.callUserPage()
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
        phoneNo = self.ui.phoneNo.text()
        email = self.ui.email.text()
        print(email)
        print("PhoneNO")
        print(phoneNo)
        if len(username) > 15 or len(username) < 6 or len(password) > 15 or len(password) < 6 or username[0:3] == "Ad_" or username[0:3] == "Dr_":
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setWindowTitle("Warning")
            self.msg.setText("Please enter the username or password between 8-16 characters long")
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
        else:
            t = SignUp(username,password,firstname,lastname,phoneNo,email,province)
            verify = t.UserExist()
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
        return user.SignIn()
    def callDriverPage(self):   
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Driver()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.table()
        self.ui.go_button.clicked.connect(self.callDriverUpdate)
    def callDriverUpdate(self):
        self.selecteditem = self.ui.tableWidget.selectedItems()
        a = self.selecteditem[0].text()
        b = self.selecteditem[1].text()
        c = self.selecteditem[2].text()
        t = Driver(a,b,self.AdminName)
        t.collected()
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Driver_Update()
        self.ui.setupUi(self.window)
        self.form.hide()
        self.window.show()
        self.ui.label_5.setText(a)
        self.ui.destination_input.setText(b)
        self.source = a
        self.destination = b
        self.ui.commandLinkButton.clicked.connect(self.callupdate)
        #
        #
        #
        #
        #
        
    def callupdate(self):
        t = Driver(self.source,self.destination,self.AdminName)
        t.ReachDestination()
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Info")
        self.msg.setText("Stage of this parcel is now change")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()
        self.callDriverPage()
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
            if t is True:
                if(a[0:3] == "Ad_"):
                    self.callAdminPage()
                elif(a[0:3] == "Dr_"):
                    self.callDriverPage()
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

