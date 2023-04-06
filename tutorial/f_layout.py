"""form layout example"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QLineEdit,
)

FIELDS = [
    "Name",
    "Age",
    "Job",
    "Hobbies",
]

# creating an application and widget instance
# setting a descriptive title to the window
app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

# creating an instance of the desired layout manager
# and adding the widgets to said layout using the
# .addWidget method
layout = QFormLayout()
for entry in FIELDS:
    layout.addRow(f'{entry}:', QLineEdit())

# setting the layout of the window object to the layout object
window.setLayout(layout)

# drawing window to screen and setting up starting the main loop
window.show()
sys.exit(app.exec())