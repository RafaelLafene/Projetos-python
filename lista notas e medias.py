notas = []
print("Progama de medias de notas usando list\nDigite [-1] para sair do programa")
while True:
    valor=float(input("Digite o valor das notas:"))
    if valor==-1:
        break
    notas.append(valor)
media=sum(notas)/len(notas)
print("A quantidade de alunos é:",len(notas))
print("A media aritmética da turma é",media)