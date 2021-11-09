from PyQt5.QtWidgets import QDialog
from dialogs.url_needed_dialog import Ui_Dialog


class URLNeeded(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('URL Needed')
        self.CloseButton.clicked.connect(self.close)
        