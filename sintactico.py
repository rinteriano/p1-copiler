import ply.yacc as yacc
from lexico import tokens
# Definir las reglas de gramática
def p_expresion_num(p):
    'expresion : NUMERO'
    p[0] = p[1]

def p_expresion_op(p):
    '''expresion : expresion OPERADOR expresion'''
    p[0] = (p[2], p[1], p[3])

def p_expresion_paren(p):
    'expresion : "(" expresion ")"'
    p[0] = p[2]

def p_error(p):
    print("Error sintáctico en '%s'" % p.value if p else "Error en entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()
