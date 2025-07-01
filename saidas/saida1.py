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
    

# Dispositivo: Termometro, temperatura
# Dispositivo: ventilador, potencia
temperatura = 40
potencia = 90
if temperatura > 30:
    ligar("ventilador")