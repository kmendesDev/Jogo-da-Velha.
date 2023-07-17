import os
import random
from colorama import Fore, Back, Style  # pip install colorama

jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1-cpu 2-jog
maxJogadas = 9
vit = "n"
velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")  # Depois adc o FOR
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.LIGHTCYAN_EX + str(jogadas) + Fore.RESET)


def JogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            print("Sua vez de jogar. Digite abaixo: ")
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                print("Sua vez de jogar. Digite abaixo: ")
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            quemJoga = 1
            jogadas += 1
        except:
            print("Jogada inválida")
            print("Sua vez de jogar. Digite abaixo: ")
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            os.system("pause")


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    print("O cpu está jogando...")
    os.system("pause")
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        quemJoga = 2
        jogadas += 1


def VerVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]

    for s in simbolos:
        vitoria = "n"
        # Verificando as linhas:
        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if velha[il][ic] == s:
                    soma += 1
                ic += 1
            if soma == 3:
                vitoria = s
                break
            il += 1
        if vitoria != "n":
            break
        # Verificar as colunas:
        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if velha[il][ic] == s:
                    soma += 1
                il += 1
            if soma == 3:
                vitoria = s
                break
            ic += 1
        if vitoria != "n":
            break
        # Verificar as diagonais:
        # Diagonal 1:
        idiag = 0
        soma = 0
        while idiag < 3:
            if velha[idiag][idiag] == s:
                soma += 1
            idiag += 1

            if soma == 3:
                vitoria = s
                break

        if vitoria != "n":
            break
        # Diagonal 2:
        idiagl = 0
        idiagc = 2

        while idiagl < 3:
            soma = 0
            while idiagc >= 0:
                if velha[idiagl][idiagc] == s:
                    soma += 1
                idiagl += 1
                idiagc -= 1

            if soma == 3:
                vitoria = s
                break
        if vitoria != "n":
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 2  # 1-cpu 2-jog
    maxJogadas = 9
    vit = "n"
    velha = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


while jogarNovamente == "s":
    redefinir()
    while True:
        tela()
        JogadorJoga()
        tela()
        vit = VerVitoria()
        if (vit != "n") or (jogadas >= maxJogadas):
            if vit == "X":
                print(Fore.LIGHTGREEN_EX + "Parabéns, você ganhou !")
            elif vit == "O":
                print(Fore.RED + "Que pena, você perdeu")
            else:
                print(Fore.YELLOW + "Empate !")
            break

        cpuJoga()
        tela()
        vit = VerVitoria()
        if (vit != "n") or (jogadas >= maxJogadas):
            if vit == "X":
                print(Fore.LIGHTGREEN_EX + "Parabéns, você ganhou !")
            elif vit == "O":
                print(Fore.RED + "Que pena, você perdeu")
            else:
                print(Fore.YELLOW + "Empate !")
            break
    print(Fore.MAGENTA + "FIM DE JOGO" + Fore.RESET)
    jogarNovamente = input(Fore.BLUE + "Deseja jogar novamente ? [s/n] : " + Fore.RESET)
    jogarNovamente = jogarNovamente.lower()
    if jogarNovamente == "n":
        os.system("cls")
        print(Fore.GREEN + "Até o próximo jogo !" + Fore.RESET)
