c=0
c1=0
c2=0
c3=0
c4=0
ct=0
print("Programa eleitoral, digite [0] para finalizar o programa\n [1] para o Lula\n [2] para o Flavio\n [3] para Tarcísio\n [5] Voto nulo\n [6] Voto em branco")
while True:
    valor=float(input("Digite o valor do candidato:"))
    if valor==0:
        break
    if valor>0:
        ct=ct+1
    if valor==1:
        c=c+1
    if valor==2:
        c1=c1+1
    if valor==3:
        c2=c2+1
    if valor==5:
        c3=c3+1
    if valor==6:
        c4=c4+1
porcentagemnulo=(c3/ct)*100
porcentagembranco=(c4/ct)*100

print("A quantidade de votos para o Lula é:",c)
print("A quantidade de votos para o Flavio é:",c1)
print("A quantidade de votos para o Tarcísio é:",c2)
print("A quantidade de votos nulos é:",c3)
print("A quantidade de votos em branco é:",c4)
print("A porcentagem de votos nulos é:",porcentagemnulo,"%")
print("A porcentagem de votos nulos é:",porcentagembranco,"%")