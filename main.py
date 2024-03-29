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
        self.button_3.clicked.connect(lambda: self.push("3"))
        self.button_4.clicked.connect(lambda: self.push("4"))
        self.button_5.clicked.connect(lambda: self.push("5"))
        self.button_6.clicked.connect(lambda: self.push("6"))
        self.button_7.clicked.connect(lambda: self.push("7"))
        self.button_8.clicked.connect(lambda: self.push("8"))
        self.button_9.clicked.connect(lambda: self.push("9"))
        self.button_0.clicked.connect(lambda: self.push("0"))
        self.button_clear.clicked.connect(self.clear)


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
            result, postfix_expression, prefix_expression = evaluate_expression(input_text)
            self.output_lcd.display(result)
            self.postfix_display.setText(postfix_expression)
            self.prefix_display.setText(prefix_expression)
        except Exception as e:
            print(f"Error calculating expression: {e}")

            
            
    def clear(self):
        # Clear input text
        self.input_text.clear()
        # Clear output LCD
        self.output_lcd.display(0)
        # Clear postfix label
        self.postfix_display.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())