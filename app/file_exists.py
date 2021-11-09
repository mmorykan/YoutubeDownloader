from PyQt5.QtWidgets import QDialog
from dialogs.file_exists_dialog import Ui_FileExistsDialog

class FileExists(QDialog, Ui_FileExistsDialog):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('File Already Exists')
        self.YesButton.setStyleSheet("background-color : blue")
        self.YesButton.clicked.connect(lambda: self.overwrite(True))
        self.NoButton.clicked.connect(lambda: self.overwrite(False))
        self.YesButton.clicked.connect(self.close)
        self.NoButton.clicked.connect(self.close)
        self.overwrite_file = None

    def set_message(self, filename):
        self.FileExistsLabel.setText(filename + ' already exists. Do you wish to overwrite this file?')

    def overwrite(self, is_overwrite):
        self.overwrite_file = is_overwrite


