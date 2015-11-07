# coding: utf-8
# Telescópio - OBI
# Anderson Sales

abertura = int(raw_input())
estrelas = int(raw_input())
lista = []
total = 0

for i in range(estrelas):
	fotons = int(raw_input())
	lista.append(fotons)
	if lista[i]*abertura >= 40000000:
		total += 1

print total
