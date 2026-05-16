c=0
s=0
print("soma de todos os numeros inteiros entre 1 e 500")
for numero in range(1,500+1):
    if numero %2 !=0 and numero % 3 == 0:
      c=c+1
      s+=numero
print(s)
print("a quantidade de numeros digitados é:",c)