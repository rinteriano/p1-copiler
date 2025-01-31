import tkinter as tk
from tkinter import ttk, scrolledtext
from lexico import lexer
from sintactico import parser
import diagram as dg

# Diccionario para la tabla de símbolos
tabla_simbolos = {}

def agregar_a_tabla(token, tipo, valor=None):
    tabla_simbolos[token] = {"tipo": tipo}

def realizar_analisis_lexico():
    codigo = editor.get("1.0", tk.END).strip()
    lexer.input(codigo)
    resultado_tokens.delete("1.0", tk.END)
    tabla_simbolos.clear()
    # Limpiar la tabla
    for item in tree_tabla_simbolos.get_children():
        tree_tabla_simbolos.delete(item)
    resultado_tokens.insert(tk.END, "--- Tokens ---\n")
    for token in lexer:
        resultado_tokens.insert(tk.END, f"{token}\n")
        agregar_a_tabla(token.value, token.type)
    # Actualizar la tabla
    actualizar_tabla_simbolos()

def realizar_analisis_sintactico():
    codigo = editor.get("1.0", tk.END).strip()
    resultado_arbol.delete("1.0", tk.END)
    try:
        resultado = parser.parse(codigo)
        resultado_arbol.insert(tk.END, f"--- Árbol Sintáctico ---\n{resultado}\n")
        dot = dg.dibujar_arbol(resultado)
        dot.render("Arbol_Sintactico", format='png', view=True)
    except Exception as e:
        resultado_arbol.insert(tk.END, f"Error en análisis sintáctico: {e}")

def actualizar_tabla_simbolos():
    for simbolo, datos in tabla_simbolos.items():
        tree_tabla_simbolos.insert("", "end", values=(simbolo, datos["tipo"]))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador Léxico y Sintáctico")
ventana.geometry("900x600")

# Marco principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(fill=tk.BOTH, expand=True)

# Marco izquierdo (entrada de código)
frame_izquierdo = tk.Frame(frame_principal)
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Editor de código
tk.Label(frame_izquierdo, text="Código a Analizar:").pack()
editor = scrolledtext.ScrolledText(frame_izquierdo, height=20, width=50)
editor.pack()

# Botones
frame_botones = tk.Frame(frame_izquierdo)
frame_botones.pack()
btn_lexico = tk.Button(frame_botones, text="Análisis Léxico", command=realizar_analisis_lexico)
btn_lexico.pack(side=tk.LEFT, padx=5, pady=5)
btn_sintactico = tk.Button(frame_botones, text="Análisis Sintáctico", command=realizar_analisis_sintactico)
btn_sintactico.pack(side=tk.LEFT, padx=5, pady=5)
btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.pack(side=tk.LEFT, padx=5, pady=5)

# Marco derecho (resultados)
frame_derecho = tk.Frame(frame_principal)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Área de resultados (tokens)
tk.Label(frame_derecho, text="Resultado Tokens:").pack()
resultado_tokens = scrolledtext.ScrolledText(frame_derecho, height=5, width=50)
resultado_tokens.pack()

# Área de resultados (árbol sintáctico)
tk.Label(frame_derecho, text="Resultado Árbol Sintáctico:").pack()
resultado_arbol = scrolledtext.ScrolledText(frame_derecho, height=5, width=50)
resultado_arbol.pack()

# Tabla de símbolos
tk.Label(frame_derecho, text="Tabla de Símbolos:").pack()
tree_tabla_simbolos = ttk.Treeview(frame_derecho, columns=("Símbolo", "Tipo"), show="headings", height=10)
tree_tabla_simbolos.heading("Símbolo", text="Símbolo")
tree_tabla_simbolos.heading("Tipo", text="Tipo")
tree_tabla_simbolos.pack(fill=tk.BOTH, expand=True)

# Iniciar la ventana
ventana.mainloop()
