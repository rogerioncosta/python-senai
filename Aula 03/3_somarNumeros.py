contador = 1
listaNumeros = []


while (contador <= 5):
    numero = float(input("Digite 5 números: "))
    listaNumeros.append(numero)
    contador += 1

soma = 0

# for numero in listaNumeros:
#     soma += numero

for i in range(len(listaNumeros)):
    soma += listaNumeros[i]

print(f"A soma dos números é: {soma}")
