# lexico.py

import ply.lex as lex
import ply.ctokens

words_reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
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
    'LBRACKET',  # Corchete de apertura [
    'RBRACKET',  # Corchete de cierre ]
    'EQUALS',
    'SEMICOLON',
    'LT',  # Menor que (<)
    'GT',  # Mayor que (>)
    'COMMA',  # Para las listas
] + list(words_reserved.values())

# Reglas para los tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LT = r'<'
t_GT = r'>'
t_COMMA = r','  # Para las listas

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
t_ignore = ' \t|\n'

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]} en la posición {t.lexpos}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()
