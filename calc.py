# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 181)
        self.num1 = QtWidgets.QLineEdit(Form)
        self.num1.setGeometry(QtCore.QRect(40, 40, 113, 25))
        self.num1.setObjectName("num1")
        self.num2 = QtWidgets.QLineEdit(Form)
        self.num2.setGeometry(QtCore.QRect(220, 40, 113, 25))
        self.num2.setObjectName("num2")
        self.Add = QtWidgets.QPushButton(Form)
        self.Add.setGeometry(QtCore.QRect(30, 120, 80, 25))
        self.Add.setObjectName("Add")
        self.Sub = QtWidgets.QPushButton(Form)
        self.Sub.setGeometry(QtCore.QRect(130, 120, 80, 25))
        self.Sub.setObjectName("Sub")
        self.Div = QtWidgets.QPushButton(Form)
        self.Div.setGeometry(QtCore.QRect(220, 120, 80, 25))
        self.Div.setObjectName("Div")
        self.Mul = QtWidgets.QPushButton(Form)
        self.Mul.setGeometry(QtCore.QRect(310, 120, 80, 25))
        self.Mul.setObjectName("Mul")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Add.setText(_translate("Form", "Add"))
        self.Sub.setText(_translate("Form", "Subtract"))
        self.Div.setText(_translate("Form", "Divide"))
        self.Mul.setText(_translate("Form", "Multiply"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
