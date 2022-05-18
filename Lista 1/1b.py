# Posição 0: Número de missionários na margem esquerda
# Posição 1: Número de canibais na margem esquerda
# Posição 2: Número de missionarios na margem direita
# Posição 3: Número de canibais na margem esquerda
# Posição 4: Posição da canoa (0 = margem esquerda, 1 = margem direita)

estadoInicial = [3,3,0,0,0]
margemEsquerda = [3,3]
margemDireita = [0,0]
canoa = {
    'd': 0,
    'e': 1
}
operadores = [(1,0), (2,0), (1,1), (0,2), (0,1)]

borda = []
visitados = []

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
        if s in visitados:
            continue

        sucessores.append(s)
    return sucessores

def obtemAdjacenteNaoVisitado(elementoAnalisar):
    l = sucessores(elementoAnalisar)
    if len(l) > 0:
        return l[0]
    else:
        return -1

def testeMeta(estado):
    if estado[2] >= 3 and estado[3] >= 3:
        return True
    else:
        return False

def dfs(estadoInicial):
    borda.append(estadoInicial)
    while (len(borda) != 0):
        elementoAnalisar = borda[len(borda) - 1]
        if testeMeta(elementoAnalisar):
            break
        
        v = obtemAdjacenteNaoVisitado(elementoAnalisar)
        if v == -1:
            borda.pop()
        else:
            visitados.append(v)
            borda.append(v)

    else:
        print("Caminho não encontrado. Busca sem sucesso")
    return borda

sol = dfs(estadoInicial)

for i in range(1, len(sol)):
    md = abs(sol[i][0] - sol[i - 1][0])
    cd = abs(sol[i][1] - sol[i - 1][1])
    canoa = sol[i][4] - sol[i - 1][4]
    if canoa == 1:
        s = "->"
    else:
        s = "<-"
    
    print(sol[i - 1], "({},{},{})".format(md, cd, s))