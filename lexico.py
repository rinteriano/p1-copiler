import ply.lex as lex

# Lista de tokens
tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'CADENA',
    'OPERADOR',
    'DELIMITADOR'
]

# Palabras reservadas
reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
}
tokens += list(reservadas.values())

# Reglas para los tokens
t_OPERADOR = r'\+|-|\*|/|='
t_DELIMITADOR = r'\(|\)|\{|\}|\[|\]|;|,'
t_CADENA = r'\".*?\"'

# Reglas para identificadores y números
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')  # Palabras reservadas
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
