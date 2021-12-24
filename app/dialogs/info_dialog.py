# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(711, 338)
        self.layoutWidget = QtWidgets.QWidget(InfoDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 675, 277))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.URLLabel = QtWidgets.QLabel(self.layoutWidget)
        self.URLLabel.setWordWrap(True)
        self.URLLabel.setObjectName("URLLabel")
        self.verticalLayout.addWidget(self.URLLabel)
        self.MetaLabel = QtWidgets.QLabel(self.layoutWidget)
        self.MetaLabel.setWordWrap(True)
        self.MetaLabel.setObjectName("MetaLabel")
        self.verticalLayout.addWidget(self.MetaLabel)
        self.TrimLabel = QtWidgets.QLabel(self.layoutWidget)
        self.TrimLabel.setWordWrap(True)
        self.TrimLabel.setObjectName("TrimLabel")
        self.verticalLayout.addWidget(self.TrimLabel)
        self.FolderLabel = QtWidgets.QLabel(self.layoutWidget)
        self.FolderLabel.setWordWrap(True)
        self.FolderLabel.setObjectName("FolderLabel")
        self.verticalLayout.addWidget(self.FolderLabel)
        self.FilenameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.FilenameLabel.setWordWrap(True)
        self.FilenameLabel.setObjectName("FilenameLabel")
        self.verticalLayout.addWidget(self.FilenameLabel)
        self.FormatLabel = QtWidgets.QLabel(self.layoutWidget)
        self.FormatLabel.setWordWrap(True)
        self.FormatLabel.setObjectName("FormatLabel")
        self.verticalLayout.addWidget(self.FormatLabel)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.CloseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.CloseButton.setObjectName("CloseButton")
        self.gridLayout.addWidget(self.CloseButton, 1, 0, 1, 1)

        self.retranslateUi(InfoDialog)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        _translate = QtCore.QCoreApplication.translate
        InfoDialog.setWindowTitle(_translate("InfoDialog", "Dialog"))
        self.URLLabel.setText(_translate("InfoDialog", "URL: Link to the Youtube video. Only required piece of information"))
        self.MetaLabel.setText(_translate("InfoDialog", "Title, Artist, Genre: Optional metadata can be added to the downloaded file"))
        self.TrimLabel.setText(_translate("InfoDialog", "Start time, End time: Optional times used to trim the audio\'s beginning and end"))
        self.FolderLabel.setText(_translate("InfoDialog", "Choose Folder: If no folder is chosen, defaults to home directory. Saves chosen folder each time"))
        self.FilenameLabel.setText(_translate("InfoDialog", "Filename: If no filename is entered, default is the title of the Youtube video. Do not enter the extension"))
        self.FormatLabel.setText(_translate("InfoDialog", "List Formats: Lists the available formats of the downloaded video. Default is .mp3"))
        self.label.setText(_translate("InfoDialog", "Keep Original Audio/Video: Saves the originally downloaded file before the conversion to your specified format"))
        self.label_2.setText(_translate("InfoDialog", "Keep Trimmed Original Audio/Video: Same as Keep Original with trimming applied to the original file"))
        self.CloseButton.setText(_translate("InfoDialog", "Close"))
