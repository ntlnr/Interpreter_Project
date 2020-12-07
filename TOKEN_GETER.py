#!/usr/bin/env python
# coding: utf-8


EOF = -1

# token type
COMMA = 'COMMA'
EQUAL = 'EQUAL'
LBRACK = 'LBRACK'
RBRACK = 'RBRACK'
TIMES = 'TIMES'
ADD = 'ADD'
PRINT = 'print'
ID = 'ID'
INT = 'INT'
STR = 'STR'
SUBTRACT = 'SUBTRACT'
MODULO = 'MODULO'
POWER = 'POWER'
LPARENTHESES = 'LPARENTHESES'
RPARENTHESES = 'RPARENTHESES'
IF = 'IF'
ELSE = 'ELSE'
SIMCOL = 'SIMCOL'
STR_ = 'STR_'

# use LL(1) 
class TOKEN_GETER:
    def __init__(self, input):
        self.input = input
        
        self.idx = 1
        
        self.cur_c = input[0]
    
    def next_token(self):
        while self.cur_c != EOF:
            c = self.cur_c
            
            if c.isspace():
                self.consume()
            elif c == '[':
                self.consume()
                return (LBRACK, c)
            elif c == ']':
                self.consume()
                return (RBRACK, c)
            elif c == '(':
                self.consume()
                return (LPARENTHESES, c)
            elif c == ')':
                self.consume()
                return (RPARENTHESES, c)
            elif c == ',':
                self.consume()
                return (COMMA, c)
            elif c == '=':
                self.consume()
                return (EQUAL, c)
            elif c == '*':
                self.consume()
                return (TIMES, c)
            elif c == '+':
                self.consume()
                return (ADD, c)
            elif c == '%':
                self.consume()
                return (MODULO, c)
            elif c == '-':
                self.consume()
                return (SUBTRACT, c)
            elif c == '^':
                self.consume()
                return (POWER, c)
            elif c == ':':
                self.consume()
                return (SIMCOL, c)
            elif c == '\'' or c == '"':
                return self._string()
            elif c.isdigit():
                return self._int()
            elif c.isalpha():
                t = self._print()
                if t: 
                    return t
                t = self._if()
                if t: 
                    return t
                t = self._else()
                if t: 
                    return t
                t = self._str()
                if t:
                    return t
                else:
                    return self._id()
            else:
                raise Exception('not support token')
        
        return (EOF, 'EOF')
    
    def has_next(self):
        return self.cur_c != EOF
    
    def _id(self):
        n = self.cur_c
        self.consume()
        while (self.cur_c.isalpha() or self.cur_c == '_'):
            n += self.cur_c
            self.consume()
            
        return (ID, n)
    
    def _int(self):
        n = self.cur_c
        self.consume()
        while self.cur_c.isdigit():
            n += self.cur_c
            self.consume()
        
        return (INT, int(n))
        
        
    def _print(self):
        n = self.input[self.idx - 1 : self.idx + 4]
        if n == 'print':
            self.idx += 4
            self.cur_c = self.input[self.idx]
            
            return (PRINT, n)
        
        return None

    def _str(self):
        n = self.input[self.idx - 1 : self.idx + 2]
        if n == 'str':
            self.idx += 2
            self.cur_c = self.input[self.idx]

            return (STR_, n)

        return None
    
    def _if(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == 'if':
            self.idx += 1
            self.cur_c = self.input[self.idx]
            
            return (IF, n)
        
        return None
    
    def _else(self):
        n = self.input[self.idx - 1 : self.idx + 3]
        if n == 'else':
            self.idx += 3
            self.cur_c = self.input[self.idx]
            
            return (ELSE, n)
        
        return None
    
    def _string(self):
        quotes_type = self.cur_c
        self.consume()
        s = ''
        
        while self.cur_c != '\n' and self.cur_c != quotes_type:
            s += self.cur_c
            self.consume()
        if self.cur_c != quotes_type:
            raise Exception('string quotes is not matched. excepted %s' % quotes_type)
        
        self.consume()
        
        return (STR, s)
    
    def consume(self):
        if self.idx >= len(self.input):
            self.cur_c = EOF
            return
        self.cur_c = self.input[self.idx]
        self.idx += 1


'''
if __name__ == '__main__':
    exp = 
        name = "Ash Ketchum"

        charmender_HP = 110
        squirtle_HP = 125
        bulbasaur_HP = 150

        charmender_attack = 40
        squirtle_attack = 35
        bulbasaur_attack = 25

        turn = 1
        print (name+"'s Charmender won!")
        if turn == 1:
            turn = 0
        else :
            turn = 1
    
    lex = TOKEN_GETER(exp)
    t = lex.next_token()
    
    while t[0] != EOF:
        print (t)
        t = lex.next_token()
'''



