# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/converter_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 302)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 301))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.UrlLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.UrlLabel.setObjectName("UrlLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.UrlLabel)
        self.UrlText = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UrlText.sizePolicy().hasHeightForWidth())
        self.UrlText.setSizePolicy(sizePolicy)
        self.UrlText.setObjectName("UrlText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.UrlText)
        self.TitleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.TitleLabel)
        self.TitleText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.TitleText.setObjectName("TitleText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TitleText)
        self.ArtistLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ArtistLabel.setObjectName("ArtistLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ArtistLabel)
        self.ArtistText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ArtistText.setObjectName("ArtistText")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ArtistText)
        self.GenreLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.GenreLabel.setObjectName("GenreLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.GenreLabel)
        self.GenreText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.GenreText.setObjectName("GenreText")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.GenreText)
        self.FilenameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.FilenameLabel.setObjectName("FilenameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.FilenameLabel)
        self.FilenameText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.FilenameText.setObjectName("FilenameText")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.FilenameText)
        self.StartTimeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.StartTimeLabel.setObjectName("StartTimeLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.StartTimeLabel)
        self.StartTimeText = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartTimeText.sizePolicy().hasHeightForWidth())
        self.StartTimeText.setSizePolicy(sizePolicy)
        self.StartTimeText.setObjectName("StartTimeText")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.StartTimeText)
        self.EndTimeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.EndTimeLabel.setObjectName("EndTimeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.EndTimeLabel)
        self.EndTimeText = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndTimeText.sizePolicy().hasHeightForWidth())
        self.EndTimeText.setSizePolicy(sizePolicy)
        self.EndTimeText.setObjectName("EndTimeText")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.EndTimeText)
        self.FolderButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.FolderButton.setObjectName("FolderButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.FolderButton)
        self.FolderText = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.FolderText.setEnabled(False)
        self.FolderText.setObjectName("FolderText")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.FolderText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DownloadButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.DownloadButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadButton.sizePolicy().hasHeightForWidth())
        self.DownloadButton.setSizePolicy(sizePolicy)
        self.DownloadButton.setObjectName("DownloadButton")
        self.horizontalLayout.addWidget(self.DownloadButton)
        self.InfoButton = QtWidgets.QToolButton(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.InfoButton.sizePolicy().hasHeightForWidth())
        self.InfoButton.setSizePolicy(sizePolicy)
        self.InfoButton.setMaximumSize(QtCore.QSize(30, 25))
        self.InfoButton.setText("")
        self.InfoButton.setObjectName("InfoButton")
        self.horizontalLayout.addWidget(self.InfoButton)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 10, 161, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FormatLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormatLabel.sizePolicy().hasHeightForWidth())
        self.FormatLabel.setSizePolicy(sizePolicy)
        self.FormatLabel.setObjectName("FormatLabel")
        self.verticalLayout.addWidget(self.FormatLabel)
        self.FormatList = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormatList.sizePolicy().hasHeightForWidth())
        self.FormatList.setSizePolicy(sizePolicy)
        self.FormatList.setObjectName("FormatList")
        self.verticalLayout.addWidget(self.FormatList)
        self.KeepOriginalBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.KeepOriginalBox.setObjectName("KeepOriginalBox")
        self.verticalLayout.addWidget(self.KeepOriginalBox)
        self.TrimOriginalBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.TrimOriginalBox.setObjectName("TrimOriginalBox")
        self.verticalLayout.addWidget(self.TrimOriginalBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UrlLabel.setText(_translate("MainWindow", "Enter URL*: "))
        self.TitleLabel.setText(_translate("MainWindow", "Enter Title: "))
        self.ArtistLabel.setText(_translate("MainWindow", "Enter Artist: "))
        self.GenreLabel.setText(_translate("MainWindow", "Enter Genre: "))
        self.FilenameLabel.setText(_translate("MainWindow", "Enter Filename: "))
        self.StartTimeLabel.setText(_translate("MainWindow", "Start Time:"))
        self.EndTimeLabel.setText(_translate("MainWindow", "End Time:"))
        self.FolderButton.setText(_translate("MainWindow", "Choose Folder"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.FormatLabel.setText(_translate("MainWindow", "Supported Formats:"))
        self.KeepOriginalBox.setText(_translate("MainWindow", "Keep Original"))
        self.TrimOriginalBox.setText(_translate("MainWindow", "Keep Trimmed Original"))
