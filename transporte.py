# coding: utf-8
# Transporte - OBI
# Anderson Sales

car = raw_input().split()
nav = raw_input().split()

if int(nav[0]) < int(car[0]) or int(nav[1]) < int(car[1]) or int(nav[2]) < int(car[2]):
	qtd = 0
else:
	qtd = (int(nav[0])/int(car[0])) * (int(nav[1])/int(car[1])) \
    * (int(nav[2])/int(car[2]))

print qtd
