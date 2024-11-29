from lua_interpreter.ply import yacc as yacc
from lua_interpreter.lexer import tokens
from collections import deque

symbols = {}

def symbol_exists(symbol):
    return symbol in symbols

def p_chunk(p):
    '''chunk : empty
             | list_statements
             | last_statement
             | list_statements last_statement'''

def p_list_statements(p):
    '''list_statements : statement
                       | statement SEMICOLON list_statements'''

def p_block(p):
    '''block : chunk'''

def p_statement(p):
    '''statement : assignment
                 | functioncall
                 | while
                 | repeat_until
                 | if
                 | for
                 | function_statement
                 | local_function_statement
                 | local_assignment'''

# Automatic assign nil if not defined
def p_assignment(p):
    'assignment : varlist EQUAL explist'
    varlist = p[1].split(", ")
    len_varlist = len(varlist)
    explist = p[3]

    # print(p[1], p[3])

    if type(explist) == deque:
        len_explist = len(explist)
        if len_varlist >= len_explist:
            i = 0
            for exp in explist:
                var = varlist[i]
                symbols[var] = exp
                i += 1

            while i < len_varlist:
                var = varlist[i]
                symbols[var] = Nil()
                i += 1 
    elif len_varlist != 1:
        symbols[varlist[0]] = explist

        i = 1
        for x in range(i, len_varlist):
            var = varlist[x]
            symbols[var] = Nil()
    else:
        symbols[p[1]] = p[3]

###### Ariel Vargas #######
def p_while(p):
    'while : WHILE exp DO block END'

def p_repeat_until(p):
    'repeat_until : REPEAT block UNTIL exp'
#########

###### Braulio Rivas  #######
def p_if(p):
    '''if : IF exp THEN block END
          | IF exp THEN block elseif_list END
          | IF exp THEN block elseif_list ELSE block END'''

    if len(p) == 6:
        pass


def p_elseif_list(p):
    '''elseif_list : elseif
                   | elseif elseif_list'''

def p_elseif(p):
    'elseif : ELSEIF exp THEN block'
#########

###### Erick Lorenzo #######
def p_for(p):
    '''for : FOR NAME EQUAL exp COMMA exp DO block END 
           | FOR namelist IN explist DO block END'''

def p_function_statement(p):
    'function_statement : FUNCTION funcname funcbody'
#########

###### Ariel Vargas #######
def p_local_function_statement(p):
    'local_function_statement : LOCAL FUNCTION NAME funcbody'
#########
                      
def p_local_assignment(p):
    '''local_assignment : LOCAL namelist
                        | LOCAL namelist EQUAL explist'''

def p_last_statement(p):
    '''last_statement : RETURN 
                      | RETURN explist
                      | BREAK'''

def p_funcname(p):
    '''funcname : NAME'''
   
def p_varlist(p):
    '''varlist : var 
               | var COMMA varlist'''
    if len(p) == 4:
        p[0] = f"{p[1]}, {p[3]}"
    else:
        p[0] = p[1]


def p_var(p):
    '''var : NAME
           | prefixexp LSQUAREDBRACKET exp RSQUAREDBRACKET
           | prefixexp DOT NAME'''
    if len(p) == 2:
        p[0] = p[1]

def p_namelist(p):
    '''namelist : NAME
                | NAME COMMA namelist'''

def p_explist(p):
    '''explist : exp
               | exp COMMA explist''' 
    
    if len(p) == 2:
        p[0] = p[1]
    else:
        if type(p[3]) == deque:
            p[3].appendleft(p[1])
            p[0] = p[3] 
        else:
            values = deque()
            values.append(p[1])
            values.append(p[3])
            p[0] = values

class Nil:
    pass

def parse_number(number_string):
    if type(number_string) == str:
        number_string = number_string.replace("\"", "")

    try:
        integer = int(number_string)
        return integer
    except:
        pass

    try:
        floating = float(number_string)
        return floating
    except:
        pass

    raise Exception("Not able to parse number") 

def p_exp(p): 
    '''exp : NIL
           | FALSE
           | TRUE
           | NUMBER
           | NAME
           | STRING
           | VARARGS
           | function
           | prefixexp
           | tableconstructor
           | exp binop exp
           | unopexp'''

    if len(p) == 4:
        binop = p[2]
        first_exp = p[1]
        first_type = type(first_exp)
        second_exp = p[3]
        second_type = type(second_exp)

        arithmetic_operators = {"+", "-", "*", "/", "^", "%", "<", "<=", ">"}
        if binop in arithmetic_operators:
            try:
                parse_number(first_exp)
            except:
                print(f"stdin: Attempt to perform arithmetic operation on {first_exp}")

            try:
                parse_number(second_exp)
            except:
                print(f"stdin: Attempt to perform arithmetic operation on and {second_exp}")
            
        if binop == '..':
            valid = (first_type == int or second_type == str) and (second_type == int or second_type == str)
            
            if not valid:
                print(f"stdin: Attempt to concatenate an invalid value between {first_exp} and {second_exp}")
    
        
    if type(p[1]) == int or type(p[1]) == str:
        if p[1] == 'true':
            p[0] = True
        elif p[1] == 'false':
            p[0] = False
        elif p[1] == 'nil':
            p[0] = Nil()
        else:
            p[0] = p[1]

        return

    p[0] = p[1]

def p_unoexp(p):
    '''unopexp : expr_uminus
               | not_exp
               | length_exp'''
    
    p[0] = p[1]

def p_expr_uminus(p):
    'expr_uminus : MINUS exp %prec UMINUS'
    p[0] = -p[2]

def p_not_exp(p):
    'not_exp : NOT exp'

def p_length_exp(p):
    'length_exp : LENGTH exp'
    
    expression = p[2]
    if type(expression) == int:
        print("stdin: attempt to get lenght of number")
    elif symbol_exists(expression):
        val = symbols[expression]
        if isinstance(val, Table):
            val: Table = val
            p[0] = val.size()
        else:
            print(f"stdin: attempt to get length of value {val}")
    else:
        print("stdin: attempt to get length of a nil value")


def p_prefixexp(p):
    '''prefixexp : var 
                 | functioncall
                 | LPAREN exp RPAREN'''
    p[0] = p[1]


def p_functioncall(p):
    '''functioncall : prefixexp args
                    | prefixexp COLON NAME args'''

def p_args(p):
    '''args : LPAREN RPAREN
            | LPAREN explist RPAREN
            | STRING'''

###### Braulio Rivas ######
def p_function(p):
    'function : FUNCTION funcbody'
######

def p_funcbody(p):
    '''funcbody : LPAREN RPAREN block END
                | LPAREN parlist RPAREN block END'''

def p_parlist(p):
    '''parlist : namelist
               | namelist COMMA VARARGS
               | VARARGS'''

class Table:
    def __init__(self, items = None):
        self.dic: dict = {}
        self.set: set = set()
        self.length: int = 0

    def add(self, val):
        if type(val) == tuple:
            [k, v] = val
            self.dic[k] = v
        else:
            self.set.add(val)

        self.length += 1

    def size(self):
        return self.length

    def __repr__(self) -> str:
        return "table"

    def __str__(self):
        string = "{"
        for k, v in self.dic.items():
            string = string + f"{k}: {v}, "

        for val in self.set:
            string = string + f"{val}, "

        if len(string) > 1:
            string = string[:-2]

        return string + "}"
        


###### Erick Lorenzo ####### Lua has only one data structure
def p_tableconstructor(p):
    '''tableconstructor : LCURLYBRACKET RCURLYBRACKET
                        | LCURLYBRACKET fieldlist RCURLYBRACKET'''

    if len(p) == 3:
        p[0] = Table()
    else:
        p[0] = p[2]


def p_fieldlist(p):
    '''fieldlist : field
                 | field fieldsep fieldlist'''

    if len(p) == 2:
        fieldlist = p[0]
        if isinstance(fieldlist, Table):
            fieldlist.add(p[1])
        else:
            table = Table()
            table.add(p[1])
            p[0] = table
            table = Table()
            table.add(p[1])
            p[0] = table
    else:
        table = p[3]
        table.add(p[1])
        p[0] = table

def p_field(p):
    '''field : LSQUAREDBRACKET exp RSQUAREDBRACKET EQUAL exp
             | NAME EQUAL exp 
             | exp'''

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = (p[1], p[3])

def p_fieldsep(p):
    '''fieldsep : COMMA
                | SEMICOLON'''
######

def p_binop(p):
    '''binop : PLUS
             | MINUS
             | MULTIPLY 
             | DIVIDE
             | CARET
             | MODULO
             | CONCATENATION
             | LESSTHAN
             | LEQUALTHAN
             | GREATERTHAN
             | GEQUALTHAN
             | EQUALITY
             | DISTINCT
             | AND
             | OR'''
    p[0] = p[1]

def p_empty(p):
    'empty :'

def p_error(p):
    try:
        print(f"{p.lexpos}: Syntax error near '{p.value}'")
    except:
        print(f"Syntax error near '{p}'")

precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'LESSTHAN', 'GREATERTHAN', 'LEQUALTHAN', 'GEQUALTHAN', 'DISTINCT', 'EQUALITY'),
        ('right', 'CONCATENATION'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
        ('left', 'NOT', 'LENGTH', 'UMINUS'),
        ('right', 'CARET'),
)

start = 'block'
parser = yacc.yacc()
