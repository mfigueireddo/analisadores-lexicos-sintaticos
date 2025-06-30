from ply.yacc import yacc
from lexer import tokens

def p_PROGRAM(regras):
    '''
    PROGRAM : DEVICES CMDS
    '''

    # DEVICES CMDS
    buffer = f"{regras[1]}\n{regras[2]}"
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

    regras[0] = buffer

def p_DEVICE(regras):
    '''
    DEVICE : dispositivo doispontos abrechaves identificador fechachaves
           | dispositivo doispontos abrechaves identificador virgula identificador fechachaves
    '''

    # dispositivo doispontos abrechaves identificador fechachaves
    if len(regras) == 6:
        buffer = f"{regras[1]}: {{{regras[4]}}}"

    # dispositivo doispontos abrechaves identificador virgula identificador fechachaves
    else:
        buffer = f"{regras[1]}: {{{regras[4]}, {regras[6]}}}"

    regras[0] = buffer

def p_CMDS(regras):
    '''
    CMDS : CMD ponto CMDS
         | CMD ponto
    '''

    # CMD ponto CMDS
    if len(regras) == 4:
        buffer = f"{regras[1]} .\n{regras[3]}"

    # CMD ponto
    else:
        buffer = f"{regras[1]} ."

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

    # set identificador igual VAR
    buffer = f"set {regras[2]} = {regras[4]}"
    regras[0] = buffer

def p_OBSACT(regras):
    '''
    OBSACT : se OBS entao ACT
           | se OBS entao ACT senao ACT
    '''

    # se OBS entao ACT
    if len(regras) == 5:
        buffer = f"se {regras[2]} entao {regras[4]}"

    # se OBS entao ACT senao ACT
    else:
        buffer = f"se {regras[2]} entao {regras[4]} senao {regras[6]}"

    regras[0] = buffer

def p_OBS(regras):
    '''
    OBS : identificador operadorlogico VAR
        | identificador operadorlogico VAR andand OBS
    '''

    # identificador operadorlogico VAR
    if len(regras) == 4:
        buffer = f"{regras[1]} {regras[2]} {regras[3]}"

    # identificador operadorlogico VAR andand OBS
    else:
        buffer = f"{regras[1]} {regras[2]} {regras[3]} && {regras[5]}"

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

    # ACTION identificador
    if len(regras) == 3:
        buffer = f"{regras[1]} {regras[2]}"

    # enviar alerta string identificador
    elif len(regras) == 5:
        buffer = f"enviar alerta {regras[3]}\n\t{regras[4]}"
    
    # enviar alerta abreparenteses string virgula identificador fechaparenteses identificador
    elif len(regras) == 9:
        buffer = f"enviar alerta ({regras[4]}, {regras[6]})\n\t{regras[8]}"
    
    # enviar alerta string para todos doispontos DEVICENAMES
    elif len(regras) == 8: 
        buffer = f"enviar alerta {regras[3]} para todos:\n\t{regras[7]}"
    
    # enviar alerta abreparenteses string virgula identificador fechaparenteses para todos doispontos DEVICENAMES
    else:
        buffer = f"enviar alerta ({regras[4]}, {regras[6]}) para todos:\n\t{regras[11]}"

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