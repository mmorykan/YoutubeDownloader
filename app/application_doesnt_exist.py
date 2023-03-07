from PyQt5.QtWidgets import QDialog
from dialogs.application_doesnt_exist import Ui_ApplicationDoesntExist

class ApplicationDoesntExist(QDialog, Ui_ApplicationDoesntExist):
    """
    Dialog that appears when the user input a filename that already exists in that directory.
    Asks the user if they want to overwrite the existing file.
    """

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Application Doesn\'t Exist')
        self.OKButton.setStyleSheet("background-color : blue")
        self.OKButton.clicked.connect(self.close)

    def set_message(self, player_name):
        self.DoesntExistLabel.setText(f'Could not connect to {player_name} application')
