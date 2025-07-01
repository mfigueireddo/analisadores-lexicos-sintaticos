def ligar(namedevice):
    print(namedevice + " ligado!")

def desligar(namedevice):
    print(namedevice + " desligado!")

def alerta(namedevice, msg):
    print(namedevice + " recebeu o alerta:\n")
    print(msg)

def alerta(namedevice, msg, var):
    print(namedevice + " recebeu o alerta:\n")
    print(msg + " " + str(var))
    

# Dispositivo: celular, movimento
# Dispositivo: higromero, umidade
# Dispositivo: lampada, potencia
# Dispositivo: Monitor
potencia = 100
if umidade < 40:
    alerta("Monitor", "Ar seco detectado")
if movimento == True:
    ligar("lampada")
else:
    desligar("lampada")