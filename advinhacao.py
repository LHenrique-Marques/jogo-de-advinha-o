import random
print("""
**********************************************************
-------------Bem-Vindo Ao jogo de Advinhação--------------
**********************************************************
""")
numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("""
Qual o nível de Dificuldade ? 
      Nivel 1 : Facil
      Nivel 2 : Médio
      Nivel 3 : Dificil
""")

nivel = int(input("Escolha:  "))
if (nivel == 1 ):
    total_de_tentativas = 20

elif (nivel == 2):
    total_de_tentativas = 10

elif (nivel == 3):
    total_de_tentativas = 5

        


for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}.")
    chute = int(input("Digite um número entre 1 e 100 : "))
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100....")
        continue
    

    if (acertou):
        print(f"Você acertou")
        break
    else:
        if (maior):
            print(f"Você errou, o seu chute foi maior que o numero secreto.")

        if (menor):
            print(f"Você errou, seu chute foi menor que o número secreto.")

print(f"Fim do jogo!!, o número era {numero_secreto}")