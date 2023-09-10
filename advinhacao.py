print("********************************")
print("Bem vindo no jogo de Advinhação!")
print("********************************")

numero_secreto = 33
chute = int(input("Digite o seu número: "))
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto


print(f"Você digitou {chute}.")

if acertou:
    print(f"Você acertou")

else:
    if maior:
        print(f"Você errou, o seu chute foi maior que o numero secreto.")

    if menor:
        print(f"Você errou, seu chute foi menor que o número secreto.")

print("Fim do jogo!!")