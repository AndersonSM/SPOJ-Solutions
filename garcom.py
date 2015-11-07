# coding: utf-8
# Garçom - OBI
# Anderson Sales

bandejas = int(raw_input())
derrubados = []

for i in range(bandejas):
	objeto = raw_input().split()
	if int(objeto[0]) > int(objeto[1]):
		derrubados.append(int(objeto[1]))
		
print sum(derrubados)
