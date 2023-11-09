import csv
import json

input_file = 'POP2022_Municipios_20230622.csv'
output_file = 'arquivo_saída.json'

data = []

with open(input_file, newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)  
    for row in reader:
        uf = row[0]
        cod_uf = row[1]
        cod_municipio = row[2]
        nome_municipio = row[3]
        populacao = row[4]

        if cod_uf.isdigit() and cod_municipio.isdigit() and populacao.replace('.', '', 1).isdigit():
            data.append({
                'uf': uf,
                'cod_uf': int(cod_uf),
                'municipios': [{
                    'cod_municipio': int(cod_municipio),
                    'nome_municipio': nome_municipio,
                    'populacao': int(populacao.replace('.', '', 1))
                }]
            })

result = {}
for entry in data:
    uf = entry['uf']
    if uf not in result:
        result[uf] = {
            'uf': uf,
            'cod_uf': entry['cod_uf'],
            'municipios': []
        }
    result[uf]['municipios'].extend(entry['municipios'])

result_list = list(result.values())

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(result_list, json_file, indent=2, ensure_ascii=False)

print(f'Arquivo JSON gerado com sucesso: {output_file}')
