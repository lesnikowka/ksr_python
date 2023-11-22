import sys
from PyQt5 import QtWidgets
import design
from matplotlib import pyplot as plt
from PyQt5.QtGui import QPixmap
import cv2
import imutils

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startCalcMain.clicked.connect(self.drawMain)
        self.startCalcTest.clicked.connect(self.drawTest)

    def resizeImage(self, imageName, height):
        image = cv2.imread(imageName)
        resized = imutils.resize(image, height=height)

        cv2.imwrite(imageName, resized)

    def drawMain(self):
        graphName = "graphMain.png"

        x = [i for i in range(1000)]
        y = [i * i for i in x]

        plt.plot(x, y)
        plt.savefig(graphName)
        plt.clf()

        size = self.graph1Main.size()
        height = size.height()
        self.resizeImage(graphName, height)

        pixmap = QPixmap(graphName)
        self.graph1Main.setPixmap(pixmap)

        size = self.graph2Main.size()
        height = size.height()

        pixmap = QPixmap(graphName)
        self.graph2Main.setPixmap(pixmap)


    def drawTest(self):
        graphName = "graphTest.png"

        x = [i for i in range(1000)]
        y = [i * i * i for i in x]

        plt.subplot(111)
        plt.plot(x, y)
        plt.savefig(graphName)
        plt.clf()

        size = self.graph1Test.size()
        height = size.height()
        self.resizeImage(graphName, height)

        pixmap = QPixmap(graphName)
        self.graph1Test.setPixmap(pixmap)

        size = self.graph2Test.size()
        height = size.height()

        pixmap = QPixmap(graphName)
        self.graph2Test.setPixmap(pixmap)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()