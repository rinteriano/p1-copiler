from lexico import lexer
from sintactico import parser

tabla_simbolos = {}

def agregar_a_tabla(token, tipo, valor=None):
    tabla_simbolos[token] = {"tipo": tipo, "valor": valor}


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
            entrada = input("Ingresa el código: ")
        elif opcion == '2':
            lexer.input(entrada)
            print("\n--- Tokens ---")
            for token in lexer:
                print(token)
                # areglar que guarde conforme a los tokens
                agregar_a_tabla(token.value, "Variable")

        elif opcion == '3':
            print("\n--- Árbol Sintáctico ---")
            resultado = parser.parse(entrada)
            print(resultado)
        elif opcion == '4':
            print("\n--- Tabla de Símbolos ---")
            for simbolo, datos in tabla_simbolos.items():
                print(f"{simbolo}: {datos}")
            # dot = dibujar_arbol(resultado)
            # dot.render("arbol_sintactico", format="png", view=True)

        elif opcion == '5':
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == '__main__':
    menu_principal()
