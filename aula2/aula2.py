'''arq = open("/home/leonardo/Documentos/aula python/texto_muito_bonito.txt", "rb")
print(arq.read())
print(arq.readline())
print(arq.readline())
print(arq.readline())
print(arq.read(5))
print("posição atual do arquivo: ", arq.tell())
arq.seek(6, 1)
print(arq.read(7))
arq.seek(11, 0)
print(arq.read(7)) '''
#l = list(arq.read())
#print(l)
#arq = open("/home/leonardo/Documentos/aula python/texto_muito_feio.txt", "w")
'''arq = open("/home/leonardo/Documentos/aula python/texto_muito_feio.txt", "a")
#texto = ("Esse texto é muito feio")
texto = input("Digite um texto: ")
arq.write(texto)
arq.close()
arq = open("/home/leonardo/Documentos/aula python/texto_muito_feio.txt", "r")
print(arq.read())
arq.close()'''



lista = ["Esse texto é muito feio\n", "Esse texto é muito feio 2\n", "Esse texto é muito feio 3\n", "Esse texto é muito feio 4\n"]
arq = open("/home/leonardo/Documentos/aula python/texto_muito_feio.txt", "w")
arq.writelines(lista)
arq.close()
arq = open("/home/leonardo/Documentos/aula python/texto_muito_feio.txt", "r")
print(arq.read())
arq.close() 
