# Lista de cadastros brutos recebidos do sistema
cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

# TODO: Escreva o laco de repeticao usando for e range() para percorrer a lista
for i in range(len(cadastros_brutos)):
   
   # 1. Remova os espacos extras do inicio e fim do cadastro atual
   cadastro_limpo = cadastros_brutos[i].strip()
   
   # 2. Separe o nome e o telefone (Dica: use o metodo .split(";"))
   nome, telefone = cadastro_limpo.split(";")
   
   # 3. Converta o nome para letras MAIUSCULAS
   nome = nome.upper()
   
   # 4. Extraia o DDD (2 primeiros digitos do telefone) usando fatiamento [0:2]
   ddd = telefone[0:2]
   
   # 5. Exiba o resultado padronizado no terminal
   # Exemplo de print formatado desejado:
   # Funcionario: NOME MAIUSCULO | DDD: 11 | Telefone: 11988887777
   print(f"Funcionario: {nome} | DDD: {ddd} | Telefone: {telefone}")

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")