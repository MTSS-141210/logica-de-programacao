valores = [12, 45, 7, 89, 23]

indice_menor = 0
indice_maior = 0

for v in range (len(valores)):
    if valores[v] < valores[indice_menor]:
        indice_menor = v
    if valores[v] > valores[indice_maior]:
        indice_maior = v
print("=== RELAÓRIO POSICIONAL DETALHADO")
for v in range(len(valores)):
    status = ""
    if v == indice_menor:
        status = " <- [MENOR VALOR]"
    elif v == indice_maior:
        status = " <- [MAIOR VALOR]"
    print(f"indice [{v}]: valor = {valores[v]}{status}")

print("-" * 38)
print(f"menor_valor: {valores[indice_menor]} (no indice {indice_menor})")
print(f"maior_valor: {valores[indice_maior]} (no indice {indice_maior})")