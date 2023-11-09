class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade

p = Pessoa("João", 20)

print(p.getNome())
print(p.getIdade())

class aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula


a = aluno("Paulo Brificado", 20, 1234)
print(a.getNome())
print(a.getIdade())
print(a.getMatricula())
