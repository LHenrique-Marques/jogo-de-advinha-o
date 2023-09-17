print("********************************")
print("Bem vindo no jogo de Advinhação!")
print("********************************")

numero_secreto = 33

for rodada in [1,2,3]:
    print(f"Tentativa {rodada} de {total_de_tentativas}.")
    chute = int(input("Digite o seu número: "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    print(f"Você digitou {chute}.")

    if acertou:
        print(f"Você acertou")
        break
    else:
        if maior:
            print(f"Você errou, o seu chute foi maior que o numero secreto.")

        if menor:
            print(f"Você errou, seu chute foi menor que o número secreto.")

    print("Fim do jogo!!")