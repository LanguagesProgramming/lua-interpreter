import ply.lex as lex

def log(txt_name: str, contenido: str):
    with open(txt_name, 'w') as archivo:
        archivo.write(contenido)

def test(script: str, txt_name: str, lexer):
    with open(script, 'r') as archivo:
        lexer.input(archivo.read())
    contenido = ""
    while True:
        tok = lexer.token()
        if not tok:
            break
        contenido += str(tok) + "\n"
        log(txt_name, contenido)