"""This module provides the galvcheckup application."""

import sys

from PyQt6.QtWidgets import(
    QApplication,
)

from .views import Window

def main():
    """galvcheckup main function."""
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())