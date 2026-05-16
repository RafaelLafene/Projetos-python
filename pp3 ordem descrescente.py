c=0
print("Gerador de numeros em ordem decrescente")
valor=int(input("Informe o valor inicial da sequencia:"))
print("\nA sequencia de",valor,"a 0 será:")
for numero  in range(valor,0,-1):
    print(numero)
    c=c+1
print("A quantidade de numeros digitados é:",c)