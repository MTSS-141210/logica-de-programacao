import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando entre 1 e 100.")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = input("Digite seu palpite: ")
        tentativas += 1

        try:
            palpite = int(tentativa)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        if palpite < 1 or palpite > 100:
            print("Escolha um número entre 1 e 100.")
            continue

        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break


if __name__ == "__main__":
    jogo_adivinhacao()
