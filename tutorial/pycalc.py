"""PyCalc is a simple calculator built with Python and PyQt."""

import sys
from functools import partial
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    # Application class
    QApplication,
    # Layout(s)
    QGridLayout,
    QVBoxLayout,
    # Widgets
    QLineEdit,
    QPushButton,
    QMainWindow,
    QWidget,
)

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HIGHT = 35
BUTTON_SIZE = 40

class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
      
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            "7 8 9 / C".split(),
            "4 5 6 * )".split(),
            "1 2 3 - (".split(),
            "0 00 . + =".split(),
        ]
        
        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)
        
        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        """Set the display's text"""
        self.display.setText(text)
        self.display.setFocus()
    
    def displayText(self):
        """gets the current display's text."""
        return self.display.text()
    
    def clearDisplay(self):
        """clears the display."""
        self.setDisplayText("")
    
def evaluateExpression(expression):
    """Evaluate an expression (Model)."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result

class PyCalc:
    """PyCalc's controller class."""
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()
        
    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
    
    def _buildExpression(self, subExpression):
        print(f"_buildExpression was called with arg: {subExpression!r}")
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)
    
    def _connectSignalsAndSlots(self):
        print(self._view.buttonMap.items())
        for keySymbol, button in self._view.buttonMap.items():
            match keySymbol:
                case "=":
                    button.clicked.connect(
                        self._calculateResult
                    )
                case "C":
                    button.clicked.connect(
                        self._view.clearDisplay
                    )
                else:
                    print(f"mapping key with keySymbol: {keySymbol!r}")
                    button.clicked.connect(
                        partial(self._buildExpression, keySymbol)
                        # this doesn't work because keySymbol changes during
                        # runtime and effects the outcome of this expression,
                        # which is evaluated every time it's run.
                        #lambda: self._buildExpression(keySymbol)
                    )
        self._view.display.returnPressed.connect(self._calculateResult)

def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([sys.argv])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()