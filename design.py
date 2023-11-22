# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1389, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rootTabControl = QtWidgets.QTabWidget(self.centralwidget)
        self.rootTabControl.setGeometry(QtCore.QRect(0, 0, 1381, 881))
        self.rootTabControl.setObjectName("rootTabControl")
        self.testTab = QtWidgets.QWidget()
        self.testTab.setObjectName("testTab")
        self.startCalcTest = QtWidgets.QPushButton(self.testTab)
        self.startCalcTest.setGeometry(QtCore.QRect(10, 50, 161, 28))
        self.startCalcTest.setObjectName("startCalcTest")
        self.gridNumberTest = QtWidgets.QTextEdit(self.testTab)
        self.gridNumberTest.setGeometry(QtCore.QRect(40, 10, 141, 31))
        self.gridNumberTest.setObjectName("gridNumberTest")
        self.label_2 = QtWidgets.QLabel(self.testTab)
        self.label_2.setGeometry(QtCore.QRect(10, 15, 21, 19))
        self.label_2.setObjectName("label_2")
        self.graph1Test = QtWidgets.QLabel(self.testTab)
        self.graph1Test.setGeometry(QtCore.QRect(270, 0, 700, 430))
        self.graph1Test.setText("")
        self.graph1Test.setObjectName("graph1Test")
        self.graph2Test = QtWidgets.QLabel(self.testTab)
        self.graph2Test.setGeometry(QtCore.QRect(270, 420, 700, 430))
        self.graph2Test.setText("")
        self.graph2Test.setObjectName("graph2Test")
        self.rootTabControl.addTab(self.testTab, "")
        self.accuracy = QtWidgets.QWidget()
        self.accuracy.setObjectName("accuracy")
        self.label_3 = QtWidgets.QLabel(self.accuracy)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 1361, 821))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.rootTabControl.addTab(self.accuracy, "")
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.startCalcMain = QtWidgets.QPushButton(self.mainTab)
        self.startCalcMain.setGeometry(QtCore.QRect(10, 50, 161, 28))
        self.startCalcMain.setObjectName("startCalcMain")
        self.label = QtWidgets.QLabel(self.mainTab)
        self.label.setGeometry(QtCore.QRect(10, 15, 21, 19))
        self.label.setObjectName("label")
        self.gridNumberMain = QtWidgets.QTextEdit(self.mainTab)
        self.gridNumberMain.setGeometry(QtCore.QRect(40, 10, 141, 31))
        self.gridNumberMain.setObjectName("gridNumberMain")
        self.graph1Main = QtWidgets.QLabel(self.mainTab)
        self.graph1Main.setGeometry(QtCore.QRect(270, 0, 700, 430))
        self.graph1Main.setText("")
        self.graph1Main.setObjectName("graph1Main")
        self.graph2Main = QtWidgets.QLabel(self.mainTab)
        self.graph2Main.setGeometry(QtCore.QRect(270, 420, 700, 430))
        self.graph2Main.setText("")
        self.graph2Main.setObjectName("graph2Main")
        self.rootTabControl.addTab(self.mainTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1389, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.rootTabControl.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startCalcTest.setText(_translate("MainWindow", "Начать вычисления"))
        self.gridNumberTest.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "N:"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.testTab), _translate("MainWindow", "Тестовая"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.accuracy), _translate("MainWindow", "График точности для тестовой задачи"))
        self.startCalcMain.setText(_translate("MainWindow", "Начать вычисления"))
        self.label.setText(_translate("MainWindow", "N:"))
        self.gridNumberMain.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">100</p></body></html>"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.mainTab), _translate("MainWindow", "Основная"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
