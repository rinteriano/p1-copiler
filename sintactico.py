import ply.yacc as yacc
from lexico import tokens

precedence = (
    ('left', 'LOR'),
    ('left', 'LAND'),
    ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

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

def p_statement_declaration(p):
    '''statement : INT ID SEMICOLON
                | FLOAT ID SEMICOLON
                | STRING ID SEMICOLON'''
    p[0] = ('declaration', p[1], p[2])

def p_statement_assignment(p):
    '''statement : ID EQUALS expression SEMICOLON
                | ID EQUALS STRING_LITERAL SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_statement_for(p):
    'statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'
    p[0] = ('for', p[3], p[5], p[7], p[9])

def p_statement_while(p):
    'statement : WHILE LPAREN expression RPAREN statement'
    p[0] = ('while', p[3], p[5])

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
    p[0] = ('expression', p[1])

def p_expression_binop(p):
    '''expression : expression PLUS term
                 | expression MINUS term
                 | expression LOR term
                 | expression LAND term'''
    p[0] = ('operation', p[2], p[1], p[3])

def p_expression_comparison(p):
    '''expression : expression LT expression
                 | expression GT expression'''
    p[0] = ('comparison', p[2], p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = ('operation', p[2], p[1], p[3])

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
    p[0] = ('identifier', p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_equals(p):
    'expression : ID EQUALS expression'
    p[0] = ('assignment', p[1], p[3])

def p_expression_list(p):
    'expression : LBRACKET elements RBRACKET'
    p[0] = ('list', p[2])

def p_elements_multiple(p):
    'elements : elements COMMA expression'
    p[0] = p[1] + [p[3]]

def p_elements_single(p):
    'elements : expression'
    p[0] = [p[1]]

def p_elements_empty(p):
    'elements : '
    p[0] = []

def p_error(p):
    print("Error sintáctico en '%s'" % p.value if p else "Error en entrada")

parser = yacc.yacc()
