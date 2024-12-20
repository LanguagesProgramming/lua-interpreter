import io
from main import run 
import tkinter as tk
from tkinter import filedialog, messagebox
from contextlib import redirect_stdout

def imprimir_contenido():
    texto_ingresado = entrada_texto.get("1.0", tk.END).strip()
    if texto_ingresado:
        salida_texto.delete("1.0", tk.END)

        with io.StringIO() as stream:
            with redirect_stdout(stream):
                run(texto_ingresado)

            s = stream.getvalue()
            salida_texto.insert(tk.END, s)
    elif archivo_ruta:
        try:
            with open(archivo_ruta, 'r') as f:
                contenido = f.read()
                salida_texto.delete("1.0", tk.END)

                with io.StringIO() as stream:
                    with redirect_stdout(stream):
                        run(contenido)
                    s = stream.getvalue()
                    salida_texto.insert(tk.END, s)
        except Exception as e:
            salida_texto.delete("1.0", tk.END)
            salida_texto.insert(tk.END, f"Error al leer el archivo: {e}")
    else:
        messagebox.showwarning("Advertencia", "No hay texto ingresado ni archivo seleccionado.")

def seleccionar_archivo():
    global archivo_ruta
    archivo_ruta = filedialog.askopenfilename(
        title="Seleccionar archivo", filetypes=[("Archivos de texto", "*.lua"), ("Todos los archivos", "*.*")]
    )
    if archivo_ruta:
        label_archivo.config(text=f"Archivo seleccionado: {archivo_ruta.split('/')[-1]}")

ventana = tk.Tk()
ventana.title("Entrada de texto o archivo")
ventana.geometry("700x500")
ventana.configure(bg="#f0f8ff")

# Estilo y widgets
titulo = tk.Label(
    ventana, text="¡Bienvenido!", font=("Arial", 18, "bold"), bg="#4682b4", fg="white"
)
titulo.pack(pady=10, fill=tk.X)

label_texto = tk.Label(
    ventana, text="Ingrese texto:", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#333"
)
label_texto.pack(pady=5)

entrada_texto = tk.Text(
    ventana, height=10, width=70, font=("Arial", 10), bd=2, relief="groove", wrap=tk.WORD
)
entrada_texto.pack(pady=5)

label_archivo = tk.Label(
    ventana, text="No se ha seleccionado ningún archivo.",
    font=("Arial", 10), bg="#f0f8ff", fg="#8b0000"
)
label_archivo.pack(pady=5)

boton_archivo = tk.Button(
    ventana, text="Seleccionar archivo",
    font=("Arial", 11), bg="#4682b4", fg="white", activebackground="#5a9bd4",
    activeforeground="white", command=seleccionar_archivo
)
boton_archivo.pack(pady=5)

boton = tk.Button(
    ventana, text="Aceptar",
    font=("Arial", 11), bg="#32cd32", fg="white", activebackground="#3e8c3e",
    activeforeground="white", command=imprimir_contenido
)
boton.pack(pady=10)

salida_texto = tk.Text(
    ventana, height=20, width=70, font=("Arial", 10), bd=2, relief="sunken", wrap=tk.WORD
)
salida_texto.pack(padx=10, pady=10)

# Pie de página
footer = tk.Label(
    ventana, text="Desarrollado por Erick, Braulio y Ariel", font=("Arial", 9, "italic"), bg="#f0f8ff", fg="#666"
)
footer.pack(side=tk.BOTTOM, pady=10)

ventana.mainloop()
