nome = input("digite seu nome: ")
turma = input("Digite sua turma: ")
materia = input("digite sua materia: ")
professor = input("digite o nome do seu professor: ")

nota1 = int(input("digite a nota do seu primeiro trimestre: "))
nota2 = int(input("digite a nota do seu segundo trimestre: "))
nota3 = int(input("digite a nota do seu terceiro trimestre: "))


media = (nota1 + nota2 + nota3)/3



print("--------------nome--------------")

print("Nome cadastrado:", nome)

print("--------------turma--------------")

print("Qual turma voce e?", turma)

print("--------------materia--------------")

print("qual materia?", materia)

print("--------------professor--------------")

print("qual seu professor?", professor)

print("----------MEDIA FINAL----------")

print("sua media final e", media)

