matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("=== Exibição de matriz em formato de grade ===")
print("-" * 48)
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:2d}", end=" ")
    print()
print("-" * 48)

print(f"Elemento na linha [0] e coluna [1]: {matriz[0][1]}")
print(f"Elemento na linha [2] e coluna [2]: {matriz[2][2]}")

print("-" * 48)
soma_diagonal = 0
for l in range(3):
    for c in range(3):
        if l == c:
            soma_diagonal += matriz[l][c]
print(f"Elemento na diagonal: {soma_diagonal}")
print("-" * 48)
