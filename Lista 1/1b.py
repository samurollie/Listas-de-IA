# Posição 0: Número de missionários na margem esquerda
# Posição 1: Número de canibais na margem esquerda
# Posição 2: Número de missionarios na margem direita
# Posição 3: Número de canibais na margem esquerda
# Posição 4: Posição da canoa (0 = margem esquerda, 1 = margem direita)

estadoInicial = [3,3,0,0,0]
estadoFinal = [0,0,3,3,1]
operadores = [(1,0), (2,0), (1,1), (0,2), (0,1)]

fronteira = []
historico = []

def deslocarCanoa(estado, m = 0, c = 0):
    if m + c > 2:
        return

    if estado[4] == 0:
        mOrigem = 0
        cOrigem = 1
        mDestino = 2
        cDestino = 3
    else:
        mOrigem = 2
        cOrigem = 3
        mDestino = 0
        cDestino = 1
    
    if estado[mOrigem] == 0 and estado[cOrigem] == 0:
        return
    
    estado[4] = 1 - estado[4]

    for i in range(min(m, estado[mOrigem])):
        estado[mOrigem] -= 1
        estado[mDestino] += 1

    for i in range(min(c, estado[cOrigem])):
        estado[cOrigem] -= 1
        estado[cDestino] += 1

    return estado

def sucessores(estado):
    sucessores = []
    for (i,j) in operadores:
        s = deslocarCanoa(estado[:],i,j)
        if s == None:
            continue
        if (s[0] < s[1] and s[0] > 0) or (s[2] < s[3] and s[2] > 0):
            continue
        if s in historico:
            continue

        sucessores.append(s)
    return sucessores

def getNext(estado):
    l = sucessores(estado)
    if len(l) > 0:
        return l[0]
    else:
        return -1

def dfs(estadoInicial):
    fronteira.append(estadoInicial)
    while (len(fronteira) != 0):
        estado = fronteira[len(fronteira) - 1]
        if estado == estadoFinal:
            print("Caminho encontrado. A busca obteve sucesso")
            break
        
        v = getNext(estado)
        if v == -1:
            fronteira.pop()
        else:
            historico.append(v)
            fronteira.append(v)

    else:
        print("Caminho não encontrado. Busca sem sucesso")
    return fronteira

sol = dfs(estadoInicial)

for i in range(1, len(sol)):
    md = abs(sol[i][0] - sol[i - 1][0])
    cd = abs(sol[i][1] - sol[i - 1][1])
    canoa = sol[i][4] - sol[i - 1][4]
    if canoa == 1:
        s = "->"
    else:
        s = "<-"
    
    print(sol[i - 1], "Movimento: ({} missionario, {} canibal, direção: {})".format(md, cd, s))