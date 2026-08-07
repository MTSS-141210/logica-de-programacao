def contagem_regressiva(numero):
    """Imprime uma contagem regressiva a partir do número informado."""
    for i in range(numero, -1, -1):
        print(i)


if __name__ == "__main__":
    entrada = input("Digite um número inteiro para iniciar a contagem regressiva: ")
    try:
        numero = int(entrada)
        if numero < 0:
            print("Por favor, digite um número inteiro maior ou igual a zero.")
        else:
            contagem_regressiva(numero)
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")
