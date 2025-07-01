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
    

temperatura = 40
potencia = 90
if temperatura > 30:
    ligar("ventilador")