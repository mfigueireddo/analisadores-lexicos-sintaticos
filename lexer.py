import ply.lex as lex

reservados = {
    'dispositivo': 'dispositivo',
    'set': 'set',
    'se': 'se',
    'senao': 'senao',
    'entao': 'entao',
    'true': 'true',
    'false': 'false',
    'ligar': 'ligar',
    'desligar': 'desligar'
}

tokens = [
    # Variáveis
    'identificador',
    'numero',
    # Auxiliares
    'igual',
    'virgula',
    'ponto',
    'abrechaves',
    'fechachaves',
    'abreparenteses',
    'fechaparenteses',
    'doispontos',
    'operadorlogico',
    'andand'
] + list(reservados.values())

# Auxiliares
t_igual = r'\='
t_virgula = r'\,'
t_ponto = r'\.'
t_abrechaves = r'\{'
t_fechachaves = r'\}'
t_abreparenteses = r'\('
t_fechaparenteses = r'\)'
t_doispontos = r'\:'
t_operadorlogico = r'(>=|<=|==|!=|>|<)'
t_andand = r'&&'

def t_numero(t): 
    r'\d+'
    t.value = int(t.value)
    return t

def t_identificador(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservados.get(t.value, 'identificador') 
    return t

t_ignore = ' \t\n' 

def t_error(t): 
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(debug=False)