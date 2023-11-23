import sys
from PyQt5 import QtWidgets
import design
from matplotlib import pyplot as plt
from PyQt5.QtGui import QPixmap
import cv2
import imutils
import method

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startCalcMain.clicked.connect(self.drawMain)
        self.startCalcTest.clicked.connect(self.drawTest)

        self.tableMain.setColumnCount(5)  # Set three columns
        self.tableMain.setRowCount(1)
        self.tableMain.setHorizontalHeaderLabels(["Номер узла", "X", "V", "V*", "|V-V*|"])

        self.tableTest.setColumnCount(5)  # Set three columns
        self.tableTest.setRowCount(1)
        self.tableTest.setHorizontalHeaderLabels(["Номер узла", "X", "U", "V", "|U-V|"])

    def resizeImage(self, imageName, height):
        image = cv2.imread(imageName)
        resized = imutils.resize(image, height=height)

        cv2.imwrite(imageName, resized)

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


    def drawTest(self):
        graph1Name = "graph1Test.png"
        graph2Name = "graph2Test.png"

        N = 0

        try:
            N = int(self.gridNumberMain.toPlainText())
        except BaseException:
            return

        x, y, y2 = method.calculate("test", N)
        diff = [abs(y[i] - y2[i]) for i in range(len(y))]

        plt.plot(x, y)
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


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()