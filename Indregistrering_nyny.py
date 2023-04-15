# Form implementation generated from reading ui file 'Indregistrering.ui'
#
# Created by: PyQt6 UI code generator 6.4.2


# The UI file is converted into a python file
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(214, 244, 244);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(255, 40, 331, 41))
        self.textEdit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 140, 141, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_2.setObjectName("")

        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(240, 330, 141, 41))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(240, 270, 141, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(240, 400, 141, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_5.setObjectName("textEdit_5")

        self.textEdit_6 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(440, 140, 141, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);\n"
"border-color: rgb(10, 8, 17);")
        self.textEdit_6.setObjectName("textEdit_6")

        self.textEdit_7 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(240, 200, 141, 31))
        self.textEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.textEdit_7.setObjectName("textEdit_7")

        self.textEdit_8 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(440, 260, 141, 31))
        self.textEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_8.setObjectName("textEdit_8")

        self.textEdit_9 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(440, 400, 141, 31))
        self.textEdit_9.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_9.setObjectName("textEdit_9")

        self.textEdit_10 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(440, 200, 141, 31))
        self.textEdit_10.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.textEdit_10.setObjectName("textEdit_10")

        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(440, 330, 161, 41))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.dateEdit.setObjectName("dateEdit")

        self.toolButton = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(760, 560, 26, 22))
        self.toolButton.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.toolButton.setObjectName("toolButton")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 450, 161, 32))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(15, 6, 9);")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.click_button)

        self.textEdit_cprfejl = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_cprfejl.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textEdit_cprfejl.setStyleSheet("color: rgb(214, 244, 244);")
        self.textEdit_cprfejl.setGeometry(QtCore.QRect(600, 135, 141, 50))

        self.textEdit_svarfejl = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_svarfejl.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textEdit_svarfejl.setStyleSheet("color: rgb(214, 244, 244);")
        self.textEdit_svarfejl.setGeometry(QtCore.QRect(600, 195, 141, 50))

        self.textEdit_weightfejl = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_weightfejl.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.textEdit_weightfejl.setStyleSheet("color: rgb(214, 244, 244);")
        self.textEdit_weightfejl.setGeometry(QtCore.QRect(600, 250, 141, 50))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# A function that defines the inputboxes and decides if the information put in is correct once the pushbuttom is pressed.
# First of all the textEdit boxes that we use are defined, so the names are easier.
    def click_button(self):
        ''' We use toPlainText to contain the plain text in the text edit'''
        text1 = self.textEdit_6.toPlainText()
        text2 = self.textEdit_8.toPlainText()
        text3 = self.textEdit_10.toPlainText()
        text5 = self.textEdit_9.toPlainText()
        # The first condition states, that the input should be numbers and that it should consist of exactly 10 numbers.
        condition1 = text1.isdigit() and len(str(text1)) == 10
        # The second condition states, that the input should be letters, and that the text3 box shall accept either, Yes, yes, No or no.
        condition2 = text3.isalpha() and (text3 == 'Yes' or text3 == 'No' or text3 == 'yes' or text3 == 'no' )
        # Condition 3 states that the number should be numbers between 30 and 200.
        condition3 = text2.isdigit() and 30 < int((text2)) < 200

# We make an if statement that makes the program say "Registration complete" when all three conditions are fulfilled
        # and that the program should tell which input is not correct if the conditions is not fulfilled.
        if condition1 and condition2 and condition3:
            print('Registration Complete')
            self.pushButton.setText("Registration Complete")
            self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0)")
        elif condition1 == False:
            print('The entered CPR-number is invalid')
            self.pushButton.setText("Registration not complete")
            self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.textEdit_cprfejl.setGeometry(QtCore.QRect(600, 135, 141, 50))
            self.textEdit_cprfejl.setStyleSheet("color: rgb(255, 0, 0)")
        elif condition2 == False:
            print('Response should be either "Yes" or "No"')
            self.pushButton.setText("Registration not complete")
            self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.textEdit_svarfejl.setGeometry(QtCore.QRect(600, 195, 141, 50))
            self.textEdit_svarfejl.setStyleSheet("color: rgb(255, 0, 0)")
        elif condition3 == False:
            print('Weight is not between 30 and 200 kilograms')
            self.pushButton.setText("Registration not complete")
            self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.textEdit_weightfejl.setGeometry(QtCore.QRect(600, 250, 141, 50))
            self.textEdit_weightfejl.setStyleSheet("color: rgb(255, 0, 0)")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#132d90;\">Registration of patient</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPR-number<span style=\" color:#fb0008; vertical-align:super;\">*</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date of positive pregnancy test<span style=\" color:#fc0a07; vertical-align:super;\">*</span> graviditetstest</p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Weight<span style=\" color:#fb0006; vertical-align:super;\">*</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Other</p></body></html>"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Partner<span style=\" color:#fb0008; vertical-align:super;\">*</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_cprfejl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*The entered CPR-number is invalid*<span style=\" color:#fb0006; vertical-align:super;\"></span></p></body></html>"))
        self.textEdit_svarfejl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*Response shold be either 'Yes' or 'No'*<span style=\" color:#fb0006; vertical-align:super;\"></span></p></body></html>"))
        self.textEdit_weightfejl.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">*Weight is not between 30 and 200 kilograms*<span style*=\" color:#fb0006; vertical-align:super;\"></span></p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Register new patient"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
