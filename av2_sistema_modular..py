 # ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: 
# Data: 
# Link do Repositório: 
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  matheus moreira suzigan;desenvolvedor;17-8637 8615  ",
   "  rebeca tavano suzigan;analista de rh;50-7863 2092  ",
   "  erik rodrigues de oliveira;gerente de projetos;51-8202 5239 "
]

# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Recebe uma string.
   - Remove espaços extras das pontas usando .strip().
   - Converte o texto para letras maiúsculas usando .upper().
   - Retorna o texto formatado.
   """
   texto_formatado = texto.strip().upper()
   
   return texto_formatado


def extrair_codigo_ou_ddd(dado):
   """
   FUNÇÃO 2:
   - Recebe um dado em formato de string (telefone ou CPF).
   - Remove espaços das pontas usando .strip().
   - Utiliza fatiamento de string [x:y] para extrair os 2 primeiros dígitos.
   - Retorna apenas os dígitos extraídos.
   """
   dado_limpo = dado.strip()
   
   # Fatiamento para pegar os dois primeiros dígitos
   codigo = dado_limpo[0:2]
   
   return codigo

def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Recebe a lista de cadastros brutos como parâmetro.
   - Utiliza um laço FOR para percorrer cada item da lista.
   - Separa as partes usando .split(";").
   - Chama a Função 1 para formatar o Nome e o Cargo.
   - Chama a Função 2 para extrair o DDD/Código do telefone.
   - Exibe o resultado usando f-string.
   - Retorna a quantidade total de registros processados.
   """
   
   total_processado = 0

   # Percorre todos os cadastros da lista
   for dado in lista_dados:
      
      # Separa nome, cargo e telefone usando o ponto e vírgula
      partes = dado.split(";")
      
      nome = partes[0]
      cargo = partes[1]
      telefone = partes[2]
      
      # Formata o nome e o cargo utilizando a Função 1
      nome_formatado = limpar_e_formatar_texto(nome)
      cargo_formatado = limpar_e_formatar_texto(cargo)
      
      # Extrai o DDD utilizando a Função 2
      ddd = extrair_codigo_ou_ddd(telefone)
      
      # Exibe os dados utilizando f-string
      print(f"Nome: {nome_formatado}")
      print(f"Cargo: {cargo_formatado}")
      print(f"DDD: {ddd}")
      print("-" * 50)
      
      # Conta o registro processado
      total_processado += 1
   
   # Retorna a quantidade total de registros
   return total_processado

# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   # Chamada da Função 3 passando a lista 'dados_brutos'
   total_processado = processar_e_exibir_cadastros(dados_brutos)
   
   # Exibe a quantidade total de registros processados
   print(f"\nTotal de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")

# Execução do programa
if __name__ == "__main__":
   main()