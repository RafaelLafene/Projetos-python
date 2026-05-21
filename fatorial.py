def fator(x):
    if x==0 or x==1:
        return 1
    resultado=1
    for i in range(2,x+1):
        resultado=resultado*i
        return resultado
if __name__ == '__main__':
    x=int(input("Informe um numero inteiro: "))
if x<0:
    print("Informe um numero positivo")
else:
    resultado=fator(x)
    print(resultado)