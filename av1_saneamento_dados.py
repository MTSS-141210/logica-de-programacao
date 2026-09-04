cadastros_brutos = [
   "  joao da silva;11988887777  ",
   "  maria sousa;21977776666  ",
   "  carlos edgardo oliveira;31966665555  ",
   "  ana paula lima;41955554444  "
]

print("==================================================")
print("     SISTEMA DE SANEAMENTO DE DADOS - AV1         ")
print("==================================================\n")

for i in range(len(cadastros_brutos)):
   cadastro_limpo = cadastros_brutos[i].strip()
   nome, telefone = cadastro_limpo.split(";")
   nome = nome.upper()
   ddd = telefone[0:2]
   print(f"Funcionario:{nome} | DDD:{ddd} | Telefone:{telefone}")

print("\n==================================================")
print("             PROCESSAMENTO CONCLUÍDO              ")
print("==================================================")