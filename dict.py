produto = {
    "codigo": 101,
    "nome": "teclado mecanico gamer",
    "preco": 250.0,
    "estoque": 14
}

print("== produto cadastrado ==")
print(produto)
print(f"nome do produto: {produto['nome']}")
print(f"preço do produto: {produto['preco']}")
print('-'* 48)

produto['preco'] = 220.0
produto['estoque'] = produto['estoque'] + 6
produto["categoria"] = "perifericos"

print("== produto atualizado ==")
print(produto)
print(f"novo estoque total: {produto['estoque']} unidade")
print("-"* 48)

usuario = {
    "nome": "Carlos Eduardo",
    "nivel": "Administrador",
    "ativo": True
}
print("== inspeção de registro ==")
print("chaves de registro", usuario.keys())
print("valores de registro", usuario.values())