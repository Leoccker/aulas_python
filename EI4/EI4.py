import csv
import banco

conn = banco.getConexao()
cur = conn.cursor()

# Abrir o arquivo CSV
with open('POP2022_Municipios_20230622.csv', 'r', encoding='utf-8') as csvFile:
    reader = csv.DictReader(csvFile)

    # Para cada linha no arquivo CSV
    for row in reader:
        uf = row['uf']
        cod_uf = int(row['cod_uf'])
        cod_municipio = int(row['cod_municipio'])
        nome_municipio = row['nome_municipio']
        populacao = int(row['pop'])

        # Inserir os dados na tabela EI4
        cur.execute("""
            INSERT INTO municipio (uf, cod_uf, cod_municipio, nome_municipio, populacao)
            VALUES (%s, %s, %s, %s, %s)
        """, (uf, cod_uf, cod_municipio, nome_municipio, populacao))

# Commitar as mudanças e fechar a conexão
conn.commit()
conn.close()