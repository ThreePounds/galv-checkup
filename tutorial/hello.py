"""Simple Hello, World example with PyQt6."""

import sys

# Import QApplication and all the required widgets
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget
)

# Creates Instance of QApplication
app = QApplication([sys.argv])

# Create Application GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h>", parent=window)
helloMsg.move(60, 15)

# Show Application GUI
window.show()

# Run application event loop
sys.exit(app.exec())