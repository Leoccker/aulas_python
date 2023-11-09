import csv  
class conta: 
    def __init__(self, numero, correntista):
        self.numero = numero
        self.correntista = correntista
        self.saldo = 0

    def alterarNome(self, nome):
        self.correntista = nome
    def depositar(self, valor):
        self.saldo += valor
    def saque(self, valor):
        self.saldo -= valor
    def transferencia(self, valor, conta):
        self.saldo -= valor
        conta.saldo += valor
    def GetPrintDados(self):
        return self.numero, self.correntista, self.saldo


conta1 = conta(123, 'Jesus')
conta2 = conta(456, 'Maria')
conta3 = conta(789, 'José')

conta1.alterarNome('Leonardo')
conta1.depositar(100)
conta2.transferencia(50, conta1)
conta3.saque(10)
arquivo = open('/home/leonarfo/Downloads/aulas/aulas/aula3-2/contas.csv', 'w')
w = csv.writer(arquivo)
for i in (conta1, conta2, conta3):
    i.GetPrintDados() 
    print(str(i.GetPrintDados()))
    w.writerow(i.GetPrintDados())
