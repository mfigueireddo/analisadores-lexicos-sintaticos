dispositivo: {celular, movimento}
dispositivo: {higromero, umidade}
dispositivo: {lampada, potencia}
dispositivo: {Monitor}
set potencia = 100 .
se umidade < 40 entao enviar alerta Ar seco detectado
	Monitor .
se movimento == True entao ligar lampada senao desligar lampada .