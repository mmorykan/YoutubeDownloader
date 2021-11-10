from PyQt5.QtWidgets import QDialog
from dialogs.url_needed_dialog import Ui_URLNeeded


class URLNeeded(QDialog, Ui_URLNeeded):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('URL Needed')
        self.CloseButton.clicked.connect(self.close)
        