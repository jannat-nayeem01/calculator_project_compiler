import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLCDNumber
from components.lexica import MyLexer
from components.parsers import MyParser
from components.memory import Memory
from components.calculator_logic import evaluate_expression

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("components/main.ui", self)
        self.button_1.clicked.connect(self.push_1)
        self.button_2.clicked.connect(lambda: self.push("2"))
        self.button_plus.clicked.connect(lambda: self.push("+"))
        self.button_multiply.clicked.connect(lambda: self.push("*"))
        self.button_equal.clicked.connect(self.calculate)

    def push_1(self):
        current_text = self.input_text.text()
        self.input_text.setText(f"{current_text}1")
    
    def push(self, text):
        current_text = self.input_text.text()
        self.input_text.setText(f"{current_text}{text}")

    def calculate(self):
        input_text = self.input_text.text()
        try:
            result = evaluate_expression(input_text)
            self.output_lcd.display(result)
        except Exception as e:
            print(f"Error calculating expression: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
