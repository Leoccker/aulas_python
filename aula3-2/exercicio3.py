import json

arq = open("/home/leonarfo/Downloads/aulas/aulas/aula3-2/gabarito.json", "r")

gabarito = json.load(arq)
print(gabarito)
gabarito = {}
alunos = {}

