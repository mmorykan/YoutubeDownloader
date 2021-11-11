from PyQt5.QtWidgets import QDialog
from dialogs.info_dialog import Ui_InfoDialog


class Info(QDialog, Ui_InfoDialog):
    """
    Dialog that appears when the info button is clicked in the program.
    Displays user input information.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Youtube Converter Info')
        self.CloseButton.clicked.connect(self.close)
        