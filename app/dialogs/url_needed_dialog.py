# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/need_url.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_URLNeeded(object):
    def setupUi(self, URLNeeded):
        URLNeeded.setObjectName("URLNeeded")
        URLNeeded.resize(400, 106)
        self.layoutWidget = QtWidgets.QWidget(URLNeeded)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 20, 221, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.InfoLabel = QtWidgets.QLabel(self.layoutWidget)
        self.InfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InfoLabel.setObjectName("InfoLabel")
        self.gridLayout.addWidget(self.InfoLabel, 0, 0, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout.addWidget(self.CloseButton, 1, 0, 1, 1)

        self.retranslateUi(URLNeeded)
        QtCore.QMetaObject.connectSlotsByName(URLNeeded)

    def retranslateUi(self, URLNeeded):
        _translate = QtCore.QCoreApplication.translate
        URLNeeded.setWindowTitle(_translate("URLNeeded", "Dialog"))
        self.InfoLabel.setText(_translate("URLNeeded", "Missing or invalid URL."))
        self.CloseButton.setText(_translate("URLNeeded", "Close"))
