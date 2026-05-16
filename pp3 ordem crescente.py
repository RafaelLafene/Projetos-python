c=0
print("Gerador de numeros em ordem crescente")
valor=int(input("Informe o valor final da sequencia:"))
print("\nA sequencia de 0 a",valor,"sera:")
for numero  in range(1,valor + 1,1):
    print(numero)
    c=c+1
print("A quantidade de numeros digitados é:",c)