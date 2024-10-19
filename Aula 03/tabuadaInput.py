# Crie um programa que solicite ao usuário qual a tabuada desejada e escreva a tabuada correspondente:
continuar = "s"

while (continuar == "s"):
    tabuada = int(input("Qual a tabuada você deseja calcular: "))
    numero = 0
    
    while (numero <= 10):
        resultado = numero * tabuada
        print(f"{tabuada} x {numero} = {resultado}")
        numero += 1

    continuar = input("Deseja continuar? sim (s) ou não (n) ")
