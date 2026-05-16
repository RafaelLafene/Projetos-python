c=0
s=0
maiornumero=-999
menornumero=999
c2=0
print("Leitor de numeros, digite [0] para finalizar o programa")
while True:
    valor=float(input("Digite o valor:"))
    if valor==0:
        break
    c=c+1
    s=s+valor
    if valor<menornumero:
        menornumero=valor
    if valor>maiornumero:
        maiornumero=valor
    if valor>=50:
       c2=c2+1
media=s/c
print("\nA quantidade de valores digitados é",c)
print("\nA soma dos valores digitados é:",s)
print("\nA media dos valores digitados é:",media)
print("\nO maior valor digitado é:",maiornumero)
print("\nO menor valor digitado é:",menornumero)
print("\nA quantidade de valores maiores ou iguais a 50:",c2)