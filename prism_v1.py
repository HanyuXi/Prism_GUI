# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prism_v1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from filedialog import App

__version__ = "1.0.0"


class Ui_Main(object):
    """
    The Ui_Main class is the main window page. For this version, the 
    """

    def setupUi(self, Main):
        # The code below are created by Qt Designer.
        Main.setObjectName("Main")
        Main.resize(746, 402)
        Main.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 160, 301, 51))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.FileList = QtWidgets.QListView(self.centralwidget)
        self.FileList.setGeometry(QtCore.QRect(395, 11, 291, 261))
        self.FileList.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.FileList.setObjectName("FileList")
        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setGeometry(QtCore.QRect(130, 260, 101, 41))
        self.Convert.setStyleSheet("background-color: rgb(170, 170, 127);\n"
                                   "border-color: rgb(0, 0, 0);")
        self.Convert.setObjectName("Convert")
        # In this code, I have only programmed convert button to direct to filedialog module
        self.Convert.clicked.connect(self.UploadButtonClick)

        self.Download = QtWidgets.QPushButton(self.centralwidget)
        self.Download.setGeometry(QtCore.QRect(490, 280, 121, 31))
        self.Download.setStyleSheet("background-color: rgb(170, 170, 127);\n"
                                    "gridline-color: rgb(255, 170, 127);")
        self.Download.setObjectName("Download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 301, 61))
        self.label.setStyleSheet("font: italic 36pt \"Monotype Corsiva\";\n"
                                 "border-color: rgb(0, 0, 0);\n"
                                 "background-color: rgb(0, 0, 255);")
        self.label.setObjectName("label")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 18))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.Convert.setText(_translate("Main", "Upload"))
        self.Download.setText(_translate("Main", "Download"))
        self.label.setText(_translate("Main", "Prism PDF separator "))

    def UploadButtonClick(self):
        ex = App()
        ex.show()
        sys.exit(ex.close)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
