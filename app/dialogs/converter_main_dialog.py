# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\converter_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1225, 359)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.DownloadTab)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.UrlLabel = QtWidgets.QLabel(self.DownloadTab)
        self.UrlLabel.setObjectName("UrlLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.UrlLabel)
        self.UrlText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UrlText.sizePolicy().hasHeightForWidth())
        self.UrlText.setSizePolicy(sizePolicy)
        self.UrlText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.UrlText.setObjectName("UrlText")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.UrlText)
        self.TitleLabel = QtWidgets.QLabel(self.DownloadTab)
        self.TitleLabel.setObjectName("TitleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.TitleLabel)
        self.TitleText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleText.sizePolicy().hasHeightForWidth())
        self.TitleText.setSizePolicy(sizePolicy)
        self.TitleText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.TitleText.setObjectName("TitleText")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TitleText)
        self.ArtistLabel = QtWidgets.QLabel(self.DownloadTab)
        self.ArtistLabel.setObjectName("ArtistLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ArtistLabel)
        self.ArtistText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArtistText.sizePolicy().hasHeightForWidth())
        self.ArtistText.setSizePolicy(sizePolicy)
        self.ArtistText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.ArtistText.setObjectName("ArtistText")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ArtistText)
        self.GenreLabel = QtWidgets.QLabel(self.DownloadTab)
        self.GenreLabel.setObjectName("GenreLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.GenreLabel)
        self.GenreText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GenreText.sizePolicy().hasHeightForWidth())
        self.GenreText.setSizePolicy(sizePolicy)
        self.GenreText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.GenreText.setObjectName("GenreText")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.GenreText)
        self.AlbumLabel = QtWidgets.QLabel(self.DownloadTab)
        self.AlbumLabel.setObjectName("AlbumLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.AlbumLabel)
        self.AlbumText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AlbumText.sizePolicy().hasHeightForWidth())
        self.AlbumText.setSizePolicy(sizePolicy)
        self.AlbumText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.AlbumText.setObjectName("AlbumText")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.AlbumText)
        self.FilenameLabel = QtWidgets.QLabel(self.DownloadTab)
        self.FilenameLabel.setObjectName("FilenameLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.FilenameLabel)
        self.FilenameText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilenameText.sizePolicy().hasHeightForWidth())
        self.FilenameText.setSizePolicy(sizePolicy)
        self.FilenameText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.FilenameText.setObjectName("FilenameText")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.FilenameText)
        self.StartTimeLabel = QtWidgets.QLabel(self.DownloadTab)
        self.StartTimeLabel.setObjectName("StartTimeLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.StartTimeLabel)
        self.StartTimeText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartTimeText.sizePolicy().hasHeightForWidth())
        self.StartTimeText.setSizePolicy(sizePolicy)
        self.StartTimeText.setObjectName("StartTimeText")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.StartTimeText)
        self.EndTimeLabel = QtWidgets.QLabel(self.DownloadTab)
        self.EndTimeLabel.setObjectName("EndTimeLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.EndTimeLabel)
        self.EndTimeText = QtWidgets.QLineEdit(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndTimeText.sizePolicy().hasHeightForWidth())
        self.EndTimeText.setSizePolicy(sizePolicy)
        self.EndTimeText.setObjectName("EndTimeText")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.EndTimeText)
        self.FolderButton = QtWidgets.QPushButton(self.DownloadTab)
        self.FolderButton.setObjectName("FolderButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.FolderButton)
        self.FolderText = QtWidgets.QLineEdit(self.DownloadTab)
        self.FolderText.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FolderText.sizePolicy().hasHeightForWidth())
        self.FolderText.setSizePolicy(sizePolicy)
        self.FolderText.setMaximumSize(QtCore.QSize(410, 16777215))
        self.FolderText.setObjectName("FolderText")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.FolderText)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DownloadButton = QtWidgets.QPushButton(self.DownloadTab)
        self.DownloadButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DownloadButton.sizePolicy().hasHeightForWidth())
        self.DownloadButton.setSizePolicy(sizePolicy)
        self.DownloadButton.setMaximumSize(QtCore.QSize(380, 16777215))
        self.DownloadButton.setObjectName("DownloadButton")
        self.horizontalLayout.addWidget(self.DownloadButton)
        self.InfoButton = QtWidgets.QToolButton(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.InfoButton.sizePolicy().hasHeightForWidth())
        self.InfoButton.setSizePolicy(sizePolicy)
        self.InfoButton.setMaximumSize(QtCore.QSize(30, 25))
        self.InfoButton.setText("")
        self.InfoButton.setObjectName("InfoButton")
        self.horizontalLayout.addWidget(self.InfoButton)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FormatLabel = QtWidgets.QLabel(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormatLabel.sizePolicy().hasHeightForWidth())
        self.FormatLabel.setSizePolicy(sizePolicy)
        self.FormatLabel.setObjectName("FormatLabel")
        self.verticalLayout.addWidget(self.FormatLabel)
        self.FormatList = QtWidgets.QListWidget(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormatList.sizePolicy().hasHeightForWidth())
        self.FormatList.setSizePolicy(sizePolicy)
        self.FormatList.setMaximumSize(QtCore.QSize(205, 16777215))
        self.FormatList.setObjectName("FormatList")
        self.verticalLayout.addWidget(self.FormatList)
        self.label = QtWidgets.QLabel(self.DownloadTab)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.KeepOriginalAudioBox = QtWidgets.QCheckBox(self.DownloadTab)
        self.KeepOriginalAudioBox.setObjectName("KeepOriginalAudioBox")
        self.verticalLayout.addWidget(self.KeepOriginalAudioBox)
        self.TrimOriginalAudioBox = QtWidgets.QCheckBox(self.DownloadTab)
        self.TrimOriginalAudioBox.setObjectName("TrimOriginalAudioBox")
        self.verticalLayout.addWidget(self.TrimOriginalAudioBox)
        self.label_2 = QtWidgets.QLabel(self.DownloadTab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.KeepOriginalVideoBox = QtWidgets.QCheckBox(self.DownloadTab)
        self.KeepOriginalVideoBox.setObjectName("KeepOriginalVideoBox")
        self.verticalLayout.addWidget(self.KeepOriginalVideoBox)
        self.TrimOriginalVideoBox = QtWidgets.QCheckBox(self.DownloadTab)
        self.TrimOriginalVideoBox.setObjectName("TrimOriginalVideoBox")
        self.verticalLayout.addWidget(self.TrimOriginalVideoBox)
        self.label_3 = QtWidgets.QLabel(self.DownloadTab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.iTunesFormatBox = QtWidgets.QCheckBox(self.DownloadTab)
        self.iTunesFormatBox.setObjectName("iTunesFormatBox")
        self.verticalLayout.addWidget(self.iTunesFormatBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.AddToITunesBox = QtWidgets.QCheckBox(self.DownloadTab)
        self.AddToITunesBox.setObjectName("AddToITunesBox")
        self.verticalLayout_4.addWidget(self.AddToITunesBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.DownloadTab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.PlaylistListWidget = QtWidgets.QListWidget(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlaylistListWidget.sizePolicy().hasHeightForWidth())
        self.PlaylistListWidget.setSizePolicy(sizePolicy)
        self.PlaylistListWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.PlaylistListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.PlaylistListWidget.setObjectName("PlaylistListWidget")
        self.verticalLayout_5.addWidget(self.PlaylistListWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.DownloadTab)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.ArtistListWidget = QtWidgets.QListWidget(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArtistListWidget.sizePolicy().hasHeightForWidth())
        self.ArtistListWidget.setSizePolicy(sizePolicy)
        self.ArtistListWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.ArtistListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ArtistListWidget.setObjectName("ArtistListWidget")
        self.verticalLayout_8.addWidget(self.ArtistListWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.DownloadTab)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.GenreListWidget = QtWidgets.QListWidget(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GenreListWidget.sizePolicy().hasHeightForWidth())
        self.GenreListWidget.setSizePolicy(sizePolicy)
        self.GenreListWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.GenreListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.GenreListWidget.setObjectName("GenreListWidget")
        self.verticalLayout_6.addWidget(self.GenreListWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.DownloadTab)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.AlbumListWidget = QtWidgets.QListWidget(self.DownloadTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AlbumListWidget.sizePolicy().hasHeightForWidth())
        self.AlbumListWidget.setSizePolicy(sizePolicy)
        self.AlbumListWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.AlbumListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.AlbumListWidget.setObjectName("AlbumListWidget")
        self.verticalLayout_7.addWidget(self.AlbumListWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.DownloadTab, "")
        self.EditFileTab = QtWidgets.QWidget()
        self.EditFileTab.setObjectName("EditFileTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.EditFileTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FilesList = QtWidgets.QListWidget(self.EditFileTab)
        self.FilesList.setObjectName("FilesList")
        self.verticalLayout_2.addWidget(self.FilesList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ChooseFilesButton = QtWidgets.QPushButton(self.EditFileTab)
        self.ChooseFilesButton.setObjectName("ChooseFilesButton")
        self.horizontalLayout_2.addWidget(self.ChooseFilesButton)
        self.ConvertButton = QtWidgets.QPushButton(self.EditFileTab)
        self.ConvertButton.setObjectName("ConvertButton")
        self.horizontalLayout_2.addWidget(self.ConvertButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.FileFormatLabel = QtWidgets.QLabel(self.EditFileTab)
        self.FileFormatLabel.setObjectName("FileFormatLabel")
        self.verticalLayout_3.addWidget(self.FileFormatLabel)
        self.FormatBox = QtWidgets.QComboBox(self.EditFileTab)
        self.FormatBox.setObjectName("FormatBox")
        self.verticalLayout_3.addWidget(self.FormatBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.EditFileTab, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.UrlText, self.TitleText)
        MainWindow.setTabOrder(self.TitleText, self.ArtistText)
        MainWindow.setTabOrder(self.ArtistText, self.GenreText)
        MainWindow.setTabOrder(self.GenreText, self.AlbumText)
        MainWindow.setTabOrder(self.AlbumText, self.FilenameText)
        MainWindow.setTabOrder(self.FilenameText, self.StartTimeText)
        MainWindow.setTabOrder(self.StartTimeText, self.EndTimeText)
        MainWindow.setTabOrder(self.EndTimeText, self.FolderButton)
        MainWindow.setTabOrder(self.FolderButton, self.FolderText)
        MainWindow.setTabOrder(self.FolderText, self.DownloadButton)
        MainWindow.setTabOrder(self.DownloadButton, self.InfoButton)
        MainWindow.setTabOrder(self.InfoButton, self.FormatList)
        MainWindow.setTabOrder(self.FormatList, self.KeepOriginalAudioBox)
        MainWindow.setTabOrder(self.KeepOriginalAudioBox, self.TrimOriginalAudioBox)
        MainWindow.setTabOrder(self.TrimOriginalAudioBox, self.KeepOriginalVideoBox)
        MainWindow.setTabOrder(self.KeepOriginalVideoBox, self.TrimOriginalVideoBox)
        MainWindow.setTabOrder(self.TrimOriginalVideoBox, self.FormatBox)
        MainWindow.setTabOrder(self.FormatBox, self.FilesList)
        MainWindow.setTabOrder(self.FilesList, self.ChooseFilesButton)
        MainWindow.setTabOrder(self.ChooseFilesButton, self.ConvertButton)
        MainWindow.setTabOrder(self.ConvertButton, self.iTunesFormatBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UrlLabel.setText(_translate("MainWindow", "Enter URL*: "))
        self.TitleLabel.setText(_translate("MainWindow", "Enter Title: "))
        self.ArtistLabel.setText(_translate("MainWindow", "Enter Artist: "))
        self.GenreLabel.setText(_translate("MainWindow", "Enter Genre: "))
        self.AlbumLabel.setText(_translate("MainWindow", "Enter Album:"))
        self.FilenameLabel.setText(_translate("MainWindow", "Enter Filename: "))
        self.StartTimeLabel.setText(_translate("MainWindow", "Start Time:"))
        self.EndTimeLabel.setText(_translate("MainWindow", "End Time:"))
        self.FolderButton.setText(_translate("MainWindow", "Choose Folder"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.FormatLabel.setText(_translate("MainWindow", "Supported Formats:"))
        self.label.setText(_translate("MainWindow", "Audio:"))
        self.KeepOriginalAudioBox.setText(_translate("MainWindow", "Keep Original"))
        self.TrimOriginalAudioBox.setText(_translate("MainWindow", "Keep Original Trimmed"))
        self.label_2.setText(_translate("MainWindow", "Video:"))
        self.KeepOriginalVideoBox.setText(_translate("MainWindow", "Keep Original"))
        self.TrimOriginalVideoBox.setText(_translate("MainWindow", "Keep Original Trimmed"))
        self.label_3.setText(_translate("MainWindow", "Download Options:"))
        self.iTunesFormatBox.setText(_translate("MainWindow", "iTunes Format (artist/album/song)"))
        self.AddToITunesBox.setText(_translate("MainWindow", "Add To iTunes"))
        self.label_4.setText(_translate("MainWindow", "Playlists:"))
        self.label_7.setText(_translate("MainWindow", "Artists:"))
        self.label_5.setText(_translate("MainWindow", "Genres:"))
        self.label_6.setText(_translate("MainWindow", "Albums:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DownloadTab), _translate("MainWindow", "Download"))
        self.ChooseFilesButton.setText(_translate("MainWindow", "Choose Files"))
        self.ConvertButton.setText(_translate("MainWindow", "Convert Files"))
        self.FileFormatLabel.setText(_translate("MainWindow", "File Format:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EditFileTab), _translate("MainWindow", "Edit File"))
