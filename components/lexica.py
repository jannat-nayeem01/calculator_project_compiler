from sly import Lexer
import sly

class MyLexer(Lexer):
    tokens = {ASSIGN, NAME, NUMBER, MINUS, DIVIDE, TIMES, LPAREN, RPAREN, PLUS}


    literals = { '+' }

    ignore = ' \t'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    @_(r'\d+')
    def NUMBER(self, token):
        token.value = int(token.value)
        return token

    ASSIGN  = r'\='
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    LPAREN  = r'\('
    RPAREN  = r'\)'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        self.index += 1
        print(f"ERROR: Illegal character '{t.value[0]}' at line {self.lineno}")

if __name__ == '__main__':
    string_input = "x1 + 1as! * ()"
    lex = MyLexer()
    for token in lex.tokenize(string_input):
        print(token)
