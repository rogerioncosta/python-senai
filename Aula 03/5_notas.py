# 5 - Uma escola precisa de ajuda para organizar as notas dos alunos. Crie um programa que leia o nome de um aluno e suas 4 notas. O programa deve continuar lendo os nomes e notas até que o usuário não deseje mais adicionar alunos. Em seguida, o programa deve exibir o nome e a média de cada um dos alunos.
# Extra:
# - Permita que o usuário possa escolher quantas notas cada aluno terá.
# - Mostre uma média geral da turma.

listaAlunos = []

listaAlunosNotas = []

listaNotasTurma = []

continuar = "s"

while continuar == "s":
    listaNotasAluno = []
    qtde_notas_aluno = 0
    nome_aluno = input("Digite o nome do aluno: ")
    listaAlunos.append(nome_aluno)

    qtde_nota_aluno = int(input("Quantas notas esse aluno terá? "))   

    while qtde_notas_aluno < qtde_nota_aluno:
        nota = float(input("Digite a nota: "))
        listaNotasAluno.append(nota)
        listaNotasTurma.append(nota)

        qtde_notas_aluno += 1

    somaNotas = 0
    for nota in listaNotasAluno:
        somaNotas += nota

    mediaAluno = somaNotas / qtde_nota_aluno    
    
    listaAlunosNotas.append([nome_aluno, mediaAluno]) 
        
    continuar = input("Deseja continuar? (s/n): \n")

for boletim in listaAlunosNotas:
    print(f"Aluno: {boletim[0]} - Média {boletim[1]:.2f}")

somaNotasTurma = 0
for nota in listaNotasTurma:
    somaNotasTurma += nota

mediaGeralTurma = somaNotasTurma / len(listaNotasTurma)

print(f"A média da turma é: {mediaGeralTurma:.2f}")