#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we reimplement an
event handler.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.qlabel = QLabel("self.text", self)

        self.setMouseTracking(True)
        self.setGeometry(300, 300, 550, 550)
        self.setWindowTitle('Event handler')
        self.show()

    def mouseMoveEvent(self, a0):
        # print(a0)
        # text = ' x: '+a0.x()+', y: '+a0.y()
        self.qlabel.setText('text')

        # return super().mouseMoveEvent(a0)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


# #!/usr/bin/python

# """
# ZetCode PyQt5 tutorial

# In this example, we display the x and y
# coordinates of a mouse pointer in a label widget.

# Author: Jan Bodnar
# Website: zetcode.com
# """

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # grid = QGridLayout()

#         # x = 0
#         # y = 0

#         # self.text = f'x: {x},  y: {y}'

#         self.label = QLabel('self.text', self)
#         # grid.addWidget(self.label, 0, 0, Qt.AlignTop)

#         self.setMouseTracking(True)

#         # self.setLayout(grid)

#         self.setGeometry(300, 300, 450, 300)
#         self.setWindowTitle('Event object')
#         self.show()

#     def mouseMoveEvent(self, e):
#         x = e.x()
#         y = e.y()

#         text = f'x: {x},  y: {y}'
#         self.label.setText('text')


# def main():
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()
