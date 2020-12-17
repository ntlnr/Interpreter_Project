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
        token_type = self.cur_token[0]
        token_val = self.cur_token[1]

        # Assignment
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
            #print ('#' + v)

        #if/else blocks
        elif token_type == TOKEN_GETER.IF:
            token_counter = self.cur_token[2]
            self.consume()
            while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                self.consume()
            sign = self.stat()

            if sign == True:
                while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                    self.consume()
                self.consume()
                while self.cur_token[2] - token_counter == 1:
                    self.stat()
                    if not self.lexer.has_next():
                        break

                if self.cur_token[0] == TOKEN_GETER.ELIF:
                    token_counter1 = self.cur_token[2]
                    self.consume()
                    while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                        self.consume()
                    sign = self.stat()

                    while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                        self.consume()
                    while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                        self.consume()
                    while (not self.lexer.has_next()) or (self.cur_token[2] - token_counter1 != 0):
                        if not self.lexer.has_next():
                            break
                        self.consume()
                        while (self.cur_token[0] != TOKEN_GETER.PRINT and 
                            self.cur_token[0] != TOKEN_GETER.IF and 
                            self.cur_token[0] != TOKEN_GETER.ELSE and 
                            self.cur_token[0] != TOKEN_GETER.ID and
                            self.cur_token[0] != TOKEN_GETER.ELIF):
                            self.consume()
                            if not self.lexer.has_next():
                                break


                if self.cur_token[0] == TOKEN_GETER.ELSE:
                    token_counter1 = self.cur_token[2]
                    self.consume()
                    while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                        self.consume()
                    while (not self.lexer.has_next()) or (self.cur_token[2] - token_counter1 != 0):
                        if not self.lexer.has_next():
                            break
                        self.consume()
                        while (self.cur_token[0] != TOKEN_GETER.PRINT and 
                            self.cur_token[0] != TOKEN_GETER.IF and 
                            self.cur_token[0] != TOKEN_GETER.ELSE and 
                            self.cur_token[0] != TOKEN_GETER.ID and
                            self.cur_token[0] != TOKEN_GETER.ELIF):
                            self.consume()
                            if not self.lexer.has_next():
                                break
                
                
            elif sign == False:
                while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                    self.consume()
                self.consume()
                while (not self.lexer.has_next()) or (self.cur_token[2] - token_counter != 0):
                    if not self.lexer.has_next():
                        break
                    self.consume()
                    while (self.cur_token[0] != TOKEN_GETER.PRINT and 
                            self.cur_token[0] != TOKEN_GETER.IF and 
                            self.cur_token[0] != TOKEN_GETER.ELSE and 
                            self.cur_token[0] != TOKEN_GETER.ID and 
                            self.cur_token[0] != TOKEN_GETER.ELIF):
                        self.consume()
                        if not self.lexer.has_next():
                            break

                if self.cur_token[0] == TOKEN_GETER.ELIF:
                    token_counter1 = self.cur_token[2]
                    self.consume()
                    while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                        self.consume()
                    sign = self.stat()
                    while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                        self.consume()

                    if sign == True:
                        while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                            self.consume()
                        while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                            self.consume()
                        while self.cur_token[2] - token_counter1 == 1:
                            self.stat()
                            if not self.lexer.has_next():
                                break
                        if self.cur_token[0] == TOKEN_GETER.ELSE:
                            token_counter2 = self.cur_token[2]                     
                            self.consume()
                            while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                                self.consume()
                            while (not self.lexer.has_next()) or (self.cur_token[2] - token_counter2 != 0):
                                if not self.lexer.has_next():
                                    break
                                self.consume()
                                while (self.cur_token[0] != TOKEN_GETER.PRINT and 
                                        self.cur_token[0] != TOKEN_GETER.IF and 
                                        self.cur_token[0] != TOKEN_GETER.ELSE and 
                                        self.cur_token[0] != TOKEN_GETER.ID and
                                        self.cur_token[0] != TOKEN_GETER.ELIF):
                                    self.consume()
                                    if not self.lexer.has_next():
                                        break
                
                        if self.cur_token[0] == TOKEN_GETER.ELIF:
                            token_counter2 = self.cur_token[2]
                            self.consume()
                            while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                                self.consume()
                            sign = self.stat()

                            while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                                self.consume()
                            while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                                self.consume()
                            while (not self.lexer.has_next()) or (self.cur_token[2] - token_counter2 != 0):
                                if not self.lexer.has_next():
                                    break
                                self.consume()
                                while (self.cur_token[0] != TOKEN_GETER.PRINT and 
                                        self.cur_token[0] != TOKEN_GETER.IF and 
                                        self.cur_token[0] != TOKEN_GETER.ELSE and 
                                        self.cur_token[0] != TOKEN_GETER.ID and
                                        self.cur_token[0] != TOKEN_GETER.ELIF):
                                    self.consume()
                                    if not self.lexer.has_next():
                                        break
                    if sign == False:
                        while (not self.lexer.has_next()) or (self.cur_token[2] - token_counter1 != 0):
                            if not self.lexer.has_next():
                                break
                            self.consume()
                            while (self.cur_token[0] != TOKEN_GETER.PRINT and 
                                    self.cur_token[0] != TOKEN_GETER.IF and 
                                    self.cur_token[0] != TOKEN_GETER.ELSE and 
                                    self.cur_token[0] != TOKEN_GETER.ID and 
                                    self.cur_token[0] != TOKEN_GETER.ELIF):
                                self.consume()
                                if not self.lexer.has_next():
                                    break



                if self.cur_token[0] == TOKEN_GETER.ELSE:
                    token_counter1 = self.cur_token[2]
                    self.consume()
                    while self.cur_token[0] == TOKEN_GETER.SIMCOL:
                        self.consume()
                    while self.cur_token[2] - token_counter1 == 1:
                        self.stat()
                        if not self.lexer.has_next():
                            break

                
                        
    
        # print statement
        elif token_type == TOKEN_GETER.PRINT:
            self.consume()
            while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                self.consume()
            v = str(self.expr())

            while self.cur_token[0] == TOKEN_GETER.COMMA:
                self.match(TOKEN_GETER.COMMA)
                if self.cur_token[0] == TOKEN_GETER.STR_:
                    self.consume()
                    while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                        self.consume()
                v += '' + str(self.expr())
                if self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                    self.consume()

            while self.cur_token[0] == TOKEN_GETER.ADD:
                self.match(TOKEN_GETER.ADD)
                if self.cur_token[0] == TOKEN_GETER.STR_:
                    self.consume()
                    while self.cur_token[0] == TOKEN_GETER.LPARENTHESES:
                        self.consume()
                v += '' + str(self.expr())
                if self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                    self.consume()
            print (v)
            while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                self.consume()


        # add statement
        elif token_type == TOKEN_GETER.ADD:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            if self.cur_token[0] == TOKEN_GETER.SUBTRACT:
                self.consume()
                second_num = -int(self.expr())
            else:
                second_num = int(self.expr())
            result = first_num + second_num
            self.symtab[num[0]] = result

        # subtract statement
        elif token_type == TOKEN_GETER.SUBTRACT:
            num = self.symtab.popitem()
            if num[1] == None:
                self.consume()
                first_num = -int(self.cur_token[1])
                self.symtab[num[0]] = first_num
                self.consume()
            else:
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
            if self.cur_token[0] == TOKEN_GETER.SUBTRACT:
                self.consume()
                second_num = -int(self.expr())
            else:
                second_num = int(self.expr())
            result = first_num * second_num
            self.symtab[num[0]] = result

        # division statement
        elif token_type == TOKEN_GETER.DIVISION:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            if self.cur_token[0] == TOKEN_GETER.SUBTRACT:
                self.consume()
                second_num = -int(self.expr())
            else:
                second_num = int(self.expr())
            result = first_num / second_num
            self.symtab[num[0]] = result

        # power statement
        elif token_type == TOKEN_GETER.POWER:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            if self.cur_token[0] == TOKEN_GETER.SUBTRACT:
                self.consume()
                second_num = -int(self.expr())
            else:
                second_num = int(self.expr())
            result = pow(first_num, second_num)
            self.symtab[num[0]] = result

        # modulo statement
        elif token_type == TOKEN_GETER.MODULO:
            num = self.symtab.popitem()
            first_num = int(num[1])
            self.consume()
            if self.cur_token[0] == TOKEN_GETER.SUBTRACT:
                self.consume()
                second_num = -int(self.expr())
            else:
                second_num = int(self.expr())
            result = first_num % second_num
            self.symtab[num[0]] = result


        

        elif self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
            self.consume()
            while self.cur_token[0] == TOKEN_GETER.RPARENTHESES:
                self.consume()
        else:
            raise Exception('not support token %s', token_type)
    
    
    def expr(self):
        token_type = self.cur_token[0]
        token_val = self.cur_token[1]
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
        # Pokemon master name
        name = "Ash Ketchum"

        # Pokemon Health Points
        charmender_HP = 110
        squirtle_HP = 125
        bulbasaur_HP = 150

        # Pokemon Attack Points
        charmender_attack = 40
        squirtle_attack = 35
        bulbasaur_attack = 25

        eq1 = 2 * -5 + 20
        print("EQ1: "+str(eq1))
        if(eq1 != 0):
            print("eq1 output not equal to 0")
        eq2 = -2 * 3 / 12
        print("EQ2: "+str(eq2))

        if charmender_HP <= 1:
            print(name+"'s Charmender won!")
        elif squirtle_HP >=1:
            print(name+"'s Squirtle won!")
        else:
            print("something went wrong!")

    '''
    lex = TOKEN_GETER.TOKEN_GETER(prog)
    parser = Interpreter(lex)
    parser.statlist()
