def ligar(namedevice):
    print(namedevice + " ligado!")

def desligar(namedevice):
    print(namedevice + " desligado!")

def alerta(namedevice, msg, var=None):
    print(namedevice + " recebeu o alerta:")
    if var is not None:
        print(msg + " " + str(var))
    else:
        print(msg)
    

potencia = 100
ligar("lampada")