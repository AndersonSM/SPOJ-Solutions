entrada = raw_input().split()
alunos = int(entrada[0])
linhas = int(entrada[1])
grupos = 0
amigos = ""
for l in range(linhas):
    par = raw_input().split()
    i = par[0]
    j = par[1]
    if i and j not in amigos:
        grupos += 1
    if i not in amigos:
        amigos += i
    if j not in amigos:
        amigos += j
print grupos + (alunos - len(amigos))