from lua_interpreter.ply import yacc as yacc
from lua_interpreter.lexer import tokens

def p_assignment(p):
    'assignment: VAR EQUAL NUMBER'

def p_error(p):
    print("Syntax error")

parser = "parser"
