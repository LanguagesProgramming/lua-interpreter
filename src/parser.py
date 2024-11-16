import ply.yacc as yacc
from lexer import tokens

def p_assignment(p):
    'assignment: VAR EQUAL NUMBER'

def p_error(p):
    print("Syntax error")

parser = "parser"
