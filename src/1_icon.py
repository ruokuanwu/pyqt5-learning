from PyQt5.QtCore import QParallelAnimationGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
import sys


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle("这是窗口")
        self.setWindowIcon(QIcon("asset\icon.png"))
        self.show()


def main():
    app = QApplication(sys.argv)

    w = MyWidget()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
