from ply.yacc import yacc
from lexer import tokens

codigo_gerado = []

def p_EXPRESSAO(regras):
    '''
    EXPRESSAO : numero OPERACAO numero
    '''

    operando1 = regras[1]
    operador = regras[2]
    operando2 = regras[3]

    # Gera a linha de código como string
    linha_codigo = f"{operando1} {operador} {operando2}"
    codigo_gerado.append(f"resultado = {linha_codigo}")

    # Também pode armazenar resultado da operação se quiser
    regras[0] = linha_codigo  # ou o valor computado, mas não obrigatório
    

def p_OPERACAO(regras):
    '''
    OPERACAO : mais
             | menos
             | multiplicacao
             | divisao
    '''
    
    regras[0] = regras[1]  # '+', '-', '*', '/'

def p_error(regras):
    print("Erro de sintaxe"+ str(regras))

parser = yacc(debug=False) # construção do parser