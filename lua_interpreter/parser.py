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
                 | while
                 | repeat_until
                 | if
                 | for
                 | function_statement
                 | local_function_statement
                 | local_assignment'''

def p_assignment(p):
    'assignment : varlist EQUAL explist'

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
           | NAME
           | STRING
           | VARARGS
           | function
           | prefixexp
           | tableconstructor
           | exp binop exp
           | unopexp'''

def p_unoexp(p):
    '''unopexp : expr_uminus
               | not_exp
               | length_exp'''

def p_expr_uminus(p):
    'expr_uminus : MINUS exp %prec UMINUS'
    p[0] = -p[2]

def p_not_exp(p):
    'not_exp : NOT exp'

def p_length_exp(p):
    'length_exp : LENGTH exp'

def p_prefixexp(p):
    '''prefixexp : var 
                 | functioncall
                 | LPAREN exp RPAREN'''

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

###### Erick Lorenzo ####### Lua has only one data structure
def p_tableconstructor(p):
    '''tableconstructor : LCURLYBRACKET RCURLYBRACKET
                        | LCURLYBRACKET fieldlist RCURLYBRACKET'''

def p_fieldlist(p):
    '''fieldlist : field
                 | field fieldsep fieldlist'''

def p_field(p):
    '''field : LSQUAREDBRACKET exp RSQUAREDBRACKET EQUAL exp
             | NAME EQUAL exp 
             | exp'''

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
