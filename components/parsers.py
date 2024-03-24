from sly import Parser
from components.lexica import MyLexer
from components.memory import Memory

# Define tokens (you may need to import token types from MyLexer)
NUMBER = 'NUMBER'
PLUS = 'PLUS'
TIMES = 'TIMES'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'

class MyParser(Parser):
    debugfile = 'parser.out'
    tokens = MyLexer.tokens

    precedence = (
        ('left', PLUS),
        ('left', TIMES),
    )

    def __init__(self):
        self.memory = Memory()

    @_('expr')
    def statement(self, p):
        return p.expr

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr TIMES expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

if __name__ == '__main__':
    lexer = MyLexer()
    parser = MyParser()
    text = input("Enter an arithmetic expression: ")
    result = parser.parse(lexer.tokenize(text))
    print("Result:", result)
