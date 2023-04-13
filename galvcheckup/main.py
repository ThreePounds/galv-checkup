"""This module proves RP Contacts application"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
)

from .views import Window
from .database import createConnection

def main():
    """RP Contacts main function."""
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    win = Window()
    win.show()
    sys.exit(app.exec())