from lua_interpreter.ply import yacc as yacc
from lua_interpreter.lexer import tokens

def p_assignment(p):
    'assignment : VAR EQUAL value'

def p_value(p):
    'value : NUMBER'
    p[0] = p[1]

def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
