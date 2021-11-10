from PyQt5.QtWidgets import QDialog
from dialogs.invalid_time_dialog import Ui_InvalidTime

class InvalidTime(QDialog, Ui_InvalidTime):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Invalid Time')
        self.CloseButton.clicked.connect(self.close)
        