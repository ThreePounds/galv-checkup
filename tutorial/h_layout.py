"""Horizontal layout example"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QPushButton,
)

# creating an application and widget instance
# setting a descriptive title to the window
app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

# creating an instance of the desired layout manager
# and adding the widgets to said layout using the
# .addWidget method
layout = QHBoxLayout()
layout.addWidget(QPushButton("Left"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Right"))

# setting the layout of the window object to the layout object
window.setLayout(layout)

# drawing window to screen and setting up starting the main loop
window.show()
sys.exit(app.exec())