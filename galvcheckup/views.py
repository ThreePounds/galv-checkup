"""This module provides views to manage the contacts table."""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()
        self._setupUI()
    
    def _setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget.
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table.resizeColumnsToContents()
        # Create Buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete...")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearContacts)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
    
    def clearContacts(self):
        """Remove all contacts from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your contacts?",
            QMessageBox.StandardButton.Ok
            | QMessageBox.StandardButton.Cancel,
        )
        
        if messageBox == QMessageBox.StandardButton.Ok:
            self.contactsModel.clearContacts()
    
    def deleteContact(self):
        """Dele the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return
        
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.StandardButton.Ok
            | QMessageBox.StandardButton.Cancel,
        )
        
        if messageBox == QMessageBox.StandardButton.Ok:
            self.contactsModel.deleteContact(row)
    
    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.contactsModel.addContacts(dialog.data)
            self.table.resizeColumnsToContents()

class AddDialog(QDialog):
    """Add Contact Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        
        self._setupUI()
    
    def _setupUI(self):
        """Setup the Add Contact dialog's GUI."""
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("Email")
        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("Job:", self.jobField)
        layout.addRow("Email:", self.emailField)
        self.layout.addLayout(layout)
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Ok 
            | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)
    
    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.jobField, self.emailField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None
                return
            
            self.data.append(field.text())
        
        if not self.data:
            return
        
        super().accept()

