from lua_interpreter.ply import yacc as yacc
from lua_interpreter.lexer import tokens

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
                 | while_do
                 | repeat_until
                 | for
                 | function_statement
                 | local_function_statement
                 | local_assignment
                 | NEWLINE statement'''

def p_assignment(p):
    '''assignment : varlist EQUAL explist
                    | namelist EQUAL explist
                    | NAME EQUAL explist
                    | NAME EQUAL NUMBER
                    | NAME EQUAL NAME'''

###### Ariel Vargas #######
def p_while_do(p):
    'while_do : WHILE exp DO block END'

def p_repeat_until(p):
    'repeat_until : REPEAT block UNTIL exp'
#########

###### Erick Lorenzo #######
def p_for(p):
    '''for : FOR NAME EQUAL exp COMMA exp DO chunk END 
           | FOR namelist IN NAME DO NEWLINE chunk END'''
#########

def p_function_statement(p):
    'function_statement : FUNCTION funcname funcbody'

def p_local_function_statement(p):
    'local_function_statement : LOCAL FUNCTION NAME funcbody'
                      
def p_local_assignment(p):
    '''local_assignment : LOCAL namelist
                      | LOCAL namelist EQUAL explist
                      | LOCAL NAME EQUAL explist
                      | LOCAL NAME EQUAL var'''

def p_last_statement(p):
    '''last_statement : RETURN 
                      | RETURN explist
                      | BREAK'''

def p_funcname(p):
    '''funcname : NAME'''
   
def p_varlist(p):
    '''varlist : var 
               | var COMMA varlist'''

def p_var(p):
    '''var : NAME
            | NAME LSQUAREDBRACKET NUMBER RSQUAREDBRACKET
            | NAME LSQUAREDBRACKET var RSQUAREDBRACKET
            | NUMBER
           | prefixexp LSQUAREDBRACKET exp RSQUAREDBRACKET
           | prefixexp DOT NAME'''

def p_namelist(p):
    '''namelist : NAME
                | NAME COMMA namelist'''

def p_explist(p):
    '''explist : LCURLYBRACKET varlist RCURLYBRACKET''' 

def p_exp(p):
    '''exp : NIL
           | FALSE
           | TRUE
           | NUMBER
           | STRING
           | TRIPLEDOT
           | function
           | prefixexp
           | exp binop exp
           | unop exp'''

def p_prefixexp(p):
    '''prefixexp : var 
                 | functioncall
                 | LPAREN exp RPAREN'''

def p_functioncall(p):
    '''functioncall : prefixexp args
                    | prefixexp COLON NAME args
                    | prefixexp DOT NAME'''

def p_args(p):
    '''args : LPAREN RPAREN
            | LPAREN explist RPAREN
            | STRING'''

def p_function(p):
    'function : FUNCTION funcbody'

def p_funcbody(p):
    '''funcbody : LPAREN RPAREN block END
                | LPAREN parlist RPAREN block END'''

def p_parlist(p):
    '''parlist : namelist
               | namelist COMMA TRIPLEDOT
               | TRIPLEDOT'''

def p_fieldsep(p):
    '''fielsep : COMMA
               | SEMICOLON'''

def p_binop(p):
    '''binop : PLUS
             | MINUS
             | MULTIPLY 
             | DIVIDE
             | MODULO
             | LESSTHAN
             | LEQUALTHAN
             | GREATERTHAN
             | GEQUALTHAN
             | EQUALITY
             | DISTINCT
             | AND
             | OR'''

def p_unop(p):
    '''unop : MINUS
            | NOT
            | LENGTH'''

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
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
        ('left', 'NOT', 'LENGTH'),
)

start = 'block'
parser = yacc.yacc()