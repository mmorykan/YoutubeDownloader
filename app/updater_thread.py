import os
from PyQt5.QtCore import QThread, pyqtSignal
from version import VERSION
import requests

class UpdateProgressThread(QThread):
    """
    A class that represents a QThread that constantly updates the progress bar upon updating the application.
    We use pyqtSignals to be able to emit data back to the main thread so that the main thread can update the GUI.
    """

    # These must be class variables outside the constructor
    progress = pyqtSignal(float)
    finished = pyqtSignal(bool)

    def __init__(self, url, dest):
        super().__init__()
        self.url = url
        self.dest = dest

    def get_latest_release(self):
        try:
            data = requests.get(self.url, timeout=5).json()
            return data["tag_name"], data["assets"][0]["browser_download_url"]
        except Exception as e:
            print(e)
            return "", ""

    def download(self):
        latest, url = self.get_latest_release()
        if not latest or not url or latest == VERSION:
            # End here if the request was unsuccessful or the version is already the most recent
            self.finished.emit(True)
            return

        resp = requests.get(url, stream=True)
        if not resp:
             # End here if the request was unsuccessful
            self.finished.emit(True)
            return

        total = int(resp.headers.get("content-length", 0))
        with open(self.dest, "wb") as f:
            downloaded = 0
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    self.progress.emit(downloaded * 100 / total)

        self.finished.emit(False)
