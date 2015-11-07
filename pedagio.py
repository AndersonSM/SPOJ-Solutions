# coding: utf-8
# Pedágio - OBI
# Anderson Sales

dist = raw_input().split()
pedagios = int(dist[0]) / int(dist[1])
preco = raw_input().split()
total = (int(preco[0])*int(dist[0])) + (int(preco[1])* pedagios)

print total
