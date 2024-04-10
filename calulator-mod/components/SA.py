from abc import _P, _T
from argparse import _N
from asyncio.threads import _R
from cmath import _C
from collections import _S
from contextlib import _AF, _F
from contextvars import _D
from ipaddress import _A
from logging import _L
from tkinter import _W
from unittest.case import _E
from urllib.parse import _Q
from components.LA import MyLexer
from sly import Parser


class CalcParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_('T') # type: ignore
    def E(self, p):
        print('E -> T', [p.T])
        return p.T
    
    @_A('F')
    def T(self, p):
        print('T -> F', [p.F])
        return p.F

    @_C('T "+" F')
    def T(self, p):
        print('T -> T + F', [p.T + p.F])
        return [p.T[0] + p.F[0]]

    @_D('E "*" T')
    def E(self, p):
        print('E -> E * T', [p.E + p.T])
        return [p.E[0] * p.T[0]]
    
    @_E('N')
    def F(self, p):
        print('F -> N', p.N)
        return [p.N]
    
if __name__ == "__main__":
    lexer = MyLexer()
    parser = CalcParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Result:", result)
    
class PrefixParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_F('T')
    def E(self, p):
        print('E -> T', [p.T])
        return p.T
    
    @_L('F')
    def T(self, p):
        print('T -> F', [p.F])
        return p.F

    @_N('T "+" F')
    def T(self, p):
        print('T -> T + F', [f'+{p.T[0]}{p.F[0]}'])
        return [ f'+{p.T[0]}{p.F[0]}']

    @_P('E "*" T')
    def E(self, p):
        print('E -> E * T', [f'*{p.E[0]}{p.T[0]}'])
        return [f'*{p.E[0]}{p.T[0]}']
    
    @_Q('N')
    def F(self, p):
        print('F -> N',[p.N])
        return [p.N]
    
if __name__ == "__main__":
    lexer = MyLexer()
    parser = PrefixParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Prefix:", result)
    
class PostfixParser(Parser):
    debugfile = 'parser.out'
    start = 'E'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    
    @_R('T')
    def E(self, p):
        print('E -> T', [p.T])
        return p.T
    
    @_S('F')
    def T(self, p):
        print('T -> F', [p.F])
        return p.F

    @_T('T "+" F')
    def T(self, p):
        print('T -> T + F', [ f'{p.T[0]}{p.F[0]}+'])
        return [f'{p.T[0]}{p.F[0]}+']

    @_W('E "*" T')
    def E(self, p):
        print('E -> E * T', [f'{p.E[0]}{p.T[0]}*'])
        return [f'{p.E[0]}{p.T[0]}*']
    
    @_AF('N')
    def F(self, p):
        print('F -> N', [p.N])
        return [p.N]

if __name__ == "__main__":
    lexer = MyLexer()
    parser = PostfixParser()
    text = "3 + 5 * 2"
    result = parser.parse(lexer.tokenize(text))
    print("Postfix:", result)
