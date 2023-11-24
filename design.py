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
        MainWindow.resize(1677, 901)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rootTabControl = QtWidgets.QTabWidget(self.centralwidget)
        self.rootTabControl.setGeometry(QtCore.QRect(0, 0, 1681, 881))
        self.rootTabControl.setObjectName("rootTabControl")
        self.testTab = QtWidgets.QWidget()
        self.testTab.setObjectName("testTab")
        self.startCalcTest = QtWidgets.QPushButton(self.testTab)
        self.startCalcTest.setGeometry(QtCore.QRect(10, 50, 161, 28))
        self.startCalcTest.setObjectName("startCalcTest")
        self.gridNumberTest = QtWidgets.QTextEdit(self.testTab)
        self.gridNumberTest.setGeometry(QtCore.QRect(40, 10, 140, 30))
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
        self.tableTest = QtWidgets.QTableWidget(self.testTab)
        self.tableTest.setGeometry(QtCore.QRect(850, 0, 820, 840))
        self.tableTest.setObjectName("tableTest")
        self.tableTest.setColumnCount(0)
        self.tableTest.setRowCount(0)
        self.infoTest = QtWidgets.QTextEdit(self.testTab)
        self.infoTest.setGeometry(QtCore.QRect(10, 90, 240, 320))
        self.infoTest.setReadOnly(True)
        self.infoTest.setObjectName("infoTest")
        self.rootTabControl.addTab(self.testTab, "")
        self.accuracy = QtWidgets.QWidget()
        self.accuracy.setObjectName("accuracy")
        self.label_3 = QtWidgets.QLabel(self.accuracy)
        self.label_3.setGeometry(QtCore.QRect(10, 15, 171, 19))
        self.label_3.setObjectName("label_3")
        self.minStep = QtWidgets.QTextEdit(self.accuracy)
        self.minStep.setGeometry(QtCore.QRect(10, 40, 100, 30))
        self.minStep.setObjectName("minStep")
        self.label_4 = QtWidgets.QLabel(self.accuracy)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 171, 16))
        self.label_4.setObjectName("label_4")
        self.maxStep = QtWidgets.QTextEdit(self.accuracy)
        self.maxStep.setGeometry(QtCore.QRect(10, 105, 100, 30))
        self.maxStep.setObjectName("maxStep")
        self.label_5 = QtWidgets.QLabel(self.accuracy)
        self.label_5.setGeometry(QtCore.QRect(10, 145, 55, 16))
        self.label_5.setObjectName("label_5")
        self.step = QtWidgets.QTextEdit(self.accuracy)
        self.step.setGeometry(QtCore.QRect(10, 170, 100, 30))
        self.step.setObjectName("step")
        self.label_6 = QtWidgets.QLabel(self.accuracy)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 151, 16))
        self.label_6.setObjectName("label_6")
        self.mult = QtWidgets.QTextEdit(self.accuracy)
        self.mult.setGeometry(QtCore.QRect(10, 235, 100, 30))
        self.mult.setObjectName("mult")
        self.drawAccuracyButton = QtWidgets.QPushButton(self.accuracy)
        self.drawAccuracyButton.setGeometry(QtCore.QRect(10, 280, 93, 28))
        self.drawAccuracyButton.setObjectName("drawAccuracyButton")
        self.graphAccuracy = QtWidgets.QLabel(self.accuracy)
        self.graphAccuracy.setGeometry(QtCore.QRect(210, 20, 1331, 811))
        self.graphAccuracy.setText("")
        self.graphAccuracy.setObjectName("graphAccuracy")
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
        self.gridNumberMain.setGeometry(QtCore.QRect(40, 10, 140, 30))
        self.gridNumberMain.setObjectName("gridNumberMain")
        self.graph1Main = QtWidgets.QLabel(self.mainTab)
        self.graph1Main.setGeometry(QtCore.QRect(270, 0, 700, 430))
        self.graph1Main.setText("")
        self.graph1Main.setObjectName("graph1Main")
        self.graph2Main = QtWidgets.QLabel(self.mainTab)
        self.graph2Main.setEnabled(True)
        self.graph2Main.setGeometry(QtCore.QRect(270, 420, 700, 430))
        self.graph2Main.setText("")
        self.graph2Main.setObjectName("graph2Main")
        self.tableMain = QtWidgets.QTableWidget(self.mainTab)
        self.tableMain.setGeometry(QtCore.QRect(850, 0, 820, 840))
        self.tableMain.setObjectName("tableMain")
        self.tableMain.setColumnCount(0)
        self.tableMain.setRowCount(0)
        self.infoMain = QtWidgets.QTextEdit(self.mainTab)
        self.infoMain.setEnabled(True)
        self.infoMain.setGeometry(QtCore.QRect(10, 90, 240, 320))
        self.infoMain.setReadOnly(True)
        self.infoMain.setObjectName("infoMain")
        self.rootTabControl.addTab(self.mainTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1677, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.rootTabControl.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startCalcTest.setText(_translate("MainWindow", "Начать вычисления"))
        self.gridNumberTest.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.6pt;\">100</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "N:"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.testTab), _translate("MainWindow", "Тестовая"))
        self.label_3.setText(_translate("MainWindow", "Минимальное число шагов:"))
        self.minStep.setMarkdown(_translate("MainWindow", "10\n"
"\n"
""))
        self.label_4.setText(_translate("MainWindow", "Максимальное число шагов:"))
        self.maxStep.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Шаг:"))
        self.step.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Константа домножения:"))
        self.mult.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>"))
        self.drawAccuracyButton.setText(_translate("MainWindow", "Построить"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.accuracy), _translate("MainWindow", "График точности для тестовой задачи"))
        self.startCalcMain.setText(_translate("MainWindow", "Начать вычисления"))
        self.label.setText(_translate("MainWindow", "N:"))
        self.gridNumberMain.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9.6pt;\">100</span></p></body></html>"))
        self.rootTabControl.setTabText(self.rootTabControl.indexOf(self.mainTab), _translate("MainWindow", "Основная"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
