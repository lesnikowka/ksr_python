# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 834)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rootTabControl = QtWidgets.QTabWidget(self.centralwidget)
        self.rootTabControl.setGeometry(QtCore.QRect(0, 0, 1091, 801))
        self.rootTabControl.setObjectName("rootTabControl")
        self.testTab = QtWidgets.QWidget()
        self.testTab.setObjectName("testTab")
        self.startCalcTest = QtWidgets.QPushButton(self.testTab)
        self.startCalcTest.setGeometry(QtCore.QRect(10, 50, 161, 28))
        self.startCalcTest.setObjectName("startCalcTest")
        self.textEdit_2 = QtWidgets.QTextEdit(self.testTab)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 10, 141, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.testTab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 21, 19))
        self.label_2.setObjectName("label_2")
        self.graph1Test = QtWidgets.QLabel(self.testTab)
        self.graph1Test.setGeometry(QtCore.QRect(260, 30, 421, 301))
        self.graph1Test.setObjectName("graph1Test")
        self.graph2Test = QtWidgets.QLabel(self.testTab)
        self.graph2Test.setGeometry(QtCore.QRect(270, 370, 421, 301))
        self.graph2Test.setObjectName("graph2Test")
        self.rootTabControl.addTab(self.testTab, "")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.startCalcMain = QtWidgets.QPushButton(self.mainTab)
        self.startCalcMain.setGeometry(QtCore.QRect(10, 70, 161, 28))
        self.startCalcMain.setObjectName("startCalcMain")
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setGeometry(QtCore.QRect(10, 30, 21, 19))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.mainTab)
        self.textEdit.setGeometry(QtCore.QRect(40, 20, 141, 31))
        self.textEdit.setObjectName("textEdit")
        self.graph1Main = QtWidgets.QLabel(self.mainTab)
        self.graph1Main.setGeometry(QtCore.QRect(270, 50, 421, 301))
        self.graph1Main.setObjectName("graph1Main")
        self.label_6 = QtWidgets.QLabel(self.mainTab)
        self.label_6.setGeometry(QtCore.QRect(280, 380, 421, 301))
        self.label_6.setObjectName("label_6")
        self.rootTabControl.addTab(self.mainTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.rootTabControl.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startCalcTest.setText(_translate("MainWindow", "Начать вычисления"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "N:"))
        self.graph1Test.setText(_translate("MainWindow", "TextLabel"))
        self.graph2Test.setText(_translate("MainWindow", "TextLabel"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.testTab), _translate("MainWindow", "Тестовая"))
        self.startCalcMain.setText(_translate("MainWindow", "Начать вычисления"))
        self.label.setText(_translate("MainWindow", "N:"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.graph1Main.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.mainTab), _translate("MainWindow", "Основная"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
