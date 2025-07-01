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
    

# Dispositivo: lampada, potencia
potencia = 100
ligar("lampada")