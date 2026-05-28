geral=[]
masculino= []
feminino= []
print("Leitor de altura e genero\nDigite [-1] para finalizar o programa")
while True:
    altura= float(input("Digite sua altura: "))
    genero= str(input("\n[m] para masculino\n[f] para feminino\nDigite o seu genero:"))
    if genero == "m":
        masculino.append(genero)
    if genero == "f":
        feminino.append(genero)
    if altura==-1:
        break
    geral.append(altura)
print("A maior altura do grupo é:",max(geral))
print("A menor altura do grupo é:",min(geral))
print("A quantidade de homens é:",len(masculino))
print("A quantidade de mulheres é:",len(feminino))