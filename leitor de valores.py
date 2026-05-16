c=0
s=0
m20=0
print("Leitor de numeros e informações,\n escreva [0] para finalizar o programa")
while True:
    valor1=float(input("Informe o valor: "))
    if valor1==0:
        break
    if valor1>20:
        m20=m20+1
    c=c+1
    s=s+valor1
media=s/c
print("\n A soma dos valores digitados é igual a:",s)
print("\n A média dos valores digitados é igual a:", media)
print("\n A quantidade de valores digitados é igual a:", c)
print("\n A quantidade de numeros maiores que 20 é igual a:", m20)