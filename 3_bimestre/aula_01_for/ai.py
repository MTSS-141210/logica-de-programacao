import random

WORD_LIST = [
    "CASAS",
    "MUNDO",
    "AMOR",
    "RODAR",
    "JOGAR",
    "FLORE",
    "PLANO",
    "CACHO",
    "TERRA",
    "SONHO",
]


def jogo_termo():
    print("Bem-vindo ao jogo estilo Termo!")
    print("Tente adivinhar a palavra de 5 letras em até 6 tentativas.")
    print("A cada palpite, você verá:")
    print("  - letra correta no lugar certo: [L]")
    print("  - letra correta no lugar errado: (l)")
    print("  - letra não está na palavra:  _")
    print()

    palavra_secreta = random.choice(WORD_LIST).upper()
    tentativas = 6

    while tentativas > 0:
        palpite = input(f"Você tem {tentativas} tentativas. Digite um palpite de 5 letras: ").strip().upper()

        if len(palpite) != 5:
            print("Digite exatamente 5 letras.")
            continue

        if not palpite.isalpha():
            print("Use apenas letras.")
            continue

        if palpite == palavra_secreta:
            print("Parabéns! Você acertou a palavra! 🟩🟩🟩🟩🟩")
            break

        resultado = []
        usados = list(palavra_secreta)

        # marcar letras corretas primeiro
        for i, letra in enumerate(palpite):
            if letra == palavra_secreta[i]:
                resultado.append(f"[{letra}]")
                usados[i] = None
            else:
                resultado.append(None)

        # marcar letras presentes em posição errada
        for i, letra in enumerate(palpite):
            if resultado[i] is not None:
                continue
            if letra in usados:
                resultado[i] = f"({letra})"
                usados[usados.index(letra)] = None
            else:
                resultado[i] = "_"

        print(" ".join(resultado))
        tentativas -= 1

    else:
        print(f"Fim de jogo! A palavra era: {palavra_secreta}")


if __name__ == "__main__":
    jogo_termo()
