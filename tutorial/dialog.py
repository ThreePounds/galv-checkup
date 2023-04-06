"""Dialog-styl application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout
)
FIELDS = [
    "Name",
    "Age",
    "Job",
    "Hobbies",
]

# create new class which inherits from QDialog
class Window(QDialog):
    def __init__(self):
        # call QDialog.__init__ for general set up
        super().__init__(parent=None)
        # QDialogs have window titles, too!
        self.setWindowTitle("QDialog")
        # dialogLayout is a vertial Box Layout
        dialogLayout = QVBoxLayout()
        # formLayout is a grid layout with two columns. To add rows, we call
        # .addRow, which takes a string as it's first argument
        # this string then becomes a label. We then add a QLineEdit object
        # to the second column of each row 
        formLayout = QFormLayout()
        for entry in FIELDS:
            formLayout.addRow(f"{entry}:", QLineEdit())
        # we then set the formlayout as the layout of dialogLayout, which is
        # the vertical layout we defined earlier. Confusing ...
        dialogLayout.addLayout(formLayout)
        # what's a QDialogButtonBox? An emtpy container?
        buttons = QDialogButtonBox()
        # now we add the StandardButtons to it. Take note of the | usuage
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        # the second time we access the dialogLayout object, this time adding
        # the widget object we just defined
        dialogLayout.addWidget(buttons)
        # now we set the layout 'dialogLayout' to our custom class
        self.setLayout(dialogLayout)

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())