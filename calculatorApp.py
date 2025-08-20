import math
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
from calculator import Ui_Calculator
import sys

class CalculatorApp(QMainWindow):
    def __init__(self):
        super(CalculatorApp, self).__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.calculate)
        self.ui.subsButton.clicked.connect(self.calculate)
        self.ui.multiButton.clicked.connect(self.calculate)
        self.ui.divButton.clicked.connect(self.calculate)
        self.ui.sqrtButton.clicked.connect(self.calculate)
        self.ui.logButton.clicked.connect(self.calculate)
        self.ui.sqrButton.clicked.connect(self.calculate)
        self.setWindowIcon(QIcon("calculator.png"))

    def calculate(self):
        sender = self.sender()
        operation = sender.text()
        try:
            number1 = float(self.ui.fNumberIn.text())
            number2 = float(self.ui.sNumberIn.text())
        except ValueError:
            self.ui.result.setText("Please enter valid numbers")
            return

        if operation == "Addition":
            result = number1 + number2
        elif operation == "Subtraction":
            result = number1 - number2
        elif operation == "Multiplication":
            result = number1 * number2
        elif operation == "Log":
            if number1 > 0 and number2 > 0 and number1 == number2:
                a = math.log(number1)
                b = math.log(number2)
                result = (a + b) / 2
            elif number1 > 0 and number2 > 0:
                a = math.log(number1)
                b = math.log(number2)
                result = a + b
            else:
                result = "Invalid input for log"
        elif operation == "Square root":
            if number1 > 0 and number2 > 0 and number1 == number2:
                a = math.sqrt(number1)
                b = math.sqrt(number2)
                result = (a + b) / 2
            elif number1 > 0 and number2 > 0:
                a = math.sqrt(number1)
                b = math.sqrt(number2)
                result = a + b
            else:
                result = "Invalid input for square root"
        elif operation == "Square":
            if number1 == number2:
                result = (number1 ** 2 + number2 ** 2) / 2
            else:
                result = number1 ** 2 + number2 ** 2
        elif operation == "Division":
            if number2 != 0:
                result = number1 / number2
            else:
                result = "Cannot divide by zero"
        else:
            result = "Invalid Operation"

        self.ui.result.setText(str(result))

def app():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

app()