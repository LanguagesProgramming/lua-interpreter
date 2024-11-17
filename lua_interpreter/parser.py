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
    'block : chunk'

def p_statement(p):
    '''statement : assignment
                 | function_statement
                 | local_function'''

def p_assignment(p):
    'assignment : varlist EQUAL explist'

def p_function_statement(p):
    'function_statement : FUNCTION funcname funcbody'

def p_local_function(p):
    'local_function : LOCAL FUNCTION NAME funcbody'

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
    'var : NAME'

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
           | STRING'''

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
    '''parlist : namelist'''

def p_fieldsep(p):
    '''fielsep : COMMA
               | SEMICOLON'''

def p_binop(p):
    '''binop : PLUS
             | MINUS
             | ASTERISC
             | SLASH'''

def p_unop(p):
    '''unop : MINUS
            | NOT
            | HASH'''

def p_empty(p):
    'empty :'

def p_error(p):
    print(f"Syntax error near '{p}'")

parser = yacc.yacc()
