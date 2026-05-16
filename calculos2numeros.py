valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))
conta=float(input("Digite a operação desejada: \n[1] para soma: \n[2] para subtração: \n[3] para mutiplicação: \n[4] para divisão: \n Operação:"))
soma=valor1+valor2
subtracao=valor1-valor2
multiplicacao=valor1*valor2
divisao=valor1/valor2
if conta==1:
    print("A soma é igual a:",soma)
elif conta==2:
    print("A subtração é igual a:", subtracao)
elif conta == 3:
    print("A mutiplicação é igual a:", multiplicacao)
elif conta == 4:
    print("A divisão é igual a:", divisao)


