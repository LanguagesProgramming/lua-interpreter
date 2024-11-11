
import datetime

def log(usuario: str, contenido: str):
    hora_actual = datetime.datetime.now()
    fecha_hora_formateada = hora_actual.strftime("%Y-%m-%d %H-%M-%S")
    with open("lexico-"+usuario+"-"+str(fecha_hora_formateada)+'.txt', 'w') as archivo:
        archivo.write(contenido)

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