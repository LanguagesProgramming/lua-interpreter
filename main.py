import ply.lex as lex

reserved = {'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'for': 'FOR'}

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

def t_PRINT(t):
    r'print'
    return t

def t_DECIMAL(t):
    r'(\d+\.\d+)'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

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
5.2 ; print(hola) (1, 2, 3) []
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
