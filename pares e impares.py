c=0
s=0
c2=0
s2=0
print("Progama de media impar e par, digite [0] para finalizar o programa")
while True:
    valor=float(input("digite o valor do numero:"))
    if valor==0:
        break
    resto = valor % 2
    if resto==0:
        c = c + 1
        s = s + valor
    else:
        c2=c2+1
        s2= s2+ valor

media=s/c
media2=s2/c2
print("o valor da media dos numeros pares é:",media)
print("O valor da media dos numeros impares é:",media2)

