from lua_interpreter.parser import parser
from lua_interpreter.lexer import lexer

lua_code = '''
print() ; print(1) ; print(2, 3, hola) ; io.read()
math = 4 + 5 * 8 / 4
if 4 < 3 and t == True then print("Yes") end
call = call_function()
array = {1, 2, 3}
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
