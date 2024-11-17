from lua_interpreter.parser import parser
from lua_interpreter.lexer import lexer

lua_code = '''
lua_code, h = 3, 2
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
    parse_result = parser.parse(lua_code)
    print(parse_result)
    print("\nEnd of Parsing\n")


if __name__ == "__main__":
    run()
