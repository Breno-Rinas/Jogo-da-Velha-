# Breno Felipe Rinas
class Jogador:
    nome = None
    simbolo = None

def printa_tabela(matriz):
    for l in range(0,3):
        for c in range(0,3):
            if(c < 2):
                print(f'{matriz[l][c]:^5}|', end='')
            else:
                print(f'{matriz[l][c]:^5}', end='')
        if(l < 2):
            print()
            print("—————————————————")
    print()
    
def coloca_valores(var, matriz, simb):
    for l in range(0,3):
        for c in range(0,3):
            if matriz[l][c] == var:
                matriz[l][c] = simb
                break
    return matriz

def verifica_vitoria(simb, matriz):
    verifica = False
    contador = 0
    for l in range(0,3):
        for c in range(0,3):
            if matriz[l][c] == simb:
                contador += 1
        if(contador == 3):
            contador = 0
            verifica = True
            break
        else:
            contador = 0    
    
    for l in range(0,3):
        for c in range(0,3):
            if matriz[c][l] == simb:
                contador += 1
        if(contador == 3):
            contador = 0
            verifica = True
            break
        else:
            contador = 0
    if(matriz[0][0] == simb and matriz[1][1] == simb and matriz[2][2] == simb):
        verifica = True
    if(matriz[0][2] == simb and matriz[1][1] == simb and matriz[2][0] == simb):
        verifica = True 

    return verifica
 
def verifica_empate(matriz):
    verifica2 = False
    contador = 0
    for l in range(0,3):
        for c in range(0,3):
            if(matriz[l][c] == "X" or matriz[l][c] == "O"):
                contador += 1
    if(contador == 9):
        verifica2 = True
    return verifica2

jogador1 = Jogador()
jogador2 = Jogador()
jogo= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("BEM VINDO AO JOGO DA VELHA")
print("__________________________")
print()

jogador1.nome = input("Digite seu nome Jogador 1: ")
while True:
    jogador1.simbolo = input(f"Escolha seu símbolo {jogador1.nome} (X OU O): ").upper()
    if(jogador1.simbolo == "X" or jogador1.simbolo == "O"):
        break
    else:
        print("Escolha um símbolo válido(X ou O)!")

jogador2.nome = input("Digite seu nome Jogador 2: ")
if(jogador1.simbolo == "X"):
    jogador2.simbolo = "O"
    print(f"{jogador2.nome} ficará com o símbolo {jogador2.simbolo} pois o {jogador1.nome} escolheu o {jogador1.simbolo}")
else:
    jogador2.simbolo = "X"
    print(f"{jogador2.nome} ficará com o símbolo {jogador2.simbolo} pois o {jogador1.nome} escolheu o {jogador1.simbolo}")

while True:
    print()
    printa_tabela(jogo)
    print()
    jogada = int(input(f"{jogador1.nome} escolha uma das posições: "))
    jogo= coloca_valores(jogada, jogo, jogador1.simbolo)
    print()
    printa_tabela(jogo)

    verifica = verifica_vitoria(jogador1.simbolo, jogo)
    empate = verifica_empate(jogo)

    if(verifica_vitoria(jogador1.simbolo, jogo) == True):
        print()
        print(f"Parabéns {jogador1.nome}, você venceu!")
        break
    if(verifica_empate(jogo) == True):
        print()
        print("O jogo terminou empatado")
        break

    print()
    jogada = int(input(f"{jogador2.nome} escolha uma das posições: "))
    jogo= coloca_valores(jogada, jogo, jogador2.simbolo)
    verifica = verifica_vitoria(jogador2.simbolo, jogo)
    empate = verifica_empate(jogo)
    if(verifica_vitoria(jogador2.simbolo, jogo) == True):
        print()
        print(f"Parabéns {jogador2.nome}, você venceu!")
        break
    if(verifica_empate(jogo) == True):
        print()
        print("O jogo terminou empatado")
        break