# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/progress.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProgressBarDialog(object):
    def setupUi(self, ProgressBarDialog):
        ProgressBarDialog.setObjectName("ProgressBarDialog")
        ProgressBarDialog.resize(485, 119)
        self.SuccessButton = QtWidgets.QPushButton(ProgressBarDialog)
        self.SuccessButton.setEnabled(False)
        self.SuccessButton.setGeometry(QtCore.QRect(180, 80, 100, 32))
        self.SuccessButton.setObjectName("SuccessButton")
        self.layoutWidget = QtWidgets.QWidget(ProgressBarDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(24, 10, 441, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProgressLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProgressLabel.sizePolicy().hasHeightForWidth())
        self.ProgressLabel.setSizePolicy(sizePolicy)
        self.ProgressLabel.setText("")
        self.ProgressLabel.setObjectName("ProgressLabel")
        self.horizontalLayout.addWidget(self.ProgressLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.ProgressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.ProgressBar.setProperty("value", 24)
        self.ProgressBar.setObjectName("ProgressBar")
        self.verticalLayout_2.addWidget(self.ProgressBar)

        self.retranslateUi(ProgressBarDialog)
        QtCore.QMetaObject.connectSlotsByName(ProgressBarDialog)

    def retranslateUi(self, ProgressBarDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressBarDialog.setWindowTitle(_translate("ProgressBarDialog", "Dialog"))
        self.SuccessButton.setText(_translate("ProgressBarDialog", "Close"))
