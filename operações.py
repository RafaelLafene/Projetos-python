def soma(x,y):
    soma=x+y
    print(soma)
def subtracao(x,y):
    sub=x-y
    print(sub)
def multiplicacao(x,y):
    mul=x*y
    print(mul)
def divisao(x,y):
    div=x/y
    print(div)
if __name__ == '__main__':
    a=int(input("Informe o primeiro numero: "))
    b=int(input("Informe o segundo numero: "))
    escolha=float(input("\n [1] para soma\n [2] para subtração\n [3] para mutiplicação\n [4] para divisao\nDigite a operação desejada: "))
    if escolha==1:
        soma(a,b)
    if escolha==2:
        subtracao(a,b)
    if escolha==3:
        multiplicacao(a,b)
    if escolha==4:
        divisao(a,b)

