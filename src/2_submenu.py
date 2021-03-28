from PyQt5.QtCore import QParallelAnimationGroup
from PyQt5.QtGui import QFont, QIcon, QWindow
from PyQt5.QtWidgets import QAction, QApplication, QDesktopWidget, QMainWindow, QMenu, QPushButton, QToolTip, QWidget, qApp
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
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self, checkable=True)
        impAct.setCheckable(True)
        impAct.triggered.connect(self.checkAction)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.show()

    def checkAction(self, status):
        if status:
            self.statusBar().showMessage("已经选中")
        else:
            self.statusBar().showMessage("取消选中")

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
