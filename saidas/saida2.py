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
    
temperatura = 0
if temperatura > 30:
    alerta("monitor", "Temperatura em ", temperatura)
    alerta("celular", "Temperatura em ", temperatura)