# coding: utf-8
# Cometa / COMETA2
# Anderson Sales

ano = int(raw_input())
possiveis = range(1986, 10043, 76)

for i in possiveis:
    if i > ano:
        print i
        break
    elif i == ano:
        print i+76
        break 