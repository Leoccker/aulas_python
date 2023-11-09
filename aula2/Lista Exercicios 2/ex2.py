# Lendo a lista de frutas
with open("/home/leonarfo/Downloads/aulas/aulas/aula2/Lista Exercicios 2/produtos.txt", "r") as lista_frutas:
    linhas = lista_frutas.readlines()
    frutas = [linha.strip().split(";") for linha in linhas]
    dados_saida = []

    for fruta in frutas:
        ident = fruta[0]
        nome = fruta[1]
        preco = float(fruta[2])
        dados_saida.append({"nome": nome, "ident": ident, "preco": preco})

    print("Lista de Produtos Disponíveis:")
for produto in dados_saida:
    print(f"ID: {produto['ident']} - Nome: {produto['nome']} - Preço: R${produto['preco']:.2f}")


produtos_escolhidos = []

quer_comprar = True

while quer_comprar:
    id_produto = input("Digite o id do produto que deseja (ou 's' para sair): ")

    if id_produto == 's':
        break

    quantidade = int(input(f"Deseja quantos desse? "))

    produto_encontrado = None
    for produto in dados_saida:
        if produto['ident'] == id_produto:
            produto_encontrado = produto
            break

    if produto_encontrado:
        produto_escolhido = {'nome': produto_encontrado['nome'],
                             'ident': produto_encontrado['ident'],
                             'preco': produto_encontrado['preco'],
                             'quantidade': quantidade}
        produtos_escolhidos.append(produto_escolhido)
        print(f"Produto '{produto_encontrado['nome']}' adicionado ao carrinho.")
    else:
        print(f"Produto com id {id_produto} não encontrado.")

valor_total = sum(produto['preco'] * produto['quantidade'] for produto in produtos_escolhidos)

print("\nProdutos Escolhidos:")
for produto in produtos_escolhidos:
    print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço Unitário: R${produto['preco']:.2f}")

print(f"\nValor Total da Compra: R${valor_total:.2f}")
# Criar e escrever no arquivo de saída
with open('carrinho.txt', 'w') as arquivo_saida:
    for produto in produtos_escolhidos:
        arquivo_saida.write(f"ID: {produto['ident']} - Nome: {produto['nome']} - Preço: R${produto['preco']:.2f}\n")
    arquivo_saida.write(f"Valor Total da Compra: R${valor_total:.2f}\n")
