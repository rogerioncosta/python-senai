# 2.  Calculadora Simples
# Peça ao usuário para inserir dois números e uma operação (+, -, *, /).
#  Realize a operação e exiba o resultado.

n1 = float(input("Digite um número: "))

n2 = float(input("Digite outro número: "))

operacao = input(""" 
                    Digite qual operação deseja fazer:
                    ================================== 
                    + para adição, 
                    - para subtração,
                    * para multiplicação,
                    / para divisão 
                    ==================================

                 """)

if (operacao == "+" ):
    print(f"O resultado da soma de: {n1} + {n2} = {n1 + n2}")
elif (operacao == "-"):
    print(f"O resultado da subtração de: {n1} - {n2} = {n1 - n2}")
elif (operacao == "*"):
    print(f"O resultado da multiplicação de: {n1} * {n2} = {n1 * n2}")
elif (operacao == "/"):
    if (n2 == 0):
        print("Não é possível dividir por zero!")
    else:
        print(f"O resultado da divisão de: {n1} / {n2} = {n1 / n2}")
else:
    print("Operação inválida, tente novamente")
