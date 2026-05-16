c=0
s=0
aprv=0
repro=0
print("Leitor de notas, para finalizar o programa digite [0]")
while True:
    nota=float(input("Informe a nota:"))
    if nota==0:
        break
    c=c+1
    s=s+nota
    if nota>=5:
        aprv=aprv+1
    if nota<5:
        repro=repro+1
media=s/c
print("\nA quantidade de alunos que fizeram a prova é:",c)
print("\nA quantidade de alunos aprovados é:",aprv)
print("\nA quantida de alunos reprovados é:",repro)
print("\nA média das notas da turma é:",media)