with open('/home/leonarfo/Downloads/aulas/aulas/aula2/Lista Exercicios 2/Gabarito.txt', 'r') as arquivo_gabarito:
    gabarito = arquivo_gabarito.readline().strip().split('-')

with open('/home/leonarfo/Downloads/aulas/aulas/aula2/Lista Exercicios 2/RESPOSTAS ALUNOS.txt', 'r') as arquivo_respostas:
    linhas = arquivo_respostas.readlines()

    dados_saida = []
        
    for linha in linhas:
        partes = linha.strip().split(';')
        nome = partes[0]
        respostas_aluno = partes[1]

        acertos = sum(1 for g, r in zip(gabarito, respostas_aluno) if g == r)
        dados_saida.append(f"{nome};{respostas_aluno};{acertos};")

with open('acertos.txt', 'w') as arquivo_saida:
    for linha in dados_saida:
        arquivo_saida.write(linha + '\n')