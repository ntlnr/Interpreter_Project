import TOKEN_GETER

class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        
        # lookahead token. Based on the lookahead token to choose the parse option.
        self.cur_token = lexer.next_token()
        
        # similar to symbol table, here it's only used to store variables' value
        self.symtab = {}
        
        
    def statlist(self):
        while self.lexer.has_next():
            self.stat()
    
    def stat(self):
        token_type, token_val = self.cur_token
        
        # Asignment
        if token_type == TOKEN_GETER.ID:
            self.consume()
            
            # Assignment operators
            # For the terminal token, it only needs to match and consume.
            # If it's not matched, it means that is a syntax error.
            # Equal
            if self.match(TOKEN_GETER.EQUAL):
            # Store the value to symbol table.
                self.symtab[token_val] = self.expr()
            
            # Plus_Equal
            elif self.match(TOKEN_GETER.PLUS_EQUAL):
                first = token_val
                first_num = self.symtab[token_val]
                second_num = self.expr()
                result = first_num + second_num
                self.symtab[first] = result

            # Minus_Equal
            elif self.match(TOKEN_GETER.MINUS_EQUAL):
                first = token_val
                first_num = self.symtab[token_val]
                second_num = self.expr()
                result = first_num - second_num
                self.symtab[first] = result

            # Times_Equal
            elif self.match(TOKEN_GETER.TIMES_EQUAL):
                first = token_val
                first_num = self.symtab[token_val]
                second_num = self.expr()
                result = first_num * second_num
                self.symtab[first] = result

            # Division_Equal
            elif self.match(TOKEN_GETER.DIVISION_EQUAL):
                first = token_val
                first_num = self.symtab[token_val]
                second_num = self.expr()
                result = first_num / second_num
                self.symtab[first] = result

            # Power_Equal
            elif self.match(TOKEN_GETER.POWER_EQUAL):
                first = token_val
                first_num = self.symtab[token_val]
                second_num = self.expr()
                result = pow(first_num, second_num)
                self.symtab[first] = result

            # Modulo_Equal
            elif self.match(TOKEN_GETER.MODULO_EQUAL):
                first = token_val
                first_num = self.symtab[token_val]
                second_num = self.expr()
                result = first_num % second_num
                self.symtab[first] = result

            # Condition statement
            # greater
            elif self.match(TOKEN_GETER.GREATER):
                first_num = self.symtab[token_val]
                second_num = self.expr()
                if first_num > second_num:
                    return True
                else:
                    return False

            # lesser
            elif self.match(TOKEN_GETER.LESSER):
                first_num = self.symtab[token_val]
                second_num = self.expr()
                if first_num < second_num:
                    return True
                else:
                    return False

            # greater_equal
            elif self.match(TOKEN_GETER.GREATER_EQUAL):
                first_num = self.symtab[token_val]
                second_num = self.expr()
                if first_num >= second_num:
                    return True
                else:
                    return False

            # lesser_equal
            elif self.match(TOKEN_GETER.LESSER_EQUAL):
                first_num = self.symtab[token_val]
                second_num = self.expr()
                if first_num <= second_num:
                    return True
                else:
                    return False

            # equivalent 
            elif self.match(TOKEN_GETER.EQUIVALENT):
                first_num = self.symtab[token_val]
                second_num = self.expr()
                if first_num == second_num:
                    return True
                else:
                    return False

            # unequal
            elif self.match(TOKEN_GETER.UNEQUAL):
                first_num = self.symtab[token_val]
                second_num = self.expr()
                if first_num != second_num:
                    return True
                else:
                    return False

        # comment statement
        elif token_type == TOKEN_GETER.COMMENT:
            self.consume()
            v = str(token_val)
            print ('#' + v)
            
            
        # print statement
        elif token_type == TOKEN_GETER.PRINT:
            self.consume()
            if self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                self.consume()
            v = str(self.expr())

            while self.cur_token[0] == TOKEN_GETER.COMMA:
                self.match(TOKEN_GETER.COMMA)
                if self.cur_token[0] == TOKEN_GETER.STR_:
                    self.consume()
                    self.consume()
                v += ' ' + str(self.expr())
                if self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                    self.consume()

            while self.cur_token[0] == TOKEN_GETER.ADD:
                self.match(TOKEN_GETER.ADD)
                if self.cur_token[0] == TOKEN_GETER.STR_:
                    self.consume()
                    self.consume()
                v += ' ' + str(self.expr())
                if self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                    self.consume()
            print (v)


        # add statement
        elif token_type == TOKEN_GETER.ADD:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            second_num = int(self.expr())
            result = first_num + second_num
            self.symtab[num[0]] = result

        # subtract statement
        elif token_type == TOKEN_GETER.SUBTRACT:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            second_num = int(self.expr())
            result = first_num - second_num
            self.symtab[num[0]] = result

        # times statement
        elif token_type == TOKEN_GETER.TIMES:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            second_num = int(self.expr())
            result = first_num * second_num
            self.symtab[num[0]] = result

        # division statement
        elif token_type == TOKEN_GETER.DIVISION:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            second_num = int(self.expr())
            result = first_num / second_num
            self.symtab[num[0]] = result

        # power statement
        elif token_type == TOKEN_GETER.POWER:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            second_num = int(self.expr())
            result = pow(first_num, second_num)
            self.symtab[num[0]] = result

        # modulo statement
        elif token_type == TOKEN_GETER.MODULO:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            second_num = int(self.expr())
            result = first_num % second_num
            self.symtab[num[0]] = result


        

        elif self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
            self.consume()

        else:
            raise Exception('not support token %s', token_type)
    
    
    def expr(self):
        token_type, token_val = self.cur_token
        if token_type == TOKEN_GETER.STR:
            self.consume()
            return token_val
        elif token_type == TOKEN_GETER.INT:
            self.consume()
            return token_val
        elif token_type == TOKEN_GETER.ID:
            self.consume()
            return self.symtab[token_val]

    
    def consume(self):
        self.cur_token = self.lexer.next_token()
    
    def match(self, token_type):
        if self.cur_token[0] == token_type:
            self.consume()
            return True
        else:
            return False
#        raise Exception('expecting %s; found %s' % (token_type, self.cur_token[0]))


if __name__ == '__main__':
    prog = '''
        p = 7 ^ 2
        t = 4 * 3 * 2
        p %= t
        print (p)
        # This is a comment

    '''
    lex = TOKEN_GETER.TOKEN_GETER(prog)
    parser = Interpreter(lex)
    parser.statlist()
