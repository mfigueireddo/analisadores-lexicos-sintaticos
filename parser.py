from ply.yacc import yacc
from lexer import tokens

variaveis_usadas = set()
variaveis_setadas = set()

def p_PROGRAM(regras):
    '''
    PROGRAM : DEVICES CMDS
    '''
    
    # DEVICES CMDS
    buffer = f"{regras[2]}"
    regras[0] = buffer

def p_DEVICES(regras):
    '''
    DEVICES : DEVICE DEVICES
            | DEVICE
    '''
    
    # DEVICE DEVICES
    if len(regras) == 3:
        buffer = f"{regras[1]}\n{regras[2]}"
        
    # DEVICE
    else:
        buffer = f"{regras[1]}"

    regras[0] = ""

def p_DEVICE(regras):
    '''
    DEVICE : dispositivo doispontos abrechaves identificador fechachaves
           | dispositivo doispontos abrechaves identificador virgula identificador fechachaves
    '''

    regras[0] = ""  # não gera nada no código


def p_CMDS(regras):
    '''
    CMDS : CMD ponto CMDS
         | CMD ponto
    '''
    
    # CMD ponto CMDS
    if len(regras) == 4:
        buffer = f"{regras[1]}\n{regras[3]}"
        
    # CMD ponto
    else:
        buffer = f"{regras[1]}"
    regras[0] = buffer

def p_CMD(regras):
    '''
    CMD : ATTRIB
        | OBSACT
        | ACT
    '''

    # ATTRIB | OBSACT | ACT
    buffer = f"{regras[1]}"
    regras[0] = buffer

def p_ATTRIB(regras):
    '''
    ATTRIB : set identificador igual VAR
    '''

    variaveis_setadas.add(regras[2])

    # set identificador igual VAR -> var = valor
    buffer = f"{regras[2]} = {regras[4]}"
    regras[0] = buffer

def p_OBSACT(regras):
    '''
    OBSACT : se OBS entao ACT
           | se OBS entao ACT senao ACT
    '''

    def indentar(codigo):
        return '\n'.join('    ' + linha for linha in codigo.split('\n'))

    if len(regras) == 5:
        comandos_then = indentar(regras[4])
        buffer = f"if {regras[2]}:\n{comandos_then}"
    else:
        comandos_then = indentar(regras[4])
        comandos_else = indentar(regras[6])
        buffer = f"if {regras[2]}:\n{comandos_then}\nelse:\n{comandos_else}"

    regras[0] = buffer


def p_OBS(regras):
    '''
    OBS : identificador operadorlogico VAR
        | identificador operadorlogico VAR andand OBS
    '''

    variaveis_usadas.add(regras[1])

    # identificador operadorlogico VAR
    if len(regras) == 4:
        buffer = f"{regras[1]} {regras[2]} {regras[3]}"

    # identificador operadorlogico VAR andand OBS
    else:
        # transformar && em and do Python
        buffer = f"{regras[1]} {regras[2]} {regras[3]} and {regras[5]}"
    regras[0] = buffer

def p_VAR(regras):
    '''
    VAR : numero
        | booleano
    '''
    
    # numero | booleano
    buffer = f"{regras[1]}"
    regras[0] = buffer

def p_ACT(regras):
    '''
    ACT : ACTION identificador
        | enviar alerta string identificador
        | enviar alerta abreparenteses string virgula identificador fechaparenteses identificador
        | enviar alerta string para todos doispontos DEVICENAMES
        | enviar alerta abreparenteses string virgula identificador fechaparenteses para todos doispontos DEVICENAMES
    '''
    if len(regras) == 3:
        buffer = f"{regras[1]}(\"{regras[2]}\")"

    elif len(regras) == 5:
        # alerta("identificador", "mensagem")
        buffer = f"alerta(\"{regras[4]}\", {regras[3]})"

    elif len(regras) == 9:
        # alerta("identificador", "mensagem", variavel)
        variaveis_usadas.add(regras[6])
        buffer = f"alerta(\"{regras[8]}\", {regras[4]}, {regras[6]})"

    elif len(regras) == 8: 
        # alerta("device", "mensagem") para cada em DEVICENAMES
        devices = regras[7].split(", ")
        calls = '\n'.join(f"alerta(\"{dev.strip()}\", {regras[3]})" for dev in devices)
        buffer = calls

    else:
        # alerta("device", "mensagem", variavel) para cada em DEVICENAMES
        variaveis_usadas.add(regras[6])
        devices = regras[11].split(", ")
        calls = '\n'.join(f"alerta(\"{dev.strip()}\", {regras[4]}, {regras[6]})" for dev in devices)
        buffer = calls

    regras[0] = buffer



def p_DEVICENAMES(regras):
    '''
    DEVICENAMES : identificador virgula DEVICENAMES
                | identificador
    '''
    
    # identificador virgula DEVICENAMES
    if len(regras) == 4:
        buffer = f"{regras[1]}, {regras[3]}"
        
    # identificador
    else:
        buffer = f"{regras[1]}"

    regras[0] = buffer

def p_ACTION(regras):
    '''
    ACTION : ligar
           | desligar
    '''
    
    # ligar | desligar
    buffer = f"{regras[1]}"
    regras[0] = buffer

def p_error(regras):
    if regras:
        print(f"Erro de sintaxe no token '{regras.type}' (valor: '{regras.value}') na linha {regras.lineno}, posição {regras.lexpos}")
    else:
        print("Erro de sintaxe: fim inesperado da entrada (EOF)")

parser = yacc(debug=False)
