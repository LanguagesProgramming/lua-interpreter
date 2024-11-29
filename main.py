from lua_interpreter.parser import parser
from lua_interpreter.lexer import lexer

lua_code = '''
-- Definition of variables
a, b, c, d = 1, 2, 3, 4
a = 2
a, b = 2
a = 2, 4
c = "asdsa"
z = true
x = false
f = nil

if a then hi = 'x' end
if 3 then x = 23 end

v = "5" + 4
g = "adsd" + true
h = "asfsads"..true
k = "asds"..'asdasd'
j = 234 + 23.2
g = 1 + 2 + 3 + 4
d = {}
b = {2}
j = {1, 3, var = "hola"}
b = #j
f = #g
v = #2

'''

def run():
    lexer.input(lua_code)
    print("\nLexical Analysis\n")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    print("\nEnd of Lexical Analysis\n")

    print("\nParsing\n")
    lines = lua_code.split("\n")
    for line in lines:
        parser.parse(line)

    print("\nEnd of Parsing\n")


if __name__ == "__main__":
    run()
