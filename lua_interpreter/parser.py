from lua_interpreter.ply import yacc as yacc
from lua_interpreter.lexer import tokens

def p_chunk(p):
    '''chunk : empty
            | for_loop
            | list_statements
            | last_statement
            | list_statements last_statement'''

def p_list_statements(p):
    '''list_statements : statement
                       | statement SEMICOLON list_statements'''

def p_block(p):
    '''block : chunk
            | NEWLINE'''

def p_for_loop(p):
    '''for_loop : FOR namelist EQUAL exp COMMA exp DO block END
    | FOR namelist IN NAME DO block END'''
 
def p_statement(p):
    '''statement : assignment
                 | functioncall
                 | function_statement
                 | local_function_statement
                 | local_assignment
                 | while_do
                 | repeat_until'''

###### Ariel Vargas #######
def p_while_do(p):
    ''' 
    while_do : WHILE exp DO block END
    '''

def p_repeat_until(p):
    '''
    repeat_until : REPEAT block UNTIL exp
    '''

#########

def p_assignment(p):
    'assignment : varlist EQUAL explist'

def p_function_statement(p):
    'function_statement : FUNCTION funcname funcbody'

def p_local_function_statement(p):
    'local_function_statement : LOCAL FUNCTION NAME funcbody'

def p_local_assignment(p):
    '''local_assignment : LOCAL namelist
                      | LOCAL namelist EQUAL explist'''

def p_last_statement(p):
    '''last_statement : RETURN 
                      | RETURN explist
                      | BREAK'''

def p_funcname(p):
    '''funcname : NAME'''

def p_explist(p):
    '''explist : LCURLYBRACKET varlist RCURLYBRACKET'''
    
def p_varlist(p):
    '''varlist : var 
                | var COMMA varlist'''

def p_var(p):
    '''var : NAME
           | prefixexp LSQUAREDBRACKET exp RSQUAREDBRACKET
           | prefixexp DOT NAME'''

def p_namelist(p):
    '''namelist : NAME
                | NAME COMMA namelist'''

def p_explist(p):
    '''explist : exp
               | exp COMMA explist''' 

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

start = 'chunk'
parser = yacc.yacc()