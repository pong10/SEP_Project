# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracking_history.ui',
# licensing of 'tracking_history.ui' applies.
#
# Created: Sat Jun  1 14:36:41 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from Customer import *

class Ui_Form_Tracking_history(object):
    def setupUi(self, Form):
        self.user = ""
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
        self.bg.setStyleSheet("QLabel{background: antiquewhite;}")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(250, 50, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel{color:darkgoldenrod;}\n"
"")
        self.text.setObjectName("text")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 120, 741, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(19)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(30, 540, 101, 31))
        self.back_button.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 15px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.back_button.setObjectName("back_button")
        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(570, 10, 121, 121))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("yellow-parcel.png"))
        self.pic.setObjectName("pic")
        self.pic1 = QtWidgets.QLabel(Form)
        self.pic1.setGeometry(QtCore.QRect(90, 10, 191, 121))
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap("PinClipart.com_volunteer-clipart-free_208642 copy 3.png"))
        self.pic1.setObjectName("pic1")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "Your tracking history", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "Tracking id", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "Sender", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Form", "Source", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("Form", "Receiver", None, -1))
        self.tableWidget.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("Form", "Destination", None, -1))
        self.back_button.setText(QtWidgets.QApplication.translate("Form", "Back", None, -1))
    def table(self):
        run = Customer(self.user)
        result = run.GetHistory()
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Tracking_history()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

