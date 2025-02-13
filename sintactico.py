import ply.yacc as yacc
from lexico import tokens

# Precedencia de operadores actualizada
precedence = (
    ('left', 'LOR'),          
    ('left', 'LAND'),          
    ('left', 'LT', 'GT', 'LE', 'GE'),     
    ('left', 'PLUS', 'MINUS'),
    ('left', 'EQ'),
    ('left', 'NE'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'TERNARY'),  
    ('right', 'DECREMENT'), 
    ('right', 'INCREMENT'),  
    ('right', 'LNOT')  
)

# Reglas de gramática
def p_program(p):
    '''program : statements'''
    p[0] = ('program', p[1])

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_increment(p):
    'statement : ID INCREMENT SEMICOLON'
    p[0] = ('increment_stmt', p[1])  

def p_statement_decrement(p):
    'statement : ID DECREMENT SEMICOLON'
    p[0] = ('decrement_stmt', p[1])  

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN statement
                 | IF LPAREN expression RPAREN statement ELSE statement'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if-else', p[3], p[5], p[7])

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression LOR term
                  | expression LAND term
                  | expression EQ term
                  | expression NE term'''
    p[0] = ('operation', p[2], p[1], p[3])

def p_expression_comparison(p):
    '''expression : expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression'''
    p[0] = ('comparison', p[2], p[1], p[3])

def p_expression_logical_not(p):
    'expression : LNOT expression'
    p[0] = ('not', p[2])

def p_expression_increment(p):
    'expression : ID INCREMENT'
    p[0] = ('increment', p[1])

def p_expression_decrement(p):
    'expression : ID DECREMENT'
    p[0] = ('decrement', p[1])

def p_expression_ternary(p):
    'expression : expression TERNARY expression COLON expression'
    p[0] = ('ternary', p[1], p[3], p[5])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER
              | FLOAT'''
    p[0] = ('number', p[1])

def p_factor_string(p):
    'factor : STRING_LITERAL'
    p[0] = ('string', p[1])

def p_factor_id(p):
    'factor : ID'
    p[0] = ('id', p[1])

def p_factor_true_false(p):
    '''factor : TRUE
              | FALSE'''
    if p.slice[1].type == 'TRUE':
        p[0] = ('bool_true', True)
    else:
        p[0] = ('bool_false', False)

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Error sintáctico en '%s'" % p.value if p else "Error en entrada")

# Construir el analizador sintáctico
parser = yacc.yacc()

