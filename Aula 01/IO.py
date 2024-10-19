"""
nome = input("Digite o seu nome: ")

# Forma de imprimir na tela
print("Olá, " + nome + "!")

# O sinal de vírgula, adiciona espaço entre as palavras
print("Olá,", nome, "!")

# O sinal de porcentagem % é uma forma antiga de formatar strings
print("Olá, %s!" % nome)

# O método format() é uma forma mais moderna de formatar strings
print("Olá, {}!".format(nome))

# O f-string é a forma mais moderna de formatar strings
print(f"Olá, {nome}!")

"""

numeroUm = float(input("Digite um número: "))
numeroDois = float(input("Digite outro número: "))

adicao = numeroUm + numeroDois
subtracao = numeroUm - numeroDois
multiplicacao = numeroUm * numeroDois
divisao = numeroUm / numeroDois

print("Os resultados são:")
print("-"*20)
print(f"Adição: {adicao}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")




