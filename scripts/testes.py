
'''
Tarefa: converter o código anterior para usar list comprehension, 
tornando-o mais limpo e eficiente.
'''

import csv


key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}
#path_csv = '../data_raw/dados_empresaB.csv'
path_csv = '/home/egaliza/WORKSPACE-PYTHON/pipeline_dados/data_raw/dados_empresaB.csv'
#encoding='unicode-escape' --> UNIX
#encoding='utf-8' --> WINDOWS

#Transformando o arquivo CSV em uma lista de dicionários
dados_csv = []
with open(path_csv, 'r') as file:
    spamreader = csv.DictReader(file, delimiter=',')
    for row in spamreader:
        dados_csv.append(row)

print(dados_csv[0])


#CODIG ANTIGO - SEM LIST COMPREHENSION
#new_dados_csv = []

# for old_dict in dados_csv:
#   dict_temp = {}
#   for old_key, value in old_dict.items():
#     dict_temp[key_mapping.get(old_key)] = value
#   new_dados_csv.append(dict_temp)

# print(new_dados_csv[0])


#CODIGO INTERMEDIARIO - PASSO 1 COM DICT COMPREHENSION
#{chave: elemento for item in lista}
# new_dados_csv = []
# for old_dict in dados_csv:
#     dict_temp = {key_mapping.get(old_key):value for old_key, value in old_dict.items()}
#     new_dados_csv.append(dict_temp)
# print(new_dados_csv[0])

#CODIGO FINAL - PASSO 2 COM LIST COMPREHENSION
#[exressão for item in lista]
new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in dados_csv]
print(new_dados_csv[0])
