brutos = [
    "  MARIA DA SILVA  ",
    "joão.souza@EMAIL.com ",
    "  RUA DAS FLORES, No 123  ",
    "  000.111.222-33  ",
    "CARLOS.ROCHA@ESCOLA.ORG  ",
    " AV. CENTRAL, No 450  "
]
#Lista para armazenar o resultado limpo
dados_limpos = []
#--- LÓGICA DE PROCESSAMENTO  EM LOTE ---
for item in brutos:
    #1. Remove espaços extras no início9 e no final
    texto = item.strip()
    # 2. Se for e-mail (contém'@'), converte para minúsculas 
    if "@" in texto:
        texto = texto.lower()
    else:
        # 3. Corrige a abreviação "No" para "Número"
        texto = texto.replace("No", "Número")

        # 4. Remove pontuações de CPF (pontos e hífen)
        texto = texto.replace(".", "").replace(".", "")
        # 5. Adiciona o texto tratado na nova lista
    dados_limpos.append(texto)
#--- EXIBIÇAO DOS RESULTADOS ---
print("========================================")
print("   Base de dados tratada e sanitada     ")
print("========================================")
for dado in dados_limpos:
    print("-", dado)
