print("********************************")
print("Bem vindo no jogo de Advinhação!")
print("********************************")

numero_secreto = 33
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}.")
    chute = int(input("Digite o seu número: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print(f"Você acertou")
        break
    else:
        if maior:
            print(f"Você errou, o seu chute foi maior que o numero secreto.")

        if menor:
            print(f"Você errou, seu chute foi menor que o número secreto.")

print("Fim do jogo!!")