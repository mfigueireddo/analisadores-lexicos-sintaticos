dispositivo: {Termometro,temperatura}
dispositivo: {ventilador,potencia}
dispositivo: {ventilador,potencia}
dispositivo: {Termometro,temperatura} dispositivo: {ventilador,potencia}
set temperatura=40
set potencia=90
temperatura > 30
ligar ventilador
SE temperatura > 30 ENTAO ligar ventilador
SE temperatura > 30 ENTAO ligar ventilador.
set potencia=90.SE temperatura > 30 ENTAO ligar ventilador.
set temperatura=40.set potencia=90.SE temperatura > 30 ENTAO ligar ventilador.
dispositivo: {Termometro,temperatura} dispositivo: {ventilador,potencia} set temperatura=40.set potencia=90.SE temperatura > 30 ENTAO ligar ventilador.
