import csv
lista = ["nome","idade,"
        "joao", "69",
        "maria", "420"]
print(lista)
with open('/home/leonarfo/Downloads/aulas/aulas/aula3/aula3.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        print(type(linha))
        print()
