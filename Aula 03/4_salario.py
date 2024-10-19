# 4 - Crie um programa que solicite ao usuário o nome e o salário de seus funcionários. Ao final imprima o nome e o salário de todos os funcionários, bem como a média salarial da empresa, o maior salário e o menor salário e o total gasto com salários.
import os

nomes_funcionarios = []
salarios_funcionarios = []
continua = "s"

while continua == "s":
    nome_funcionario = input("Digite o nome do funcionário: ")
    nomes_funcionarios.append(nome_funcionario)

    salario_funcionario = float(input("Digite o salário do funcionário: "))
    salarios_funcionarios.append(salario_funcionario)

    continua = input("Deseja continuar? (s/n): \n")

    os.system("cls") # Limpa a tela

total_salarios = 0
maior_salario = salarios_funcionarios[0]
menor_salario = salarios_funcionarios[0]
funcionario_salario_maior = nomes_funcionarios[0]
funcionario_salario_menor = nomes_funcionarios[0]

for i in range(len(salarios_funcionarios)):
    total_salarios = total_salarios + salarios_funcionarios[i]
    if salarios_funcionarios[i] > maior_salario:
        maior_salario = salarios_funcionarios[i]
        funcionario_salario_maior = nomes_funcionarios[i]

    if salarios_funcionarios[i] < menor_salario:
        menor_salario = salarios_funcionarios[i] 
        funcionario_salario_menor = nomes_funcionarios[i]

media = total_salarios / len(salarios_funcionarios)

print("Registros de valores: ")
print("=" * 21)
print("")

for i in range(len(nomes_funcionarios)):
    print(f"Funcionário: {nomes_funcionarios[i]} - Salário: {salarios_funcionarios[i]:.2f}")

print(f"A média salarial da empresa é de: R$ {media:.2f}")

print(f"O maior salário é do(a) funcionário: {funcionario_salario_maior} no valor de R$ {maior_salario:.2f}")

print(f"O menor salário é do(a) funcionário: {funcionario_salario_menor} no valor de R$ {menor_salario:.2f}")

print(f"O total de gastos com salários é de: R$ {total_salarios:.2f}")
