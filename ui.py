import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTabWidget, QTableWidgetItem
import design
from matplotlib import pyplot as plt
from PyQt5.QtGui import QPixmap
import cv2
import imutils
import method
from PyQt5.QtCore import QSize, Qt

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startCalcMain.clicked.connect(self.drawMain)
        self.startCalcTest.clicked.connect(self.drawTest)
        self.drawAccuracyButton.clicked.connect(self.drawAccuracy)

        self.tableMain.setColumnCount(5)  # Set three columns
        self.tableMain.setRowCount(1)
        self.tableMain.setHorizontalHeaderLabels(["Номер узла", "X", "V", "V*", "|V-V*|"])
        self.tableMain.verticalHeader().hide()

        self.tableTest.setColumnCount(5)  # Set three columns
        self.tableTest.setRowCount(1)
        self.tableTest.setHorizontalHeaderLabels(["Номер узла", "X", "V", "U", "|U-V|"])
        self.tableTest.verticalHeader().hide()

        self.infoText = """
Для решения задачи использована равномерная сетка с числом разбиений n = %;

задача должна быть решена с заданной точностью ε = 0.5⋅10 –6; 

задача решена с точностью ε2 = %; 

максимальная разность численных решений в общих узлах сетки наблюдается в точке x=%;"""

    def fillInfo(self, taskName, data):
        text = self.infoText
        for val in data:
            text = text.replace("%", str(val), 1)
        if taskName == "main":
            self.infoMain.clear()
            self.infoMain.append(text)
        else:
            self.infoTest.clear()
            self.infoTest.append(text)


    def resizeImage(self, imageName, height):
        image = cv2.imread(imageName)
        resized = imutils.resize(image, height=height)

        cv2.imwrite(imageName, resized)

    def addRowToTable(self, table, data):
        table.insertRow(table.rowCount())
        rowCount = table.rowCount()
        columnCount = table.columnCount()
        for j in range(columnCount):
            table.setItem(rowCount-1, j, QTableWidgetItem(str(data[j])[:10]))

    def clearTable(self, table):
        rowCount = table.rowCount()
        for i in range(0, rowCount - 1):
            table.removeRow(1)


    def drawMain(self):
        graph1Name = "graph1Main.png"
        graph2Name = "graph2Main.png"

        N = 0

        try:
            N = int(self.gridNumberMain.toPlainText())
        except BaseException:
            return

        x, y, x2, y2 = method.calculate("main", N)
        y2 = [y2[2 * i] for i in range(len(y))]
        diff = [abs(y[i] - y2[i]) for i in range(len(y))]

        plt.plot(x, y)
        plt.savefig(graph1Name)
        plt.clf()

        plt.plot(x, diff)
        plt.savefig(graph2Name)
        plt.clf()

        size = self.graph1Main.size()
        height = size.height()
        self.resizeImage(graph1Name, height)
        pixmap = QPixmap(graph1Name)
        self.graph1Main.setPixmap(pixmap)

        size = self.graph2Main.size()
        height = size.height()
        self.resizeImage(graph2Name, height)
        pixmap = QPixmap(graph2Name)
        self.graph2Main.setPixmap(pixmap)

        self.clearTable(self.tableMain)

        for i in range(len(x)):
            self.addRowToTable(self.tableMain, [i, x[i], y[i], y2[i], diff[i]])

        maxdiff = max(diff)
        maxdiffIndex = diff.index(maxdiff)
        self.fillInfo("main", [N, maxdiff, x[maxdiffIndex]])

    def drawTest(self):
        graph1Name = "graph1Test.png"
        graph2Name = "graph2Test.png"

        N = 0

        try:
            N = int(self.gridNumberTest.toPlainText())
        except BaseException:
            return

        x, y, y2 = method.calculate("test", N)
        diff = [abs(y[i] - y2[i]) for i in range(len(y))]

        plt.title("Синий - численное решение")
        plt.plot(x, y)
        plt.plot(x, y2)
        plt.savefig(graph1Name)
        plt.clf()

        plt.plot(x, diff)
        plt.savefig(graph2Name)
        plt.clf()

        size = self.graph1Test.size()
        height = size.height()
        self.resizeImage(graph1Name, height)
        pixmap = QPixmap(graph1Name)
        self.graph1Test.setPixmap(pixmap)

        size = self.graph2Test.size()
        height = size.height()
        self.resizeImage(graph2Name, height)
        pixmap = QPixmap(graph2Name)
        self.graph2Test.setPixmap(pixmap)

        self.clearTable(self.tableTest)

        for i in range(len(x)):
            self.addRowToTable(self.tableTest, [i, x[i], y[i], y2[i], diff[i]])

        maxdiff = max(diff)
        maxdiffIndex = diff.index(maxdiff)
        self.fillInfo("test", [N, maxdiff, x[maxdiffIndex]])

    def drawAccuracy(self):
        graphName = "accuracyGraph.png"

        minN = 0
        maxN = 0
        step = 0
        mult = 0

        try:
            minN = int(self.minStep.toPlainText())
            maxN = int(self.maxStep.toPlainText())
            step = int(self.step.toPlainText())
            mult = int(self.mult.toPlainText())
        except BaseException:
            return


        N = []
        acc = []

        for i in range(minN, maxN + 1, step):
            x, y, y2 = method.calculate("test", i)
            diff = [abs(y[j] - y2[j]) for j in range(len(y))]
            maxdiff = max(diff)
            N.append(i)
            acc.append(maxdiff)


        plt.figure(figsize=[16,10])
        plt.plot(N, acc)
        plt.savefig(graphName)
        plt.clf()
        plt.figure(figsize=[8, 6])

        size = self.graphAccuracy.size()
        height = size.height()
        self.resizeImage(graphName, height)
        pixmap = QPixmap(graphName)
        self.graphAccuracy.setPixmap(pixmap)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()