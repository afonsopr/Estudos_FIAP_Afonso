import random


dados_com_indice = [[0, 'senha'], [1, 'ajuda de senha'], [2, 'telefone'], [3, 'nome'], [4,'email'],]

def gerar_dados_classificados():
    inteiro = random.randint(1, len(dados_com_indice))
    dados_aleatorios = random.sample(dados_com_indice, k=inteiro)
    dados_aleatorios.sort()

    dados = []
    for i in dados_aleatorios:
        for j in i:
            if type(j) is str:
                dados.append(j)

    return dados

def definir_tipo_de_dados():
    tipos_de_dados = []
    for k in dados_com_indice:
        for l in k:
            if type(l) is str:
                tipos_de_dados.append(l)
    
    return tipos_de_dados

def gerar_data():
    dia = random.randint(1, 31)
    mes = random.randint(1, 12)
    ano = random.randint(1990, 2022)

    return dia, mes, ano
