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
DIVISION = 'DIVISION'
LPARENTHESES = 'LPARENTHESES'
RPARENTHESES = 'RPARENTHESES'
IF = 'IF'
ELSE = 'ELSE'
SIMCOL = 'SIMCOL'
STR_ = 'STR_'
PLUS_EQUAL = 'PLUS_EQUAL'
MINUS_EQUAL = 'MINUS_EQUAL'
TIMES_EQUAL = 'TIMES_EQUAL'
DIVISION_EQUAL = 'DIVISION_EQUAL'
POWER_EQUAL = 'POWER_EQUAL'
MODULO_EQUAL = 'MODULO_EQUAL'
GREATER = 'GREATER'
LESSER = 'LESSER'
EQUIVALENT = 'EQUIVALENT'
GREATER_EQUAL = 'GREATER_EQUAL'
LESSER_EQUAL = 'LESSER_EQUAL'
UNEQUAL = 'UNEQUAL'
COMMENT = 'COMMENT'


# use LL(1) 
class TOKEN_GETER:
    def __init__(self, input):
        self.input = input
        
        self.idx = 1
        
        self.cur_c = input[0]
    
    def next_token(self):
        while self.cur_c != EOF:
            c = self.cur_c
            add_ = self._plus_equal()
            minus_ = self._minus_equal()
            times_ = self._times_equal()
            division_ = self._division_equal()
            power_ = self._power_equal()
            modulo_ = self._modulo_equal()
            eq_ = self._equivalent()
            ge_ = self._greater_equal()
            le_ = self._lesser_equal()
            uneq_ = self._unequal()
            
            if eq_:
                return eq_
            elif ge_:
                return ge_
            elif le_:
                return le_
            elif uneq_:
                return uneq_
            elif add_:
                return add_
            elif minus_:
                return minus_
            elif times_:
                return times_
            elif division_:
                return division_
            elif power_:
                return power_
            elif modulo_:
                return modulo_
            elif c == '#':
                return self._comment()
            elif c == '[':
                self.consume()
                return (LBRACK, c)
            elif c == ']':
                self.consume()
                return (RBRACK, c)
            elif c == '>':
                self.consume()
                return (GREATER, c)
            elif c == '<':
                self.consume()
                return (LESSER, c)
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
            elif c == '/':
                self.consume()
                return (DIVISION, c)
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
            elif c.isspace():
                self.consume()
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
    
    def _greater_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '>=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (GREATER_EQUAL, n)

        return None

    def _lesser_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '<=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (LESSER_EQUAL, n)

        return None

    def _equivalent(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '==':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (EQUIVALENT, n)

        return None

    def _unequal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '!=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (UNEQUAL, n)

        return None

    def _plus_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '+=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (PLUS_EQUAL, n)

        return None

    def _minus_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '-=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (MINUS_EQUAL, n)

        return None

    def _times_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '*=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (TIMES_EQUAL, n)

        return None

    def _division_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '/=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (DIVISION_EQUAL, n)

        return None

    def _power_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '^=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (POWER_EQUAL, n)

        return None

    def _modulo_equal(self):
        n = self.input[self.idx - 1 : self.idx + 1]
        if n == '%=':
            self.idx += 1
            self.cur_c = self.input[self.idx]

            return (MODULO_EQUAL, n)

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
    
    def _comment(self):
        self.consume()
        s = ''

        while self.cur_c != '\n':
            s += self.cur_c
            self.consume()
        if self.cur_c != '\n':
            raise Exception('comment is not correct')

        self.consume()

        return (COMMENT, s)



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

        z != 25
        
        # This is a comment
        
    
    lex = TOKEN_GETER(exp)
    t = lex.next_token()
    
    while t[0] != EOF:
        print (t)
        t = lex.next_token()

'''
