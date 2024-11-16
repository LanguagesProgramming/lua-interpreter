import ply.lex as lex
#from test_lex import *

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
    'while' : 'WHILE',
    'print' : 'PRINT'
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
   'EQUALITY',
   'DISTINCT',
   'GEQUALTHAN',
   'LEQUALTHAN',
   'EQUAL',
   'LESSTHAN',
   'GREATERTHAN',
   'LPAREN',
   'RPAREN',
   'LCURLYBRACKET',
   'RCURLYBRACKET',
   'COMMA',
   'SEMICOLON',
   'COLON',
   'DOT',   
   'COMILLA',
   'NUMBER',
   'VAR',
   'STRING',
   'COMMENT',
) + tuple(reserved.values())

###### Braulio Rivas ######
t_PLUS    = r'\+'
t_HYPHEN   = r'-'
t_ASTERISC   = r'\*'
t_SLASH = r'\/'
t_PERCENTAGE = r'%'
t_CARET = r'\^'
t_HASH = r'\#'
t_DISTINCT = r'~='
t_GEQUALTHAN = r'>='
t_LEQUALTHAN = r'<='
t_EQUALITY = r'=='
t_EQUAL = r'='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLYBRACKET = r'\{'
t_RCURLYBRACKET = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_COMILLA = r'\"'
t_ignore  = ' \t'
###### 


###### Erick Lorenzo ######
def t_NUMBER(t):
    r'0[xX][0-9a-fA-F]+|\d+(\.\d*)?([eE][+-]?\d+)?'
    if t.value.lower().startswith("0x"):
        t.value = int(t.value, 16) 
    elif 'e' in t.value.lower() or '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t
######

def t_COMMENT_mline(t):
    r'-- \[\[.*\]\]'
    t.type = 'COMMENT'
    return t

def t_COMMENT_oline(t):
    r'-- .*'
    t.type = 'COMMENT'
    return t

def t_STRING_single(t):
    r"''"
    t.type = 'STRING'
    return t

def t_STRING_double(t):
    r'".*"'
    t.type = 'STRING'
    return t

def t_STRING_multiline(t):
    r"\[\[[^\[]*\]\]"
    t.type = 'STRING'
    return t

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

data = """
c = [[ asd
]]

-- [[
    asd
]]

"""

# test("Num_Par.lua", "Ariel-Vargas", lexer)
# test("factorial.lua", "erillope", lexer)
# test("sort.lua", "brauliorivas", lexer)
