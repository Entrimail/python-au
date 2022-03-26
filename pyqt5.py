# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomizer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random



class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(70, 130, 180);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 200, 75, 23))
        

        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:silver;\n"
"width:40px;\n"
"height:30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:white;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:grey;}")
        self.pushButton.setObjectName("pushButton")
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 140, 171, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 80, 71, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 60, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Sylfaen")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")      

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Password generator"))
        self.pushButton.setText(_translate("Dialog", "Generate"))
        self.label.setText(_translate("Dialog", "Pass length:"))
        self.label_2.setText(_translate("Dialog", "Result:"))



app = QtWidgets.QApplication(sys.argv)

#create form and init ui
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()



def pb():
    txt = int(ui.lineEdit_2.text()) 
  
    psw = ''
    for i in range(txt):
        psw = psw + random.choice(list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))            

        
        
        ui.lineEdit.setText(psw)
    
ui.pushButton.clicked.connect(pb)




#run mainloop
sys.exit(app.exec_())








