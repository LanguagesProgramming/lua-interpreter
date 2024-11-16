import datetime

def log(user: str, content: str):
    current_time = datetime.datetime.now()
    formatted_date = current_time.strftime("%Y-%m-%d-%H-%M-%S")

    with open(f"logs/lexico-{user}-{str(formatted_date)}.txt", 'w') as file:
        file.write(content)

def test(script: str, usuario: str, lexer):
    with open(script, 'r') as archivo:
        lexer.input(archivo.read())
    contenido = ""
    while True:
        tok = lexer.token()
        if not tok:
            break
        contenido += str(tok) + "\n"
    log(usuario, contenido)
