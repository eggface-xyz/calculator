from mytoken import *

class Lexer:
    def __init__(self, text):
        self.current_pos = 0
        self.current_char = text[0]
        self.text = text

    def error(self):
        raise Exception('Unknown char')

    def advance(self):
        self.current_pos += 1
        if self.current_pos == len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.current_pos]

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        if self.current_char is not None and self.current_char.isspace():
            self.skip_whitespace()

        if self.current_char is not None:
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(ADD, '+')
            if self.current_char == '-':
                self.advance()
                return Token(SUB, '-')
            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')
            self.error()
        else:
            return Token(EOF, None)


