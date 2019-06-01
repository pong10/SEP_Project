# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driver_task.ui',
# licensing of 'driver_task.ui' applies.
#
# Created: Sat Jun  1 17:27:13 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from Parcel import *

class Ui_Form_Driver(object):
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
        self.bg.setStyleSheet("QLabel{background: cornsilk;}")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(160, 150, 451, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 361))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 300))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.text = QtWidgets.QLabel(Form)
        self.text.setGeometry(QtCore.QRect(80, 50, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(33)
        self.text.setFont(font)
        self.text.setStyleSheet("QLabel{color:steelblue;}\n"
"\n"
"")
        self.text.setObjectName("text")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 40, 301, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("truck.png"))
        self.label.setObjectName("label")
        self.go_button = QtWidgets.QPushButton(Form)
        self.go_button.setGeometry(QtCore.QRect(680, 530, 93, 28))
        self.go_button.setStyleSheet("QPushButton\n"
"{\n"
"  border: 2px solid gray;\n"
"  border-radius: 10px;\n"
"  padding: 0 8px;\n"
"  background: white;\n"
"}\n"
"QPushButton:hover:enabled { color: green }\n"
"QPushButton:enabled { color: purple }")
        self.go_button.setObjectName("go_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Form", "Source:", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Form", "Destination:", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Form", "Number of Parcel:", None, -1))
        self.text.setText(QtWidgets.QApplication.translate("Form", "Let\'s choose task!", None, -1))
        self.go_button.setText(QtWidgets.QApplication.translate("Form", "GO!", None, -1))
    def table(self):
        run = Parcel()
        result = run.getParcelBygroup()
        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Driver()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

