def formatar_citacao(nome_completo):
	partes = nome_completo.split()
	sobrenome = partes[-1].upper()
	nomes = " ".join(partes[:-1])
	return f"{sobrenome}, {nomes}"

autor = "Matheus Moreira Suzigan"
citacao_formatada = formatar_citacao(autor)
print("Citacao Biografica:", citacao_formatada)

def gerar_codigo(ano, cpf):
	cpf_limpo = cpf.replace(" ", "").replace(".", "").replace("-", "")
	primeiros_digitos = cpf_limpo[:3]
	return f"ALU-{ano}-{primeiros_digitos}"

ano = 2026
cpf = "989.562.009-39"
codigo_gerado = gerar_codigo(ano, cpf)
print("Codigo Gerado:", codigo_gerado)
