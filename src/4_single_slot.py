#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QGridLayout, QLCDNumber, QLabel, QSlider, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        label_ = QLabel("label", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(label_)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        gbox = QGridLayout()
        gbox.addLayout(vbox, 1, 1)

        self.setLayout(gbox)

        lnum = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        sld.valueChanged.connect(lnum.display)
        vbox.addWidget(lnum)
        vbox.addWidget(sld)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
