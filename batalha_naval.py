import random
import os

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
    print(f"\nTabuleiro do Computador")
    print_matriz(m_C)
    print(f"Gabarito Computador: {gabarito_C}")
    print(f"Embarcações Restantes: {embarcacoes_C}")

def verificar_vitoria(embarcacoes_J, embarcacoes_C):
    if embarcacoes_J == 0:
        os.system('cls')
        print_tabuleiro()
        print(f"\nVitória do Computador!")
        print("Obrigado por jogar.")
        print("Autores: Adriel Asafe e Leticia Oliveira\n")
        return True
    if embarcacoes_C == 0:
        os.system('cls')
        print_tabuleiro()
        print(f"\nParabéns, vitória do Jogador!")
        print("Obrigado por jogar.")
        print("Autores: Adriel Asafe e Leticia Oliveira\n")
        return True
    
    return False

# MATRIZES

m_J = criar_matriz(5,10)
m_C = criar_matriz(5,10)
m_JG = criar_matriz(5,10)
m_CG = criar_matriz(5,10)

while True:

    # LOOP POSICIONAMENTO JOGADOR

    while jogadas_J != 5:
        
        print(f"Seu tabuleiro")
        print_matriz(m_JG)

        try:
            x = int(input("\nDigite o X (0 a 4): "))
        except ValueError:
            os.system('cls')
            print(f'X inválido. Digite de 0 a 4\n')
            continue

        if x in (range(0, 5)):

            while True:

                try:
                    y = int(input("Digite o Y (0 a 9): "))
                except ValueError:
                    os.system('cls')
                    print(f'Y inválido. Digite de 0 a 9\n')
                    print("Seu tabuleiro")
                    print_matriz(m_JG)
                    print(f'\nDigite o X (0 a 4): {x}')
                    continue

                if y in (range(0,10)):           
                    if m_JG[x][y] != "X":
                        m_JG[x][y] = "X"
                        jogadas_J += 1
                        gabarito_J.append(str(x) + str(y))
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
                        print(f'Posição já escolhida.\n')
                        break
                else:
                    os.system('cls')
                    print(f'Y inválido. Digite de 0 a 9\n')
                    print("Seu tabuleiro")
                    print_matriz(m_JG)
                    print(f'\nDigite o X (0 a 4): {x}')
        else:
            os.system('cls')
            print(f'X inválido. Digite de 0 a 4\n')
        
        if jogadas_J == 5:
            os.system('cls')
            print("Seu tabuleiro")
            print_matriz(m_JG)
            print("Posições incluídas.")
            continuar = input(f"\nAperte enter para continuar.")
            os.system('cls')
    
    # LOOP POSICIONAMENTO COMPUTADOR

    while jogadas_C != 5:

        x = random.randint(0, 4)
        y = random.randint(0, 9)
        if m_CG[x][y] != "X":    
            m_CG[x][y] = "X"
            jogadas_C += 1
            gabarito_C.append(str(x) + str(y))

    # LOOP JOGADA

    while True:

        # ESCOLHA JOGADOR

        print("Sua vez de jogar\n")

        while True:
            
            print_tabuleiro()

            try:
                x = int(input("\nDigite o X (0 a 4): "))
            except ValueError:
                os.system('cls')
                print(f'X inválido. Digite de 0 a 4\n')
                continue
            
            if x in (range(0, 5)):

                while True:
                
                    try:
                        y = int(input("Digite o Y (0 a 9): "))
                    except ValueError:
                        os.system('cls')
                        print(f'Y inválido. Digite de 0 a 9\n')
                        print_tabuleiro()
                        print(f'\nDigite o X (0 a 4): {x}')
                        continue

                    if y in (range(0,10)):
                        if m_CG[x][y] == "X":
                            os.system('cls')
                            embarcacoes_C -= 1
                            print(f"Jogador acertou!\n")
                            print_tabuleiro()
                            continuar = input(f"\nAperte enter para continuar.")
                            os.system('cls')
                            break
                        else:
                            os.system('cls')
                            print(f"Jogador errou.\n")
                            print_tabuleiro()
                            continuar = input(f"\nAperte enter para continuar.")
                            break
                    else:
                        os.system('cls')
                        print(f'Y inválido. Digite de 0 a 9\n')
                        print_tabuleiro()
                        print(f'\nDigite o X (0 a 4): {x}')
            else:
                os.system('cls')
                print(f'X inválido. Digite de 0 a 4\n')
                continue

            break

        # VERIFICAR VITÓRIA JOGADOR

        if verificar_vitoria(embarcacoes_J,embarcacoes_C):
            break        

        # ESCOLHA COMPUTADOR

        os.system('cls')
        print("Agora é a vez do computador\n")
        print_tabuleiro()

        x = random.randint(0, 4)
        y = random.randint(0, 9)

        print(f"\nComputador escolheu X: {x}")
        print(f"Computador escolheu Y: {y}")
        continuar = input(f"\nAperte enter para continuar.")

        if m_JG[x][y] == "X":
            os.system('cls')
            embarcacoes_J -= 1
            print(f"Computador acertou!\n")
            print_tabuleiro()
            continuar = input(f"\nAperte enter para continuar.")
            os.system('cls')
      
        else:
            os.system('cls')
            print(f"Computador errou.\n")
            print_tabuleiro()
            continuar = input(f"\nAperte enter para continuar.")
            os.system('cls')
        
        # VERIFICAR VITÓRIA COMPUTADOR

        if verificar_vitoria(embarcacoes_J,embarcacoes_C):
            break 

    break
