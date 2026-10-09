alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana PAula"]

aluno_procurado = input("Digite um nome: ")
for aluno in alunos:
    if aluno_procurado.lower() in aluno.lower():
        print (aluno)