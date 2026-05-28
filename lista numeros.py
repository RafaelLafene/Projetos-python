numeros = []

print("Digite números inteiros. Digite [-1] para encerrar.")

while True:
    numero = int(input("Digite um número: "))
    if numero == -1:
        break
    numeros.append(numero)

print("A quantidade de numeros digitados é:", len(numeros))
print("numeros digitados:", numeros)