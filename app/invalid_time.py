from PyQt5.QtWidgets import QDialog
from dialogs.invalid_time_dialog import Ui_InvalidTime

class InvalidTime(QDialog, Ui_InvalidTime):
    """
    Dialog that appears when start or end times are not in the right format, 
    greater than the song duration, or start time is greater than end time.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Invalid Time')
        self.CloseButton.clicked.connect(self.close)
        