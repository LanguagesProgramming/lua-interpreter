import ply.lex as lex

###### Ariel Vargas ######
reserved = {
    'and' : 'AND',
    'break' : 'BREAK',
    'do' : 'DO',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'end' : 'END',
    'false' : 'FALSE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'if' : 'IF',
    'in' : 'IN',
    'local' : 'LOCAL',
    'nil' : 'NIL',
    'not' : 'NOT',
    'or' : 'OR',
    'repeat' : 'REPEAT',
    'return' : 'RETURN',
    'then' : 'THEN',
    'true' : 'TRUE',
    'until' : 'UNTIL',
    'while' : 'WHILE'
}

##########

tokens = (
   'PLUS',
   'HYPHEN',
   'ASTERISC',
   'SLASH',
   'PERCENTAGE',
   'CARET',
   'HASH',
   'EQUAL',
   'TILDE',
   'LESSTHAN',
   'GREATERTHAN',
   'LPAREN',
   'RPAREN',
   'LCURLYBRACKET',
   'RCURLYBRACKET',
   'LSQUAREDBRACKET',
   'RSQUAREDBRACKET',
   'COMMA',
   'SEMICOLON',
   'COLON',
   'DOT',   
   'NUMBER',
   'VAR'
) + tuple(reserved.values())

###### Braulio Rivas ######
t_PLUS    = r'\+'
t_HYPHEN   = r'-'
t_ASTERISC   = r'\*'
t_SLASH = r'\/'
t_PERCENTAGE = r'%'
t_CARET = r'\^'
t_HASH = r'\#'
t_EQUAL = r'='
t_TILDE = r'~'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLYBRACKET = r'\{'
t_RCURLYBRACKET = r'\}'
t_LSQUAREDBRACKET = r'\['
t_RSQUAREDBRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_ignore  = ' \t'

###### 
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t
###### Erick Lorenzo ######

def t_VAR(t): 
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"{t.lineno}:{t.lexpos}: unexpected symbol {t.value[0]}" )
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
b+9*h
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
