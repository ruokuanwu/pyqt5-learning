from PyQt5.QtCore import QParallelAnimationGroup
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QToolTip, QWidget
import sys


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("Fira Code", 10))

        self.setToolTip("这是提示")

        btn = QPushButton("这是按钮", self)
        btn.setToolTip("这是按钮的提示 tip")
        btn.resize(btn.sizeHint())
        # 绑定按钮事件
        btn.clicked.connect(QApplication.instance().quit)
        btn.move(50, 50)

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
