# clac grammer:
# expr = term (ADD | SUB term)*
# term = factor (MUL | DIV factor)*
# factor = INTEGER | LPAREN expr RPAREN | (ADD | SUB) factor

import unittest
from mytoken import *
from lexer import Lexer
from parser import Parser

class TestLexer(unittest.TestCase):
    def test_get_next_token_1(self):
        lexer = Lexer('1+2')
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 1))
        self.assertEqual(lexer.get_next_token(), Token(ADD, '+'))
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 2))

    def test_get_next_token_2(self):
        lexer = Lexer('  1 + ( + 2) - 3  + 3*5/3 ')
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 1))
        self.assertEqual(lexer.get_next_token(), Token(ADD, '+'))
        self.assertEqual(lexer.get_next_token(), Token(LPAREN, '('))
        self.assertEqual(lexer.get_next_token(), Token(ADD, '+'))
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 2))
        self.assertEqual(lexer.get_next_token(), Token(RPAREN, ')'))
        self.assertEqual(lexer.get_next_token(), Token(SUB, '-'))
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 3))
        self.assertEqual(lexer.get_next_token(), Token(ADD, '+'))
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 3))
        self.assertEqual(lexer.get_next_token(), Token(MUL, '*'))
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 5))
        self.assertEqual(lexer.get_next_token(), Token(DIV, '/'))
        self.assertEqual(lexer.get_next_token(), Token(INTEGER, 3))
        
if __name__ == '__main__':
    unittest.main()
