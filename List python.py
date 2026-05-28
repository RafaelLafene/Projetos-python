lista=  []
while True:
    valor=int(input("Digite um valor: "))
    if valor==0:
        break
    lista.append(valor)
print("valores digitados: \n",lista)
print('valores digitados na verticial:')
for numero in lista:
    print(numero)
print("A quantidade de elementos da lista:",len(lista))
print("Soma dos elementos da lista",sum(lista))
print("O maior valor é:", max(lista))
print("O menor valor é:", min(lista))
pesquisa=int(input("valor de pesquisa:"))
if pesquisa in lista:
    print("valor encontrado na lista")
    print("posição da pesquisa:", lista.index(pesquisa))
else:
    print("valor não encontrado")
lista.sort()
print("depois do sort():\n",lista)
lista.insert(1,33)
print(lista)
