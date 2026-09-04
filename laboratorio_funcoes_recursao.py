def calcular_frete(valor_compra, peso_kg):
    frete = peso_kg * 5

    if valor_compra >= 200:
        frete = frete * 0.5

    return frete

TAXA_PROCESSAMENTO = 2.00

def aplicar_cupom(valor_item, cupom_desconto):
    desconto = valor_item * (cupom_desconto / 100)
    valor_com_desconto = valor_item - desconto
    preco_final = valor_com_desconto + TAXA_PROCESSAMENTO

    return preco_final

def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return

    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela}")
    exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela)

print("=== CALCULADORA DE FRETE ===")

valor_compra = float(input("Digite o valor da compra: R$ "))
peso_kg = float(input("Digite o peso da encomenda em kg: "))

frete = calcular_frete(valor_compra, peso_kg)

print(f"Frete final: R$ {frete:.2f}")

print("\n=== CUPOM DE DESCONTO ===")

valor_item = float(input("Digite o valor do item: R$ "))
cupom_desconto = float(input("Digite o desconto do cupom (%): "))

preco_final = aplicar_cupom(valor_item, cupom_desconto)

print(f"Preço final: R$ {preco_final:.2f}")

print("\n=== PARCELAMENTO ===")

parcelas = int(input("em quantas vezes: "))
valor_parcela = float(input("Digite o valor de cada parcela: R$ "))

exibir_cronograma_regressivo(parcelas, valor_parcela)