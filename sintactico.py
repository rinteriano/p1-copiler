import ply.yacc as yacc
from lexico import tokens  # Importar tokens desde el analizador léxico

# Precedencia de operadores
precedence = (
    ('left', 'LT', 'GT'),  # Comparaciones
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'LNOT'),  # Operador unario (!)
    ('right', 'INCREMENT')  # Operador de incremento (++)
)

# Reglas de gramática
def p_statement_declaration(p):
    'statement : ID EQUALS expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_statement_expression(p):
    'statement : expression SEMICOLON'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_comparison(p):
    '''expression : expression LT expression
                  | expression GT expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_unary(p):
    '''expression : LNOT expression
                  | ID INCREMENT'''
    if p[1] == '!':
        p[0] = ('not', p[2])
    else:
        p[0] = ('increment', p[1])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    if p:
        print(f"Error sintáctico en '{p.value}' en la posición {p.lexpos}")
    else:
        print("Error en entrada")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Prueba del parser
if __name__ == "__main__":
    data = "x = 5; y = x++ + !z;"
    result = parser.parse(data)
    print("Árbol sintáctico:", result)

