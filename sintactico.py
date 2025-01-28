import ply.yacc as yacc
from lexico import tokens

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

# Reglas de gramática

def p_statement_for(p):
    'statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'
    p[0] = ('for', p[3], p[5], p[7], p[9])  # Inicialización, condición, incremento, cuerpo

def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN statement'
    p[0] = ('while', p[3], p[5])  # Condición y cuerpo


def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_block(p):
    'statement : LBRACE statements RBRACE'
    p[0] = ('block', p[2])

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN statement
                 | IF LPAREN expression RPAREN statement ELSE statement'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if-else', p[3], p[5], p[7])

def p_statement_expression(p):
    'statement : expression SEMICOLON'
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = (p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = (p[2], p[1], p[3])

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

def p_expression_equals(p):
    'expression : ID EQUALS expression'
    p[0] = ('=', p[1], p[3])

def p_error(p):
    print("Error sintáctico en '%s'" % p.value if p else "Error en entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()
