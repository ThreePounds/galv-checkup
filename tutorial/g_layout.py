"""grid layout example"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
)

ROWS = 2
COLUMNS = 3

# creating an application and widget instance
# setting a descriptive title to the window
app = QApplication([])
window = QWidget()
window.setWindowTitle("QGridLayout")

# creating an instance of the desired layout manager
# and adding the widgets to said layout using the
# .addWidget method
layout = QGridLayout()
for row in range(ROWS):
    for column in range(COLUMNS):
        layout.addWidget(QPushButton(f'Button ({row}, {column})'), row, column)
layout.addWidget(QPushButton(f'Button ({ROWS}, 0)'), ROWS, 0)
layout.addWidget(
    QPushButton(f'Button ({ROWS}, 1) + 2 Columns Span'), ROWS, 1, 1, 2,
)

# setting the layout of the window object to the layout object
window.setLayout(layout)

# drawing window to screen and setting up starting the main loop
window.show()
sys.exit(app.exec())