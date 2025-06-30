import ply.lex as lex

# nome dos tokens de operadores e constantes
reservados = ('mais','menos','multiplicacao','divisao') 

# expressões regulares para tokens de operadores e constantes 

t_mais = r'\+'
t_menos = r'-'
t_multiplicacao = r'\*'
t_divisao = r'/'

def t_numero(t): # aqui definimos o token numero, ele nesse caso converte o valor direto para um inteiro, mas poderia ser um float
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n' # ignora espaços e tabs

def t_error(t): # nos dizer qual caractere ilegal e se tem erro
    print("Caracter ilegal: ", t.value[0])
    t.lexer.skip(1)

tokens = reservados + ('numero',)

lexer = lex.lex(debug=False)