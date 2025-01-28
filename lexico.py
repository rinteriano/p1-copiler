import ply.lex as lex


words_reserved = {
    'if': 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while': 'WHILE',
}
# Lista de tokens
tokens = [
    'ID',
    'NUMBER',
    'LPAREN',  # Paréntesis de apertura
    'RPAREN',  # Paréntesis de cierre
    'PLUS',
    'MINUS',
    'DIVIDE',
    'TIMES',
    'LBRACE',  # Llave de apertura {
    'RBRACE',  # Llave de cierre }
    'EQUALS',
    'SEMICOLON',

] + list(words_reserved.values())


# Reglas para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
# t_CADENA = r'\".*?\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'

# Reglas para identificadores y números
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9_]*'
    t.type = words_reserved.get(t.value, 'ID')  # Palabras reservadas
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]} en la posición {t.lexpos}")
    t.lexer.skip(1)


# Construir el analizador léxico
lexer = lex.lex()
