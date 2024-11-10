import ply.lex as lex

###### Ariel Vargas ######
reserved = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR'}
######

tokens = (
   'INT',
   'DECIMAL',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRACKET',
   'RBRACKET',
   'MOD',
   'VAR',
   'SEMICOLON',
   'COLON',
   'PRINT',
) + tuple(reserved.values())

###### Braulio Rivas ######
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_MOD = r'%'
t_SEMICOLON = r';'
t_COLON = r','
t_ignore  = ' \t'

###### 

###### Erick Lorenzo ######

###### 

def t_VAR(t): 
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

### 

lexer = lex.lex()

data = '''
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
