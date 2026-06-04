import random

# VARIAVEIS

embarcacoes_C = 5
embarcacoes_J = 5
jogadas_J = 0
jogadas_C = 0
gabarito_J = []
gabarito_C = []

# FUNÇÕES

def criar_matriz(linhas, colunas):
    matriz = []

    for i in range(linhas):
        matriz.append([0] * colunas)

    return matriz

def print_matriz(matriz):
    for linha in matriz:
        print(linha)

def print_tabuleiro():
    print("Tabuleiro do Jogador")
    print_matriz(m_J)
    print(f"Gabarito Jogador: {gabarito_J}")
    print(f"Embarcações Restantes: {embarcacoes_J}")
    print("Tabuleiro do Computador")
    print_matriz(m_C)
    print(f"Gabarito Computador: {gabarito_C}")
    print(f"Embarcações Restantes: {embarcacoes_C}")

# MATRIZES

m_J = criar_matriz(5,10)
m_C = criar_matriz(5,10)
m_JG = criar_matriz(5,10)
m_CG = criar_matriz(5,10)

while True:

    # LOOP POSICIONAMENTO JOGADOR

    
    while jogadas_J != 5:
        
        print("Seu tabuleiro:")
        print_matriz(m_JG)

        try:
            x = int(input("Digite o X (0 a 4): "))
        except ValueError:
            print('X inválido. Digite de 0 a 4')
            continue

        if x in (range(0, 5)):

            try:
                y = int(input("Digite o Y (0 a 9): "))
            except ValueError:
                print('Y inválido. Digite de 0 a 4')
                continue

            if y in (range(0,10)):           
                if m_JG[x][y] != "X":
                    m_JG[x][y] = "X"
                    jogadas_J += 1
                    gabarito_J.append(str(x) + str(y))
                else:
                    print('Posição já escolhida.')
            else:
                print('Y inválido. Digite de 0 a 9.')
        else:
            print('X inválido. Digite de 0 a 4')
        
        if jogadas_J == 5:
            print("Seu tabuleiro:")
            print_matriz(m_JG)
            print("Posições incluídas.")
            continuar = input("Aperte enter para continuar.")

    
    # LOOP POSICIONAMENTO COMPUTADOR

    while jogadas_C != 5:

        x = random.randint(0,4)
        y = random.randint(0,9)
        if m_CG[x][y] != "X":    
            m_CG[x][y] = "X"
            jogadas_C += 1
            gabarito_C.append(str(x) + str(y))

    # LOOP JOGADA

    while True:

        print_tabuleiro()

        # ESCOLHA JOGADOR

        while True:

            try:
                x = int(input("Digite o X (0 a 4): "))
            except ValueError:
                print('X inválido. Digite de 0 a 4')
                continue
            
            if x in (range(0, 5)):

                try:
                    y = int(input("Digite o Y (0 a 9): "))
                except ValueError:
                    print('Y inválido. Digite de 0 a 4')
                    continue

                if y in (range(0,10)):
                    if m_CG[x][y] == "X":
                        embarcacoes_C -= 1
                        print("Jogador acertou!")
                        break
                    else:
                        print("Jogador errou.")
                else:
                    print('Y inválido. Digite de 0 a 9.')
            else:
                print('X inválido. Digite de 0 a 4')
            
        

        # ESCOLHA COMPUTADOR

        x = random.randint(range(0, 5))
        y = random.randint(range(0,10))
        if m_JG[x][y] == "X":
            embarcacoes_J -= 1
            print("Computador acertou")
        else:
            print("Computador errou")
        
        # CONDIÇÃO DE VITÓRIA DO JOGADOR

        if embarcacoes_J == 0:
            print("Parabéns, vitória do Jogador!")
            print("Obrigado por jogar.")
            print("Autores: Adriel Asafe e Leticia Oliveira")
            break

        # CONDIÇÃO DE VITÓRIA DO COMPUTADOR

        if embarcacoes_C == 0:
            print("Vitória do Computador!")
            print("Obrigado por jogar.")
            print("Autores: Adriel Asafe e Leticia Oliveira")
            break

    break
