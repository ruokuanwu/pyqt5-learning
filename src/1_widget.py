import PyQt5
import sys
import cv2
from PyQt5.QtWidgets import *


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(100, 100)
    w.move(300, 300)
    w.setWindowTitle("这是一个窗口")
    w.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
