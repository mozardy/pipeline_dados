from processamento_dados import Dados


# Extract

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


dados_empresaA = Dados.leitura_dados(path_json, 'json')
dados_empresaB = Dados.leitura_dados(path_csv, 'csv')

print(f'Dados json: {dados_empresaA.dados[0]}')
print(f'Dados csv: {dados_empresaB.dados[0]}')
print(f'Colunas json: {dados_empresaA.nome_colunas}')
print(f'Colunas csv: {dados_empresaB.nome_colunas}')
print(f'Quantidade de linhas json: {dados_empresaA.qtd_linhas}')
print(f'Quantidade de linhas csv: {dados_empresaB.qtd_linhas}')

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columms(key_mapping)
fusao_dados = Dados.fusion_data(dados_empresaA, dados_empresaB)



print(f'Csv atualizado: {dados_empresaB.nome_colunas}')
print(f'Fusão dos dados: {fusao_dados.dados[-1]}')


# Load

path_fusao = 'data_processed/classe_dados.csv'

fusao_dados.save_data(path_fusao)

print(path_fusao)