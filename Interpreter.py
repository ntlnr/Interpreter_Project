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
            
            # For the terminal token, it only needs to match and consume.
            # If it's not matched, it means that is a syntax error.
            self.match(TOKEN_GETER.EQUAL)
            
            # Store the value to symbol table.
            self.symtab[token_val] = self.expr()
            
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
        raise Exception('expecting %s; found %s' % (token_type, self.cur_token[0]))

if __name__ == '__main__':
    prog = '''
        name = "Ash Ketchum"
        
        charmender_HP = 110
        squirtle_HP = 125
        bulbasaur_HP = 150

        charmender_attack = 40
        squirtle_attack = 35
        bulbasaur_attack = 25
        
        print ("name", name)
        print (name, "name")
        print ("Charmender did "+str (charmender_attack)+" damage")
    '''
    lex = TOKEN_GETER.TOKEN_GETER(prog)
    parser = Interpreter(lex)
    parser.statlist()