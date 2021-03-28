from PyQt5.QtCore import QParallelAnimationGroup
from PyQt5.QtGui import QFont, QIcon, QWindow
from PyQt5.QtWidgets import QAction, QApplication, QDesktopWidget, QMainWindow, QPushButton, QToolTip, QWidget, qApp
import sys


class MyWindow(QMainWindow):

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

        self.center()
        self.resize(100, 100)
        self.setWindowTitle("这是窗口")
        self.setWindowIcon(QIcon("asset\icon.png"))

        self.statusBar().showMessage("这是状态栏")

        # 菜单栏
        exit_action = QAction('&exit', self)
        exit_action.setShortcut('ctrl+q')
        exit_action.setStatusTip('退出')
        exit_action.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&file')
        file_menu.addAction(exit_action)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)

    w = MyWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
