"""Main window-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self._createCentralWidget()
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()
    
    def _createCentralWidget(self):
        central = QLabel("I'm the central Widget")
        self.setCentralWidget(central)
        
    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)
            
    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)
    
    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the status Bar")
        self.setStatusBar(status)
        
if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
