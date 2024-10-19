# Imprime numeros de 0 a 4
for i in range(10):
    print(i)

# Imprime numeros de 5 a 9
for i in range(5, 10):
    print(i)

# Imprime numeros de 0 a 100 de 2 em 2
for i in range(0, 101, 2):
    print(i)

# Imprime numeros de 1 a 100 de 2 em 2
for i in range(1, 101, 2):
    print(i)

# Cria uma lista de nomes
nomes = [
    "João Cleber",
    "Maria das Graças",
    "Goreti Milagres",
    "Claudia Orrana",
    "Umberlinda Zulene"
]

# len() é uma função que retorna o tamanho de uma lista
print(len(nomes)) # Imprime o tamanho da lista

# Imprime os nomes da lista
for nome in nomes:
    print(f"O nome da vez é: {nome}")

print("*" * 40)

# Imprime os nomes da lista COM O ÍNDICE
for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]}")


nomes = [] # Cria uma lista vazia
continua = "s"
while continua == "s":
    nome = input("Digite um nome: ")
    nomes.append(nome) # Adiciona o nome na lista de nomes

    continua = input("Deseja continuar? (s/n): ")

# Imprime os nomes da lista que o usuário digitou
for nome in nomes:
    print(f"O nome da vez é: {nome}")
