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
    

# Dispositivo: monitor
# Dispositivo: celular
# Dispositivo: Termometro, temperatura
if temperatura > 30:
    alerta("monitor", "Temperatura em ", temperatura)
alerta("celular", "Temperatura em ", temperatura)