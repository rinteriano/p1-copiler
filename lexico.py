import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'LT', 'GT', 'LNOT', 'INCREMENT'
]

# Expresiones regulares para tokens simples
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_EQUALS    = r'='
t_LT        = r'<'
t_GT        = r'>'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_SEMICOLON = r';'
t_COMMA     = r','
t_LNOT      = r'!'      # Operador lógico de negación (!)
t_INCREMENT = r'\+\+'   # Operador de incremento (++)

# Identificadores (variables, nombres de funciones, etc.)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Números enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Ignorar comentarios de una línea tipo "//..."
def t_COMMENT(t):
    r'//.*'
    pass

# Manejo de errores léxicos
def t_error(t):
    print(f"Error léxico: carácter ilegal '{t.value[0]}' en la posición {t.lexpos}")
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Prueba del lexer
if __name__ == "__main__":
    data = "x = 5; y = x++ + !z;"
    lexer.input(data)
    
    print("Tokens encontrados:")
    for tok in lexer:
        print(tok)

