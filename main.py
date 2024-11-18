from lua_interpreter.parser import parser
from lua_interpreter.lexer import lexer

lua_code = '''while 1 do
    repeat
        x = 1
    until x > 10
end
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
