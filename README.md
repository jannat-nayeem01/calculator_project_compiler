 [Compiler Starter Project](#compiler-starter-project)

Instruction to run the code:
Python needs to be installed on machine.
Run on local machine. Not Docker.

Dependencies:
step1: 
pip3 install PyQt6 sly
step2:
python3 main.py

 
- [Code Explain](#code-explain)
components/parser.py: This file contains the definition of a parser class (MyParser) using the SLY library. It defines the grammar rules for parsing arithmetic expressions and builds a parse tree.

components/lexica.py: This file contains the definition of a lexer class (MyLexer) using the SLY library. It defines the rules for tokenizing input strings into tokens like numbers, operators, parentheses, etc.

parser.out: This file is an output file generated by the parser. It typically contains debugging information such as the states and transitions of the parser's finite state machine.

main.py: This file contains the main logic for the calculator application. It integrates the parser and lexer to parse and evaluate arithmetic expressions entered by the user. It also handles the GUI using PyQt6.

components/main.ui: This file is a user interface file. It defines the layout and design of the calculator GUI, including buttons, labels, and input/output fields.

components/calculator_logic.py: This file contains the logic for evaluating arithmetic expressions. It defines functions for performing arithmetic operations like addition, multiplication, etc. This logic is used by the parser to evaluate expressions and produce results and postfix and prefix expression.

Manual:
1. Grammar used for my calculator:

Rule 0     S' -> statement
Rule 1     statement -> expr
Rule 2     expr -> NUMBER
Rule 3     expr -> LPAREN expr RPAREN
Rule 4     expr -> expr TIMES expr  [precedence=left, level=2]
Rule 5     expr -> expr PLUS expr  [precedence=left, level=1] Note: level 1 means higher priority

2. 
Type of the parser:

The parser used in the code is an LR(0) parser. This is evident from the parsing states and transitions described in the parser.out file, which are characteristic of LR(0) parsing.

3. Method of Translation and Integration of Parser and Translation:

Lexer Tokenization:

The process begins with tokenization, where the input arithmetic expression is broken down into individual tokens by the lexer (MyLexer). Each token represents a distinct element of the expression, such as numbers, operators, and parentheses.

Parsing:

Once the input expression is tokenized, the parser (MyParser) processes these tokens according to the defined grammar rules. The parser constructs a parse tree or abstract syntax tree (AST) based on the structure defined by the grammar.

Evaluation During Parsing:

While parsing the input expression, the parser also evaluates the expression based on the defined precedence and associativity of operators. This evaluation occurs as part of the parsing process itself, embedded within the parsing rules.

Handling Precedence and Associativity:

The parser handles operator precedence and associativity by defining precedence levels for operators in the precedence attribute. This ensures that the parser evaluates expressions correctly according to the standard rules of arithmetic operations.

Result Generation:

As the parsing process completes, the parser generates a result based on the evaluation of the input expression. This result represents the outcome of the arithmetic operation specified by the input expression. The result also includes postfix and prefix expression which is generated from calculator_logic.py file.

Integration of Parser and Translation:

The integration of parser and translation occurs seamlessly within the parsing rules defined in the parser class. The parsing rules not only parse the input expression but also perform the translation (evaluation) of the expression into a result.

Final Output:

Finally, the result of the evaluation is printed out, providing the user with the outcome of the arithmetic expression and postfix and prefix expression entered as input.

Overall, the method of translation and the integration of parser and translation in my code demonstrate a cohesive approach where parsing and evaluation are tightly integrated, allowing for the seamless processing of result from input to output








