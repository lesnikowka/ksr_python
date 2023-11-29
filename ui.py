import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTabWidget, QTableWidgetItem, QHeaderView
import design
from PyQt5.QtGui import QPixmap
import cv2
import imutils
import KSR
import subprocess



class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.drawMain)
        self.pushButton.clicked.connect(self.showHelp)

        self.table.setColumnCount(7)
        self.table.setRowCount(1)
        self.table.setHorizontalHeaderLabels(["Номер узла: строка", "Номер узла: столбец", "T", "X", "V", "V*", "|V-V*|"])
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.table.verticalHeader().hide()


        self.infoText = """
Для решения задачи использована равномерная сетка с числом разбиений по x: %, по t: % 
0 <= x <= 1
0 <= t <= %
|V-V*| максимален и равен % при x=%, t = %;"""

    def fillInfo(self, data):
        text = self.infoText
        for val in data:
            text = text.replace("%", str(val), 1)
        self.infoMain.clear()
        self.infoMain.append(text)



    def resizeImage(self, imageName, height):
        image = cv2.imread(imageName)
        resized = imutils.resize(image, height=height)

        cv2.imwrite(imageName, resized)

    def addRowToTable(self, table, data):
        table.insertRow(table.rowCount())
        rowCount = table.rowCount()
        columnCount = table.columnCount()
        for j in range(columnCount):
            table.setItem(rowCount-1, j, QTableWidgetItem(str(data[j])))

    def clearTable(self, table):
        rowCount = table.rowCount()
        for i in range(0, rowCount - 1):
            table.removeRow(1)


    def drawMain(self):
        first2d_ = "first2d.png"
        second2d_ = "second2d.png"
        plane3d_ = "3d.png"
        N_ = 0
        M_ = 0
        Tm_ = 0

        try:
            N_ = int(self.N.toPlainText())
            M_ = int(self.M.toPlainText())
            Tm_ = int(self.Tm.toPlainText())

        except BaseException:
            return

        v, x, t, v2, x2, t2 = KSR.calculate(N_, M_, Tm_)

        size = self.first2d.size()
        height = size.height()
        self.resizeImage(first2d_, height)
        pixmap = QPixmap(first2d_)
        self.first2d.setPixmap(pixmap)

        size = self.second2d.size()
        height = size.height()
        self.resizeImage(second2d_, height)
        pixmap = QPixmap(second2d_)
        self.second2d.setPixmap(pixmap)

        size = self.plane3d.size()
        height = size.height()
        self.resizeImage(plane3d_, height)
        pixmap = QPixmap(plane3d_)
        self.plane3d.setPixmap(pixmap)

        self.clearTable(self.table)

        maxabs = 0
        maxabs_x = 0
        maxabs_t = 0

        for i in range(len(x)):
            for j in range(len(v[i])):
                curabs = abs(v[i][j]-v2[i][j])
                if curabs > maxabs:
                    maxabs = curabs
                    maxabs_x = x[i]
                    maxabs_t = t[j]
                self.addRowToTable(self.table, [i, j, t[j], x[i], v[i][j], v2[i][j], abs(v[i][j]-v2[i][j])])

        self.fillInfo([N_, M_, Tm_, maxabs, maxabs_x, maxabs_t])




    def showHelp(self):
        subprocess.run("python helpui.py")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()