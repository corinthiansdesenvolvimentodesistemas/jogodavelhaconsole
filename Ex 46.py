
def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tabuleiro(tabuleiro):
    print("\n 0 1 2")
    for i, linha in enumerate(tabuleiro):
        print(i, " | ".join(linha))
        if i < 2:
            print(" ---+---+---")
    print()


def realizar_jogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print(" Posição já ocupada! Escolha outra.")
        return False


def verificar_vitoria(tabuleiro, jogador):

    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    
    for c in range(3):
        if all(tabuleiro[l][c] == jogador for l in range(3)):
            return True
    
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


def verificar_empate(tabuleiro):
    return all(c != " " for linha in tabuleiro for c in linha)


def alternar_jogador(jogador):
    return "O" if jogador == "X" else "X"


def main():
    print("=== JOGO DA VELHA ===\n")

    nome1 = input("Digite o nome do Jogador 1 (X): ")
    nome2 = input("Digite o nome do Jogador 2 (O): ")

    placar = {nome1: 0, nome2: 0}

    while True:
        tabuleiro = criar_tabuleiro()
        jogador_atual = "X"
        nomes = {"X": nome1, "O": nome2}

        print("\nNova partida iniciada!\n")
        mostrar_tabuleiro(tabuleiro)

        while True:
            print(f" Vez de {nomes[jogador_atual]} ({jogador_atual})")
            try:
                linha = int(input("Escolha a linha (0-2): "))
                coluna = int(input("Escolha a coluna (0-2): "))
            except ValueError:
                print(" Entrada inválida! Digite números de 0 a 2.")
                continue

            if linha not in range(3) or coluna not in range(3):
                print("Posição inválida! Use números de 0 a 2.")
                continue

            if not realizar_jogada(tabuleiro, linha, coluna, jogador_atual):
                continue

            mostrar_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f" Vitória de {nomes[jogador_atual]}!\n")
                placar[nomes[jogador_atual]] += 1
                break

            if verificar_empate(tabuleiro):
                print("O jogo terminou em empate!\n")
                break

            jogador_atual = alternar_jogador(jogador_atual)

        print("Placar Atual:")
        for jogador, pontos in placar.items():
            print(f"{jogador}: {pontos} pontos")

        continuar = input("\nDesejam jogar outra partida? (s/n): ").lower()
        if continuar != "s":
            print("\n Jogo encerrado!")
            print(" Placar Final:")
            for jogador, pontos in placar.items():
                print(f"{jogador}: {pontos} pontos")
            break


if __name__ == "__main__":
    main()