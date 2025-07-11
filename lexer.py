import ply.lex as lex

reservados = {
    'dispositivo': 'dispositivo',
    'set': 'set',
    'se': 'se',
    'senao': 'senao',
    'entao': 'entao',
    'ligar': 'ligar',
    'desligar': 'desligar',
    'para': 'para',
    'todos': 'todos',
    'enviar': 'enviar',
    'alerta': 'alerta'
}

tokens = [
    # Variáveis
    'identificador',
    'numero',
    'string',
    # Auxiliares
    'igual',
    'virgula',
    'ponto',
    'abrechaves',
    'fechachaves',
    'abreparenteses',
    'fechaparenteses',
    'abreaspas',
    'fechaaspas',
    'doispontos',
    'operadorlogico',
    'andand',
    'booleano'
] + list(reservados.values())

# Variáveis
t_string = r'"(([^\\"]|\\.){0,100})"'

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

# Variáveis

def t_numero(t): 
    r'\d+'
    t.value = int(t.value)
    return t

def t_booleano(t):
    r'True|False'
    return t

# Reconhece identificador e reservados
def t_identificador(t): 
    r'[a-zA-Z]+'  # apenas letras
    t.type = reservados.get(t.value, 'identificador') 
    return t

t_ignore = ' \t\n' 

def t_error(t): 
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(debug=False)