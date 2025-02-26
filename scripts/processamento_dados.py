import json
import csv

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nome_colunas = self.__get_columms()
        self.qtd_linhas = self.__size_data()


    def __leitura_json(path):
        json_dados = []
        with open(path, 'r') as file:
            json_dados = json.load(file)
        return json_dados
    

    def __leitura_csv(path):
        csv_dados = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file)
            for dados in spamreader:
                csv_dados.append(dados)
        return csv_dados
    

    @classmethod
    def leitura_dados(cls, path, tipo_arquivo):
        dados = []
        if tipo_arquivo == 'json':
            dados = cls.__leitura_json(path)
        elif tipo_arquivo == 'csv':
            dados = cls.__leitura_csv(path)
        return cls(dados)
    

    def __get_columms(self):
        return list(self.dados[-1].keys())
    

    def rename_columms(self, key_mapping):
        new_data = []
        for old_dict in self.dados:
            temp_dict = {}
            for old_keys, values in old_dict.items():
                temp_dict[key_mapping[old_keys]] = values
            new_data.append(temp_dict)
        self.dados = new_data
        self.nome_colunas = self.__get_columms()


    def __size_data(self):
        return len(self.dados)
        

    def fusion_data(dados1, dados2):
        dados_combinados = []
        dados_combinados.extend(dados1.dados)
        dados_combinados.extend(dados2.dados)
        return Dados(dados_combinados)
    

    def __update_columms(self):
        nova_coluna = [self.nome_colunas]
        for linhas in self.dados:
            temp_list = []
            for coluna in self.nome_colunas:
                temp_list.append(linhas.get(coluna, 'Indisponivel'))
            nova_coluna.append(temp_list)
        return nova_coluna
    

    def save_data(self, path):
        dados_atualizados = self.__update_columms()
        with open(path, 'w') as file:
            write = csv.writer(file)
            write.writerows(dados_atualizados)
        

        
        
        