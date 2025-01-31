from lexico import lexer
from sintactico import parser
import diagram as dg

tabla_simbolos = {}

def agregar_a_tabla(token, tipo, valor=None):
    tabla_simbolos[token] = {"tipo": tipo}

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ingreso de texto en el editor")
        print("2. Análisis léxico")
        print("3. Análisis sintáctico en árbol")
        print("4. Tabla de símbolos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            codigo = input("Ingresa el código: ")
        elif opcion == '2':
            lexer.input(codigo)
            print("\n--- Tokens ---")
            for token in lexer:
                print(token)
                agregar_a_tabla(token.value, token.type)

        elif opcion == '3':
            print("\n--- Árbol Sintáctico ---")
            resultado = parser.parse(codigo)
            print(resultado)

            dot = dg.dibujar_arbol(resultado)

            dot.render("Arbol Sintactico", format='png', view=True)

        elif opcion == '4':
            print("\n--- Tabla de Símbolos ---")
            for simbolo, datos in tabla_simbolos.items():
                print(f"{simbolo}: {datos}")

        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == '__main__':
    menu_principal()
