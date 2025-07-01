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
    
movimento = 0
umidade = 0
potencia = 100
if umidade < 40:
    alerta("Monitor", "Ar seco detectado")
if movimento == True:
    ligar("lampada")
else:
    desligar("lampada")