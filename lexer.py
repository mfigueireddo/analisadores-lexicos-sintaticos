import ply.lex as lex

# Lista de tokens
tokens = [
    'doispontos',   # :
    'abrechaves',   # {
    'fechachaves',  # }
    'virgula',      # ,
    'ponto',        # .
    'igual',        # =
    'abreparenteses', # (
    'fechaparenteses', # )
    'andand',       # &&
    'oplogic',      # operadores lógicos: ==, !=, <, >, <=, >=
    'num',          # números
    'bool',         # true ou false
    'nome',         # namedevice, observation, msg, ACTION (identificadores)
]

# Palavras reservadas (keywords)
reserved = {
    'dispositivo': 'dispositivo',
    'set': 'set',
    'se': 'se',
    'entao': 'entao',
    'senao': 'senao',
    'enviar': 'enviar',
    'alerta': 'alerta',
    'ligar': 'ligar',
    'desligar': 'desligar',
}

# Junta os tokens das palavras reservadas à lista tokens
tokens = tokens + list(reserved.values())

# Expressões regulares para tokens simples
t_doispontos = r':'
t_abrechaves = r'\{'
t_fechachaves = r'\}'
t_virgula = r','
t_ponto = r'\.'
t_igual = r'='
t_abreparenteses = r'\('
t_fechaparenteses = r'\)'
t_andand = r'&&'

# Operadores lógicos
def t_OPLOGIC(t):
    r'(==|!=|<=|>=|<|>)'
    return t

# Números (inteiros ou float)
def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Booleanos (true, false)
def t_BOOL(t):
    r'\b(true|false)\b'
    t.value = True if t.value == 'true' else False
    return t

# Identificadores (namedevice, observation, msg, ACTION, etc)
def t_NOME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Se for palavra reservada, converte o tipo do token
    t.type = reserved.get(t.value, 'NOME')
    return t

# Ignorar espaços e tabs
t_ignore = ' \t'

# Ignorar comentários (exemplo: linhas começando com #)
def t_COMMENT(t):
    r'\#.*'
    pass

# Nova linha para contagem de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construir o lexer
lexer = lex.lex()