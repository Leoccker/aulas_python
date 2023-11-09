import pandas as pd
import csv
import json

xlsFile = pd.read_excel('popxls.xls')
xlsFile.to_csv('popcsv.csv', index = None, header=True)

csvFile = open('popcsv.csv', 'r', encoding='utf-8')

data = []

for row in csv.DictReader(csvFile):

    uf = row['uf']
    cod_uf = int(row['cod_uf'])
    cod_municipio = int(row['cod_municipio'])
    nome_municipio = row['nome_municipio']
    populacao = int(row['populacao'])

    uf_existente = next((item for item in data if item['uf'] == uf), None)

    if uf_existente != None:

        uf_existente['municipios'].append({
            "cod_municipio": cod_municipio,
            "nome_municipio": nome_municipio,
            "populacao": populacao
        })

    else:

        uf_nova = {
            "uf": uf,
            "cod_uf": cod_uf,
            "municipios": [
                {
                    "cod_municipio": cod_municipio,
                    "nome_municipio": nome_municipio,
                    "populacao": populacao
                }
            ]
        }

        data.append(uf_nova)

with open('popjson.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

csvFile.close()