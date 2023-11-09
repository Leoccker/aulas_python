import json

arq = open('/home/leonarfo/Downloads/aulas/aulas/aula3/aula3.json', 'r')
dados = json.load(arq)

print(dados)
print(type(dados))
print()

for i in dados:
    print(i)
    print(type(i))
